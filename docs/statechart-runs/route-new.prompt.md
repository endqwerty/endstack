## Skill routing

Before acting on a new task, match it here. On a match, open the skill by name
(if it is not in your skill list, read its SKILL.md from your skills directory),
follow it, and say which one shaped a decision. Several can apply. Casual chat,
a one-fact lookup (a time zone, a version), or the user opting out: skip this.
Explaining code, reviewing and checking safety are tasks, short or not.

- Every task, first: decide whether it splits into independent parts (sources,
  files, questions, candidates) worth running at once. If it does, `swarm`;
  say which way you decided.
- Change requests: `build` to implement, `babysit` to get a PR green,
  `verify` before calling behaviour changes done or when asked if a change is
  safe. `ship` or `autopilot-full` only when the user explicitly asks to merge,
  land or ship; their gates apply. "Autopilot" or "full send" on a change
  is that request: autopilot it, without waiting for approval. "Full stop"
  means build it and babysit it to ready, unmerged.
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
  artifact: `arena`.
- A timing or performance number you will report, compare or turn into a
  limit: `benchmark-checklist`.
- Long, unattended or multi-phase work: `show-me-your-work`. No narrower
  playbook fits: `figure-it-out`.
- You were corrected, a mistake recurs, or you are about to add a rule to
  AGENTS.md or another agent instruction file: `correct`.
- Asked to prove or model-check a property (a race, invariant or case tests
  rarely reach): `create-formal-verification-skill`; an existing formal check
  covers code changed since its recorded sync commit: `maintain-formal-verification-skill`.
- A state diagram: `statechart` to draw it from a checked model or show a bug
  as a path through states; `archify` for a picture only.

Only when named: `bro`, `ketchup`, `recall`, `reflect`, `sharpen`.

Using only this index, say which skills you would open for each numbered prompt and briefly why. Respect explicit-only helpers.

1. Draw the states a checkout order goes through so our PM can see it.
2. Our offline note sync sometimes shows "Synced" when the edit was never saved. Show me, checked against a model, the path through states that gets there.
3. Draw the architecture of our payment service.
4. Fix the race where two workers pick up the same job, and add a regression test.
5. Prove that the lease protocol never lets two holders write at once.