---
name: build-design
tags:
- build
- principles
- architect
- test-design
- typescript-best-practices
- no-comments
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

Let users archive tasks in this todo app. An archived task disappears from the default task list in both the web view (`web/taskList.ts`) and the command-line list (`cli/list.ts`), and archiving can be undone through the same PATCH endpoint (`server/tasks.ts`). Tests run with `node --test`. There is no remote, so put the pull request title and description in your final reply. Do not ask questions; finish and summarize.
