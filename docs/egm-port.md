# EGM port: staged goldfish review, concept brief and drift

Daniel compared endstack with Google's Elephant-Goldfish Model
(`google/elephant-goldfish-model` at `72d06f5`), a plugin built on the same
Rensin essay as `interview` and `goldfish`, and chose to match it unless
there was a good reason not to. He asked for one question at a time, EGM's
full reviewer set with its merging worker, its design-pattern reviewer, a
drift check of expected against actual behaviour, and the brief as a file.
What each port kept and dropped: [import-notes/egm.md](import-notes/egm.md).

## Why EGM is shaped as it is

- About half of each EGM skill is harness support: dispatch text for three
  agent tools, plugin paths, per-harness manifests. Its 24,000-byte skill
  limit comes from one harness's load limit. None of that is ported.
- It is human-led by design: the author picks the architecture, every stage
  and section ends in an approval gate, and there is no unattended path.
- Its rules restate themselves (a tone charter copied into three skills, one
  prohibition four times in one skill) where endstack would add a check.
- Its test scenarios each encode one observed failure: inventing interfaces
  from directory names, crediting rejections to maintainers, counting a
  silent reviewer as clean.
- Most numbers have no stated reason (eight reviewers, five rounds, two
  instances per reviewer) and no recorded measurements. The exceptions, with
  reasons, are two clean rounds ("fresh reviewers sample differently") and
  the separate design-pattern reviewer (EGM expects that merging it into the
  critic would give conflicting directions).

## What changed

- `goldfish`: design docs get EGM's five stages, eight reviewer roles,
  merging worker, standards, loop rules and resolve categories. Agent
  instruction files keep one goldfish with three passes and realistic tasks,
  now under the same loop and resolve rules.
- `interview`: one question at a time; a brief file reviewed by seven
  concept reviewers; the design doc reconciled against the brief, which is
  then deleted.
- `build`'s design reference: *Goals* and *Non-goals*; goldfish runs until
  its review converges.
- New explicit `drift` skill, routed in ROUTING.md.

Turned down:

- EGM's human gates between stages and its "author picks among options".
  Agents decide engineering questions themselves, and the agent proposing
  first is how `interview` exposes misunderstanding. The user is still asked,
  one question at a time, for escalated findings, brief contradictions and
  the round cap.
- EGM's rule against adding context only a fresh agent needs. In endstack
  the next session resumes from the doc, so a fresh agent is a real reader.
- Bootstrap (directory README contracts): no recurring need.
- Keeping the brief after the doc is written: two files describing one
  feature would drift.

## Checks defined before running

Each scenario ran once with the old text (ROUTING.md, build's design
reference, interview, goldfish and its brief at `origin/main` f270729) and once
with the new at 2db953f (those plus the reviewer roles, standards and drift;
the review fixes after it were not rerun), in fresh
`codex exec` sessions (`codex-cli 0.169.0`, `--ignore-user-config
--ignore-rules --ephemeral --skip-git-repo-check -s read-only --json`, CLI
default model) from `/tmp`, on 2026-11-17. Prompts, events, answers and the
runner are in [egm-port-runs/](egm-port-runs/).

1. User present, new feature: NEW asks one question at a time and writes a
   brief that concept reviewers critique.
2. Brief and draft disagree: NEW quotes both, asks the user, then deletes the
   brief.
3. Goldfish on a full design doc: NEW runs the five stages with their
   reviewers and stops on two clean rounds.
4. A comprehension finding the author wants to contest, then one clean
   round: NEW fixes it and runs another round.
5. "Do the design docs still match the code?": NEW uses `drift`.
6. Settled bug fix: neither arm interviews, writes a brief or runs goldfish.
   Guards against over-applying.
7. "Does my rewritten AGENTS.md hold up?": NEW uses one goldfish, not the
   design-doc stages. Guards against over-applying.

## Results

| Case | Arm | Deciding line | Result |
| --- | --- | --- | --- |
| 1 | OLD | "I would ask three questions: which timezone defines 8 pm …" | Fail: batch, no brief |
| 1 | NEW | "I’ll continue one question at a time …" / "I’ll write the interview brief, then have a separate merging worker run all seven fresh, read-only concept reviewers" | Pass |
| 2 | OLD | "I would update the brief and design doc together" | Fail: asks, but keeps both files |
| 2 | NEW | "I would quote both passages …" / "Once reconciled, I would delete the brief in the same change" | Pass |
| 3 | OLD | "I would start three fresh, read-only readers at once" | Fail: three passes |
| 3 | NEW | "Stage 1: start zoom-out and design-pattern readers together …" / "repeat with fresh readers until two consecutive clean rounds" | Pass |
| 4 | OLD | "otherwise dismiss the finding with a one-line, evidence-based reason" / "Finish the critic loop only when no blocker or should remains" | Fail: may contest a comprehension gap; one clean round ends the loop |
| 4 | NEW | "treat round 1’s comprehension gap as **Fix**" / "Continue the critic loop with fresh reviewers in round 3" | Pass |
| 5 | OLD | "I would give each doc to a fresh read-only goldfish" / "check each finding against current code and relevant deterministic checks, distinguishing stale documentation from a possible implementation bug" | Partial: compares with code, but only through findings from comprehension, critic and readiness passes; no scenario-by-scenario check |
| 5 | NEW | "I would choose `drift` …" / "recommend changing the doc for intended changes, the code for supported bugs" | Pass |
| 6 | OLD | "`interview`, a design doc and `goldfish` are unnecessary" | Pass |
| 6 | NEW | "`interview`, `architect`, and a new design doc are unnecessary" | Pass |
| 7 | OLD | "comprehension, criticism and readiness are independent; … parallel readers" | Pass |
| 7 | NEW | "I would keep the initial review with one fresh reader" / "repeat with a new fresh reader until two consecutive rounds are clean" | Pass |

All fourteen runs exited 0.

## Read of the result

NEW passes all seven; OLD fails four targeted cases, half-passes the drift
case and passes both guards. Several OLD failures hold by construction, since the old text has
no stages, brief or drift skill. One run per arm per case, on one model:
this shows the text is read as intended, not how often or what it costs. A
full design-doc review now starts at least eight reviewer runs plus merging
workers, and more per extra loop round. That cost is not measured yet; the
first real feature reviewed under it is the measurement.
