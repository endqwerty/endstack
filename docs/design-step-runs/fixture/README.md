# gatekeep

A tiny CI gate. A change (a branch) gets runs, one per pushed head. Each run has
test results and a verdict. Two clients show a change: the web page
(`src/web`) and the command line (`src/cli`). Both talk to the server through
the `Api` interface in `src/server/api.ts`. Tracker requests (`src/core/tracker.ts`,
`src/server/trackers.ts`) file an issue in an external tracker for a failing test.

`bun test` runs the tests.
