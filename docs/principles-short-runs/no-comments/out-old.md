1. KEEP (licence header). Text: `// Copyright 2026 Acme Inc. Licensed under the MIT License.`
2. KEEP (shebang). Text: `#!/usr/bin/env node`
3. DELETE (restates the code).
4. KEEP (interface doc on an exported public API). Text: `/** Returns the order total in cents. Throws if any order is negative. */`
5. KEEP (hazard in something we cannot change, no check can catch it). Rewritten to the one-line WARNING form: `// WARNING: Safari 17 drops the first `resize` event after a rotation, so we listen twice. See https://bugs.webkit.org/show_bug.cgi?id=271234`
6. DELETE. It is a constraint on our own code (warm the cache before start), not something we cannot change. Encode it instead (for example, make start() warm the cache itself or fail with a message stating the reason), pending approval. If not approved, delete and report the constraint as open and unenforced.
7. KEEP (formatter directive). Text: `// prettier-ignore`
8. KEEP as a coverage directive, but audit: debugDump is an empty function, so the ignore guards dead code. Text: `// istanbul ignore next`
9. DELETE. This is rationale and belongs in the pull request. The API's string ids are outside our control, but no check is claimed, so it does not need a WARNING comment. If it is kept, it must be `// WARNING: the API returns ids as strings until v3`.

MUST KILL flags:
- (6) `IMPORTANT: do not remove` is a constraint comment about our own code. Kill it, offer an encoding, and report the constraint open if it is not approved.
- (3) restates the code. Kill it.
- (9) a rationale comment. Kill it and move the tracking link to the PR.
