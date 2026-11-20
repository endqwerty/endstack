Before the first edit to production code, in order:

**1. Outcome, checks, scope** (from build)
- Outcome: a user can archive a task. Archived tasks disappear from the default list in both the web client and the CLI. Archiving can be undone.
- Checks: `server/tasks.test.ts` covers archiving, re-archiving the same task and unarchiving. Web and CLI each get a test that hides archived tasks.
- Scope: the Task type, the PATCH endpoint, the two list views and the stored schema. An "archived" view is out of scope; it goes under Open questions.

**2. Principles.** I read the whole index, then the references that match this change: Redesign From First Principles, Foundational Thinking, Model the Domain, Type System Discipline, Make Operations Idempotent and Subtract Before You Add.

**3. Ground.** I search for every reader of `deletedAt`, `done` and `Task` across the repo, including persistence and serialization. Known consumers: `web/TaskList.tsx` and `cli/list.ts`, which both filter with the same predicate, and `server/tasks.ts`. All of them change. Anything else the search finds either changes too or gets a written reason for staying as it is.

**4. Shape.** If archiving had been there from the start, a task's lifecycle would be one field, not two nullable flags:
```ts
type Lifecycle = { state: "live" } | { state: "archived"; at: Date } | { state: "deleted"; at: Date };
type Task = { id: TaskId; title: string; done: boolean; lifecycle: Lifecycle };
```
This rules out "archived and deleted at once". `done` stays separate because a finished task can still be archived. JSON goes through `parseTask` at the server boundary.

**5. Alternatives (architect).**
- A: add `archivedAt: Date | null` next to `deletedAt`. That allows invalid combinations and adds a third term to both filters.
- B: the union above, plus one `isListed(t)` in `shared/task.ts`.

I pick B: one owner for lifecycle and one visibility rule.

**6. Subtract.** Delete `deletedAt` and the two copies of the filter. Both clients call `isListed`.

**7. Failure.** PATCH must be idempotent. Archiving an already archived task keeps its original `at`. Archiving a deleted task is rejected. Moving existing rows from `deletedAt` to `lifecycle` happens in one migration that can run again safely.

**8. Tests.** No test may avoid the archived+deleted state. The type makes it impossible to build.

**9. Order.**
1. Type, `parseTask` and `isListed`, with unit tests.
2. Migration.
3. PATCH, with tests.
4. Web and CLI switch to `isListed`.

**Design note.** `Task.lifecycle` is a union of live, archived and deleted, and it replaces `deletedAt`. One `isListed` replaces the duplicated filters in web and CLI. PATCH sets lifecycle idempotently. Principles that changed a choice:
- Redesign From First Principles / Model the Domain: a union instead of a second nullable date.
- Subtract: delete the duplicated filter.
- Idempotent: re-archiving keeps the original timestamp.

**Design doc** `docs/design/archive-tasks.md`, written one section at a time:
- Problem; Goals / Non-goals
- Plan
- Behaviour, as numbered when…then scenarios, each naming its test
- Alternatives (A turned down)
- Implementation and Tasks
- Open questions. Assumed meanwhile: unarchive is allowed, and there is no archived view yet.

**Goldfish** on the doc: zoom-out, then comprehension, then the critic loop and the readiness loop. I fix findings until two clean rounds in a row.

**After:** I implement each unit and finish it with its check. The doc's scenarios become tests: `server/tasks.test.ts`, plus web and CLI list tests. I commit per unit. In a separate commit I finish the doc: delete Implementation and Tasks, rewrite Plan as built, and drop answered questions. Then I get independent review through verify. Finally I open a non-draft PR that links the doc, carries the design note, and lists:
- each choice made for the user and how to reverse it (lifecycle union, removal of `deletedAt`, unarchive allowed)
- checks with their deciding lines quoted
- the reviewer and the revision

I report the PR and revision. No watching or merging.

Files opened: `skills/build/SKILL.md`, `skills/build/references/design.md`, `skills/principles/SKILL.md`, `skills/principles/references/{redesign-from-first-principles,model-the-domain,type-system-discipline,foundational-thinking,make-operations-idempotent,subtract-before-you-add}.md`, `skills/architect/SKILL.md`, `skills/goldfish/SKILL.md`.
