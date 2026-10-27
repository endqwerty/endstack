# Verification of reported test spans
Revision: ed6050e265a9ca943bf15f5a4f644689e3085440.
Base: 46a9ab0c1657515e49bc7961c416013f07d1250d.
Patch judged: the head commit `git show ed6050e2`, addressing F1-F4 after the verdict on 597c19a2a, plus its affected parser, storage and aggregate callers in the full base-to-head diff.
Full-patch SHA-256: `8badb28dfdb88f4fbc25c7c57c2c312e6da5e0b2ad40238fd7f35809dfd9d1d5`. Computed from the diff after removing index metadata and replacing hunk headers with `@@`; changed-line whitespace is preserved.

Safety fact: a reported span must not appear unless every contributing report supplies usable, complete timing, with no declared work outstanding; timing must not change verdicts or server write times. Parser cases were exercised. The stored-data and completeness guarantees remain unproven without PostgreSQL.

Checks
- PASS: read the seven-file head patch and affected format, report-input, acceptance, migration, archive and results-read paths. F1 now explicitly requires both columns non-null; the aggregate counts either missing half as untimed. This is inspection, not a PostgreSQL execution pass.
- NOT CHECKED: `bun run check` exited 4 at preflight: `23 of the packages package.json names are not installed`; `nothing was run`. No packages were installed.
- PASS: ran unchanged `span.test.ts`, `junit.test.ts` and `diagnostics.test.ts` from the head export. Deciding lines: `160 pass`, `0 fail`, `2501 expect() calls`. Used `bun test --config=/dev/null --preload /dev/fd/0` from the export's parent, with a stdin preload mapping package names to the checkout's actual installed dependencies. Project preflight was omitted to avoid starting PostgreSQL; application code was not replaced.
- NOT CHECKED: report.test.ts and retries.test.ts initially failed module loading on `@noble/hashes/sha2.js`; both also import the database harness. They were not counted as passing or rerun against a server.
- PASS: 32 additional assertions executed real `parseReport`, `zonedTime` and `ReportSpan` code. Deciding line: `PASS 32 additional parser/date/contract probes`. Covered null/string/object/boolean/negative Jest times, invalid calendar dates and offsets, valid leap years and signed offsets, and incomplete/reversed/fractional API spans.
- PASS: original F2/F3 cases retain results, omit spans and warn once for an invalid file time or negative run start. Original F4 February 30 case now omits the span. The unit regression tests and additional assertions passed.
- ISSUES: two boundary probes below reproduced identically twice. Deciding lines: `reproduction 1: year 0099 produces 1999 span; startTime=1e20 produces file-only span and 0 span warnings`, and the identical `reproduction 2`.
- PASS: head-change lint, `Checked 5 files ... No fixes applied.` No diagnostics. SQL and snapshot files are outside this lint check.
- ISSUES, unrelated to this patch: full-tree Biome exited 1, `Found 4 errors`, `Found 1 warning`, `Found 14 infos`. Errors were noMisusedPromises at src/web/runs/cockpit.tsx:433,480,627 and noFloatingPromises at test/audit.test.ts:661. `git diff 46a9ab0c ed6050e2 --` those two files is empty. These are not attributed to the change.
- PASS: full-range and head-only `git diff --check` both exited 0 with no diagnostics.
- NOT CHECKED: PostgreSQL migration/constraint, aggregate, archive import, report HTTP/CLI, gate/write-time and browser integration tests, including test/reported-span.test.ts, test/e2e/reported-span.test.ts, src/cli/report-span.test.ts, transfer, schema and HTTP tests. The brief supplies no PostgreSQL server and prohibits requiring one. F1's runtime fix remains unverified.
- NOT CHECKED: complete typecheck and iOS checks. The full check stopped before typechecking; no Swift build was run.

Findings
N1. nit. src/surfaces/formats/span.ts:27,34. The new Date.UTC construction maps years 00-99 to 1900-1999. Real JUnit input with timestamp="0099-01-01T00:00:00Z", time="1" and one testcase returns `{startedAt:915148800000,endedAt:915148801000}`, although that ISO date is before the supported epoch and previously yielded no span. A malformed early-year timestamp can now fabricate timing. Preserve the literal year or reject unsupported pre-epoch dates. Ranked nit because these years are a rare runner input.
N2. nit. src/surfaces/formats/jest.ts:130-141. An out-of-range numeric run start still falls back silently to file times. Setting only real-jest.json's startTime to 1e20 yields `{startedAt:1792040850138,endedAt:1792040850412}` with zero span warnings. The finite/nonnegative guard admits it, then Math.min discards it. Reject an unrepresentable run start and return the unusable diagnostic. This is a residual boundary case of F2/F3, ranked nit because it requires an extreme malformed numeric timestamp.

No blocker or should was confirmed. A full delivery pass is withheld because the required stored-data safety fact has not been proved on PostgreSQL; the two confirmed nits are not delivery blockers by themselves.
VERDICT: issues
