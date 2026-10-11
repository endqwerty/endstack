# endstack

<img src="assets/endstack-icon.svg" width="96" height="96" alt="endstack: a mint stacked E with an amber endpoint">

Daniel Yang's agent stack: skills for Claude Code and Codex (through T3 Code),
distilled from Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack).

**State: six core skills distilled.** Build, babysit, ship, autopilot-stack,
autopilot-full and verify keep implementation, readiness and merge authority
separate. Start with the [command cookbook](docs/cookbook.md) for the full
catalog, copyable prompts, outputs and stopping points. Installation and
global-rule migration remain pending; these are not installed commands yet.
[DISTILL.md](DISTILL.md) records the plan, checks and remaining work.

The remaining upstream material is pstack at `cursor/plugins@978ca6e`, with
its `pstack/` history and three linked `cursor-team-kit` skills in
`vendor/cursor-team-kit/`. The original README is
[docs/pstack-readme.md](docs/pstack-readme.md); its guide is
[docs/guide/](docs/guide/README.md). Retained upstream skills are reference
material, not the distilled collection to install wholesale.

## Why not just install pstack

pstack is a Cursor plugin: Cursor-only entry points, Grok and Opus named per
role, a 19 KB always-on mode and 23 playbooks. Daniel works from Codex and
Claude Code inside T3 Code, on several machines, and his providers and tools
update constantly. endstack keeps pstack's ideas (merge is a separate decision
from building, prove it works on the real artifact, a verifier that did not
write the code, short briefings) in a small set of skills phrased as outcomes,
with no exact commands, tool names, model names or harness features, so a
harness update does not break them. Each repository names the skills it uses
in its `AGENTS.md`.

## Install

Not yet. The intended path is the `homelab` CLI (`homelab sync`), which
installs skills into `~/.codex/skills` and `~/.claude/skills`; whether
endstack is synced from here or vendored into the homelab repository is an
open question in DISTILL.md.

## License

MIT, as upstream. pstack is © 2026 Lauren Tan ([LICENSE](LICENSE));
the vendored team-kit skills are © 2026 Cursor
([vendor/cursor-team-kit/LICENSE](vendor/cursor-team-kit/LICENSE)).
