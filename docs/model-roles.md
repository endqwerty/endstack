# Which model for which role

pstack's `setup-pstack` wrote an always-on rule that set a model per role, with
Opus and Grok at `xhigh` by default ("large") and a budget menu from `medium` up
to `max`. endstack does not import it: the skills name roles, never models (see
[AGENTS.md](../AGENTS.md)), and the model table lives in homelab's
`routing.json`, next to the allowance-based provider routing.

Daniel uses Claude and Codex and wants a middle ground, not unlimited effort.
`homelab route models` prints the table (add `--profile lean|balanced|deep`,
`--role <class>`, `--json`). Balanced is the default.

## pstack role to class

| pstack role (as the ported skills describe it) | Class |
| --- | --- |
| feature, bug-fix, refactoring, perf-issue, hillclimb work; arena and architect candidates | `author` |
| how explorer, why investigators, reflect tooling reviewer, swarm workers | `worker` |
| how explainer, why synthesizer, reflect judgment, divergent and synthesizer, arena cross-judge, interrogate panel, judgment and prose | `reviewer` |
| the independent check in `verify` | `verifier` (always a different provider from the author) |
| hardest tasks | `hard` |

A panel (arena, architect, interrogate, reflect) puts one member on each
provider: the Codex row and the Claude row of its class.

## What balanced runs

| Class | Codex (Sol 6.1) | Claude |
| --- | --- | --- |
| worker | low | Sonnet 5.5, medium |
| author | medium | Sonnet 5.5, medium |
| reviewer, verifier | medium | Sonnet 5.5, high |
| hard | high | Opus 5.5, high |

Nothing above `high`. `lean` drops each one a step; `deep` (about pstack's own
"large") raises them, uses Opus for the Claude judges, and goes to `xhigh` only
for `hard`. A test in homelab pins the balanced ceiling.

## Why these numbers

Measured on this machine on 2026-10-10: a scoped Codex review at medium effort
took about 25 seconds and found a real gap; the large review at high ran over
ten minutes, and a three-round build review took about ten. Reading and
gathering do not need judgment effort, so `worker` is the cheapest class.
Not measured: how the lower efforts change review quality across many tasks.
The first reading of any profile is a starting point; edit `routing.json` and run
`homelab install` to change it.
