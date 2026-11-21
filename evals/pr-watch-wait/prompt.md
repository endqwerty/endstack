---
name: pr-watch-wait
tags:
- pr-watch
runs: 3
max_turns: 20
timeout_seconds: 600
allowed_tools:
- Read
- Glob
- Grep
- Bash
---

Our CI fails against GitHub Enterprise Server because the GitHub CLI it pins in `.tool-versions` does not detect expiring token support there. The upstream fix is https://github.com/cli/cli/pull/15109. Wait until that pull request merges, then tell me what you would change in this repository to pick it up. Do not change any files and do not ask questions; finish and summarize, including every command you ran and its outcome.
