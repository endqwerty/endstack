---
name: verify-test-bloat
tags:
- verify
- test-design
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Bash
---

The change in `slug.diff` is already applied in this checkout: it adds `slugify` for blog post URLs and its tests in `test/slug.test.js`. All tests pass with `node --test`. I'm about to merge it. Review it first and tell me if anything should change. Do not edit files.
