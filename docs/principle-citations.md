# Principle groups and step citations

Why: pstack's router listed every principle with its trigger on every task,
required the agent to name each principle that shaped a decision, and its
playbooks cited a principle at the step it governs. The endstack port kept the
23 principle bodies but only `architect`, `figure-it-out`, `reflect`,
`show-me-your-work` and `typescript-best-practices` cite any. `build` and `tdd`,
the skills most changes run through, cite none, and the index lost upstream's
five groups because the grouping lived in the router, not in the principle
directories that were ported.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes.
   `build` stays under the 2200-byte cap for a core skill.
2. Index integrity, by script: the index links each of the 23 files in
   `skills/principles/references/` exactly once; the groups and their order
   match the Principles section of `candidates/poteto-mode/SKILL.md` (Prove It
   Works excepted, which `verify` replaced); every trigger phrase is unchanged
   from `main`.
3. `ROUTING.md` is unchanged, so the copy in homelab still matches.
4. Dry run, with and without the change (method below). Two tasks in a scratch
   repository, prompts that name no skill and no principle:
   - **feature:** add pause and resume to a job class that tracks its state in
     three booleans.
   - **bug:** a report crashes on an expired job. The cause is a queue method
     that marks a job failed without recording an error; a second method has
     the same fault. A guard in the report hides it.

   Pass for the "with" arm: the transcript shows the agent reading the
   reference cited at that step (`model-the-domain.md` for the feature,
   `fix-root-causes.md` for the bug) before its first edit to production code,
   and the final reply names the principle and the choice it changed. No reply
   names a principle whose reference the transcript does not show being read.

   Observed and reported, not pass or fail: the code shape (one state value or
   a fourth boolean; a fix at the cause in both methods or a guard in the
   report). The "without" arm is reported as it comes out. If it already reads
   the principles through `ROUTING.md`, the change shows no uplift on that task.

## What changed

- `skills/principles/SKILL.md`: the 23 lines are regrouped under upstream's
  Core, Architecture, Verification, Delegation and Meta, in upstream's order,
  with the trigger phrases untouched. Verification gains one line saying Prove
  It Works is `verify`. The index now carries upstream's rule: name each
  principle that shaped a decision and the choice it changed, and cite only
  principles whose reference you read this session.
- `skills/build/SKILL.md`: one bullet tells the agent to read a principle
  before the step it governs (`fix-root-causes` for a bug, `model-the-domain`
  before stateful or branchy logic, `sequence-verifiable-units` when ordering
  units and commits) and to report each one that changed a choice. These are
  the principles upstream's feature and bug-fix playbooks cite. 2131 bytes.
- `skills/tdd/SKILL.md`: steps 1, 3 and 4 cite `fix-root-causes`,
  `test-behavior-not-implementation` and `sequence-verifiable-units`. Step 4
  also takes upstream's bug-fix rule that the failing test is committed before
  the fix. The reply names each principle that changed a choice.

Turned down:

- Listing every principle with its trigger in `ROUTING.md`, which is what
  upstream's router did. It is the strongest version, but the list is about
  2.5 KB on every turn and `ROUTING.md` is capped at 2.6 KB.
- Citing principles from `verify`. It has 30 bytes of room under its cap.
- Citing from the other imported skills. `architect` and `figure-it-out`
  already do. The rest wait until a miss shows the need.

## Dry run (2026-10-12)

Method: Claude Code (Sonnet 5.5, medium effort) headless in a fresh clone of a
scratch repository, two samples per cell. The run uses the installed global
rules, `ROUTING.md` included. Its tools are limited to shell, file read, edit,
write and search, so it has no skill tool and no subagents. The repository's
rules name the skills directory for the run: `main` at `110d7cb` (without) or
this branch (with). The repository has no remote and forbids starting a
verifier. An isolated config directory, as used in
[pointer-only-checks.md](pointer-only-checks.md), was not available because it
is not signed in. The scratch repository and the launch script are in
[principle-citation-runs/fixture/](principle-citation-runs/fixture/) (its
rules file is stored as `AGENTS.md.txt` so it does not apply here), and each
run's tool calls, commits and reply are in
[principle-citation-runs/](principle-citation-runs/).

"Reference read" means the transcript shows the file being printed before the
first edit. "Named" means the final reply names the principle and the choice.

| Task | Arm | Skills opened | Reference read | Named | Code |
| --- | --- | --- | --- | --- | --- |
| feature | without | `build`, `principles` | `model-the-domain` and `redesign-from-first-principles`, 2 of 2 | 0 of 2 | one `state` field, 2 of 2 |
| feature | with | `build`, `principles` (one run also `architect`) | `model-the-domain` 2 of 2 | 2 of 2 | one `state` field, 2 of 2 |
| bug | without | `tdd` (one run also `principles`) | none | 0 of 2 | fixed in both queue methods, 2 of 2; failing test committed first, 0 of 2 |
| bug | with, first wording | `tdd` | none | 0 of 2 | fixed in both queue methods, 2 of 2; failing test committed first, 2 of 2 |
| bug | with, final wording | `tdd`, `principles` | `fix-root-causes` and `model-the-domain`, 2 of 2 | 2 of 2 | fixed in both queue methods, 2 of 2; failing test committed first, 2 of 2 |

Deciding lines from the replies:

- feature, with: "I replaced them with a single `state` field (the "model the
  domain" principle), so that combination can't exist. I turned down adding a
  `paused` boolean."
- bug, with, final wording: "A `None` guard in `render` would have hidden the
  crash and left those jobs with no reason recorded (the `fix-root-causes`
  principle)."

Read:

- The first `tdd` wording failed check 4. It linked each principle with "per
  the ... principle" and no run opened a link. Adding "When a step names a
  principle, read that reference before doing the step" made both runs read
  `fix-root-causes` before the first edit. A link alone is not followed; an
  instruction to read is.
- The code did not change. Every run, with or without, chose one state field
  and fixed the cause in both queue methods. `ROUTING.md` already sent the
  feature task to `principles`, and both baseline runs read `model-the-domain`.
- What changed is the reply (with the final wording it names the principle and
  the choice, 4 of 4 against 0 of 4), the references read on the bug task, and
  the commit order on the bug task (failing test first, 4 of 4 against 0 of 2).
  On the feature task the "with" runs read one reference fewer.
- No reply named a principle whose reference the run had not read.

## Not checked

- Whether the `build` bullet or the index rule caused the naming on the feature
  task. Both arms opened both files, so the run cannot separate them.
- `build` on a bug. No bug run opened `build`; all six went to `tdd`.
- `test-behavior-not-implementation` and `sequence-verifiable-units` in `tdd`:
  no run read either reference, though both "with" arms followed the commit
  order.
- A task where a principle changes the code. Both tasks were easy enough that
  the baseline got the shape right.
- Codex, a larger model, and real sessions with the skill tool. Two samples per
  cell is a sample, not a rate.
- Cost: each cited reference is 0.6 to 1.7 KB read on demand.
