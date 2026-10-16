# gatekeep

A small CI gate. A change (a branch) gets runs, one per pushed head; each run
has test results and a verdict.

- `src/core`: the model, pure.
- `src/server`: the store and the operation registry (`ops.ts`). Everything
  outside the server reaches it through `Api` or through `call(op, input)`.
- `src/cli`: the `gatekeep` command line, one file per command.
- `src/web`: server-rendered pages, one file per page.
- `src/integrations`: chat digests and commit statuses.

`bun test` runs the tests.
