# endstack: rules for coding agents

Your global `~/.<agent>/AGENTS.md` applies.
Read [README.md](README.md) and [DISTILL.md](DISTILL.md) first.

## What this repository is

Daniel's portable agent skills for Claude Code and Codex, distilled from pstack
(`cursor/plugins`) and no longer tracking it. `skills/` holds only installable,
distilled skills. `candidates/` holds the pstack skills not yet imported, as
reference; importing one means distilling it to the rules below, with a dry run,
and recording it in DISTILL.md and CHANGELOG.md. Nothing in `candidates/` is
installed or maintained.

## Rules for a distilled skill

- Say the outcome and the roles, never the tool. No `gh`, `git`, `Task`,
  `/loop`, model names, provider names, Cursor or T3 Code features. "If the
  harness can watch a pull request, use it" is fine; a tool name is not.
- Under about 2 KB. Judgment and policy only; anything deterministic belongs
  in the `homelab` CLI with tests, not in a skill.
- One skill, one job. The approved core delivery split includes:
  build, babysit, ship, autopilot-stack and autopilot-full, alongside verify.
  Add further skills only when the same failure has shown up twice.
- Frontmatter `name` and `description` that trigger correctly from both Codex
  and Claude Code; test the trigger before merging.

## Delivery

Delivery: review-first. Work on the T3 branch in your worktree and follow
[build](skills/build/SKILL.md) through a checked, independently verified PR.
The user reviews and merges by default. Opening a PR does not start a watcher;
use [babysit](skills/babysit/SKILL.md) when requested. An explicit request to
merge identified work invokes [ship](skills/ship/SKILL.md), with its gates.
“Keep going” and a budget request are not merge authority. Do not arm auto-merge
or push directly to `main` to bypass the review boundary.
Changes to a skill's behaviour get a dry run described in the PR (what the
agent did with and without the skill). Record changes in CHANGELOG.md.
