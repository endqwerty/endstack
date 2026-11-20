# Architect: per-customer rate limiting (stopped before implementation)

Phase tracking: 1 Ground (done, from context only), 2 Sketch (done), 3 Agree (skipped: no checkpoint requested), 4 Implement (not started, stopped by task), 5 Scrap (not triggered).

Note on method: I have no tools and no workers, so I ran the how/why grounding and the candidate designers myself in sequence, from the context given. I could not seek other model perspectives. The candidates below are from one perspective, so their spread is weaker evidence than the skill intends.

## Phase A: Ground (how, from the stated context only)

- Request path: LB -> one of 4 replicas -> chi router in `api/server.go` -> auth middleware sets `CustomerID` in context -> one of 40 handlers.
- Job path: `jobs/runner.go` calls 6 handler functions directly as Go calls, with a system customer ID. It never touches the router or its middleware.
- Existing `ratelimit` package: in-memory token bucket per process, used only by the public login endpoint. It is per-process, so it cannot enforce a cross-replica limit.
- Redis is already a dependency (sessions). Postgres holds the override table, edited a few times a month.
- Constraints the design must honor: 100 req/min/customer across all 4 replicas; per-customer override from Postgres; jobs never limited; the 6 handlers called by jobs must stay callable without a limiter.
- Unknowns I could not resolve (see Open questions): whether the login limiter keys on IP, what the handler function signature is, whether Redis is cluster or single node.
- The why pass on the existing shape: the in-memory bucket was likely right for login (one endpoint, abuse control, approximate). Treat that rationale as evidence, not a constraint. It does not fit a cross-replica quota.

## Phase B: Sketch, three candidates

**A. Router middleware, Redis counter.** A chi middleware after auth reads `CustomerID`, asks a `Limiter` for a decision, returns 429 with `Retry-After` on deny. Jobs bypass it structurally because they skip the router.

**B. Limit check inside the handler layer.** Wrap the 40 handler functions (or their shared core) with a decorator that checks the limiter. Jobs call the same functions, so they need an explicit exemption on the system customer ID.

**C. Per-replica local buckets with a quota split.** Each replica enforces 100/4 = 25 per minute in memory. No Redis.

Screen against the red flags:

| Flag | A | B | C |
|---|---|---|---|
| Two ways to do one task | Yes unless login moves onto the same limiter (fixed below) | Same | Same |
| Split ownership of state | No, Redis counter is the one owner | No | Yes, 4 independent counters |
| Information leakage | Redis key format private to the limiter | Handlers know about exemption rules | Quota split leaks replica count |
| Pass-through / shallow | Interface is one call | Decorator on 40 handlers is 40 touch points | Shallow but wrong |
| Hand-synced list | None | The set of 6 job-called handlers must be exempt: a list that drifts | None |
| Importable internals | Fixable by an `internal/` package | Same | Same |

Result: C is rejected on correctness. Uneven load balancing means a customer is throttled at 25 on one replica while 75 unused remain elsewhere, so it does not meet "100 across all replicas". B works but needs an exemption rule that agents can get wrong: a new job-called handler that is not exempted gets limited, and it is applied in the wrong layer. A makes "jobs are not limited" true by construction: the limiter is mounted on the router and jobs never pass through the router.

Interface depth: A's public surface is `Allow(ctx, key, rule) -> Decision` plus one middleware constructor. Hidden behind it: the Redis script, window algorithm, key naming, fail-open policy, the override lookup and its cache. B exposes the same limiter but adds a per-handler wrapping surface. A is deeper.

Chosen base: A. Grafts: from B, nothing structural; from C, the idea of a process-local cache, used only for the override table, not for counting.

## Rationale (shape per the rationale template)

### Problem

Limit each customer to 100 requests per minute across 4 replicas, with a Postgres override per customer, and never limit scheduled jobs that call 6 handlers directly. The existing `ratelimit` package counts in process memory, so it cannot be reused as is. Constraints from grounding: jobs bypass HTTP, `CustomerID` is in context after auth, Redis is available, overrides change rarely.

### Usage (caller's view)

Written first; the types below are derived from it.

```go
// api/server.go: the only place a limit is applied
limiter := ratelimit.New(redisClient, ratelimit.PostgresRules(db, 100/*default per minute*/))
r.Use(authMiddleware)
r.Use(ratelimit.Middleware(limiter, customerKey)) // after auth, before handlers
r.Get("/orders", listOrders) // handlers unchanged
```

```go
// jobs/runner.go: unchanged. Calls listOrders(...) directly. No limiter import.
```

```go
// public login endpoint, migrated off the in-memory bucket so there is one way
r.With(ratelimit.Middleware(limiter, clientIPKey)).Post("/login", login)
```

A denied request gets 429 and `Retry-After`. Staff change an override by updating a Postgres row; it takes effect within the cache TTL, with no deploy.

### Shape

```go
package ratelimit

type Key string

type Rule struct {
    Limit  int           // requests
    Window time.Duration // 1 minute
}

type Decision struct {
    Allowed    bool
    RetryAfter time.Duration
}

// Limiter is the one public interface. Not implemented bodies below.
type Limiter interface {
    Allow(ctx context.Context, key Key) (Decision, error) // rule resolved inside
}

func New(rdb *redis.Client, rules RuleSource) Limiter // not implemented

// RuleSource resolves the Rule for a key. Postgres-backed with a short-TTL cache.
type RuleSource interface {
    RuleFor(ctx context.Context, key Key) Rule
}

func PostgresRules(db *sql.DB, defaultLimit int) RuleSource // not implemented

func Middleware(l Limiter, keyFn func(*http.Request) (Key, bool)) func(http.Handler) http.Handler // not implemented
func CustomerKey(r *http.Request) (Key, bool) // reads CustomerID from context; ok=false -> pass through
```

Load-bearing decisions:
- Counting lives in Redis only: sliding-window-counter or fixed window via one Lua script, atomic increment and expiry in one round trip. Key `rl:{customer}:{window}` is private to the package. State has one owner, so there is no per-replica copy to reconcile. (separate-before-serializing: not needed, as a single atomic Redis op is the owner.)
- Rule resolution is separate from counting. Overrides load from a Postgres table `customer_rate_limits(customer_id, limit_per_minute)` into a process-local cache with a TTL of about 30-60 seconds. The cache is read-only config, never counted state, so it is safe to be per-process.
- Fail open: on a Redis error, allow and log. A limiter outage must not take the API down. Idempotency: a retried increment can over-count by one request, which is acceptable at this precision.
- Jobs exempt by construction: the limiter is mounted only on the router. No `if customer == system` branch exists anywhere. Add a test that the router chain has the middleware and that `jobs` does not import `ratelimit`.
- Interface depth: callers see `Allow` and one middleware. Hidden: Redis script, windowing, key layout, rule lookup, cache, fail-open policy. The package moves under `internal/` so nothing outside can import the Redis or Postgres details.
- One way to do the task: the login endpoint moves onto this limiter keyed by client IP, and the in-memory token bucket is deleted in the same change.

### Synthesis decision

Base: A. Rejected B because the exemption becomes a hand-maintained list of handlers and spreads limiter knowledge across 40 handlers. Rejected C because a per-replica quota cannot guarantee a global 100. Adapted from C only the local cache idea, applied to rule config rather than counters.

### Tradeoffs accepted

- We accept a 30-60 second delay before an override edit takes effect, in exchange for no Postgres query per request.
- We accept fail-open during a Redis outage, in exchange for availability. A customer can briefly exceed 100/min.
- We accept window-boundary burstiness (up to about 2x at a fixed-window edge) if a fixed window is used, in exchange for a simpler script. Sliding-window counter would reduce it at slightly more cost.
- We accept one extra Redis round trip on every API request, in exchange for an accurate global limit.
- We accept changing the login path in this work, in exchange for one limiter instead of two.

### Alternatives considered

- B (handler-layer check): lost on interface depth and drift. It exposes a wrapper to 40 handlers and a job exemption that has to be remembered.
- C (quota split per replica): lost on correctness under uneven load balancing and on replica-count leakage.
- Not considered further: edge or load-balancer rate limiting. It cannot see `CustomerID` after auth and cannot read the Postgres overrides, so it would need to duplicate auth.

### Open questions and risks

- Does the login limiter key on IP, and is a distributed limit acceptable for it, or should login stay as is and be treated as a deliberate second way?
- Is Redis a single node or cluster? The Lua script needs a single key per call, which this key layout satisfies.
- What should the 429 body and any rate-limit headers look like for existing API clients?
- Should unauthenticated routes (other than login) be limited by IP, or left alone?
- Is a staleness of up to a minute on overrides acceptable to support staff?
- Do any of the 6 job-called handlers read the request or context set by the router middleware? Removing nothing here, but worth confirming.

### Next implementation step

Write the Lua script and `Limiter.Allow` against a real Redis in a test, asserting that two simulated replicas share one count of 100.
