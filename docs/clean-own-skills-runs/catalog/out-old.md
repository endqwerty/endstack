Skills I would open, in order:

1. `swarm` (decision only): "Every task, first: if it splits into independent parts worth running at once, `swarm`." I would choose not to fan out. The diff is about 60 lines of retry logic plus its test, and the test only makes sense next to the code, so splitting it would cost more than it saves.
2. `verify`: "`verify` before calling a behaviour change done or when asked if one is safe." "Review before I merge it, tell me if anything is wrong" asks whether a behaviour change is safe. The routing also says reviewing is a task however short. This skill shapes the review.
3. `unslop`: "Any prose, replies included." It applies to the findings I write back.

Considered and rejected:
- `ship` / `autopilot-full`: "before I merge it" means the user is merging. It isn't a request for me to merge, land or ship.
- `typescript-best-practices`: it is for editing .ts files, and I'm only reading retry.ts.
- `test-design`: it is for adding, keeping, moving or deleting a test myself. The test here is only being reviewed, though I might open it if the added test looks weak.
- `tdd`: no bug fix by me and no request for a test.
- `principles` / `architect`: these are design-time skills. This is a review of finished code.
- `how` / `why` / `teach`: the user wants a verdict, not an explanation.
- `benchmark-checklist`: there is no timing number to report.
- `build` / `babysit`: no implementation or PR to fix.

Fan-out: no `swarm` and no parallel workers. If `verify` asks for an independent fresh-context verifier, I would spawn just that one.
