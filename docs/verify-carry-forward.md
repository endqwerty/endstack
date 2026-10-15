# Verify: carry a verdict forward

## Why (2026-10-14)

homelab's `skill-usage` review of every verification thread on both machines:
173 of 297 rounds after the skills were re-verifications, and on omarchy 23
re-checked code the verifier itself called unchanged after a rebase ($26
API-equivalent). Examples: "only the requested sentence changed" checked with
nine CI jobs; application files "100% identical" to the previous round. The
rule "Any revision change needs a fresh verdict" (check 9 of
[verify-gate-checks.md](verify-gate-checks.md)) forced a full round for each.
Daniel asked to stop re-verifying unchanged code.

## What changed

- A re-review covers what changed since the last verdict and what that can
  affect, not the whole change again.
- A verdict carries forward when the new revision only rebased the change
  unchanged onto a base that touches nothing it uses, or only edited docs or
  comments. The author records that evidence and reruns the required checks.
  Anything else, including a one-character code change, still needs a fresh
  verdict. Check 9 of the gate now reads that way; the rest of the gate (a
  review limit is not approval, not-checked is not a pass, blockers stop
  delivery) is unchanged.
- `ship` and `autopilot-stack` point at verify for when a verdict carries
  forward. homelab's global rule says the same.

## Dry run

Six scenarios, each decided by GPT 6.1 Sol (medium effort) holding only the
old or the new `verify` text, no tools. Deciding lines:

| Scenario | Old text | New text |
| --- | --- | --- |
| Rebase, diff byte-identical, main touched unrelated files | "A new independent verifier round is required" | "No new independent verifier round is required: the r1 verdict ... carries forward" after rerunning required checks |
| Rebase, diff identical, main changed `validate_token()` the change calls | fresh round | fresh round: "r1's verdict cannot carry forward despite the byte-identical diff" |
| Only a README sentence fixed after a pass | fresh round on "the whole endpoint change" | "No new independent verifier round is required for this docs-only correction" |
| Blocking bug fixed in a 20-line diff of a 900-line change | review "the full change through r2 ... not just the 20-line fix" | "covers the retry-loop fix and everything it can affect" |
| `>` changed to `>=` after a pass, called non-material | fresh round | fresh round: "qualifies for neither carry-forward exception" |
| Two-round limit reached after a material fix | cannot merge | cannot merge: "The two-round plan limit does not grant approval" |

The new text skips the two rounds the measurement called waste and keeps every
round that guards behaviour. A dry run is the model's stated decision, not an
observed delivery.
