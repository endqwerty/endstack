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

## 2026-10-21: a verdict covers the patch (pstack's rule)

### Why

Daniel asked for upstream's looser rule. pstack's shipping playbook (at
`190d287`, cut to principles in
[ce649c0](https://github.com/cursor/plugins/commit/ce649c0)) treats a verdict
as covering a patch, not a revision, for three reasons it states:

- In a stack, a rebase moves every request above it to a new revision
  "without failing any check", so a revision-keyed verdict goes stale on every
  rebase while the code it judged is unchanged. pstack compares a patch
  identity (`git patch-id` of the base-to-head diff) instead: cheap and
  mechanical, where endstack's "a base touching nothing it uses" was a
  judgment. But that command ignores whitespace by default, so it is not
  exact; see "Review" below.
- A base that moved under an unchanged patch is a merge-prep question, not a
  review question: "When trunk changed a caller of the patch or something the
  patch depends on, ... run the patch's checks on the merge result and merge
  on a pass" (autopilot-full step 5). "Rebasing for every trunk move never
  ends."
- When only tests, docs or lint configuration changed, the shipped artifact is
  the same, so the expensive runtime results ("lanes") still describe it. pstack
  proves "the same" by building: twice at the verdict revision and once at the
  head, so that noise (an embedded revision id, a timestamp) is told apart from
  a real difference. A lane with no build output, such as a dev server, cannot
  show this and reruns. The changed part itself still gets fresh checks and a
  review, "because the old verdict never saw it". Nothing goes unreviewed; only
  the runtime evidence is reused.

pstack also sizes the re-review: one verifier after a rebase, a conflict
resolution or a minor fix, a full panel again only for new behaviour, a
redesign or a large new diff (multi-phase-plan, autopilot-full step 4). And it
charges a defect to the change only when the change copies it or newly reaches
it; one the base already has is recorded against the base.

### What changed

- `verify` step 5 says a verdict covers the patch and points at
  [references/carry-forward.md](../skills/verify/references/carry-forward.md),
  which holds the cases: same patch on a new base (verdict stands; if the base
  changed something the patch uses, the change's checks run on the combined
  result and a pass keeps it); tests, docs or lint configuration only (built
  results stand when the build matches apart from noise, the changed part gets
  a scoped independent review); prose nothing reads as instructions (as
  before); anything else (a fresh, scoped verdict; one verifier enough after a
  conflict resolution or small fix). The author records the patch comparison;
  a claim that nothing changed carries nothing. Agents' rules and skills count
  as behaviour, not docs.
- The verifier records the patch it judged, and a defect the base already has
  is the base's unless the change copies it or newly reaches it.
- `autopilot-stack`: topology has one writer. Builders push only their own
  branches, start a dependent item from its parent's branch, and never rebase
  or retarget (pstack autopilot-stack steps 1 and 2).
- `ship`, `autopilot-stack` and the global rule already defer to `verify` for
  when a verdict carries forward; unchanged.

Turned down:

- Naming the comparison tool in the skill. Skills here name outcomes, not
  tools; the reference describes the fingerprint (the base-to-head diff,
  ignoring line offsets and commit metadata) instead.
- A `homelab` command that does the comparison and the build check. The patch
  comparison is one command any agent knows, and the build and its noise are
  per project, so a generic command would mostly take the build as an
  argument. Worth adding if verdicts are carried wrongly.
- pstack's lockfile shortcut (no rebase when a frozen install passes on the
  merge result). It needs project-specific proof and saves one rebase.

### Dry run

Each scenario decided by Sonnet 5.5 at medium effort, no tools, holding only
the old `verify` text or the new text with its reference; one sample each.

| Scenario | Old text | New text |
| --- | --- | --- |
| A. Same patch, main changed `validate_token()` the change calls | fresh round: "the base touches something the change uses" | "If those checks pass, the r1 verdict carries forward and no new verifier round is needed" |
| B. Only tests added and a docs typo fixed; binary differs only by an embedded hash | fresh round: "the rule has no exception for that" | "the r1 server-binary check still stands ... a different-provider verifier must review the two new test cases and the docs/usage.md fix" |
| C. Three lines of retry code changed after a pass | fresh round scoped to the change, "It sets no panel size" | fresh round scoped to the change; "one independent verifier" |
| D. Rebase needed a conflict resolution | fresh round | fresh round: "A conflict resolution changes the patch" |
| E. "I only rebased, nothing changed", no comparison recorded | cannot use r1: "The author's claim ... is not evidence" | cannot use r1: "a claim that 'nothing changed' without it carries nothing" |
| F. Only an AGENTS.md line telling agents to skip slow tests | fresh round | fresh round: "An agent's rules or skills ... are behaviour here, not docs" |
| G. Verifier finds string-built SQL in an untouched endpoint on main | not blocking, reported | not blocking: "A defect the base already has is the base's, unless the change copies it or newly reaches it" |
| H. Test-only edit; the earlier check drove a dev server | rerun | rerun: "A check with no build output ... cannot show this: rerun it" |
| I. Rebase plus a re-indent of `return amount` into an `if`; fingerprints from a whitespace-blind tool match (2 samples each, text at `d0abbec` vs the fix) | refuse, 2 of 2: "Ignoring whitespace is not the same thing" | refuse, 2 of 2: "a fingerprint that ignores whitespace gives an indentation change ... the same identity" |

The new text loosens exactly the two cases pstack loosens (A, B) and keeps
every other round, including agent rules (F) and an unrecorded claim (E). In
A, the new-text answer opened with "a fresh verification is needed" before
concluding the verdict carries on a pass; the decision is right, the wording
is a sample's. G and H already came out right under the old text. Row I shows no uplift
because the scenario discloses the re-indent; the fix matters when an author
relies on the fingerprint alone, which the reference now forbids for a
whitespace-blind one.

### Review

Codex GPT 6.1 Sol (medium), read-only, on `d0abbec`: **fail**. The rule as
first written followed pstack's `git patch-id`, which ignores whitespace. Two
Python patches, one returning `amount` after an `if` and one with that line
indented into the `if`, got the same identity (`927fcabc...`) while
`bill(5)` returned `5` and `None`: an indentation change would have inherited
the earlier verdict. Fixed: the identity must keep every byte of the changed
lines, whitespace included (`git patch-id --verbatim` does; reproduced here,
default `82c0e9f49cda` for both patches, verbatim `2e55bbde6f8c` and
`da4b49fd06f1`). Dry-run row I below was added with the fix.

### Not checked

- Real deliveries under the new rule. The dry run is one model's stated
  decision per row.
- Whether agents actually build twice to separate noise; nothing checks it
  but the verifier and the reviewer of the record.
