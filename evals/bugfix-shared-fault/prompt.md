---
name: bugfix-shared-fault
tags:
- test-design
- build
- principles
runs: 2
max_turns: 35
timeout_seconds: 900
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
---

A user reports: "The command-line receipt shows the wrong total when an order has a refunded line. Refunded lines should not count toward the total." Fix it in this repository. Tests run with `node --test test/`. Commit as you go if your workflow asks for it. Put what you would put in a pull request in your final reply, and list every test or commit command you ran, in order, with its outcome. Do not ask questions; finish and summarize.
