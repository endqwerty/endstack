# Architecture: per-customer rate limiting

## 1. Systems the change touches

- `api/server.go`: chi router, 40 handlers, auth middleware that sets `CustomerID` in context. Rate limiting must run after auth.
- `jobs/runner.go`: calls 6 handler functions directly, with a system customer ID. It bypasses the router, so any middleware-level limiter never sees these calls. That satisfies "jobs must not be limited" by construction, as long as the limiter lives in middleware and not inside the handlers.
- Redis (sessions already use it): the shared counter store across 4 replicas.
- Postgres: new per-customer override table, edited by support a few times a month.
- Existing `ratelimit` package: in-memory token bucket per process, used by login. It cannot give a cross-replica limit (effective limit would be about 400/min with 4 replicas and an even balancer, and uneven otherwise). It is also keyed for login, not per customer.
- Load balancer: spreads one customer's requests across replicas, so local state is wrong.
- Failure paths: Redis down, Postgres down, a customer with no override row, a request with no `CustomerID` (unauthenticated routes).

## 2. Two candidate shapes

### Shape A: HTTP middleware with a `Limiter` interface and a Redis implementation

```go
// package ratelimit
type Decision struct {
    Allowed    bool
    Limit      int
    Remaining  int
    RetryAfter time.Duration
}

type Limiter interface {
    Allow(ctx context.Context, key string, limit int, window time.Duration) (Decision, error)
}

// package ratelimit/redislimiter: fixed or sliding window via one Lua script / INCR+EXPIRE
func New(rdb *redis.Client) Limiter

// package ratelimit (policy)
type LimitSource interface {
    LimitFor(ctx context.Context, c CustomerID) int // override or default 100
}

// package api
func RateLimit(l ratelimit.Limiter, src ratelimit.LimitSource, onErr FailMode) func(http.Handler) http.Handler
```

`LimitSource` is a Postgres-backed table with an in-process cache (TTL about 60s). Overrides change a few times a month, so a short TTL is fine and a Postgres read is not on the request path. Middleware sits after auth in `server.go`; jobs call handlers directly and so are never limited.

### Shape B: limiter embedded in each handler or in a service layer both callers use

Handlers (and so jobs) call `limiter.Check(customerID)` at the top, and the job runner passes a system ID that the limiter exempts.

### Comparison

| | A: middleware | B: in handler/service |
|---|---|---|
| Who owns "is this call limited"? | one place (router wiring) | 40 handlers, plus an exemption rule for the system ID |
| Jobs exempt | by construction (no HTTP path) | by special-case ID, which is a workaround that can leak |
| Ways to add a limit | one (middleware) | per handler, easy to forget |
| Callers must know | nothing | to call `Check`, and to pass the right ID |

Choose A. B forces every handler to know about limiting and turns "jobs are exempt" into a magic ID, which is state with two owners.

## 3. State ownership (one owner each)

- Request counts: Redis, owned by the `Limiter` implementation. No other code reads or writes the keys. Key shape `rl:{customerID}:{windowStart}` with TTL slightly over the window.
- Per-customer limits: Postgres table `customer_rate_limits(customer_id pk, requests_per_minute int, updated_at)`, owned by the `LimitSource`. Support edits go to the table only. The cache is derived and disposable.
- Default (100): a single constant/config in the `LimitSource`, not repeated in the middleware.
- Existing in-memory `ratelimit` bucket: stays for login only. Do not stretch it. Put the new Redis limiter behind the same package name only if the interface stays clearly separate; otherwise name it `ratelimit/distributed` to avoid two meanings of "limiter" in one namespace. Login could later move to the new `Limiter` (keyed by IP), which would leave one way to limit; note it as a follow-up, not part of this change.

## 4. One way to do each task

- Check a request: `Limiter.Allow` only.
- Find a customer's limit: `LimitSource.LimitFor` only.
- Reject: middleware writes 429 with `Retry-After` and `X-RateLimit-*` headers from `Decision`. Handlers never write 429 for this reason.

## 5. Failure behaviour (decide now)

- Redis error: fail open (allow, log, metric). The limit protects capacity and is not a security control; a Redis blip must not take the API down. Make this a `FailMode` parameter, defaulting to open.
- Postgres error or cache miss with DB down: use last cached value, else default 100.
- No `CustomerID` in context (unauthenticated routes): middleware skips. Wire it only on the authenticated route group, so this cannot happen silently.
- Accuracy: fixed window allows up to 2x burst at window boundaries. Acceptable for "100/min"; sliding window is a drop-in change inside the Redis implementation only if product objects.

## 6. Module boundaries and dependencies

- `ratelimit` (interfaces, `Decision`, `LimitSource` contract): no Redis or Postgres imports.
- `ratelimit/redislimiter`: imports redis client only.
- `ratelimit/pglimits` (or inside the existing storage package): implements `LimitSource`, owns the cache.
- `api`: `RateLimit` middleware; depends on the interfaces only.
- `jobs`: untouched.

Wiring in `server.go`: construct once in main, pass to the router builder, apply with `r.Group(func(r chi.Router){ r.Use(auth); r.Use(RateLimit(...)); ... })` so order is explicit.

## 7. Testing seams

- `Limiter` fake for middleware tests (allowed, denied, error under each `FailMode`).
- Redis implementation tested against a real Redis (or miniredis) for window rollover and cross-"replica" sharing by using two clients.
- `LimitSource` tested for override, missing row, cache TTL.
- A test that calls a handler function directly with the system ID and shows no limiting happens, pinning the job behaviour.

## 8. Risks and open questions

- Do any of the 6 job-called handlers also get hit over HTTP by the system customer? If so, the middleware would limit them; exempt that ID in the `LimitSource` (returns "unlimited") only as a fallback.
- Is 100/min applied across all endpoints combined (assumed) or per endpoint? Assumed combined.
- Cache TTL means an override edit takes up to 60s to apply; confirm acceptable to support staff.

## Redesign check

No workaround repeats in Shape A: the job exemption, shared state and single owner all fall out of the placement. Stop here before implementation. For a contested version of this design, the arena skill would be the next step; this one is not contested.
