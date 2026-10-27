# Verification report
Revision judged: ed6050e265a9ca943bf15f5a4f644689e3085440; base: 46a9ab0c1657515e49bc7961c416013f07d1250d.
Patch judged: full base-to-head diff, with re-review focused on `git show ed6050e2` and affected callers; prior findings supplied for 597c19a2a. No later revisions or GitHub consulted.
Patch identity: SHA256 521c966bfef1d6e2ce94c303781a1dbd8f67b0be45a973ec7526edc50aef0461, over `git diff 46a9ab0c ed6050e2` excluding lines beginning `index ` or `@@`, retaining whitespace.

Safety fact: a displayed span must use usable timing from every counted report, wait for pending evidence, and leave server write times and verdicts unchanged. UNPROVEN end to end: PostgreSQL aggregation, storage constraints, pending-report handling and write-time invariance could not run. Parser probes also found incorrect timing below.

Checks run in the supplied head export, without installing packages or writing test artifacts:
- **pass**: read incremental and full diffs; inspected parser callers, CLI joining, aggregation, pending checks, migration, archive handling and web/iPhone consumers. No previous verdict carried forward because executable code changed.
- **not checked**: `bun --no-install run check`, exit 4 before checks; deciding lines: `23 of the packages package.json names are not installed` and `nothing was run. This is about the machine, not the code.`
- **not checked**: named format unit suites. Direct `bun test --config=/dev/null ...` attempts stopped loading with `Cannot find package 'zod'`; `0 pass`. Read-only dependency-resolver preload attempt also failed. These are environment failures, not product findings.
- **not checked**: `test/reported-span.test.ts`, schema, HTTP, transfer, CLI integration and `test/e2e/reported-span.test.ts`; they require PostgreSQL, which the brief excludes. Browser rendering and iPhone builds/tests were not run.
- **pass**: existing Biome binary, `check` on evidence.ts, jest.ts, span.ts, span.test.ts and reported-span.test.ts; `Checked 5 files ... No fixes applied.`
- **pass**: `NODE_PATH=/Volumes/SSD/Work/mainworthy/node_modules bun --no-install -e` with node:assert, importing the export's real `parseReport`, `zonedTime` and `joinSpans`. Deciding line: `PASS 12 malformed-date, valid-zone and incomplete-join probes`; includes February 30, non-leap February 29, invalid month/hour/minute/second/offset and valid leap date/offsets.
- **pass**: same real-code assertion method for prior F3 and ordinary F2 cases; `PASS negative start: no span, one warning, one result`, `PASS bad end: no span, one warning, one result`, `PASS reverse pair: no span, one warning, one result`; valid Jest returned span 90..250.
- **pass**: real Playwright/Jest/Vitest fixtures matched their authored span expectations: respectively 1792040852255..1792040854285, 1792040850012..1792040850412 and 1792040851216..1792040851715.
- **pass**: real ReportSpan schema assertions; `six invalid spans rejected, zero-length span accepted`. Invalid cases covered either missing half, reversed times, negative/fractional start and unsafe integers. This does not prove the database constraint.
- **issues**: warning and calendar counterexamples below, each reproduced twice through `parseReport`, with assertions of the observed behavior.

F2 remains partly unresolved: some unusable Jest/Vitest timing still disappears without its promised warning.
Location: src/surfaces/formats/jest.ts:136 and :141, reached by `parseReport` for accepted Jest/Vitest JSON and then the report CLI.
Input A: a valid passing Jest file with run/file start `1e20` and file end `1e20 + 100000`. All timing is present and finite, but cannot become safe epoch milliseconds. The preliminary validation accepts it and `spanOf` returns undefined instead of the `unusable` sentinel.
Input B: two valid passing Jest files, first with start 100 and no end, second with start 200 and end 199. The first missing end returns before the second file's reversed pair is checked.
Deciding output, repeated twice: A `{span:null,warnings:[],results:1}`; B `{span:null,warnings:[],results:2}`. Results survive, but the CLI cannot warn that present timing was unusable, contrary to the documented contract and previous F2. Validate all supplied timing before returning for missing values, and classify failed span construction as unusable.

F5: the calendar fix remaps years 0000..0099 through Date.UTC's 1900 offset.
Location: src/surfaces/formats/span.ts:27 and :34, reached by both the JUnit and Playwright timing readers.
Input: `parseReport('<testsuite timestamp="0099-10-11T00:00:00Z" time="1"><testcase name="a"/></testsuite>', {file:'x.xml'})`.
Deciding output, repeated twice: reported start `939600000000`, ISO `1999-10-11T00:00:00.000Z`, warnings `[]`; the input's actual epoch is `-59018544000000`. This pre-epoch timestamp should supply no span under ReportSpan's nonnegative contract, rather than fabricate one in 1999. If combined with a current report it can inflate the displayed aggregate by decades. The prior Date.parse implementation did not remap the year. Preserve the literal year or reject pre-epoch input before constructing a span.

Earlier findings: F1's explicit non-null pair constraint and missing-end aggregate check look corrected in source, but remain not checked on PostgreSQL. F3 and the reported February-30 case from F4 passed executable probes. F2 has the remaining cases above; F5 was introduced by the F4 fix.
VERDICT: issues
