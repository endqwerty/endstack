I would own coordination of A–F through delivery, with **merging awaiting explicit authority**. “Orchestrate” and “own the program” authorize the work; they do not invoke `ship` or `autopilot-full`. This is a plan only; nothing is executed.

The work splits into independent parts, so I would use `swarm`. `build` shapes implementation, `verify` supplies the delivery gate, and `show-me-your-work` shapes durable coordination. `ship` applies only if landing is authorized.

**First hour**

**Minutes 0–15: establish scope and durable state.**

Record the six-PR queue, destination `main`, branch ownership, dependency graph, completion checks, authority boundary, and any existing work:

- A defines the contract; B and C follow A.
- D follows both B and C.
- E adds independent diagnostic fixtures.
- F follows both D and E.

Before edits or implementation briefs, complete a shared design note covering the contract, adapter responsibilities, migration compatibility, and removal criteria. Define checks proving all callers converted, all parser fixtures passing, and the old API removed. Record each PR’s current head, base, checks, review findings, and next action.

**Minutes 15–30: route and assign bounded work.**

Plan to consult `homelab route plan`, the live catalog, allowance readings, and `homelab route models` before delegation; fixture text supplies no live results or exact profile efforts.

Use the routed provider and class effort: Codex authors/verifiers/reviewers use Sol; gathering workers use Terra at max effort, priority. Include Astra as a `hard` participant for this large program at the active profile’s effort, after checking allowance. If unavailable, record the constraint and permitted fallback explicitly.

Keep at most four workers active. Initially assign separate owners to A and E, with Astra checking the cross-PR design and another worker gathering caller coverage. Each brief names boundaries, checks, artifacts, and completion criteria. One owner writes each branch. A fresh read-only verifier later gets a separate context and no author conclusions.

**Minutes 30–60: start the dependency frontier and establish recovery.**

Start A and E after the design step. Prepare B/C checks and ownership while A progresses; start their implementation when its contract prerequisite is ready. D waits for B/C; F waits for D/E. Keep eligible independent work moving through blockers.

Subscribe to PR updates, check completions, review results, worker completion/failure, and dependency landings. Persist subscription identifiers and recovery instructions. Add periodic reconciliation so a silent context-limit exit cannot strand the program. Track progress through commits and check evidence, not heartbeat claims.

Give every assignment a generation identifier and expected head. Before replacing a silent worker, confirm it has stopped writing, preserve its artifacts, and revoke its assignment. Treat late results as evidence only until their generation, branch, base, and head match current state.

**Delivery across the following days**

Require passing checks and an independent read-only verifier’s passing verdict on each current head. Recheck changed revisions and bases. If merging is authorized, land one eligible PR at a time with merge commits and head matching; confirm it reached `main` before reassessing dependents. Never arm descendants behind unlanded prerequisites. No deployment.

Exactly what I would ask:

> Do you authorize me to merge A–F into `main` as each dependency and verification gate passes, or should I stop with all six ready for you to land? Coordination and implementation can proceed while you decide; your wording has not yet authorized merging.

If you add **“don’t merge, I’ll land it,”** no authority question remains. The endpoint becomes six checked, independently verified PRs ready in dependency order, with branches preserved and landing instructions recorded. Final integration checks follow your landings; readiness is not completion of the migration on `main`.