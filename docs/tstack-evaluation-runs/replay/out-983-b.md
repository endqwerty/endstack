Revision: b9a57179; base: f04e69e6; previous verdict: 34a3187f.
Patch judged: read the full f04e69e6..b9a57179 diff, concentrating fresh verification on 34a3187f..b9a57179 and affected map/undo/answer callers.
Patch identity: SHA256 of file paths and exact added/deleted lines, preserving whitespace and excluding hunk offsets/commit metadata.
Full patch: df11a74cdd1451f055c2d47cf8d8a1a6331daa53a919c8b487b9498483b41646
Re-review patch: 39fd17f652327c1f514694e11daf0f796dc89490394abe05f4bd8b53a3389646
Head tree: d9f57bb481a7cb5f14b2bbe40991444e8328788b.
The behavioral patch changed, so the earlier verdict alone does not cover this revision.

Safety fact: withdrawing an older map answer must preserve later links, reopen one question with current unlinked tests/count/basis, and reject answers bearing the previous evidence hash.
Status: demonstrated at the production-function boundary with an in-memory database fixture; UNPROVEN against PostgreSQL and the real operation surface.

Checks:
- PASS — git diff --check for both revision ranges: exit 0, no output.
- PASS — existing Biome binary checked all eight changed TypeScript files: “Checked 8 files in 345ms. No fixes applied.”
- PASS, limited — imported actual head undo/mapRaise/answer/HANDLERS through NODE_PATH pointing to existing dependencies; no installed packages or repository edits.
  Deciding line: “PASS real undo + mapRaise with in-memory DB fixture: open=[Q-1], evidence=[T-1,T-3], count=2, T-2 remains linked, old hash conflicts, track holds refreshed basis”.
  Fixture exercised two earlier partial links plus an open remainder, ownership-aware restoration, refreshed evidence and stale-answer rejection; database methods were substitutes, not PostgreSQL.
- PASS, limited — actual mapRaise with fixture counts 0, 1, 50, 500, 520: “PASS mapRaise count/display limits with in-memory DB fixture: counts=0,1,50,500,520; visible<=50, refs<=20”.
  This checks presentation/assembly, not SQL aggregation, database paging or transaction atomicity.
- NOT CHECKED — bun run check: exit 4; “23 of the packages package.json names are not installed”; “check: nothing was run. This is about the machine, not the code.”
- NOT CHECKED — bun test test/policy.test.ts test/map-create-limit.test.ts test/work.test.ts test/e2e/settings.test.ts test/e2e/triage.test.ts test/e2e/queue-and-runs.test.ts test/e2e/queue-select.test.ts: exit 4 at preload, same missing-package diagnostic; “bun test: nothing was run.”
- NOT CHECKED — PostgreSQL operation-level regressions: whole-file create beyond 500, immediate remainder after link, whole-set track basis, undo persistence, command-wide creation limit and rollback. No PostgreSQL server is available under the brief; none was started.
- NOT CHECKED — browser journeys and full type-check: preflight prevented the claimed suite from running. Existing dependencies used for the isolated probe do not satisfy the export's frozen dependency installation.

Issues:
- SHOULD — Required verification remains incomplete. The real PostgreSQL/operation safety fact and required regression suites have no independently reproduced passing result at b9a57179. The isolated fixture and lint do not establish database behavior or browser behavior; rerun the required checks with the head's dependencies and PostgreSQL before treating this revision as verified.
No code defect was confirmed in this re-review; the verdict below reflects the verification gap, not a reproduced product regression.
VERDICT: issues
