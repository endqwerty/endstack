# Source playbooks

The why skill assigns one investigator per available evidence category, each reading a single source-specific playbook below. The playbooks are concrete examples for available evidence sources. Adapt them for a different source integration in the same category.

| Category | Playbook | Evidence source |
|---|---|---|
| Source control history | [`code-archaeology.md`](./sources/code-archaeology.md) | Repository and PR history |
| Issue / ticket tracker | [`linear.md`](./sources/linear.md) | Issue tracker (adapt to the available source) |
| Long-form documents | [`notion.md`](./sources/notion.md) | Document store (adapt to the available source) |
| Real-time team chat | [`slack.md`](./sources/slack.md) | Team chat (adapt to the available source) |
| Infrastructure observability | [`datadog.md`](./sources/datadog.md) | Infrastructure telemetry (adapt to the available source) |
| Error / exception tracking | [`sentry.md`](./sources/sentry.md) | Error tracker (adapt to the available source) |
| Product analytics warehouse | [`databricks.md`](./sources/databricks.md) | Analytics warehouse SQL (adapt to the available source) |

Cross-cutting:

- [`incident-postmortem.md`](./sources/incident-postmortem.md). Add this if the target code looks defensive (null checks, retry, timeout, rate limit, feature flag, egress guard, OOM handler).
