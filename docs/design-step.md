# Design step: pstack's design discipline, without the mode

Why: an audit of Mainworthy (2026-10-15) found its code mostly sound, with
misses a design step catches: a fix made in the iPhone client and not ported
to the web client, a receipt type that admits impossible states, a test that
waits past a failing state instead of fixing it. The principles skill was
rarely used. Across 15 Claude lead sessions and 227 Codex sessions on this
machine, 23 opened the principles index. Three named a principle that shaped a
decision. None of 191 pull request descriptions did. Codex read only the two
principles `typescript-best-practices` links. Of 230 briefs to child agents,
two named one of these principles.

pstack got there four ways. Its mode was reminded every turn. Its index stated
each rule, not only when it applies. Its Feature playbook made the lead name
the data shape and port shared fixes to every consumer before delegating.
Every child ran as `poteto-agent`, which reads the mode and its index first.
The distillation dropped the first three because they are Cursor features or
did not fit the 2 KB cap on `build`, and the fourth because a subagent type is
a harness feature.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes.
   Core skills stay under the 2200-byte cap.
2. Index integrity, by script: the index links each of the 23 files in
   `skills/principles/references/` exactly once, in the same groups and order
   as on `main`, and every entry states a rule after its trigger.
3. `ROUTING.md` is unchanged, so the copy in homelab still matches.
4. Dry run, with and without the change, on three tasks chosen so that a
   principle should change the code, not only the reply. Prompts name no
   skill and no principle.
   - **port:** a bug report against one of two clients that share a defect
     (the Mainworthy web/iPhone miss). Pass for "with": the change fixes both
     clients, or the reply names the second one as not fixed and why.
   - **shape:** add a state to a type stored as independent nullable fields.
     Pass for "with": the result makes the new state's data required for that
     state and absent for the others (one tagged value, not another nullable
     field).
   - **brief:** coordinate a feature by writing the brief for a builder, not
     the code. Pass for "with": the brief names the data shape, the files the
     builder owns, the consumers to change, and tells the builder to read the
     principles index and the design step before writing code.

   The "without" arm is reported as it comes out. A task the baseline already
   gets right shows no uplift; it is not a failure of the change.

## What changed

- `skills/build/references/design.md` (new, 3.2 KB): the design step, read
  before the first edit to production code. Nine steps from pstack's Feature
  playbook and non-negotiables: read the principles index, find every consumer,
  name the data shape and make impossible states unrepresentable, alternatives
  through `architect`, subtract, change every consumer, failure and retries,
  tests, throughput. Each step keeps a checklist line, with `n/a: <reason>`
  when it does not apply. A short design note goes into the pull request and
  every brief. A delegated builder gets the note and reads the index and this
  file first: the portable form of pstack's `poteto-agent`.
- `skills/build/SKILL.md`: the bullet that cited three principles now says to
  read the design step and do it. 1993 bytes.
- `skills/autopilot-full/SKILL.md`, `skills/autopilot-stack/SKILL.md`: read
  the design step and do it before any code or brief for an item; each
  participant gets the note.
- `skills/tdd/SKILL.md`: step 1 reads the design step; step 5 says to fix the
  cause in every consumer with the same fault.
- `skills/principles/SKILL.md`: every entry states its rule after its trigger,
  adapted from pstack's index, and the index is read whole, not skimmed for a
  match. 5789 bytes.

Turned down:

- Listing the rules in `ROUTING.md`, which is what pstack's per-turn reminder
  did. ROUTING is capped at 2.6 KB and is nearly full; every change reaches
  `build` or `tdd` already.
- Making `principles` visible in the catalog. Codex then lists it in every
  request ([catalog-size.md](catalog-size.md)); the design step reads it
  whenever code is about to be written.
- A design check in `verify`. It is at its cap, and the verifier already looks
  at what else uses the changed code.

## Dry run (2026-10-15 and 16)

Method as in [principle-citations.md](principle-citations.md): headless runs
in fresh clones of a scratch repository (a 150-line TypeScript CI gate with a
web and a command-line client, and tracker receipts stored as independent
nullable fields; [design-step-runs/fixture/](design-step-runs/fixture/)). The
repository's rules name the skills directory: `main` at `c1e52bf` (without) or
this branch (with). Global rules, `ROUTING.md` included, are loaded in every
run. Claude Code ran Sonnet 5.5 at medium effort with shell and file tools
only; Codex ran GPT 6.1 Sol at medium. Prompts name no skill or principle
([run.sh](design-step-runs/fixture/run.sh)). "Read" means the transcript
shows the file's text in a tool result before the run's first edit to
`src/` (a first count matched paths in commands, missed shell loops and brace
expansions, and was corrected after the independent review; the counting
script is [reads.py](design-step-runs/reads.py)).

Round 1 used the first wording; round 2 the final wording of `build`,
`autopilot-*` and the design step; round 3 the final `tdd` and two Codex
builders given a Claude lead's brief from round 2; round 4 Codex on an
explicit full-autopilot request.

| Task | Arm, agent | Read design step | Read whole index | Outcome |
| --- | --- | --- | --- | --- |
| port | without, Claude ×2 | n/a | 0 of 2 | both clients fixed, 2 of 2 |
| port | without, Codex ×1 | n/a | 1 of 1 | both clients fixed |
| port | with, Claude ×5 via `tdd` (rounds 1 to 3) | 0 of 5 | 0 of 5 | both clients fixed, 5 of 5 |
| port | with (round 1), Codex ×1 | 1 of 1 | 1 of 1 | both clients fixed |
| shape | without, Claude ×2 | n/a | 0 of 2 | tagged union 1 of 2; the other added a nullable `cancellation` field |
| shape | without, Codex ×1 | n/a | 1 of 1 | tagged union |
| shape | with (round 1), Claude ×2 | 2 of 2 | 0 of 2 | tagged union 2 of 2 |
| shape | with (round 1), Codex ×1 | 1 of 1 | 1 of 1 | tagged union |
| shape | with (round 2), Claude ×2 | 2 of 2 | 2 of 2 | tagged union 2 of 2 |
| brief | without, Claude ×2 | n/a | 0 of 2 | names files and both clients; no design step |
| brief | without, Codex ×1 | n/a | 1 of 1 | names files and both clients; no design step |
| brief | with (round 1), Claude ×2 | 2 of 2 | 0 of 2 | tells the builder to read the design step, 2 of 2 |
| brief | with (rounds 1, 2), Codex ×2 | 0 of 2 | 2 of 2 | opened `architect`, `principles` and others, not `build`; no design step in the brief |
| autopilot brief | without, Claude ×2 | n/a | 0 of 2 | no design step in the brief |
| autopilot brief | without, Codex ×1 | n/a | 1 of 1 | no design step in the brief |
| autopilot brief | with, Claude ×2 | 2 of 2 | 2 of 2 | tells the builder to read the design step and the index, 2 of 2 |
| autopilot brief | with, Codex ×1 | 0 of 1 | 0 of 1 | opened no skill; no design step in the brief |
| explicit "full autopilot this queue" | without, Codex ×1 | n/a | 1 of 1 | opened `autopilot-full`, `build`, `tdd`; tagged union, both items committed |
| explicit "full autopilot this queue" | with, Codex ×1 | 1 of 1 | 1 of 1 | same skills, then the design step and two references; tagged union, both items committed |
| builder from a brief | given the "without" brief, Codex ×2 | n/a | 2 of 2 | `quarantine: Quarantine \| null` on each result, both clients |
| builder from a brief | given the "with" brief, Codex ×2 | 2 of 2 | 2 of 2 | a `quarantined` result variant carrying the observed outcome and reason, both clients |

The two briefs from the builder round are kept:
[with](design-step-runs/brief-with.md), [without](design-step-runs/brief-without.md).

Checks: 1 to 3 pass (`0 problem(s)` from both linters, 16 unit tests OK; the
index script prints "23 refs once, same groups and order, triggers kept, each
with a rule"; `ROUTING.md` unchanged). Check 4: port passes, but so does the
baseline; shape passes; brief passes for Claude (4 of 4) and fails for Codex
as the lead on a planning prompt (0 of 3). Codex on an explicit autopilot
request reached the design step (1 of 1).

Read:

- Through `build`, every run with the change read the design step before
  code (13 of 13). Claude read the whole index in 0 of 4 runs with the first
  wording and 4 of 4 with the final one ("open it now and read all of it"); a
  link alone is not followed, as [principle-citations.md](principle-citations.md)
  also found. Claude never read the index without the change (0 of 8). Codex
  reads it on its own (7 of 7 runs without the change), so for Codex the gap
  was the design step, not the index.
- Briefs change. With the change, every Claude brief told the builder to read
  the design step (4 of 4); without it, none did (0 of 4). A Codex builder
  given such a brief read the design step (2 of 2). This is the path most
  Mainworthy code took: a Claude lead, a Codex builder.
- Code changed in one cell: the shape task, tagged unions in 5 of 5 runs with
  the change against 2 of 3 without; the miss was Claude's (1 of 2). That is a
  small sample, not a rate.
- The port task did not discriminate: on a 150-line repository every run, with
  or without, saw the second client and fixed it. The Mainworthy miss was in a
  repository about 450 times larger.
- `tdd` does not hand off: 0 of 5 Claude runs on that route read the design
  step, even when told to. Its step 5 now states the every-consumer rule inline (round 3,
  1 of 1 fixed both clients), which matters more than the pointer.
- Codex as a lead did not open `build` for a planning prompt (0 of 3), so
  those briefs carry no design step. Asked explicitly for full autopilot, it
  opened `autopilot-full` and `build` with or without the change; with it, it
  went on to the design step and two principle references (1 of 1).

## Not checked

- A large repository, where a second consumer is not in view. That is where
  step 6 should matter and where this fixture could not test it.
- Real `autopilot-full` with child agents and a remote to merge into. The
  autopilot-brief rows wrote a brief only; the explicit full-autopilot rows
  built both items in one session and committed to a local `main`.
- The design note wording ("not into a file in the repository") was added
  after round 3 and not rerun. Both round-3 builders had committed their note
  as a file.
- The bounded `architect` hand-off in step 4 (ground and sketch, then return;
  `n/a` when the shape is settled) was added after the independent review and
  not rerun. No dry-run task was large enough to send a run to `architect`
  from the design step.
- Whether the replies name principles: few did, with or without. The code and
  the briefs are what this change is for.
- Cost: the design step and the index are about 9 KB read once per change.
