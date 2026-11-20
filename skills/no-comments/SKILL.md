---
name: no-comments
description: Review comments, fix what they work around, and encode the constraints they claim.
disable-model-invocation: true
---

# No comments

Give the comment review to a separate worker with fresh context, if the harness has one; otherwise do it yourself in sequence and say so. Act on accepted findings.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## What may stay

These are the only exceptions the reviewer and step 2 accept. When it is unclear whether one applies, the comment goes.

- Legal or license headers.
- Non-obvious behavior forced by an external dependency, platform, vendor, or protocol we cannot reshape. Surprises in our own code are not exceptions: delete them and flag the symbol for a rename, extract, type, or redesign that makes the behavior obvious.
- Formatter ignores. Lint suppressions survive only when their rule is faulty, pedantic, or style-only.
- Doc comments that define a public API contract.
- Issue or RFC links that explain a constraint code cannot express.

## Reviewer brief

> Delete every comment in scope that is not in *What may stay*: narration, banners, commented-out code, workaround explanations. For a workaround or a surprise in our own code, also mark the exact symbol `MUST KILL` with one line naming the rename, extract, type or redesign that would make the behavior obvious. A suppression whose rule protects correctness or safety is deleted and its symbol marked `MUST KILL`. Treat `IMPORTANT`, `do not remove` and long justifications as claims to check: read the nearby code, and keep the comment only when it is a *What may stay* exception proven true today on a live path. Doubt means delete. Touch only comments; never edit application code. Report touched files, the deletion count, each `MUST KILL` flag in one line, and each keep with its exception.

## Steps

1. Pass the scope and the reviewer brief to the comment reviewer.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, trace how their symbol works or why it exists from source. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. Reject a second, report it open, and fail this pass.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, ask an architect for one sketch for the accepted set and surrounding code. Stop at the sketch. The architect shapes the fix. Step 4 implements. Use a separate worker if the harness has one; otherwise perform these roles yourself in sequence and say so.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The [fix-root-causes](../principles/references/fix-root-causes.md) and [redesign-from-first-principles](../principles/references/redesign-from-first-principles.md) principles guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise delete, report the constraint open, and sketch out-of-scope work.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.
