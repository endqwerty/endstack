(a) First message to the user, sent before the first unit starts: every question I can foresee that might later hold a merge, each with a stated default. Examples: which endpoints share middleware and how the stacks group, whether API contract or behaviour changes are allowed, whether a final PR that deletes the old router fits the program, and whether deployment is out of scope (by default it is). I proceed on the defaults for anything left unanswered. I do not ask whether to merge or keep going.

(b) First three actions:
1. Create the durable notes file (goal, the 14 units, stacking plan, ownership, PR links, verdicts, blockers) and start the decision trail through show-me-your-work.
2. Send the one questions-with-defaults message above.
3. Kick off a single pilot endpoint to one owner. The kickoff names the goal, allowed and forbidden paths, branch ownership, forbidden actions, dependencies, standing orders, landing authority and the evidence that proves completion. Fan-out waits until that pilot has gone through owner, verifier and merge.

(c) The endpoint 3 typo: I don't fix it, because I run the program, never the code. I add it to the endpoint 3 owner's kickoff and to the notes file, since that owner is the only writer of that branch. If the fix doesn't block the migration, it can also be parked as a follow-up.

(d) Merges: there are no user approval gates, because naming orchestrate grants landing authority. Each PR's owner merges it through ship's gates, and only with a passing verdict from a fresh, read-only, non-author verifier on the current head, required checks green and holds honored. The pilot lands first; stacked PRs land in chain order, with the owners handling rebases. A final unit removes the old router. Failed gates go back to an owner instead of to the user. If the user says "don't merge" or "I'll land it", owners stop at merge-ready.
