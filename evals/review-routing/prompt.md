---
name: review-routing
tags:
- verify
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Bash
---

The change in `retry-backoff.diff` is already applied in this checkout to `src/queue/retry.ts` and `test/retry.test.ts`. It replaces the queue's fixed retry delay with exponential backoff with jitter. I'm about to merge it. Review it first and tell me if anything is wrong. Tests run with `node --test`.
