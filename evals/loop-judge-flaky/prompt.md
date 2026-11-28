---
name: loop-judge-flaky
tags:
- loop-judge
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
- Agent
---

I've been fixing the flaky test in `test/cache.test.js` for a while; `attempts.md` is my log of each round so far. Pick it up from the next round and keep going until it is fixed. Tests run with `node --test`. Do not ask questions; finish and summarize.
