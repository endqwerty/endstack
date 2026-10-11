# Investigator roster

Each category below is uniquely positioned to surface one shape of "why", shown after "Best at". Use it to know what to expect back, to name a gap when a category returns empty, and, only in the rare provably-irrelevant case, to justify a skip.

1. **Source control** (history, PRs, code comments, tests). Always assign this investigation; report missing history as an access gap. Best at *implementation-time rationale captured during review*.
2. **Issue / ticket tracker**. Best at *the product or business forcing function*. Strongest when the why is external to engineering.
3. **Long-form documents**. Best at *long-form design rationale*, written out before it becomes code.
4. **Real-time team chat**. Best at *real-time deliberation that never reached a doc*. Especially important when the source control, ticket, and doc paper trail is thin.
5. **Infrastructure observability**. Best at *infrastructure and runtime reality that motivated the code*. Strongest when the target reacts to an infra signal (timeouts, retries, rate limits, circuit breakers).
6. **Error / exception tracking**. Best at *the specific exceptions and error trajectories that motivated defensive or corrective code*. Strongest for catch blocks, null guards, type checks, retries, and other defenses.
7. **Product analytics warehouse**. Best at *product and data reality that shaped the code*. Strongest for flag-gated code, experiment-driven ships, data migrations, and "where did this number come from" questions.

