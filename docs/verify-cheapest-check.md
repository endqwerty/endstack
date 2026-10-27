# Verify: the cheapest check that catches a finding

## Why (2026-10-27)

In Mainworthy, unit tests were 32 of 231 test files and 0.2% of the test time;
browser tests were 39% of it and 45 of 66 `flaky-test` issues (Mainworthy
#1010). A finding seen in a browser tended to get a browser test even when its
cause was pure logic. Daniel, on that item: "4 is critical". Mainworthy's own
rule and check are in Mainworthy #1012; this puts the same rule in `verify`,
which every project's author follows.

## What changed

Author step 5: "Fix blockers and shoulds with the cheapest check catching them
again" (was "with a check that catches them again"). To fit the 2,200-byte
limit, "the current revision" became "this revision" in the same step. Nothing
else changed. The dry run below ran on the step's earlier wording ("Fix each
reachable finding with the cheapest check that catches it again"), before
findings were ranked; the instruction about the check's layer is the same.

## Dry run

One GPT 6.1 Sol (medium) author per side, holding only the old or the new
`SKILL.md`, no tools, asked which test to add for a confirmed finding: a merged
step keeps a deleted last line, seen in the browser, caused in the pure
`merge3()`. The repository has unit tests (0.3 s), database tests (6 s) and a
browser file (43 tests, 27 s, most flaky-test issues).

| Old text | New text |
| --- | --- |
| A unit regression in `merge3.test.ts`, and "in `test/e2e/conflict-merge.test.ts`, add or extend one targeted Chromium test reproducing the verifier's two-editor sequence" | A unit regression in `merge3.test.ts`: "This is the cheapest check at the faulty pure function. Add no database or browser tests"; then "Rerun the confirmed browser reproduction against the fixed artifact" |

One run per side, so a sample, not a rate. Not exercised: a finding that only a
browser can show, where the cheapest check is a browser test.
