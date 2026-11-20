---
name: interrogate-pager
tags:
- interrogate
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
---

The latest change to `pager.py` is meant to make `page` a real 1-based pager that raises ValueError when page_no < 1 or size < 1, as its docstring says, and to add `page_count(n_items, size)`, which returns the number of pages needed to hold n_items. `test_pager.py` is its only test. Tear this change apart before I merge it and tell me what is actually broken. Do not ask questions; finish and summarize.
