# endstack

<img src="assets/icon.svg" width="96" height="96" alt="endstack: a mint stacked E with an amber endpoint">

Daniel Yang's agent stack: skills for Claude Code and Codex (through T3 Code),
distilled from Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack).

**State: six core skills distilled.** Build, babysit, ship, autopilot-stack,
autopilot-full and verify keep implementation, readiness and merge authority
separate. Start with the [command cookbook](docs/cookbook.md) for the full
catalog, copyable prompts, outputs and stopping points. Distribution uses a
reviewed revision selected by homelab sync; global-rule migration remains pending.
[DISTILL.md](DISTILL.md) records the plan, checks and remaining work.

endstack started as a copy of pstack and has since broken from it: upstream is
no longer tracked or fetched. The 52 pstack skills not yet imported are kept as
reference in [candidates/](candidates/README.md), outside `skills/`, so one can
be imported later without being installed by accident. The full pstack copy
(`cursor/plugins@978ca6e`, with its history) is the git tag `pstack-snapshot`.

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

Only `skills/` is installable: exactly the six skills, nothing else.

**With npx** (any machine; installs to Claude Code, Codex and other agents):

```sh
npx skills add <path-or-owner/repo> -g -y -a claude-code -a codex
```

`<path-or-owner/repo>` is a local checkout, or `endqwerty/endstack` (private,
needs GitHub access). Without `-a`, a non-interactive run installs only to the shared
`~/.agents/skills`, which Claude Code does not read. Add `--copy` to copy instead
of symlink, and `-s <name>` for a subset (the skills link to each other, so
install `verify` with `build`). Checked with Claude Code's directory layout in a
disposable home; Codex's use of `~/.agents/skills` is not checked. Do not run this on a machine where
homelab sync already manages these names: both write the same directories.

**On Daniel's machines** use homelab instead. Install its CLI from its checkout
(`scripts/homelab install`); `homelab sync` installs the six skills into
`~/.codex/skills` and `~/.claude/skills` from the exact reviewed commit pinned in
homelab's `skill-sources.json`. Run `homelab sync --check` and start a fresh
agent session.

The [cookbook](docs/cookbook.md) lists `$build`/`/build` and the other entry
points, update steps, prompts and stopping points.
[Distribution checks](docs/distribution-checks.md) record the tested surface
and remaining limits. First installation through homelab requires access to the
private source repository; cached checks work offline.

## License

MIT, as upstream. pstack is © 2026 Lauren Tan ([LICENSE](LICENSE)).
