---
name: why-retry
tags:
- why
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools:
- Read
- Glob
- Grep
---

Why does `sync/client.go` retry exactly 7 times with a 250 ms base backoff, and is it safe to drop it to 3? This checkout has no useful history: `retry-record.md` holds everything the repository and code host record about those lines.
