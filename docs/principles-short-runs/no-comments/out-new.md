No Comment Sicko worker is available, so I did the review myself in sequence.

1. Keep. `// Copyright 2026 Acme Inc. Licensed under the MIT License.` (legal header, unchanged).
2. Keep. `#!/usr/bin/env node` with the `// (2) shebang line` annotation removed. The shebang is code, not a comment, so only the annotation goes.
3. Delete. It restates the loop.
4. Keep. `/** Returns the order total in cents. Throws if any order is negative. */` (doc comment defining a public API contract, unchanged).
5. Keep. `// Safari 17 drops the first `resize` event after a rotation; we listen twice. See https://bugs.webkit.org/show_bug.cgi?id=271234`. The behavior comes from an external platform we cannot reshape, and the link explains a constraint the code cannot express.
6. Delete. This is a surprise in our own code, not an external constraint, so the comment goes. Flag `warmCache()` and `start()` for a redesign, such as having `start()` warm the cache itself or taking a warmed-cache type, so the ordering is obvious. The "do not remove" constraint is open until someone encodes it. Offer the cheapest in-scope encoding: a runtime assert in `start()` that the cache is warm, or a test that fails if `start()` runs cold. If approved, encode it, then delete the comment. If not, delete the comment and report the constraint as unenforced.
7. Keep. `// prettier-ignore`. It is a formatter ignore, and it keeps the matrix layout.
8. Delete. `// istanbul ignore next` is a coverage suppression on an empty function. Delete `debugDump`, which is dead, or cover it. Flag it as a lint or coverage suppression whose rule is not faulty.
9. Keep. `// Tracked in https://github.com/acme/app/issues/88: the API returns ids as strings until v3`. The API is an external dependency we cannot change, and the issue link explains a constraint the code cannot express.

MUST KILL flags:
- (3) restates the code.
- (6) is an `IMPORTANT: do not remove` comment about our own code. Delete it, flag the `warmCache()` and `start()` ordering for redesign, and report the constraint open unless the encoding is approved.
- (8) is a coverage suppression on dead code. Delete it and the function, or cover the function.
