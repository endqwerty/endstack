Design note and actions for the hypothetical "archive tasks" build, before the first edit to production code:

**1. Interview.** What archiving does depends on the user's intent, so I'd run `interview` before step 1. First I'd confirm how I read the system: `shared/task.ts` defines `Task`, and the web client and CLI each repeat the filter `!t.done && !t.deletedAt`. Then I'd ask one question at a time, each with the answer I'd assume if nobody replies:
- Can a task be archived and done at once, or is archiving a way to hide old tasks? Assumed: archive is separate from done and is reversible.
- Where do archived tasks show up? Assumed: an "Archived" view on web and a `--archived` flag on the CLI.
- How will you judge it's working? Assumed: an archived task disappears from both lists and an unarchived one comes back.

I'd write the brief to `docs/design/archive-tasks.brief.md` and run goldfish's concept reviewers on it. If the user isn't there, I'd take my defaults and log them under Open questions.

**2. Principles index.** Six entries match this change. I'd read the five I relied on: Redesign From First Principles, Model the Domain, Type System Discipline, Experience First and Subtract Before You Add. Test Behavior, Not Implementation also matches; I'd read it before writing tests, as the index says.

**3. Ground.** The behaviour lives in `shared/task.ts`. Two consumers do the same filtering job: `web/TaskList.tsx` and `cli/list.ts`. Writes go through `PATCH /tasks/:id` in `server/tasks.ts`. I'd also search for any other readers of `done` or `deletedAt`, such as counts or exports.

**4. Shape.** Adding `archivedAt: Date | null` next to `done` and `deletedAt` would allow combinations the domain doesn't want, such as deleted and archived together. So I'd treat archiving as a state that was there from the start:
`type Lifecycle = {kind:'active'} | {kind:'archived', at} | {kind:'deleted', at}` with `done: boolean` kept separate, because done and lifecycle really are independent. The PATCH body gets parsed into a typed action (`archive`, `unarchive`, ...) at the boundary.

**5. Alternatives.** The change crosses the shared, server, web and CLI boundaries, so I'd run `architect`. It would compare two shapes: (A) a `lifecycle` union with action-based PATCH, against (B) an `archivedAt` field with field-based PATCH. I expect A to win: each piece of state has one owner and there's one way to archive.

**6. Subtract.** Both copies of the filter get deleted. In their place goes one `visibleTasks(tasks, view)` in `shared/task.ts`. The `deletedAt` field is removed too, and its data moves into `lifecycle`.

**7. Every consumer.** Web and CLI both change and both get checked.

**8. Failure.** Archiving is idempotent: archiving an archived task returns 200 with no change. Two actors doing it at once is last-write-wins on a single field. Stored rows need a migration from `deletedAt` to `lifecycle`.

**9. Tests.** These go in `server/tasks.test.ts` and go through PATCH, then check what a list returns. They are behaviour tests, not checks on internals.

**10. Throughput.** The shared type and migration have to land first. After that, server, web and CLI touch separate files and can proceed in parallel. Each unit ends with a check.

**Design note:** The new shape is a `Lifecycle` union plus `done`, with one shared visibility function. Web and CLI both switch to it, and the duplicated filters and `deletedAt` are deleted. Model the Domain and Redesign From First Principles are why I chose a union over a third flag. Subtract Before You Add is why the filter exists once.

**Design doc:** `docs/design/archive-tasks.md` with these sections: Problem, Goals/Non-goals, Plan, Behaviour (scenarios such as "when a task is archived, then the web and CLI lists omit it", each naming its test), Alternatives (B and why it lost), Implementation, Tasks, Open questions. Then I'd run `goldfish` on the doc until its review converges, and reconcile the doc against the brief and delete the brief, as the interview skill says.

**After:** I'd write a failing test first, then implement unit by unit: type and migration, server PATCH, shared filter, web, CLI. Each runs its checks on the real artifact, I keep the output that settles it, and I mark the task done in the doc. Once the build is finished, I'd rewrite the doc in its own commit: delete Implementation and Tasks, and make Plan describe the shape as built. I'd read the whole diff and get an independent review through `verify`. Then I'd open a non-draft PR. It leads with the choices I made for the user and how to reverse each (the assumed defaults, the `deletedAt` migration). Then it gives the brief: why, what changed, where to start reading, the design note, checks and evidence, reviewer and revision, findings and limits. I'd report the PR, its revision and whether it's ready, and stop there: no babysitting, no merge.

Files opened: `delivery-dry/old/build/SKILL.md`, `delivery-dry/old/build/references/design.md`, `skills/principles/SKILL.md`, principles references (`redesign-from-first-principles.md`, `model-the-domain.md`, `type-system-discipline.md`, `experience-first.md`, `subtract-before-you-add.md`), `skills/interview/SKILL.md`, `skills/architect/SKILL.md` (and only the byte count of `skills/goldfish/SKILL.md`, not its text).
