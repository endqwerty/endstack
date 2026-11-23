# endstack: rules for coding agents

Your global agent rules apply (`~/.claude/CLAUDE.md` for Claude Code, `~/.codex/AGENTS.md`
for Codex; their source is homelab's `agents/AGENTS.md`).
Read [README.md](README.md) and [DISTILL.md](DISTILL.md) first.

## What this repository is

Daniel's portable agent skills for Claude Code and Codex, distilled from pstack
(`cursor/plugins`) and no longer tracking it. `skills/` holds only installable,
distilled skills. `candidates/` holds the pstack skills not yet imported, as
reference; importing one means distilling it to the rules below, with an eval
case and its score (below), and recording it in DISTILL.md and CHANGELOG.md. Nothing in `candidates/` is
installed or maintained.

## Rules for a skill in `skills/`

`python3 scripts/check-skills.py` enforces the mechanical ones (frontmatter,
size, no tool or model names, links) and must pass.

- Say the outcome and the roles, never the tool. No `gh`, `git`, `Task`,
  `/loop`, model names, provider names, Cursor or T3 Code features. "If the
  harness can watch a pull request, use it" is fine; a tool name is not.
  Judge or reviewer roles ask for a different provider or model family "if
  available", never a named one.
- One skill, one job, one role. Deterministic work goes in a script, not in
  prose. A script a skill needs ships inside that skill (`scripts/`, standard
  library, with tests beside it run by
  `python3 -m unittest discover -s skills/<skill>/scripts`), so it works
  wherever the skills are installed; tooling tied to Daniel's machines stays in
  the `homelab` CLI.
- **Core delivery skills** (build, babysit, ship, autopilot-full, verify): `SKILL.md` at most 2,200 bytes, judgment and policy
  only; a behaviour change gets an eval score table in the PR (below).
- **Role skills**, imported (ported from pstack, see `candidates/README.md` and
  DISTILL.md) or new: keep an imported skill's role, identity, structure and
  judgment; `SKILL.md` at most 6,000 bytes, longer material in `references/` read on demand. Porting removes
  tool, model and harness coupling and dead links; it does not rewrite the
  substance. Record what each port changed in `docs/import-notes/`.
- Frontmatter `name` and `description` that trigger correctly from both Codex
  and Claude Code, the description at most 200 characters: a visible one is
  paid on every request. Keep `disable-model-invocation: true` where the source
  has it, and on any new role skill, and give such a skill `agents/openai.yaml`
  copied byte for byte from an existing hidden skill (`policy:` then
  `  allow_implicit_invocation: false`), which keeps it out of Codex's catalog the
  way the frontmatter does for Claude Code ([docs/catalog-size.md](docs/catalog-size.md)).
- Adding a delivery skill beyond these five needs either a recurring failure or Daniel's
  request.

## Routing

[ROUTING.md](ROUTING.md) is the always-on skill index: homelab copies it into
the global rules so every turn sees it, and the hidden skills stay out of the
catalog. Adding, renaming or dropping a skill means updating it, the README
skill table and counts, and, after merge, the skill names in homelab's
`skill-sources.json` (a name not listed there is not installed; your global
rules say where the homelab checkout is). Skills from another plugin, such as
EGM, are not copied into `skills/`: [plugins.json](plugins.json) pins each
plugin by commit and lists its skills, and adding a plugin, moving its pin or
changing its skill list updates homelab after merge the same way;
`python3 scripts/check-routing.py` must pass (every skill in `skills/` named
once, a plugin's at most once and never also in `skills/`, plugins.json well formed, the
merge skills and a routed `orchestrate` tied to an explicit request, 2,800 bytes at most), and the copy in homelab's `agents/AGENTS.md` must match.
Evidence and limits: [docs/routing.md](docs/routing.md).

## Delivery

This repository grants agents merge authority. Work on the T3 branch in your
worktree, follow [build](skills/build/SKILL.md) through a checked,
independently verified PR, then merge it yourself with
`gh pr merge --merge --match-head-commit <verified sha>`. When the merge
changes an installed skill or `ROUTING.md`, update homelab's pin and copies as
described under Routing. Do not arm auto-merge or push directly to `main`.
Opening a PR does not start a watcher; use [babysit](skills/babysit/SKILL.md)
when requested.

EGM runs unattended in this repository: where an EGM skill halts for a command
or approval, give the next one yourself and resolve its findings yourself.

Use `gh` for pull requests. Where `gh auth status` shows no valid login (over
SSH to the Mac, whose login keychain holds the token but stays locked), push
with `git`, give the compare URL the push prints, and name opening and merging
the PR as the pending step.

Changes to a skill's behaviour, or to ROUTING.md, get evidence from the standing
evals in [evals/](evals/README.md). Keep the check short: run only the cases
tagged with the touched skills, or for a ROUTING.md change the skills named in
the changed lines (the full suite when no case is tagged), once each, in
parallel: `homelab skill-eval --runs 1 --jobs <4 x cases> --case <glob> main
HEAD`. One or two cases take about ten minutes. Paste the score table in the PR. Repeat with more runs only to confirm
a surprising difference before acting on it. A skill with no case gets one in the same change; a hand-run dry run
stays acceptable only for a behaviour no case can grade, and the PR says why.
Record changes in CHANGELOG.md.
