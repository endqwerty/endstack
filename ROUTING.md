## Skill routing

Before acting on a new task, match it here. On a match, open the skill by name
(if it is not in your skill list, read its SKILL.md from your skills directory),
follow it, and say which one shaped a decision. Several can apply. Casual chat,
a one-fact lookup (a time zone, a version), or the user opting out: skip this.
Explaining code, reviewing and checking safety are tasks, short or not.

- Change requests: `build` to implement, `babysit` to get a PR green,
  `autopilot-stack` for a queue the user will land, `verify` before calling
  behaviour changes done or when asked if a change is safe. `ship` or
  `autopilot-full` only when the user explicitly asks to merge, land or ship;
  their gates apply.
- Any prose, your reply included: `unslop`. Docs, README, RFC, PR text, commit
  message: also `technical-writing`.
- Understand or explain code, before changing it or not: `how` (runtime flow,
  where it belongs), `why` (history, rationale), `teach` (explain it to me).
- Non-trivial code that crosses a function boundary or adds a module:
  `architect` first. Stateful or branchy logic, or a design call: `principles`.
- Editing .ts or .tsx: `typescript-best-practices`.
- Bug fix with a cheap local test, or a failing or regression test asked for:
  `tdd`.
- Asked to remove comments or replace workaround comments: `no-comments`.
- Contested design, "tear this apart": `interrogate`. Competing attempts at one
  artifact: `arena`. Parallel fan-out or coverage: `swarm`.
- A benchmark number you will report: `benchmark-checklist`.
- Long, unattended or multi-phase work: `show-me-your-work`. No narrower
  playbook fits: `figure-it-out`.
- The same mistake keeps recurring, or you were corrected: `correct`.
- No scripted way to prove UI, CLI or service behaviour: `create-verification-skill`;
  keeping one accurate: `maintain-verification-skill`.

Only when named: `bro`, `ketchup`, `recall`, `reflect`, `automate-me`.
