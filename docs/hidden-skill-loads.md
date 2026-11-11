# Hidden skill loads

## Why (2026-11-11)

Daniel heard that hiding skills (`disable-model-invocation: true` for Claude
Code, `allow_implicit_invocation: false` for Codex) while other skills and
ROUTING.md point at them works only some of the time. This records what real
T3 Code sessions on omarchy and the Mac show, and what changed.

## How the harnesses differ

- **Claude Code** (2.1.322) drops a hidden skill from the model's list and
  refuses its skill tool for it, with: "Skill correct cannot be used with
  Skill tool due to disable-model-invocation. Ask the user to run /correct
  themselves … Do not replicate this skill's workflow by other means". An agent
  that asks the skill tool first is told not to read the file, and obeys.
- **Codex** (0.167.1) only leaves the skill out of the catalog. It has no gated
  skill tool; the agent reads SKILL.md like any file, so nothing refuses it.

## What the sessions show

Read-only scans of Claude transcripts and Codex rollouts since 2026-10-14
(the catalog change), matching skill-tool calls, slash commands and reads of
`<skill>/SKILL.md`. File and text matching, so about ±10%. The Mac's scan found
no Codex rollouts in that window; its Claude numbers are below.

| | Claude, omarchy | Claude, Mac | Codex, omarchy |
| --- | --- | --- | --- |
| Skill-tool refusals for a hidden skill | 4 (3 `correct`, 1 `principles`) | 3 (all `correct`) | none possible |
| …recovered by reading the file | 1 | 0 | n/a |
| Top-level sessions loading `build` that also loaded `principles` or `architect` | 91 of 114 (80%) | not split | 387 of 479 (81%) |
| Top-level sessions loading `unslop` | 28 of 687 (4%) | 8 of 718 sessions incl. subagents | 1,060 of 1,316 (81%) |

Skill-to-skill references already land: a skill that links another's
SKILL.md is followed by reading the file in both harnesses. Two things failed:
routing sent Claude agents to the skill tool for `correct`, which refused and
forbade the fallback, and routing alone almost never got Claude to open
`unslop`, which applies to every reply.

## What changed

- ROUTING.md: open a listed skill by name, any other by reading its SKILL.md,
  never through a skill tool.
- `unslop` is visible in both harnesses, with a description that names when to
  use it. Codex already loaded it in most sessions; the cost there is one
  catalog entry, about 60 tokens a request.
- Turned down: rewriting every skill-to-skill reference as a file path (they
  already work), and making every routed skill visible (the catalog cost the
  2026-10-14 change removed, for skills that are mostly reached through `build`).

## Dry run

Claude Code 2.1.322, Sonnet, headless, with `--setting-sources project` so
neither the installed global rules nor the installed skills were visible. Each
arm was a fresh repository whose `.claude/skills/` held endstack's skills and
whose `CLAUDE.md` held ROUTING.md: **old** from `fdff53b`, **new** from this
change. Three runs per prompt per arm.

- P1, a correction: "You got that wrong again: this repo indents with tabs,
  not spaces, and you keep using spaces. Handle this correction the way your
  instructions say, then stop."
- P2, prose: "Write a three-sentence README.md introduction for a command-line
  tool called exifname that renames photos by their EXIF capture date. Save it
  to README.md."

| Run | Old | New |
| --- | --- | --- |
| P1 #1 | read `correct` | read `correct` |
| P1 #2 | read `correct` | read `correct` |
| P1 #3 | skill tool `correct`, refused, never read | read `correct` |
| P2 #1 | read `unslop`, `technical-writing` | skill tool `unslop`, read `technical-writing` |
| P2 #2 | skill tool `unslop` and `technical-writing`, both refused, never read | read `unslop`, `technical-writing` |
| P2 #3 | skill tool `unslop` and `technical-writing`, both refused, never read | skill tool `unslop`, read `technical-writing` |

Old: 3 of 6 runs hit the refusal and none recovered. New: no refusals, and
every run loaded the skills its task routes to. Six runs per arm is a sample,
not a rate.

## Not checked

- Whether visible `unslop` raises its use in real Claude sessions over weeks;
  rerun the scan after a few hundred sessions.
- The Mac's Codex rollouts, which were not where the scan looked.
