---
name: formal-verification-boundary
tags:
- formal-verification
- test-design
runs: 3
max_turns: 15
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
---

A developer asks you to formally verify two parts of a TypeScript service before shipping. There is no checkout; the context below is all there is. Stop before writing models or code. Do not ask questions; finish and summarize.

Context:
- `cache/lru.ts`: a single-process in-memory LRU cache (`get`, `set`, `delete`, `clear`, max size) with no concurrency. The team wants confidence that arbitrary sequences of operations never corrupt the eviction order or exceed max size.
- `leases/claim.ts`: a distributed job lease protocol where two workers race against Postgres to claim, renew, and complete a job before lease expiry. The team wants to know whether any interleaving of worker crashes, slow renewals, and reclaims can let two workers execute the same job at once.

For each part, decide whether to use formal verification or another testing approach, explain why, and state what you would verify or test.
