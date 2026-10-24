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

## Rules for a skill in `skills/`

`python3 scripts/check-skills.py` enforces the mechanical ones (frontmatter,
size, no tool or model names, links) and must pass.

- Say the outcome and the roles, never the tool. No `gh`, `git`, `Task`,
  `/loop`, model names, provider names, Cursor or T3 Code features. "If the
  harness can watch a pull request, use it" is fine; a tool name is not.
  Judge or reviewer roles ask for a different provider or model family "if
  available", never a named one.
- One skill, one job, one role. Deterministic work belongs in the `homelab` CLI
  with tests, not in a skill.
- **Core delivery skills** (build, babysit, ship, autopilot-full, verify): `SKILL.md` under about 2 KB, judgment and policy
  only; changes get a dry run in the PR.
- **Imported role skills** (ported from pstack, see `candidates/README.md` and
  DISTILL.md): keep the role, identity, structure and judgment; `SKILL.md`
  under 6 KB, longer material in `references/` read on demand. Porting removes
  tool, model and harness coupling and dead links; it does not rewrite the
  substance. Record what each port changed in `docs/import-notes/`.
- Frontmatter `name` and `description` that trigger correctly from both Codex
  and Claude Code, the description at most 200 characters: a visible one is
  paid on every request. Keep `disable-model-invocation: true` where the source
  has it, and give such a skill `agents/openai.yaml` with
  `allow_implicit_invocation: false`, which keeps it out of Codex's catalog the
  way the frontmatter does for Claude Code ([docs/catalog-size.md](docs/catalog-size.md)).
- Adding a delivery skill beyond these five needs either a recurring failure or Daniel's
  request.

## Routing

[ROUTING.md](ROUTING.md) is the always-on skill index: homelab copies it into
the global rules so every turn sees it, and the hidden skills stay out of the
catalog. Adding, renaming or dropping a skill means updating it too;
`python3 scripts/check-routing.py` must pass (every skill named once, the
merge skills tied to an explicit request, 2.6 KB at most), and the copy in homelab's `agents/AGENTS.md` must match.
Evidence and limits: [docs/routing.md](docs/routing.md).

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
