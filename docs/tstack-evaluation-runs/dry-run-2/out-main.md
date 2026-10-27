# Dry run 2, SKILLDIR main (paper exercise)

Note: nothing in main defines "full send" or "full stop" (grep finds neither). Both are read as plain language.
Swarm check for every case: one small change, no independent parts, so no `swarm`.

## Case 1: "autopilot: add a retry for failed uploads"
- Skills: `build` (with its design.md step and `verify`). `autopilot-full` is opened only because the word is in the message, and its own clause sends it back to build.
- Rule: ROUTING "`ship` or `autopilot-full` only when the user explicitly asks to merge, land or ship"; autopilot-full "a skill name, 'autopilot' or 'keep going' alone is insufficient. Without landing authority, build each item and leave landing to the user".
- Stop: at a non-draft, standalone PR with an independent (other-provider) verifier verdict on the current revision. Without a verifier: "report unverified; do not deliver".
- Merge: no. build: "Do not merge, arm automatic merging... Opening a pull request does not start babysitting."
- Waits for the user: yes, the merge. I report the PR, revision and readiness and stop.

## Case 2: "full send on #412"
- Skills: `ship` is the only one that could land it. Its gate fails on the wording, so I follow `ship` step 1 and stop. Nothing is merged.
- Rule: ship 1, "An explicit 'ship this pull request' counts; selecting this skill, ownership or a budget request alone does not... If the scope is unclear, do not land anything." ROUTING needs the user to "explicitly ask to merge, land or ship". "Full send" names none of those.
- Second, independent block: ship 2, "unresolved blockers or unavailable review stop landing". The unanswered bot finding is one until checked. babysit: "Treat comments as claims... fix real findings... answer the rest with evidence." A fix changes the patch, so verify's carry-forward ("Anything else: a fresh verdict on the current revision") requires a new independent verdict.
- Stop: I report that #412 is green and verified at its head, that one bot finding is open, and that no merge words were given. Any writes beyond that (triaging the finding) are babysit's job and its scope is not requested here, so I only report.
- Merge: no.
- Waits for the user: yes. The user must say merge/land/ship (or confirm "full send" means that). If they do, I answer the finding first, get a fresh verdict if the patch changed, then ship merges #412 alone.

## Case 3: "full stop: add a retry for failed uploads"
- Skills: none executed. `build` matches the task, but the message also carries an explicit stop.
- Rule: build "An explicit stop means no further writes"; ship "a stop instruction prevents writes"; build "A plan or help request explains the workflow without executing it".
- Stop: before any edit, branch or PR. The message contradicts itself, so I take the stricter reading. I would report the plan (design, checks, verifier) in text only.
- Merge: no.
- Waits for the user: yes, one clarification: stop, or build it (the review-first path of case 1). If main meant a different thing by "full stop", it does not say so.
