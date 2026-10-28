# Scoped recheck: Anthropic review proposal, round 2

Verifier: Claude Opus 5.5, read-only, fresh context, no subagents. The author
ran on Codex (per round 1's transcript metadata), so the provider differs.
I read round 1's verdict, the incremental diff, the full patch and the
affected context. I did not read the author's reasoning.

## Identity

| Item | Value |
| --- | --- |
| Head judged | `7784b24ab1272aeec0a1e402e4ab2a32186863b6` (HEAD, working tree clean) |
| Previous verdict head | `606bf73093108b69a14eedad844f2749da7f8948` (review-round-1.md, ISSUES) |
| Original base | `6136a6b5cf83cf4361ddda03c8b445375d22aa5a` |
| Base..head | 23 files, 1123 insertions, no deletions; `git patch-id --verbatim` `e8d3bcadbd04eb24e4f9d751045cec89a89f311c` |
| 606bf73..head | 5 files (proposal, experiment.md, final-rubric.md new, review-round-1.md new, verify.patch); patch-id `024d5f912b0890e0767f32b0695f21d9d16d5838` |
| verify.patch sha256 | `64e64e4a91b02518bc734588193b5ec267e21dc5f068b87d37fa8945006fce10` |
| proposed-policy.md sha256 | `588eda8a…` (unchanged since round 1) |
| final-rubric.md sha256 | `f54c09ec…` |
| references/review-rubric.md sha256 | `bb8b4792…` (byte-identical to the rubric round 1 judged) |

## Mechanical checks

| Check | Result | Deciding lines |
| --- | --- | --- |
| check-skills.py at head | PASS | `0 problem(s)`, rc=0 |
| check-routing.py at head | PASS | `0 problem(s)`, rc=0 |
| `git apply --check verify.patch` at head | PASS | rc=0 |
| Patch applied to a temporary `git archive HEAD` copy | PASS | `apply rc=0`; checkers there `0 problem(s)` each |
| Patched core == proposed-policy.md | PASS | `core cmp rc=0`; 2,162 bytes vs `CORE_MAX = 2200` |
| Patched rubric == final-rubric.md | PASS | `rubric-final cmp rc=0` |
| Patched rubric differs from the retained draft only at the new sentence | PASS | `cmp` differs at line 24; `diff` shows only the factual-errors sentence, with the line rewrapped |
| Live rules unchanged base..head | PASS | `git diff --stat 6136a6b HEAD -- skills ROUTING.md scripts AGENTS.md` empty |
| Temporary copy removed | done | deleted by its literal path; `ls` reports `No such file or directory` |

## F1 (should, round 1): RESOLVED

The final rubric adds: "Factual errors in evidence or requirements are
correctness defects, not wording nits." Core step 5 says "Decline nits
without edits or another round", and the core's first line makes both roles
read the rubric. So a false claim in evidence can no longer be ranked
"wording" and declined. It falls outside the nit tier, needs a fix, and
blocks delivery ("no blocker or should open"). The sentence does not say
which tier applies (blocker or should). Both block delivery, so the outcome
is the same.

No regressions found:
- Skip-style: "Skip style, naming, optional refactors, redundant tests and
  guards for hypothetical future code" is unchanged. The new sentence covers
  only factual claims in evidence or requirements, not identifiers or
  phrasing.
- Safety: the core still has "Data loss, security or a trust boundary is
  never a nit". The rubric still has "Do not label an evidenced security or
  data-loss path a nit because it is unusual".
- Required checks: both of these are unchanged: "The verifier still runs
  every required check under this policy" and "not checked still prevents a
  passing verdict when evidence is required".
- Open choices: provider gate, exemptions and trigger are untouched. The
  proposal now says the one-first-pass wording "implements the recommended
  option for the still-open extra-pass choice; it is not neutral between
  those options and is not active policy" (F3 handled by disclosure).

## Draft versus final text: PASS

- experiment.md: "The paired runs above used the earlier rubric, retained in
  references/review-rubric.md. They are not claimed as a run of the final
  text." The earlier mechanical paragraph now reads "Before independent
  review, the parent applied the tested draft patch … compared … with
  proposed-policy.md and the tested rubric."
- Proposal: "Independent review found a factual-correction gap in the tested
  draft. The experiment record separates that draft from the corrected final
  rubric." The retained draft's hash matches the one round 1 judged.

## Paper regression on the final rubric (not empirical recall evidence, not a paired run)

| Case | Disposition | Deciding text |
| --- | --- | --- |
| Incorrect factual attribution in an evidence report | Actionable defect: at least a should. Fix it; delivery waits | Rubric: "Factual errors in evidence … are correctness defects, not wording nits"; core 5: "no blocker or should open" |
| Private local-variable rename, no compatibility or contract consequence | Declined. No edit, no round | Rubric: "Skip style, naming…"; the compatibility carve-out does not apply; core 5: "Decline nits without edits or another round" |
| Guard for nonexistent future code | Declined. No edit, no round | Rubric: "guards for hypothetical future code"; core nit: "what only later code makes" |
| Demonstrated imported-data defect | Should, or blocker if the intended case fails. Fix with the cheapest check that catches it; delivery waits | Core: "Should: … stored or imported data … reaches it"; rubric: "Do not label an evidenced … data-loss path a nit" |
| Unrun required check | Not checked, not a confirmed defect. No PASS; delivery waits | Rubric: "Put a missing check … under not checked"; "A code trace … does not replace an unrun required check"; core 5: "independent pass of every required check" |
| Unchanged, fully checked artifact with no defect found | PASS with no findings. No extra reviewer; nothing invented | Rubric: "No findings is a valid result"; "not a minimum count"; "Do not add a reviewer just to seek more findings" |

All six give the intended outcome. Case 1 is the one that changed: under the
tested draft it read as a nit and would have been declined.

## Prior nits (documented, behaviour unchanged): PASS with one wording note

- F3: disclosed in the proposal (quoted above). Choice 3 still lists the
  option, and its recommendation matches the rubric. Closed.
- F2: experiment.md says "The core's 'full diff' still includes delegated
  changes; the reviewer agreed the duty is preserved." Round 1 agreed in
  substance ("ranks this as wording"). It also noted that the explicit
  "never a summary" guard is dropped, and the proposal's lists of intended
  changes still do not mention that. Nit, still open. "Agreed" slightly
  overstates round 1, and the dropped phrase is still undisclosed. It does
  not block.

## Trail rows (decisions.tsv, two appended at 2026-10-28T06:15:13Z): PASS, partial coverage

- `correction` ("Classify false evidence as correctness rather than a wording
  nit … fixed") covers F1 and the nit-allowance part of round 1's flag 2. It
  matches the rubric change.
- `clarification` ("Supersede the earlier retain-gates row: provider and
  exemption gates stay; extra-pass default is a proposal … three earlier rows
  were recorded together after the actions") covers flag 1 (the shared
  timestamp) and the over-broad `proposal` row and one-pass default in flag
  2.
- Not covered: the line-8 rewording that drops "a subagent's included, never
  a summary" (the F2 part of flag 2) is still not logged as a decision. Flag
  3 (the draft written 3 s before arm A returned) was only a process note and
  needs no row. Flag 4 (`__pycache__`) is the parent's cleanup.

## Observation (nit, outside F1's scope)

The exception covers "evidence or requirements". A false factual claim in
other prose, such as a README or how-to stating a wrong default, is not named.
The core's reach rule ("ordinary use … reaches it") would usually still make
it a should. Round 1 asked only about evidence. Not a finding against this
revision.

## Not checked

- experiment.md's "Claude Opus 5.5 at high effort" for round 1: the effort
  level is not recorded in review-round-1.md.
- No new paired run of the final rubric. That is intended and disclosed.
- I did not repeat the primary-source audit (round 1 passed it).

## Verdict: PASS

F1 is resolved without regressing skip-style, safety, required-check or
open-choice handling. Every required mechanical check passes on this head
and patch. No blocker or should is open. The open nits are the F2 wording,
which still overstates round 1 and leaves "never a summary" undisclosed and
unlogged, and the observation above.
