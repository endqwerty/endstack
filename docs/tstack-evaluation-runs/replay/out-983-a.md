Revision: b9a571799588917525bb44e0a4aa1c18c0c67f4e; base: f04e69e65f2d22ceae3b6a7bea52d31f5596de87.
Re-review: 34a3187f310ce63363425bfb80c378377550bd75..b9a57179, plus affected undo, rule reconsideration, evidence storage and map handlers.
Read the full base-to-head diff and incremental diff; no earlier verdict was substituted for these checks.
Patch identity: SHA256 of ordered diff file headers and added/deleted lines, preserving whitespace and omitting context, hunk offsets and metadata.
Full patch: df11a74cdd1451f055c2d47cf8d8a1a6331daa53a919c8b487b9498483b41646.
Incremental patch: 39fd17f652327c1f514694e11daf0f796dc89490394abe05f4bd8b53a3389646.

Safety fact: reopening must show the current unlinked set and reject stale evidence, while a withdrawn question stays with a person until its evidence changes again.
That fact fails for policy reconsideration. PostgreSQL persistence and browser behaviour remain unproven.

Checks:
- pass — Read the incremental patch and affected callers: mapRaise supplies the same material, evidence and refs to initial raise and undo; attachEvidence stores the refreshed title, evidence, basis and hash.
- pass — Ran real exported undo/mapRaise/answer functions from the head export with an in-memory database stub, using existing packages through NODE_PATH (no installation).
  Deciding lines: "PASS undo link tests/a.spec.ts n=3 count=2 shown=2 staleAnswer=conflict laterLink=2"; "PASS undo link tests/large.spec.ts n=521 count=520 shown=50 staleAnswer=conflict laterLink=2".
  Also passed no-file grouping and create-answer withdrawal probes; refreshed material/hash equality and preservation of the later link were asserted.
  Limit: SQL results/count/digest and writes were simulated, not executed by PostgreSQL; this does not prove database integration or original creation limits.
- issues — Ran real undo, heldOpen and reconsiderPolicySteps against identical simulated three-test/two-link state, twice at head and once using decisions.ts from 34a3187f.
  Private functions were exposed by adding exports to an in-memory transpilation; their bodies were unchanged. No source file was written.
  After undo, changed only the policy setting from ask to track and drained reconsiderPolicySteps, as accepting a policy change does.
  Previous revision: "BEFORE POLICY rev=base count=3 protected=true"; "AFTER POLICY ruled=0 state=open latestAnswer={\"is\":\"withdrawn\"} remaining=2".
  Head, reproduced: "BEFORE POLICY rev=head count=2 protected=false"; "AFTER POLICY ruled=1 state=decided latestAnswer={\"is\":\"track\"} remaining=2".
  Initial probe attempts stopped on unimplemented stub queries; those were corrected and rerun. They were method failures, not application findings.
- pass — Ran the existing Biome executable against src/server/decisions/decisions.ts, src/server/decisions/kinds.ts and test/policy.test.ts: "Checked 3 files ... No fixes applied."
- not checked — bun run check exited 4 at preflight: "23 of the packages package.json names are not installed"; "nothing was run".
- not checked — bun test test/policy.test.ts test/map-create-limit.test.ts test/e2e/queue-and-runs.test.ts exited 4 at the same preflight; no unit or browser tests ran.
- not checked — Full typecheck, PostgreSQL integration, browser UI, real 501/520-test creation and cross-file 100,000-case limits. The export lacks installed packages and the brief supplies no PostgreSQL server.

Issue: [P2] Preserve withdrawal protection when refreshing a map question's basis.
Location: src/server/decisions/decisions.ts:1100–1120; heldOpen at 390–392 and reconsiderPolicySteps at 545.
Reachable sequence: under ask, report three tests in one file; link T-1 in the first question, then T-2 in the follow-up; undo the first link; accept a policy change to track.
Undo inserts the withdrawn decision with the old question basis, then attachEvidence replaces the question basis with the current T-1/T-3 set.
heldOpen compares that new basis with the withdrawn decision's old basis and returns false. Policy reconsideration therefore records a rule answer and closes the question without another report or test change.
The previous revision keeps the bases equal and leaves the question open. This is newly introduced by the refresh, rather than a defect merely inherited from the base.
Keep withdrawal protection tied to the refreshed state; add a regression check covering partial links, undo and policy reconsideration without intervening evidence changes.

VERDICT: issues
