# Routing

Why: the pstack router (`poteto-mode`) made the agent pick among its skills on
every task. endstack dropped it, so the 24 explicit-invocation skills were only
used when Daniel named them, and nothing chained them (for example `build`
writing docs never reached `unslop`). Asking him to think about 24 skills per
message was the failure.

What: [ROUTING.md](../ROUTING.md) is a 1.6 KB index, one line per situation. It
is loaded on every turn through the global rules in homelab (`agents/AGENTS.md`),
the only file both Claude Code and Codex read each session. The model matches the
task against it, opens the named skill, and says which one shaped a decision. A
casual turn skips it.

Turned down:

- Making all 24 skills model-invocable. Their descriptions would sit in every
  catalog, and the import rule keeps them explicit.
- Editing `build` and the other core skills to call `unslop` and friends. They
  are capped near 2 KB and one job each; the index chains across all skills.
- A new router skill. A skill loads only when matched, which is the problem
  being solved; and "one skill, one job" does not cover a table.
- A per-turn hook. Claude-only and configured in homelab; revisit if the index
  proves too weak.

## Checks (written before the file existed)

1. Every skill in `skills/` appears in `ROUTING.md` once, and nothing else is
   named. Prose routes to `unslop`, docs to `technical-writing`, a casual turn
   skips routing. Size at most 2.6 KB, no tool, model or provider names.
   `python3 scripts/check-routing.py`, tested by `scripts/test_check_routing.py`.
   Before `ROUTING.md` existed it printed `ROUTING.md: missing` (exit 1); now
   `0 problem(s)`.
2. A dry run of the routing decision with and without the index (below).

## Dry run (2026-10-12)

Five tasks, answered by a small model with no tools, once seeing only the six
core skills and once also seeing the index text. The decision only; nothing ran.

| Task | Without | With |
| --- | --- | --- |
| README install section | none | `unslop`, `technical-writing` |
| Fix off-by-one in a .ts file, keep it fixed | `build`, `verify` | `tdd`, `typescript-best-practices`, `build`, `verify` |
| Two teams disagree on a design | none | `architect`, `interrogate`, `principles` |
| "what time zone is the server in?" | none | none |
| Retry logic across queue module, then open a PR | `build`, `verify` | `architect`, `principles`, `build`, `verify`, `unslop`, `technical-writing` |

The casual question stayed unrouted; docs, bugs and design calls reached the
hidden skills. Delivery tasks gained `unslop` and `technical-writing`, which is
the chaining missing before.

## Not checked

- Real sessions: the dry run is one small model's stated choice, not observed
  skill use in Claude Code or Codex, and one sample, not a rate. Whether the
  model really opens a hidden skill by reading its SKILL.md is unconfirmed.
- Cost and noise: the index adds about 1.6 KB per turn; whether it over-triggers
  on short turns is not measured. If it does, tighten the "casual turn" line.
- Drift: the copy in homelab is checked by hand, not by a script.
