# Delivery skills cleanup: paired dry runs

Old text: `git show 05cad93:<path>`. New text: this branch. Each arm was a fresh
general-purpose subagent, read-only, told to read only the skill and what it links.

## Run 1: build design step

Task: "build: let users archive tasks in our todo app." `Task { id, title, done: boolean,
deletedAt: Date | null }` in `shared/task.ts`; web `web/TaskList.tsx` and CLI `cli/list.ts`
both filter `!t.done && !t.deletedAt`; `PATCH /tasks/:id` in `server/tasks.ts`; tests in
`server/tasks.test.ts`. Asked for everything produced before the first production edit.

| Check | Old | New |
| --- | --- | --- |
| Read design.md and the whole principles index before code | yes | yes |
| Shape: one lifecycle union instead of a third nullable field | yes (`Lifecycle` union) | yes (`Lifecycle` union) |
| Consumers: web and CLI both change, shared filter replaces both copies | yes | yes |
| Tests named (scenarios naming their test, PATCH-level tests) | yes | yes, plus web and CLI list tests |
| Architect run, design doc and goldfish before code | yes | yes |
| Non-draft PR with choices and reversal; stops before merge | yes | yes |
| Ran interview first | yes (design.md told it) | no (line dropped; ROUTING sends intent-shaped features to interview, and this arm did not see ROUTING) |

## Run 2: "how would you ship PR #12?" to ship (plan/help sentence removed)

PR #12 open, green, passing verdict on head; merge rights. Asked for the reply and the
actions taken this turn.

| | Old | New |
| --- | --- | --- |
| Actions this turn | none | none |
| Reply | explains the steps, asks for "ship #12" | explains the steps, asks for "ship #12" |
| Reason given | skill's "planning and help questions explain" | "how would you" asks about the method, not a request to ship |

Result: no behaviour change in either run; the removed text was not what produced the
outcome.

## Outputs

Old and new subagent replies, verbatim, are in `build-old.md`, `build-new.md`,
`ship-old.md`, `ship-new.md`.
