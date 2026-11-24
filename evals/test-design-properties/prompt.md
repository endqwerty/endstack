---
name: test-design-properties
tags:
- test-design
runs: 3
max_turns: 15
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
---

Decide what tests to write for three modules in a billing service, before anyone writes code. There is no checkout; the context below is all there is. Stop before implementation. Do not ask questions; finish and summarize.

Context:
- `billing/allocate.ts`: pure function that splits an integer-cent invoice total across weighted line items and returns integer-cent shares (handling zero weights, single items, and rounding remainders).
- `billing/lease_cache.ts`: single-process in-memory TTL cache with `get`, `set`, `invalidate`, `evictExpired`, and a max capacity that evicts the least-recently-used key.
- `billing/routes.ts`: registers three HTTP routes (`GET /health`, `POST /invoices`, `GET /invoices/:id`) and maps a `NotFoundError` to HTTP 404.

For each module, state what test shape you would write, how you would design and run it in the every-change suite, and what pitfalls you would guard against.
