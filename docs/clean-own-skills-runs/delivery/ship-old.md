**Part A (reply to the user):**

To land PR #12, I would:

1. Make sure the verifier's passing verdict is for the current head commit. If anything was pushed after that verdict, or the base branch moved, the PR needs fresh checks and a new verdict first.
2. Check that the required checks still pass and every review finding, bot comments included, has either a fix or a written reason. Then confirm the host reports the PR as mergeable and that nothing it depends on is still unmerged.
3. Merge it once through the project's normal merge path, pinned to the verified head commit so the merge fails if the branch has moved. I would not turn on auto-merge.
4. Check that the merge actually appears on the target branch, then tell you the commit and where it landed. I'd leave the source branch in place and do any local cleanup the project calls for.

Your message asks how I'd do it, so I haven't merged anything. Say "ship #12" or "merge it" and I'll run those steps.

**Part B (actions this turn):** None.

The skill says planning and help questions get an explanation of the process, not a run of it. "How would you ship PR #12?" is a question about the process, not a request to merge, so this turn makes no tool calls, merges or comments.
