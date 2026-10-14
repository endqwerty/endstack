# Which model for which role

pstack's `setup-pstack` wrote an always-on rule that set a model per role, with
Opus and Grok at `xhigh` by default ("large") and a budget menu from `medium` up
to `max`. endstack does not import it: the skills name roles, never models (see
[AGENTS.md](../AGENTS.md)), and the model table lives in homelab's
`routing.json`, next to the allowance-based provider routing.

Daniel uses Codex, Claude and Gemini (through Antigravity) and wants a middle
ground, not unlimited effort.
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
provider: the Codex, Claude and Gemini rows of its class.

## What balanced runs

| Class | Codex (Sol 6.1) | Claude | Gemini (Argon 4) |
| --- | --- | --- | --- |
| worker | medium | Sonnet 5.5, medium | medium |
| author | medium | Sonnet 5.5, medium | medium |
| reviewer, verifier | medium | Sonnet 5.5, high | high |
| hard | Astra, medium | Fable 5.1, medium | high |
| lead (one session coordinating a large multi-agent task) | Astra, high | Fable 5.1, high | high |

Gemini has one model, Argon, with three tiers (low, medium, high) and no
separate premium allocation, so `hard` and `lead` run Argon at high. Flash was
dropped on 2026-10-14.

There is no effort ceiling: high and xhigh may be the right default for a class
or a job when the work needs them. The rule for agents is to choose for that
reason and not to assume everything runs at xhigh. The premium models (Astra,
Fable, which has its own weekly allocation) are for `hard` and `lead` only; a test
in homelab pins that, and that gathering never costs more effort than judging.
`lean` falls back to Sol or Sonnet at high for `hard`; `deep` (about pstack's own
"large") raises each class, uses Opus for the Claude judges, and goes to `xhigh`
for `lead`.

## Why these numbers

Measured on this machine on 2026-10-10: a scoped Codex review at medium effort
took about 25 seconds and found a real gap; the large review at high ran over
ten minutes, and a three-round build review took about ten. Reading and
gathering need less judgment than reviewing, so `worker` is the cheapest class;
Daniel raised Sol's worker from low to medium because everything after the
gathering trusts it.
Not measured: how the lower efforts change review quality across many tasks.
The first reading of any profile is a starting point; edit `routing.json` and run
`homelab install` to change it.
