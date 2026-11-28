## Skill routing

Match each new task here before acting. On a match, open the skill: by name if
listed, else read its SKILL.md from your skills directory (EGM: the egm
plugin's), never through a skill tool. Follow it and say which skill shaped a
decision; several can apply. Skip for casual chat, a one-fact lookup or an
opt-out. Reviewing and checking safety are tasks, however short.

- Changes: `build` implements, `babysit` gets a PR green, `verify` before
  calling a behaviour change done or when asked if one is safe. `ship` or
  `autopilot-full` only on an explicit request to merge, land or ship;
  "autopilot" or "full send" on a change is that request for the latter, with
  no waiting for approval. "Full stop": build, then babysit to ready, unmerged.
- What a change could break past its diff, or whether it is a one-way door:
  `blast-radius`.
- A change of three or more verifiable units, or several pull requests:
  `orchestrate` coordinates fresh workers, landing only on an explicit request.
- Waiting on a pull request, yours or anyone's: `pr-watch`.
- Independent parts worth running at once: `swarm`.
- Any prose, replies included: `unslop`. Docs, README, RFC, PR text, commit
  messages: also `technical-writing`.
- The user asks how code works: `how`; why it is shaped that way: `why`.
- Design: `architect` for non-trivial code crossing a function boundary or
  adding a module; `principles` for stateful or branchy logic or a design call;
  an intent-shaped feature: `egm-brainstorm`, `egm-draft`, `egm-review` (any
  design doc); agent rules: `egm-review-loop`; docs vs code: `egm-drift-report`;
  optional for a change: `egm-lite`. EGM keeps gates unless project rules say
  unattended: then answer halts and findings yourself, in stage order with
  fresh reviewers.
- Editing .ts or .tsx: `typescript-best-practices`.
- Adding, keeping, moving or deleting a test, a bug fix with a cheap local
  test, or a failing or regression test asked for: `test-design`.
- Writing code: no comments, except license headers, public API docs, formatter
  or style-only lint directives, and one line naming a constraint from something
  you can't change; reasoning goes in the commit or PR. Cleaning up existing
  ones: `no-comments`.
- Contested design ("tear this apart"): `interrogate`. Competing attempts at
  one artifact: `arena`.
- A timing or performance number to report, compare or limit:
  `benchmark-checklist`.
- Long, unattended or multi-phase work: `show-me-your-work`. A loop on one goal
  (retries, fix and rerun, hill climbs, review rounds): `loop-judge` each round.
- Corrected, a mistake recurs, or adding a rule to agent instructions:
  `correct`.
- Asked to prove or model-check a race, invariant or rare case, or code
  changed under a formal check since its sync commit: `formal-verification`.
- State diagrams: `statechart` from a checked model or to show a bug as a path;
  `archify` for a picture only.

Only when named: `bro`, `ketchup`, `sharpen`.
