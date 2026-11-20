Note on method: this harness has no separate workers, so I ran the investigator and synthesizer roles myself in sequence. The only evidence was the supplied record, which covers source control history and PR discussion. I read no other source.

### The Question

Why does `sync/client.go` retry exactly 7 times with a 250 ms base backoff, and is it safe to drop the count to 3?

### The Code in Question

`sync/client.go`: `const maxRetries = 7` and `const baseBackoff = 250 * time.Millisecond`. Both come from commit a91f3c2 (2025-03-04). Commit 4be0d17 later added jitter to the backoff.

### What We Found

- **[Direct]** The retry exists because the partner gateway returns 503 during its nightly rotation. Source: PR #812 (Priya): "Partner gateway returns 503 during their nightly rotation, which lasts up to ~25s... Without this, the 02:00 sync fails every night." Commit a91f3c2 is titled "sync: retry on 503 from partner gateway (#812)".
- **[Direct]** The count of 7 was chosen to outlast that window. Source: PR #812 (Priya): "Exponential backoff from 250ms with 7 tries covers ~32s total."
- **[Direct]** A reviewer asked for a lower cap and the author declined. Source: PR #812 review. Marco: "Could we cap at 5? 7 feels high." Priya: "5 only covers ~8s, the rotation is longer. Keeping 7."
- **[Direct]** Jitter was added later for a different reason. Source: PR #1104 (commit 4be0d17, Sam): "Thundering herd from 30 workers retrying in lockstep after gateway blips." That PR does not discuss the retry count.

### What We Can Reasonably Infer

- **[Inferred]** Dropping to 3 retries would likely leave the nightly sync failing whenever it hits the rotation. Reasoning: the author's own figures say 5 retries cover about 8s against a rotation of up to ~25s. Doubling from 250 ms, 3 retries wait 250 + 500 + 1000 ms, about 1.75s, which is shorter still. That sum is my arithmetic, not a figure from the record. The record also does not say whether jitter changes the total.
- **[Inferred]** The gateway "blips" in #1104 suggest the retries also absorb short outages at other times. The PR does not say how long they last.

### Competing Hypotheses

- **Hypothesis:** 3 is safe because the partner has since shortened or removed the rotation.
  - Evidence for: nothing in the record.
  - Evidence against or missing: the record says nothing about whether the rotation still happens, so this is open, not supported.
- **Hypothesis:** 3 is unsafe because the rotation is unchanged.
  - Evidence for: PR #812's rationale and Priya's rebuttal of the cap at 5.
  - Evidence against or missing: that evidence is from 2025-03 and may be stale. No later source confirms the rotation.

### What We Don't Know

- Whether the partner's nightly rotation still occurs, and how long it lasts now. This is the deciding fact for the question about 3, and the record does not contain it.
- The exact total wait with jitter applied. I did not see the jitter change.
- Whether the 02:00 sync has failed or succeeded recently. No logs or error data were available.
- Whether anyone has discussed the retry count since #812. No other commits touch these lines, and the record has no tracker links.
- Who would know: Priya (author of #812) and Sam (author of #1104). The partner's integration contact could confirm the rotation.

### Sources Consulted

- **Source control history**: `git blame` on both constants, commits a91f3c2 and 4be0d17, PRs #812 and #1104, and the #812 review thread. No other commits touch these lines.
- **Issue / ticket tracker**: Not searched. The record has no issue links and no tracker integration was available.
- **Long-form documents**: Not searched. No matching source was available in this environment.
- **Real-time team chat**: Not searched. No matching source was available in this environment.
- **Infrastructure observability**: Not searched. No matching source was available, so recent gateway 503s could not be checked.
- **Error / exception tracking**: Not searched. No matching source was available.
- **Product analytics warehouse**: Not searched. No matching source was available.

### Confidence Summary

The reason for 7 retries and the 250 ms base is well supported by direct PR evidence: they were sized to outlast a rotation of up to ~25s. Whether dropping to 3 is safe turns on whether that rotation still exists, which the record does not say. Given the 2025 evidence, 3 retries would cover only about 2s, so I would not drop it without first confirming the partner's current behaviour or checking recent logs.

### Constraints if you change this

- **Preserve:** a total backoff window longer than the rotation (~25s as of #812), or the 02:00 sync fails.
- **Change:** the retry count or base only after confirming the rotation window has changed.
- **Avoid:** removing jitter. It exists to prevent lockstep retries from 30 workers (#1104).
- **Risk:** a nightly failure of the 02:00 sync if the rotation still lasts longer than the new window.
