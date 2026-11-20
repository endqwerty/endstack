# Guard the Context Window

Context overflow degrades reasoning and halts progress.

- Give verbose outputs, screenshots, and large documents to a separate worker or a file, if the harness allows; the main thread gets summaries, not raw payloads.
- Keep content used on every invocation inline, not in a file that costs a read each time.
- Size phases and cap scope. Limit files per phase, set turn budgets, account for mechanism costs.
