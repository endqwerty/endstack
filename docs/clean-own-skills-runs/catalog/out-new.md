1. `verify`, from the Changes line: "`verify` before calling a behaviour change done or when asked if one is safe." Daniel asks whether a behaviour change (retry backoff) is fine to merge, and line 6 says "Reviewing and checking safety are tasks, however short", so routing applies.
2. `unslop`, from "Any prose, replies included: `unslop`." I'd open it before writing the findings reply.

Considered and rejected:
- `test-design` ("Adding, keeping, moving or deleting a test"): this is the closest call. The diff adds a test, but I'm judging it, not adding or keeping one myself. If the test looks weak, I'd open it while judging the test.
- `typescript-best-practices`: the trigger is editing .ts or .tsx, and a review edits nothing.
- `principles`: backoff is branchy logic, but that line sits under Design and this is a review, not a design call.
- `ship` and `autopilot-full`: "before I merge it" means he will merge, so there's no explicit request for me to merge.
- `build` and `babysit`: nothing to implement, and he gave no PR to get green.
- `swarm`: one 60-line file plus a test has no independent parts worth running at once.
- `benchmark-checklist`: no timing number to report, compare or limit.
- `interrogate`: the design isn't contested.

Fan-out: no swarm and no worker split. The only extra agent would be whatever independent reviewer `verify` itself requires. I can't confirm that from the routing text alone.
