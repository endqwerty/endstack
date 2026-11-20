Apply the skill you were given to answer the question. You have no tools; the record below is all the evidence that exists. Write the answer you would give the user.

Question: why does `sync/client.go` retry exactly 7 times with a 250 ms base backoff, and is it safe to drop it to 3?

Record:
- `git blame` on the constants: `const maxRetries = 7` and `const baseBackoff = 250 * time.Millisecond` both from commit a91f3c2 (2025-03-04, author Priya), message: "sync: retry on 503 from partner gateway (#812)".
- PR #812 body (Priya): "Partner gateway returns 503 during their nightly rotation, which lasts up to ~25s. Exponential backoff from 250ms with 7 tries covers ~32s total. Without this, the 02:00 sync fails every night."
- PR #812 review comment (Marco): "Could we cap at 5? 7 feels high." Reply (Priya): "5 only covers ~8s, the rotation is longer. Keeping 7."
- Commit 4be0d17 (2025-09-18, author Sam), message: "sync: add jitter to backoff (#1104)". PR #1104 body: "Thundering herd from 30 workers retrying in lockstep after gateway blips." No discussion of retry count.
- No other commits touch these lines. No issue tracker links. Nothing in the record says whether the partner's nightly rotation still happens.
