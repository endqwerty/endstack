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
  unchanged onto a base that touches nothing it uses, or only edited prose
  that no tool or agent reads as instructions (not a lint directive, not an
  agent's rules or skills). The author records that evidence and reruns the required checks.
  Anything else, including a one-character code change, still needs a fresh
  verdict. Check 9 of the gate now reads that way; the rest of the gate (a
  review limit is not approval, not-checked is not a pass, blockers stop
  delivery) is unchanged.
- `ship` and `autopilot-stack` point at verify for when a verdict carries
  forward. homelab's global rule says the same.

## Dry run

Each scenario decided by GPT 6.1 Sol (medium effort) holding only the old or
the new `verify` text, no tools. The new-text column is the final wording,
rerun after independent review (round 1) showed that "only edited docs or
comments" let a lint directive skip review; the last two rows were added
then. Deciding lines:

| Scenario | Old text | New text |
| --- | --- | --- |
| Rebase, diff byte-identical, main touched unrelated files | "A new independent verifier round is required" | "The r1 independent verdict carries forward, so no new independent verifier round is required" after rerunning required checks |
| Rebase, diff identical, main changed `validate_token()` the change calls | fresh round | fresh round: "the verdict at r1 cannot carry forward because main changed `validate_token()`" |
| Only a README sentence fixed after a pass | fresh round on "the whole endpoint change" | record "that no tool or agent reads that prose as instructions", rerun checks: "no new independent verifier round is required" |
| Blocking bug fixed in a 20-line diff of a 900-line change | review "the full change through r2 ... not just the 20-line fix" | "the review should cover the retry fix and anything it could affect" |
| `>` changed to `>=` after a pass, called non-material | fresh round | fresh round: "calling the tweak non-material does not qualify for either exception" |
| Two-round limit reached after a material fix | cannot merge | "No. The two-round limit does not approve r3" |
| Only a `# ruff: noqa: E501` comment added | not run | fresh round: "a tool instruction that changes lint behavior, so the prose-only exception does not apply" |
| Only AGENTS.md edited (agents' rules) | not run | fresh round: "AGENTS.md controls how agents deliver changes; it does not qualify" |

The new text skips the two rounds the measurement called waste and keeps every
round that guards behaviour, including prose that tools or agents follow. A
dry run is the model's stated decision, not an observed delivery.
