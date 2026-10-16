# Lessons go into code, not into rules files

Why: endstack's skills deliver one change well, but none of the skills that run
on every task says where a lesson goes. `correct` does (architecture, then
types, then lint, then tests, then docs last), but it was loaded 3 times in 824
threads, and its route fired only on "you were corrected". The cost shows in
mainworthy: its AGENTS.md reached 33.5 KB, touched by 55 of 514 commits, much
of it dated incident notes ("On 2026-10-13 an agent ran...") that a script, a
setting or a test could hold. Every agent there pays for that file on every
request.

What changes:

- `verify`, author step 5: each real finding is fixed with a check that
  catches it again. To stay at the 2200-byte cap, the verifier's "do not
  accept the author's output" goes (running every check yourself already says
  it), and two phrases are shortened.
- `build`: one bullet after verification. A correction, or a mistake made
  before, gets the strongest guard `correct` names; a rule in an instruction
  file is for judgment only.
- `ROUTING.md`: `correct` also routes when an agent is about to add a rule to
  AGENTS.md or another agent instruction file.
- `correct`: a short "One rule" section for that case: skip the repository
  sweep, take the one mistake down the ladder, and write a rule only if the
  user asked for it (one row naming what enforces it) or it still needs
  judgment.

Turned down:

- Making `correct` model-invocable. ROUTING.md already reaches hidden skills
  by reading their SKILL.md, and the import rule keeps `disable-model-invocation`
  where the source has it.
- A deterministic check on instruction files (size, dated incident notes,
  inline shell recipes). That is deterministic work, so it belongs in the
  homelab CLI, and it is a separate task.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts -p 'test_*.py'`
   passes. `build` and `verify` stay at or under 2200 bytes, ROUTING.md under
   2600.
2. Dry run in the jobkit fixture (`docs/principle-citation-runs/fixture`),
   with and without the change, Claude and Codex, prompts that name no skill.
   Arm N gets the skills and ROUTING.md from `main`, arm S the changed ones.
   Both arms also carry the installed global rules, whose routing is still the
   old text, so arm S sees the new route in addition to the old one.
   - **rule:** "Add a rule to AGENTS.md: nothing outside the Job class sets a
     job's state fields directly; use its methods. Agents have done it twice
     and the report crashed both times."
   - **finding:** a verifier reports that `Queue.expire` sets `job.failed`
     without an error, so the report crashes on an expired job, and that the
     same fault was fixed by hand in `Queue.drain` before and came back.

   Pass for arm S: the change adds a guard that fails on the mistake (the state
   fields cannot be set from outside `Job`, or a test or check fails when they
   are), and AGENTS.md gains no rule, or only a short one that names what
   enforces it. The transcript shows `correct` read. Arm N is reported as it
   comes out: if it already encodes the lesson, the change shows no uplift on
   that task.
3. Independent review by a different provider of the whole diff and of the
   dry-run reading.

## Results (2026-10-16)

Claude Sonnet 5.5 and GPT 6.1 Sol, both at medium effort, one run per cell,
and a second run of the rule task. Scripts:
[run.sh](lessons-in-code-runs/run.sh), [score.py](lessons-in-code-runs/score.py).
"Guard" means the change makes the mistake fail: state fields made read-only,
or a test that fails on a write outside `Job`. Each guard was checked by
putting `job.failed = True` back into `Queue.expire` and running the tests.

| Task | Arm | Claude | Codex |
| --- | --- | --- | --- |
| rule | N (main) | 2 of 2: a paragraph in AGENTS.md only; `expire` and `drain` still crash the report; did not read `correct` | 2 of 2: a paragraph only; read `correct`, `build` and `verify` and still wrote prose |
| rule | S (change) | 2 of 2: guard, `expire` and `drain` fixed, report tests, one AGENTS.md table row naming the guard; read "One rule" | 2 of 2: the same; the first run also added a 4-line paragraph under the table |
| finding | N (main) | guard and tests; also added an AGENTS.md table row | guard and tests; no AGENTS.md change |
| finding | S (change) | guard and tests; no AGENTS.md change | guard and tests; no AGENTS.md change |

All twelve runs' test suites pass. Every guard failed with the mistake put back
(two failing tests in each of the four arm-S rule runs).

Reading:

- The rule task is where the change works. Asked to add a rule, no run without
  it wrote code (0 of 4) and the crash stayed. With it, every run (4 of 4)
  encoded the rule in code, fixed the cause, and wrote the rule as one row
  that names its guard. Codex on `main` read the old `correct` and still wrote
  only prose: the old skill has no case for one rule, and its rule table says
  "add the rule". That makes the "One rule" section the likely cause, but not
  an isolated one: the four files changed together and no run tested the
  section alone.
- The finding task shows no uplift. Both arms added a guard and tests; the old
  route ("a mistake recurs") already reaches `correct`, and a bug fix already
  draws a test. The only difference in these categories is that the arm-N
  Claude run also added an AGENTS.md row; the code and tests differ in detail
  between runs (for example, only arm-N Claude rejects an empty error).

## Not checked

- Two samples on the rule task and one on the finding task: a direction, not
  a rate.
- The new route was seen beside the old one (arm S's repository AGENTS.md says
  it replaces the global routing). Installed alone it is not tested until the
  homelab copy changes.
- The runs used the text at `2faf18d`. Review then restored `verify`'s
  "Never" section and changed "One rule" to say that a rule the user asked for
  is still written, as one row naming its guard. Every arm-S rule run already
  did that; the final wording was not run again.
- `verify`'s new step 5 wording was not exercised by a real verifier round:
  no verifier runs in the fixture.
- Real repositories: whether this slows the growth of mainworthy's AGENTS.md
  shows only over the coming weeks.
