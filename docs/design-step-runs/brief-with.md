# Brief: quarantine a test

Queue item 1 of 2. Item 2 (cancel a queued tracker request) touches only `src/core/tracker.ts`, `src/server/trackers.ts` and `src/trackers.test.ts`. Do not edit those files here.

## Outcome

An operator can quarantine a test by name and give a reason. While a test is quarantined:

- its failure no longer makes the gate fail,
- `gatekeep show` and the web change page both mark it as quarantined and show the reason.

An operator can also release the test, which restores the old behaviour.

## Read first

Before the first production edit, read `~/.cache/endstack-design-dryrun/skills-S/build/references/design.md` and the principles index in `skills-S/principles/SKILL.md`. Then read the references this brief cites: `model-the-domain`, `type-system-discipline`, `test-behavior-not-implementation`. Also apply `typescript-best-practices` to every `.ts` edit and `technical-writing` to the commit message.

## Where the behaviour lives

- `src/core/model.ts` has `Result` and `verdictOf`. `verdictOf` is the only place that decides pass or fail.
- `src/server/api.ts` has `Api` and `Store`. `gate`, `results` and `runResults` all read run data from `Store`.
- `src/cli/changes.ts` (`show`) and `src/web/changes.ts` (`changePage`) are the two clients. Each renders `api.results(...)` on its own. Both must change, and both must be tested.

## Design note

Quarantine is operator state about a test name. It is not an outcome of a run, so do not add it to the stored `Run.results`.

- `Store` holds `Map<string, string>` from test name to reason. Quarantine is global to the test, not per change.
- Add `quarantine(test, reason)` and `release(test)` to `Api` and `Store`. Calling `quarantine` on an already quarantined test replaces the reason. Calling `release` on a test that is not quarantined does nothing. Both are safe to repeat.
- Parse at the boundary. A blank reason (empty or only whitespace) is rejected with an `Error`, and the stored reason is trimmed. Downstream code trusts it.
- `Api.results` and `Api.runResults` return a tagged union instead of today's `Result`. A quarantined result carries what the run saw, so nothing is lost:

```ts
export type Reported =
	| Result
	| { test: string; outcome: "quarantined"; observed: Result["outcome"]; reason: string };
```

- `verdictOf` takes `Reported[]`. A quarantined result never counts as a failure. Verdict rules after the change: no results is `pending`; any `failed` that is not quarantined is `fail`; otherwise `pass`. A run whose only failures are quarantined therefore passes.
- Apply quarantine when `Store` reads, for the latest run and for `runResults(id)`. Releasing a test therefore changes the verdict of old runs too. That is intended: the store keeps raw results and the operator state decides how to read them.
- Both clients switch on `outcome` with a `never` check so a new variant fails compilation.
  - CLI line: `  quarantined login (failed): flaky on CI`, in the same column layout as other lines.
  - Web: `<li class="quarantined">login (failed): flaky on CI</li>`. Escape nothing new; follow the existing page, which does not escape.
- Add a CLI entry `quarantine(api, test, reason)` and `release(api, test)` in `src/cli/changes.ts` returning a one-line confirmation. There is no router or command parser in the repo, so do not build one.

Deleted or made redundant: nothing is dead after this change. The `Result` type stays as the stored shape.

Out of scope: tracker requests for quarantined tests, persistence across restarts (`Store` is in memory already), per-change quarantine, expiry.

Product choices made here, so do not reopen them: global scope, retroactive reading, a quarantined run with no other failures passes.

## Checks to write first, and see fail

Each test calls the real client or `Store` and asserts the literal output. Put them in `src/changes.test.ts`.

1. Push `feat` with `login` failed and `search` passed. Quarantine `login` with `flaky on CI`. `await show(store, "feat")` must equal `"feat @ a1: pass\n  quarantined login (failed): flaky on CI\n  passed  search"` (check the exact column padding against the existing `padEnd(7)` line before you write it).
2. Same data. `await changePage(store, "feat")` must equal `'<h1>feat @ a1: pass</h1><ul><li class="quarantined">login (failed): flaky on CI</li><li class="passed">search</li></ul>'`.
3. Quarantine `login`, with `login` and `search` both failed. The verdict is `fail`, because `search` still fails. This proves quarantine is per test.
4. After `release(store, "login")`, the verdict in check 1 is `fail` again and the line reads `  failed  login`.
5. `quarantine(store, "login", "   ")` rejects, and the verdict is unchanged.
6. The two existing tests pass unchanged.

`bun test` must pass before you commit.

## Limits from the repository

`AGENTS.md` applies. There is no remote. Do not push, open a pull request, or start a reviewer or verifier. Do not install packages. Commit on the current branch with a clear message. Report the change as unverified, since no independent verdict is possible here. The report states the commit, the deciding lines of `bun test`, each principle that changed a choice, and any place the shape did not fit. If it does not fit, stop and report instead of redesigning alone.

The builder does not merge. The operator merges the queue later under autopilot.
