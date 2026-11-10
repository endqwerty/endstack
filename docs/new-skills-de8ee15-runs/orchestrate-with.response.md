The `orchestrate` invocation authorizes landing these six PRs into `main`. I would coordinate, assign owners, inspect artifacts and enforce gates; owners would write code and land their PRs. This is a planning dry run: nothing is executed.

`orchestrate` shapes ownership and supervision, `swarm` shapes the independent work, and `verify` and `ship` govern delivery.

### First-hour plan

**Minutes 0–15: establish authority and recover state.**

Create durable program notes and a decision trail covering scope, dependencies, completion checks, branch ownership, worker identities, PR links, current heads, verifier verdicts, blockers and standing orders. Completion means all callers converted, all parser fixtures passing and the old API removed on `main`. No deployment or additional PRs enter scope.

Reconcile live branches, PRs, checks and workers before assigning anything. For the worker that stopped at its context limit, inspect its artifacts, establish that it has stopped writing, then transfer exclusive ownership to a fresh worker with a smaller brief and explicit handoff. Record it as replaced. Treat the potentially late result as historical evidence: compare it with the current head and ownership before acting; send unique findings to the current owner without restoring the old worker’s write authority.

Before delegation, consult the live catalog, `homelab route plan`, model profiles and allowances. This multi-day program requires an Astra seat at the active profile’s `hard` effort, subject to allowance; use it for bounded architecture work. Other authors use the routed author model and effort; verification uses the routed verifier. Prefer a different provider or model family for verification when available. Report unavailable routing or allowance evidence rather than inventing it.

**Minutes 15–30: define checks and launch the pilot.**

Record the dependency graph:

- A → B and C
- B + C → D
- E is independent
- D + E → F

Pilot A through owner, independent verifier and landing before fan-out. E waits for that pilot despite being independent. Do not force pilot completion into the first hour.

Before code, delegate the design step and define checks for the shared contract, caller compatibility, adapter integration, diagnostic fixtures and eventual old-API absence.

Give A’s owner a self-contained brief: goal, allowed and forbidden paths, exclusive branch ownership, dependencies, standing orders, design note, required checks and expected evidence, landing authority and scope exclusions.

**Minutes 30–60: validate the workflow and prepare fan-out.**

Subscribe to worker completion, failure, PR changes and checks. Use events, without polling scripts or routine status requests. Inspect A’s diff and evidence. Assign a fresh read-only verifier who reads the entire diff and runs the checks independently.

After A lands and its result is confirmed on `main`, launch fresh owners for B, C and E, including complete relevant upstream reports. Keep at most four workers active, including verifiers; reserve capacity for verification. D starts after B and C land; F starts after D and E land.

Each changed head or base requires applicable checks and a current independent passing verdict. No exemption substitutes for this project’s required review. Owners resolve conflicts, failures and review findings; I coordinate retries and inspect results. After two retries, stop that unit and replan while independent work continues.

Across subsequent days, resume from durable records, reconcile live state, and report each linked PR’s head, verdict and landed or merge-ready state. Unknown evidence remains unknown.

### Exactly what I ask the user

**Nothing initially.** No product choice, credential need or other unresolved decision is known. I would state the defaults: six PRs only, destination `main`, gated owner-led landing, no deployment. Later questions require a genuinely new decision or blocker.

### If the user adds “don’t merge, I’ll land it”

Every owner stops at **verified merge-ready**. No merges or automatic merging. I still own implementation, checks, review fixes and dependency management; descendants are rechecked after user landings. The endpoint becomes six reviewable, verified PRs with explicit dependency and landing instructions—not a completed migration on `main`.