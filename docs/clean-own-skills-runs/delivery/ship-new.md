**Part A: reply to the user**

You asked how I would ship it, not for me to ship it, so I haven't merged anything. If you tell me to ship, merge or land PR #12, I would:

1. Treat that as the go-ahead and not ask again.
2. Check the gates on the current head commit: the verifier's passing verdict covers that exact commit, required checks pass, every review finding (bot findings too) is fixed or answered, and the host reports the PR as mergeable. If any of these fails, I report the gap and stop.
3. Make sure no unmerged parent PR sits under #12. I land one PR at a time, starting from the lowest unmerged dependency.
4. Merge with the project's delivery mechanism, pinned to the verified head commit so the merge is refused if the branch has moved since. I would not turn on auto-merge.
5. Check that the merge actually reached the target branch, not just that it was requested. If the result is unclear, I look before retrying.

Merging doesn't extend to deploying, deleting anything, or other work. Say "ship #12" and I'll do it.

**Part B: actions this turn**

None. The ship skill applies only when the user names it or asks to merge, land or ship. "How would you ship PR #12?" asks about the method, and the user's rules allow merging only on an explicit request.
