# Upstream review at de8ee15 (2026-11-10)

## Why and scope

Daniel asked to review upstream, take useful new concepts, and trim existing
skills where the changes give a concrete reason. Review covers the 23 commits
from `190d287` through `de8ee15dd1194627d21eb5fcd41cb1873208dabb`
touching `pstack`. Source is a read-only local clone. Baseline endstack is
`4897ee1a3c72ccc742aa5e50452bfd9b155a278b`.

This author works sequentially under the coordinator's explicit no-subagents
instruction. Swarm's decomposition was considered, but delegation is excluded.
Build shapes delivery, verify keeps agent-instruction changes subject to fresh
review, and correct prevents turning presentation preferences into checkers.
How and why inform the local flow and history inspection. Technical-writing
and unslop shape this report. The coordinator owns independent verification
and all commits, pushes and PR work.

## Checks defined before skill edits

- Both skill and routing checkers must report `0 problem(s)`.
- All script unit tests must pass. Every core entrypoint must remain below
  2200 bytes and every imported entrypoint below 6000 bytes.
- Inspect the whole diff, links, invocation metadata and unchanged routing.
- Run one tool-free paired scenario per new behavior: goal restatement,
  cache destination before approval, rejected candidate seats, and the
  measurement decision before running. Without arms omit the changed skill;
  with arms receive its complete relevant text. Keep prompts and raw output.
- No new review exemption: changed agent instructions require a fresh verdict
  from the coordinator's independent reviewer before delivery.

Baseline checks passed: both checkers `0 problem(s)`; unit tests `Ran 17 tests`
and `OK`, with existing unclosed-file ResourceWarnings.

## Progress

Read the required repository and previous-port documents, all current target
skills, upstream patches and changed-path summaries. Statechart remains an
external homelab pin, not code to import here. This author adds no new skill. Daniel subsequently chose Ketchup Video and Orchestrate; their separate W8 port owns those additions.
The decisions and completed run results are recorded below.

## Per-commit decisions

| Commit | Decision and reason |
| --- | --- |
| `c742dd6` | Taken, ported separately (W8). Daniel chose Orchestrate after the initial review. The separate author owns portable standing-program coordination and its overlap with existing bounded autonomy. |
| `ab1f702` | Adapt. Take goal restatement, rejected runner handling and pre-run decisions. Keep endstack's evidence and review policy; details below. |
| `519d36a` | Leave. Statechart process-reaping test belongs to the external code pin. |
| `164ced1` | Leave. Upstream package version only. |
| `740d2c0` | Leave. Qualified action-name compiler fix belongs to the external statechart pin. |
| `7c7bde7` | Leave. Upstream package version only. |
| `34b1b7c` | Leave. Statechart compiler code import is outside this portable skill repository. No homelab pin update is implied. |
| `e73df47` | Leave, already satisfied. Endstack's swarm Phase A is numbered 1-5 and has no missing-table reference. |
| `a0b0ad9` | Leave. Marketplace auto-update instructions do not describe homelab's reviewed-revision distribution. |
| `f83fbe6` | Leave. GNU transcript timestamp handling is in the uninstalled worktree-audit script. |
| `3c596e7` | Leave. Active-PR selection is in an uninstalled Orchestrate store, later removed upstream. |
| `86c2448` | Leave. Inline-code delimiter parsing fixes an uninstalled plan-checking script. |
| `fe096ef` | Leave. Poll deadline fix is watch-pr implementation, not a portable skill policy. |
| `96dec8e` | Leave. Fork-head stack discovery is watch-pr implementation. |
| `7054003` | Adapt. Reflect must show a durable destination before approval, copy cached skill folders there afterward, and never publish. Keep source-repository edits in their maintained source. Remove editor-specific paths. |
| `b1a1298` | Leave. Upstream package version only. |
| `3c0fdb4` | Taken, ported separately (W8). Daniel chose Ketchup Video after the initial review. The separate author owns the video presentation role and its portable rendering requirements. |
| `00d5dec` | Leave, already taken. Generated formal checks already read results with statechart, as documented on 2026-10-30. |
| `642289e` | Leave. Upstream package version only. |
| `076f4b2` | Leave. Pele renderer and statechart runtime are externally pinned code. |
| `4ec7ffa` | Leave. Statechart helper/comment refactor belongs with that code. |
| `7698375` | Leave. Statechart runtime fixes belong with that code. |
| `eb4db2b` | Leave, concept already adopted separately. Checked state diagrams route to the external statechart skill; do not duplicate it here. |

### Decisions within ab1f702

| Concept | Decision and reconciliation |
| --- | --- |
| Restate the user's goal in first message, briefs, PR rationale and final report | Adapt into technical-writing, already routed for prose, with the one-line final-report exception. One owner avoids repeating the same wording in build, autopilot-full and swarm. Keep the evidence-rules-out-change stop. |
| Block PRs only on demonstrated failures or wrong shipped docs | Leave local policy intact. Verify already requires reachable evidence, distinguishes base defects and has a calibrated rubric. Interrogate also accepts code traces and structural simplification evidence. A failed required gate or unproven safety fact must still hold delivery. |
| Wording-only changes get no verifier | Adapt by retaining verify's existing review-scope policy. Ordinary prose may qualify for a recorded exemption; agent instructions, including these skill edits, cannot. No blanket exemption and no new text needed. |
| Push each finished unit | Leave. Build already owns delivery through a PR. Publishing cadence belongs to the authorized delivery workflow, not an unconditional push rule that could override a delegated author's no-push boundary. |
| Autopilot-stack becomes full autopilot minus merge | Leave. There is no installed autopilot-stack. Build and babysit preserve readiness without landing; a sixth delivery role adds no demonstrated need. |
| Interrogate keeps only findings proved by runs and rerun by lead | Leave the run-only rewrite. The 2026-11-02 endstack policy already demands evidence and allows checkable traces, design evidence and unresolved safety concerns. Removing those would lose useful review coverage; keeping independent reviewers read-only matters too. See [local decision](2026-11-02-evidence-over-dissent.md). |
| Rejected Arena runner seats | Adapt into an authorized replacement or disclosed dropout, at least two independent attempts for a comparison unless explicitly specified otherwise. No model names, hardcoded defaults or silent family changes. Runtime constraints still win. |
| Arena judge must be from another family, otherwise skipped | Leave. Endstack expressly makes family diversity optional. Fresh independent context qualifies. Existing sequential fallback discloses that it is self-judgment, and verify remains a separate gate. Do not add a skipped-judge branch that only exists because of the rejected family requirement. |
| Ketchup Video refinements | Taken, ported separately (W8), together with the new skill Daniel chose. This author makes no edits to that port. |
| Write the measurement decision before running | Adapt into explain-the-number and link from benchmark-checklist, which routing already selects. State the result that changes a decision and noise floor; when spread exceeds effect, stop claiming a difference, rather than forbid useful diagnostic runs. |
| Store wording, setup defaults, background execution and stacked rebases | Leave store and tool/model routing changes to their owners. Patch carry-forward already lives in verify's carry-forward reference. Parent-branch topology is recorded in docs/verify-carry-forward.md and the uninstalled stack candidate; copying command-specific rebases into an installed role would add topology policy outside its bounded job. |

## Trim and refactor decisions

Made one core trim: autopilot-full refers to build's already-composed design
step without repeating its reference path and reading instruction. It still
requires the step before any code or brief and passes the note to participants.
The design note's production and contents remain owned by build. No authority
or verification gate was removed.

The goal rule has one owner in technical-writing. The measurement policy has
one owner in the principle reference, with the benchmark checklist explicitly
applying it at the routed entry point. The routing index needs no change.

Considered and rejected:

- Merging build, autopilot-full and verify instructions would erase distinct
  implementation, autonomy and independent-check roles. Their short links are
  useful composition, not duplicated procedures to inline or delete.
- Replacing interrogate's rubric with verify's would collapse a design panel
  into a delivery verdict and lose structural findings and explained
  dismissals. Upstream's deletion changes substance, not just size.
- Removing Arena's dissenter would confuse competing design synthesis with
  the review dissenter already removed locally. Keep the distinction recorded
  on 2026-11-02.
- Deleting reference-only candidates or repairing intentionally dead upstream
  links would turn this review into maintenance of uninstalled snapshots.
- Existing benchmark questions and principle evidence rules overlap because
  one is a procedure and one explains judgment. Keep them, sharing only the
  new pre-run rule through a link.
- No skill was over budget at baseline. Do not shorten imported identities
  and frameworks just to make the diff larger.

This author adds, renames or removes no skill and leaves README, cookbook and
ROUTING.md to the coordinator. The separate W8 port adds Ketchup Video and
Orchestrate at Daniel's direction. Its index integration belongs to the
coordinator, including matching homelab's routing copy when ROUTING.md changes.
The candidate copies remain historical reference data, not refreshed upstream
mirrors. The external statechart pin and its new compiler were not tested or
updated by this work.

## Dry runs

All four predeclared with/without pairs completed, using supplied policies in
scratch, with no tools. Prompts, complete answers, JSONL events, environment
flags, deciding quotes and reproduction command are in
[the run records](upstream-de8ee15-runs/README.md).

- Goal: both arms preserve the goal in all four requested artifacts. No uplift.
- Cache: both arms show a local destination, wait for approval and avoid
  publication. With explicitly copies the whole folder. No outcome uplift.
- Seats: both arms replace the rejected runner when authorized and disclose
  incomplete comparison if no replacement starts. No uplift.
- Number: with explicitly records the unresolved decision threshold and
  unknown noise floor before running; without asks for a controlled test.
  Both decline adoption on the noisy hypothetical result. Planning detail
  changes in this sample; no adoption-outcome uplift.

No dry run is needed for the autopilot reference trim: the before/after both
require build's design step before code or briefs and pass its note to every
participant. The instruction remains explicit; only its duplicated link and
reading wording are removed. No intended behavior changes in that trim.

## Checks and limits

Final authored-text checks:

| Check | Deciding output |
| --- | --- |
| `python3 scripts/check-skills.py` | `0 problem(s)` |
| `python3 scripts/check-routing.py` | `0 problem(s)` |
| `python3 -W ignore::ResourceWarning -m unittest discover -s scripts` | `Ran 17 tests`, `OK` |
| `git diff --check` | No output, exit 0. |
| All entrypoint sizes | 29 checked; core maximum 2196 bytes, imported maximum 5900 bytes. |

The initial unsuppressed suite also passed and emitted existing unclosed-file
ResourceWarnings; final repeat hides only those warnings. No test or checker
was changed. Inspection of this author's diff confirms invocation metadata and routing
unchanged by this port. This author leaves ship and cookbook untouched; the coordinator's separate ship
work is outside this author's scope. The changelog has an independent dated
section for this port. W8's new skill directories and port reports also belong
to the separate author; this review records their acceptance without
claiming their implementation or validation.

These are skill-instruction behavior changes, so this author claims no
review exemption. Fresh read-only review is still required from the
coordinator before calling the overall change verified. No commits, pushes
or PRs were made by this author. No installed caches or homelab files changed.

Not checked: live cache installation and precedence, runner launch and
replacement, actual benchmark behavior, automatic skill discovery, other
providers, external statechart runtime and homelab's pinned update. Tool-free
samples show response behavior only and share built-in CLI instructions.
One-line-edit, maintained-source and single-requested-candidate exceptions
were inspected in text but not separately dry-run. No measured outcome uplift
is claimed for three pairs; the fourth shows planning detail only.
