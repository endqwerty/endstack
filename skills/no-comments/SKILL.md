---
name: no-comments
description: "Review scoped comments as Comment Sicko, fix accepted findings, and offer enforceable encodings for claimed constraints. Use when asked to remove comments or replace workaround comments with root-cause fixes."
disable-model-invocation: true
---

# No comments

Give the comment review to a separate worker acting as Comment Sicko, if the harness has one; otherwise do it yourself in sequence and say so. Act on accepted findings.

Defer to Comment Sicko's fresh perspective.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Steps

1. Pass the scope to the comment reviewer. Use the available Comment Sicko role rules without restating them. If that role definition is unavailable, use the acceptance contract below and report that limitation.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, trace how their symbol works or why it exists from source. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. Reject a second, report it open, and fail this pass.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, ask an architect for one sketch for the accepted set and surrounding code. Stop at the sketch. The architect shapes the fix. Step 4 implements. Use a separate worker if the harness has one; otherwise perform these roles yourself in sequence and say so.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The the [fix-root-causes](../principles/references/fix-root-causes.md) and [redesign-from-first-principles](../principles/references/redesign-from-first-principles.md) principles guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise delete, report the constraint open, and sketch out-of-scope work.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.
