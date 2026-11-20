## Why `sync/client.go` retries 7 times at 250 ms base backoff

**Short answer:** the record shows both constants were chosen to outlast the partner gateway's nightly 503 window. Whether 3 is safe depends on whether that window still exists, and the record does not say.

### What the record says

- Both constants came in together in commit a91f3c2 (2025-03-04, Priya), "sync: retry on 503 from partner gateway (#812)".
- PR #812, Priya: "Partner gateway returns 503 during their nightly rotation, which lasts up to ~25s. Exponential backoff from 250ms with 7 tries covers ~32s total. Without this, the 02:00 sync fails every night."
- Marco asked in review: "Could we cap at 5? 7 feels high." Priya replied: "5 only covers ~8s, the rotation is longer. Keeping 7." So a lower count was proposed and rejected on the stated grounds that it would not outlast the rotation.
- Commit 4be0d17 (2025-09-18, Sam), "sync: add jitter to backoff (#1104)", addressed a thundering herd from 30 workers retrying in lockstep after gateway blips. Its PR body does not discuss the retry count. It only added jitter.
- No other commits touch these lines. There are no linked issues.

### Is it safe to drop to 3?

**On the record, no.**

- Priya's own reasoning was that 5 tries covers only about 8s against a rotation of up to about 25s. That is the stated reason 5 was rejected. 3 tries would cover less, so by that reasoning the 02:00 sync would fail during the rotation.
- My arithmetic (inference, not quoted): with doubling from 250 ms, 3 retries wait roughly 0.25 + 0.5 + 1 = about 1.75s before jitter, far short of 25s. Priya's figures for 5 and 7 (about 8s and about 32s) are roughly consistent with a doubling schedule, so I assume the same here. The record does not show the exact schedule or whether it caps.
- Jitter (#1104) was added after the original sizing. The record does not say how it changes total coverage. Treat the 32s figure as approximate.

### What the record does not answer

- Whether the partner's nightly rotation still happens, or still lasts up to about 25s. Nothing after March 2025 mentions it.
- Whether the 02:00 sync has any other fallback (a later re-run, a queue) that would make a failed first attempt harmless.
- Whether the 503 window was ever re-measured.

### Before changing it

Dropping to 3 is safe only if the partner has confirmed the rotation is gone or much shorter. Check that with the partner or in recent 503 logs around 02:00. Without that, keep 7. If the real concern is that 7 feels high, as Marco said, the cost of a long retry is a longer wait on a failing call, which the record shows was accepted deliberately.
