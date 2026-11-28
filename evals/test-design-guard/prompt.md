---
name: test-design-guard
tags:
- test-design
runs: 2
max_turns: 40
timeout_seconds: 900
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
---

`INCIDENTS.md` lists two admin routes that shipped without a permission check. Fix them and make sure this cannot happen again as more admin routes get added. Tests run with `node --test`. Do not ask questions; finish and summarize.
