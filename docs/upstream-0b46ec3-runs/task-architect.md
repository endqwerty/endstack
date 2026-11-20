Apply the skill you were given to this design task. You have no tools and cannot read code; the context below is all there is. Produce the output the skill asks for before any implementation code (describe phases you would run in sequence yourself where the skill wants separate workers). Stop before implementation.

Task: add per-customer rate limiting to an internal Go HTTP API.

Context:
- `api/server.go` registers 40 handlers on a chi router. Auth middleware puts a `CustomerID` in the request context.
- `jobs/runner.go` runs scheduled jobs that call 6 of the same handler functions directly (not over HTTP), using a system customer ID.
- The service runs as 4 replicas behind a load balancer. Redis is already a dependency (used for sessions).
- Product wants: 100 requests per minute per customer across all replicas, with a per-customer override table in Postgres that support staff edit a few times a month. Jobs must not be limited.
- There is an existing `ratelimit` package that wraps an in-memory token bucket per process, used only by the public login endpoint.
