The program splits into independent work: B and C after A, and E alongside them. **Orchestrate** supplies program landing authority; **swarm** shapes parallel work, and **verify/ship** gate every landing. This is a plan only; nothing is executed.

**First hour**

1. **Establish the durable program record.** Record the six-PR boundary, destination `main`, dependency graph, ownership, standing orders, decisions, PR links, current revisions, checks, verdicts, blockers and worker lifecycle. Maintain a linked decision trail. Completion means all callers converted, all parser fixtures passing and the old API removed. Deployment and the suggested irreversible old-data purge are excluded; API removal requires neither.

2. **Reconcile existing work before assigning replacements.** Inspect branches, diffs, PR activity and worker state. Classify every previous worker as active, done, replaced or absorbed. For the worker stopped by a context limit, preserve its artifacts and resume through a smaller, self-contained assignment after confirming it cannot still write. Treat a late result as evidence against the current revision, never permission to overwrite newer work; route unique findings to the current owner or a fresh worker.

3. **Select routed workers.** Plan to consult the live catalog, allowance and `homelab route plan/models` before delegation. Use the active balanced profile’s efforts: authors use routed Sol/Opus, verifiers use the verifier route, and bounded gathering uses Terra at max effort with priority service. As a multi-day program, include an allowance-checked Astra `hard` assignment, such as contract design review; disclose catalog or allowance constraints rather than inventing availability. No exact effort or allowance is known from this fixture.

4. **Run A as the pilot.** Before its kickoff, complete the contract design note and define completion checks, including malformed-input behavior, diagnostics and caller compatibility. Give A one exclusive branch owner. Its brief specifies dependencies, allowed/forbidden paths, scope, standing orders, checks and expected evidence, and authority to land through ship’s gates. The coordinator reviews artifacts and directs work but never writes code or merges.

5. **Verify, land, then fan out.** Give A a fresh independent read-only verifier, preferably from another provider or model family. Supply the revision range and checks without the author’s conclusions. After A lands, launch fresh owners for B, C and E, reserving the fourth worker slot for verification. D follows B+C; F follows D+E. Each dependent kickoff includes its upstream reports in full and the required built state.

Subscribe to completion, review and check events; do not poll or ask workers for routine status. On pickup, reconcile durable records with live state. Retry by cause; after two retries, drop the failing assignment and replan its required scope without expanding the six-PR program.

**Exact single up-front question batch**

> Two reversible product choices before kickoff:
>
> 1. Should malformed legacy input be rejected or normalized? **Default: reject it with a clear diagnostic**, avoiding silent interpretation.
> 2. Should diagnostics preserve old wording or explain the new contract? **Default: explain the new contract**, updating diagnostic fixtures accordingly.
>
> I’ll proceed with these defaults if unanswered. The old-data purge is outside this program and will not be performed.

**Checkpoint: A passes current-head independent verification and required checks**

Nothing new was discovered; no answer arrived. Both defaults stand. A’s owner checks live mergeability, dependency readiness, holds and verdict/head alignment, then merges A to `main` with a merge commit matched to the verified head and confirms the landed revision. Changed revisions require renewed evidence. B, C and E then proceed. No later question is needed unless a genuinely new decision arises; failed gates, retries and rebases remain owner work.

**If the user adds “don’t merge, I’ll land it”**

Every owner stops at **merge-ready**. A’s pilot ends there; downstream work may prepare against explicit dependency revisions. Report the ready stack and evidence, distinguish it from landed work, and leave all landing to the user.