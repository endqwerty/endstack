---
name: no-comments-nine
tags:
- no-comments
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
---

Clean up the comments in `src/app.ts`: remove the ones that should not be there, and fix what they work around where the fix fits in `src/app.ts` and `src/runtime.ts`. Do not ask questions; finish and summarize.
