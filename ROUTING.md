## Skill routing

Match each new task here before acting. On a match, open the skill: by name if
listed, else read its SKILL.md from your skills directory, never through a
skill tool. Follow it and say which skill shaped a decision; several can apply.
Skip for casual chat, a one-fact lookup or when the user opts out. Explaining
code, reviewing and checking safety are tasks, however short.

- Every task, first: if it splits into independent parts worth running at once,
  `swarm`. Say which you chose.
- Changes: `build` implements, `babysit` gets a PR green, `verify` before
  calling a behaviour change done or when asked if one is safe. `ship` or
  `autopilot-full` only on an explicit request to merge, land or ship;
  "autopilot" or "full send" on a change is that request for the latter, with
  no waiting for approval. "Full stop": build, then babysit to ready, unmerged.
- Any prose, replies included: `unslop`. Docs, README, RFC, PR text, commit
  messages: also `technical-writing`.
- Understanding code: `how` (runtime flow, placement), `why` (history,
  rationale), `teach` (explain it to me).
- Design: `interview` first for a feature shaped by the user's intent or taste;
  `architect` for non-trivial code crossing a function boundary or adding a
  module; `principles` for stateful or branchy logic or a design call;
  `goldfish` to test a design doc or agent rules on a fresh agent.
- Editing .ts or .tsx: `typescript-best-practices`.
- Adding, keeping, moving or deleting a test: `test-design`. Bug fix with a
  cheap local test, or a failing or regression test asked for: also `tdd`.
- Removing comments or replacing workaround ones: `no-comments`.
- Contested design ("tear this apart"): `interrogate`. Competing attempts at
  one artifact: `arena`.
- A timing or performance number to report, compare or limit:
  `benchmark-checklist`.
- Long, unattended or multi-phase work: `show-me-your-work`. Nothing narrower
  fits: `figure-it-out`.
- Corrected, a mistake recurs, or adding a rule to agent instructions:
  `correct`.
- Asked to prove or model-check a race, invariant or rare case:
  `create-formal-verification-skill`. Code changed under a formal check since
  its sync commit: `maintain-formal-verification-skill`.
- State diagrams: `statechart` from a checked model or to show a bug as a path;
  `archify` for a picture only.

Only when named: `bro`, `ketchup`, `ketchup-video`, `orchestrate`, `recall`,
`reflect`, `sharpen`.
