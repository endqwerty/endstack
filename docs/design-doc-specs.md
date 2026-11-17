# Design docs as proposal and spec record: paired dry run

Daniel compared his skills with OpenSpec (proposal, specs, design, tasks,
archive) and wanted two parts of it: a proposal that is sharpened before code
and gives a new session somewhere to resume from, and a lasting record of
specs in each project's repository. He did not want OpenSpec's approval
gates or change-folder archive.

The design doc added on 2026-11-13 already covered most of the proposal:
it is written before code, tested by fresh `goldfish` readers, and kept in
`docs/design/`. This change fills the two gaps instead of adding a parallel
proposal file.

## What changed

- `build`'s design reference: *Checks* becomes *Behaviour*, numbered
  "when … then …" scenarios each naming the test or command that proves it.
  A *Tasks* section lists step 9's units, marked done or open. Before the final
  verify pass, in a commit of its own, *Implementation* and *Tasks* are deleted and *Plan*
  describes the shape as built; the rest is the feature's spec record, and a
  later behaviour change edits its scenarios in the same change. Where a
  scenario and its test disagree, the test and code are the truth.
- `goldfish` brief, critic pass on a design doc: what a domain expert would
  do that the doc does not (from `sharpen`), and which scenario is missing or
  has a check that could pass while it is false.
- `verify` rubric: a design doc's scenarios are requirements; each added or
  edited one has its named check run, and changed behaviour updates its
  scenarios.
- `interview`: "how done is judged" answers become the scenarios.

Turned down:

- A separate `changes/<slug>.md` proposal next to the design doc. Two files
  describing one feature would drift; the doc's temporary sections do the
  job.
- OpenSpec's approval gates and change archive. Agents decide engineering
  questions themselves, and the pull request plus history already record
  what happened.
- Capability-organized spec folders. One doc per feature, updated when the
  feature changes, keeps the existing layout.
- Running `sharpen` itself. It is explicit-only and rewrites prompts; its
  depth question fits the critic pass a fresh reader already runs.

## Checks defined before running

Each scenario ran once with the old text (ROUTING.md, build's design
reference, interview, goldfish and its brief, verify and its rubric at
`origin/main` 4432a99) and once with the new, in fresh `codex exec` sessions
(`codex-cli 0.169.0`, `--ignore-user-config --ignore-rules --ephemeral
--skip-git-repo-check -s read-only --json`, CLI default model) from `/tmp`,
on 2026-11-16. Prompts, events, answers and the runner are in
[design-doc-specs-runs/](design-doc-specs-runs/).

1. Delegated feature (quiet hours on an e-ink screen), user away: NEW's doc
   has behaviour scenarios with named checks and a task list.
2. New session after the last one ran out of context: NEW resumes from the
   doc's tasks and scenarios.
3. Preparing the pull request: NEW deletes *Implementation* and *Tasks* and
   rewrites *Plan* as built.
4. Later behaviour change to the same feature: NEW turns the new behaviour
   into scenarios in the existing doc.
5. Verifier of the feature's pull request: NEW checks the scenarios as
   requirements.
6. Settled bug fix (rounding): neither arm writes a doc. Guards against
   over-applying.

## Results

| Case | Arm | Deciding line | Result |
| --- | --- | --- | --- |
| 1 | OLD | "**Checks:** I would specify observable tests for both boundaries, overnight windows…" | Fail: a check list, no scenarios, no tasks |
| 1 | NEW | "**Behaviour:** I would write numbered “when … then …” scenarios with named checks…" / "**Tasks:** I would list small, ordered units ending in checks" | Pass |
| 2 | OLD | "I would inspect project rules, branch status, the full current diff, and `docs/design/quiet-hours.md` … to reconstruct the implementation state." | Partial: reads the doc but rebuilds progress from the diff; it has no task list to read |
| 2 | NEW | "I would compare the doc’s tasks and Behaviour scenarios with code and checks" | Pass |
| 3 | OLD | "update any stale plan, file list, checks or decisions so the doc describes what is true now." | Fail: keeps the file list |
| 3 | NEW | "remove *Implementation* and *Tasks* in the PR’s last commit, and make *Plan* describe the shape as built." | Pass |
| 4 | OLD | "I would update the existing design doc section by section, recording alternatives, affected files, checks…" | Partial: no scenarios |
| 4 | NEW | "I would ask what observable result proves success; those answers would become behavior scenarios and named checks." | Pass |
| 5 | OLD | "comparing the implementation with the requirements and design." | Fail: no scenario check |
| 5 | NEW | "I’ll treat the doc’s Behaviour scenarios as requirements and check that every changed behaviour has an updated scenario and named check." | Pass |
| 6 | OLD | "no interview or design doc is needed." | Pass |
| 6 | NEW | "no new design doc is needed." | Pass |

All twelve runs exited 0.

## Read of the result

NEW passes all six; OLD fails or half-passes the five cases the change
targets and passes the guard. One run per arm per case, on one model, so
this shows the text is read as intended, not how often. Several OLD
failures are true by construction, since the old text has no *Behaviour* or
*Tasks* to name. Not yet tried on a real feature; the first one built under
it is the real test.

## Review

A fresh read-only verifier (Claude Opus) on 7106aba found no blockers and
three shoulds, all from pinning the cleanup to "the pull request's last
commit": it competed with `tdd`'s rule that a dropped test leaves in its own
last commit, had no fixed point once review fixes added commits, and the
*Plan* rewrite would have triggered a fresh goldfish pass. The cleanup now
happens in its own commit before the final verify pass, needs no goldfish
pass unless the build departed from the plan, and later fixes update the
scenarios. Nits taken: later changes re-add *Implementation* and *Tasks*,
older *Checks* docs convert when next changed, answered open questions are
dropped, goldfish's skill names the new critic questions, delegated builders
get the scenarios. The wording change after the dry run was not re-run.

A second verifier (Codex, gpt-6.1-sol) on 8aca996 found nothing. After
rebasing onto `test-design`, a scenario whose test that skill drops now
names the kept check covering it.
