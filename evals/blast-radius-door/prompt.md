---
name: blast-radius-door
tags:
- blast-radius
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Bash
---

The change in `orders-cleanup.diff` is already applied in this checkout. It tidies the orders API to camelCase and drops the old float `legacy_total` column now that `total_cents` exists. Tests pass with `node --test`. Before it ships tonight: what could this break outside the diff, and can we undo it if it goes wrong? Do not edit files; tell me what you found.
