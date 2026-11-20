# Upstream review at 0b46ec3 (2026-11-20)

## Why and scope

Daniel asked to pull in pstack's recent changes, which are mostly cuts. The
review covers the five commits touching `pstack` from `de8ee15` through
`0b46ec3` (2026-11-14 to 2026-11-19), read from a read-only clone of
`cursor/plugins`. Baseline endstack is `0b918db`.

## Per-commit decisions

| Commit | Decision and reason |
| --- | --- |
| `bf0c7cd` | Mostly taken. `why` drops to one paragraph and `how` to a single read-only worker with a brief, and their prompt, roster and source-playbook files go. `recall` runs its own per-source investigators and `teach` loses the `why` narrowing advice, because `why` no longer has investigators or categories. `sharpen` asks the rewritten prompt to prototype choices an experiment can settle. Left: the statechart Mermaid and SANY fixes (external pin), the model defaults and setup-pstack. |
| `2f87c85` | Partly taken. `architect` becomes a short brief that routes large or contested designs to `arena`. `reflect` becomes one file with no reviewer or synthesizer workers. `unslop` and `technical-writing` take the shorter bodies, and `technical-writing` no longer needs `references/style-layers.md`. Left: the 14 shorter principle leaves (below), the poteto-mode, playbook and `worker.md` changes (endstack has no mode or playbooks; the global rules already brief delegates), and the model routing. |
| `e58dd04`, `dd24b67` | Left. Gemini model slugs for panel seats; endstack names no models, and homelab routing picks seats. |
| `0b46ec3` | Left. Statechart on native Windows belongs to the external statechart pin. |

## What changed

| Skill | SKILL.md bytes, files before | After |
| --- | --- | --- |
| why | 5784, 16 | 427, 2 |
| how | 2076, 4 | 974, 2 |
| architect | 5639, 5 | 578, 2 |
| reflect | 4371, 6 | 1591, 2 |
| technical-writing | 3937 + 7 KB reference, 3 | 4727, 2 |
| unslop | 5928, 1 | 2481, 1 |

Endstack additions kept on top of upstream's text: `technical-writing`'s
"Keep the goal visible" section (W7); `reflect`'s rule that only a recurring
defect becomes a check, with `correct` saying which is which, and its
cache-destination rule without editor paths (W7). `build`'s design step 4 now
takes the shape `architect` picks instead of naming its removed phases.

Dropped with upstream's cut, on purpose: `why`'s seven-category coverage map,
confidence template and Preserve / Change / Avoid / Risk block; `architect`'s
red-flag list, runner prompt, rationale template, checkpoint option and scrap
signals; `reflect`'s three lenses, synthesizer and routing table;
`technical-writing`'s worked example and its rule to propose new `unslop`
offenders. `unslop` keeps every rule number; rule 26 loses the rarer metaphor
nouns (evacuate, endgame, gold-plating and others).

## Turned down: the 14 shorter principle leaves

The 190d287 review turned down the same kind of shortening because pstack's
per-turn mode restates the rules and endstack has no such mode. That still
holds, and the new bodies drop rules endstack relies on: Fix Root Causes loses
"after a restart, suspect persisted state" and the long-comment workaround
rule; Type System Discipline keeps "reject impossible states" as one line
but loses the sum-type guidance and examples, exhaustive matching, casts and
partiality, which the index line and `build`'s design step rely on; Minimize
Reader Load's new "inline one-caller wrappers" contradicts endstack's "one
caller alone is not a reason to remove a useful helper"; Boundary Discipline
loses the error-catching rules. The leaves load only when one applies, so the
saving is small.

## Checks

Written before the edits:

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` prints `OK`.
2. No link points at a deleted file.
3. One tool-free paired dry run each for `unslop`, `architect` and `why`: the
   old text (with the reference files it tells the agent to read) and the new
   text, same scenario, one sample each on Claude Sonnet 5.5.

Results: 1 passes (`0 problem(s)` twice, `OK`). 2 passes (`check-skills.py`
checks links). 3, in [upstream-0b46ec3-runs](upstream-0b46ec3-runs/):

- `unslop`: three pieces (PR description, final reply, README section). A
  counter for dashes, curly quotes, bold labels, the AI word list, chatbot
  phrases, hedges and trailing "-ing" clauses found 0 in both arms (299 and
  302 words).
- `architect`: per-customer rate limiting across four replicas, with jobs
  that call handlers directly. Both arms chose router middleware with a Redis
  counter, so jobs are exempt by construction, and both let requests through
  when Redis fails and skip a request with no customer ID. The old arm also
  covered retries overcounting; the new arm also covered a Postgres outage. The old arm wrote three candidates, a red-flag table and the
  rationale template (1601 words); the new arm wrote two shapes, a comparison
  by owner, one way per task and caller knowledge, and the failure policy
  (1034 words).
- `why`: why a retry count is 7 and whether 3 is safe. Both quoted PR #812,
  marked the backoff arithmetic as their own inference, said the record does
  not show whether the partner's rotation still happens, and advised keeping
  7 until that is confirmed. The old arm added the seven-source table and a
  constraint list (831 words); the new arm said the same in 473.

Limits: one sample per arm on one model, scenarios with all evidence in the
prompt, so this shows the shorter texts keep the decisions on these cases,
not that they match the old texts on live repositories with remote sources.
