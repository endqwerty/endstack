# Infrastructure telemetry Telemetry

## What this source contains

Infrastructure telemetry holds the runtime record, what actually happened in production, as opposed to what was planned or discussed.

- **Metrics.** Counters, gauges, histograms instrumented by the team. A metric's *presence* is itself evidence that someone thought the number worth watching.
- **Monitors & alerts.** Conditions the team decided warranted waking someone up. A monitor firing on `rate_limit_hit > 10/min` is direct evidence the team worried about that threshold.
- **Dashboards.** Curated views of what the team considers important for a subsystem.
- **APM traces & spans.** Request-level runtime data, for "why is this slow" / "why is there a timeout here" questions.
- **Logs.** High-volume event records, often holding the error conditions that motivated defensive code.
- **Incidents.** Formal incident records with timelines and linked postmortems.
- **Notebooks.** The team's exploratory investigations, often with hypotheses and analyses.

## How to search it

Use the available infrastructure-observability source. Start broad, then narrow.

1. **Identify the owning service(s).**

   Identify services by name or owning team and inspect upstream/downstream dependencies.

2. **Dashboards and monitors first.**

   Search dashboards and monitors by feature, service and symbol.

   When a dashboard or monitor covers the target, note its queries and watched thresholds. The threshold is frequently the answer to "why is this clamped at N?"

3. **Metrics around the target.**

   Search metric names; read metadata, units and tags; fetch time series around the PR date.

   Correlating a metric's trajectory with the target's add/change date is strong supporting evidence: "the `payment_timeout` metric spiked 2023-11-03, and the retry logic merged 2023-11-06."

4. **Logs. Narrow, don't dump.**

   Search raw log patterns and aggregate counts when needed.

   Search with symbols, error strings, or feature names. **Strongly prefer time-bounded queries** (e.g., 30 days before/after the change).

5. **APM spans and traces.**

   Aggregate span statistics, inspect individual spans, and fetch a specific trace by identifier.

   Useful for timeouts, retries, slow paths, and cross-service behavior.

6. **Incidents.**

   Search incidents by title, team and date range, then read each relevant incident in full.

   If the target looks defensive, search for incidents around the time it was added. An incident whose timeline includes "added defensive check for X" is near-direct evidence.

## What good evidence looks like here

- A monitor whose query and threshold match the constraint the code enforces (code clamps to 100, monitor alerts when requests exceed 100/min)
- A dashboard created by the target's author, with widgets that correspond to what the code measures or guards against
- A metric showing a production spike immediately before the code was merged, and stable values after
- An incident record referencing the target code, the same symbols, or the same error strings
- Logs showing a specific error pattern the defensive code would prevent, timestamped in the window before the change

## Common pitfalls

- **Correlation is not causation.** A spike before a PR and stabilization after is suggestive, not definitive, since other changes may have landed in the same window. Check neighboring PRs.
- **Overfitting to the chart you found.** A chart reflects its maker's framing. A chart named "retry success rate" is evidence the team cared about retry success, not that it's why a specific line of code exists.
- **Vanished telemetry.** Metrics can be renamed, deleted, or have short retention. If you can't find data from the relevant window, that's a gap, not a null result.
- **Noise at scale.** Narrow log searches by service, tag, and time window aggressively. Aggregate counts rather than dumping raw logs.
- **Instrumented != caused.** A metric shows someone cared enough to measure something, not that the code was added *because* of it. Cross-reference with commit/PR dates.

## What to return

For each relevant item:
- Type (dashboard / monitor / metric / log pattern / trace / incident / notebook)
- Title or name
- Link or identifier (dashboard ID, monitor ID, metric name, incident ID)
- Owner/author and created/modified date
- The specific condition, query, or quote that bears on the question (verbatim where possible)
- Relevance: what this suggests about the target code, and how strong the connection is
