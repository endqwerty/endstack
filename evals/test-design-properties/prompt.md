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
- `billing/allocate.ts`: pure function that splits an integer-cent invoice total across weighted line items, returning integer-cent shares that must sum to the original total with no negative shares and handle zero weights, single items, and rounding remainders.
- `billing/lease_cache.ts`: in-memory TTL cache with `get`, `set`, `invalidate`, `evictExpired`, and a max capacity that evicts the least-recently-used key. Recent bugs came from specific sequences of `set`, `invalidate`, and `evictExpired`.
- `billing/routes.ts`: registers three HTTP routes (`GET /health`, `POST /invoices`, `GET /invoices/:id`) and maps a `NotFoundError` to HTTP 404.

For each module, state which test shape you would write, what it should assert, and how to keep the every-change suite fast and deterministic.
