# endstack

Daniel Yang's agent stack: skills for Claude Code and Codex (through T3 Code),
distilled from Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack).

**State: day zero.** This is pstack as of `cursor/plugins@978ca6e`, with its full
history for the `pstack/` folder, plus the three `cursor-team-kit` skills it
links to (`vendor/cursor-team-kit/`). Nothing is distilled yet. The original
README is [docs/pstack-readme.md](docs/pstack-readme.md); the original guide
is [docs/guide/](docs/guide/README.md). [DISTILL.md](DISTILL.md) is the plan
for turning it into mine.

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
