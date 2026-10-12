# Routing

Why: the pstack router (`poteto-mode`) made the agent pick among its skills on
every task. endstack dropped it, so the 24 explicit-invocation skills were only
used when Daniel named them, and nothing chained them (for example `build`
writing docs never reached `unslop`). Asking him to think about 24 skills per
message was the failure.

What: [ROUTING.md](../ROUTING.md) is a 1.9 KB index, one line per situation. It
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

1. `python3 scripts/check-routing.py`, tested by `scripts/test_check_routing.py`
   (14 tests with the rest of `scripts/`). It enforces the mechanical parts:
   every skill in `skills/` named exactly once; no unknown backticked name; a
   non-empty "Only when named" list; one bullet routing prose to `unslop` and
   docs to `technical-writing`; `ship` and `autopilot-full` only in a bullet
   that says "explicit"; a casual-chat skip; at most 2.6 KB; no tool, model or
   provider names. Before `ROUTING.md` existed it printed `ROUTING.md: missing`
   (exit 1); now `0 problem(s)`.
   It cannot judge whether a line sends a skill to the right situation, or
   catch a skill name written without backticks. Those are review's job.
2. A dry run of the routing decision with the index (below).
3. Independent review (Codex, round 1) failed the first draft: one-line tasks
   were exempt from routing, the checker passed five wrong variants,
   `no-comments` was routed wider than its own description, and the merge
   skills read as authority. Fixed in the next commit. The checker now rejects duplicate
   and conflicting routes, an empty or missing named list, and merge skills
   without "explicit"; it still passes a wrong situation or an unquoted name
   (limit above).

## Dry run (2026-10-12, final text)

Ten tasks, answered by a small model with no tools, from the index text only.
The "without" column is the same model seeing only the six core skills (earlier
draft run, first five tasks). The decision only; nothing ran.

| Task | Without | With |
| --- | --- | --- |
| README install section | none | `unslop`, `technical-writing` |
| Fix off-by-one in a .ts file, keep it fixed | `build`, `verify` | `build`, `tdd`, `typescript-best-practices` |
| Two teams disagree on a design | none | `interrogate`, `principles` |
| "what time zone is the server in?" | none | none |
| Retry logic across queue module, then open a PR | `build`, `verify` | `architect`, `principles`, `build` |
| "Merge PR 12." / "Ship PR 12." | not run | `ship` / `ship` |
| "Is it safe to merge PR 12?" | not run | `verify` |
| "How does the scheduler pick the next job?" / "How does this small function work?" | not run | `how` / `how` |

The casual question stayed unrouted; docs, bugs, design calls, explanations and
safety checks reached the hidden skills, and the safety question did not reach
`ship`. The small model dropped `verify` on the bug fix and the PR task, and
`unslop` on the PR task, so routing is a nudge, not a guarantee; an independent
Codex probe on the round 1 wording did add them.

## Not checked

- Real sessions: the dry run is one small model's stated choice, not observed
  skill use in Claude Code or Codex, and one sample, not a rate. Whether the
  model really opens a hidden skill by reading its SKILL.md is unconfirmed.
- Cost and noise: the index adds about 1.9 KB per turn; whether it over-triggers
  on short turns is not measured. If it does, tighten the "casual turn" line.
- Drift: the copy in homelab is checked by hand, not by a script.
