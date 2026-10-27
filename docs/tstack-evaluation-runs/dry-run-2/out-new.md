Read: ROUTING.md, autopilot-full, ship, build, babysit, verify, verify/references/carry-forward.md.
First step in every case: decide whether the task splits into parallel parts (ROUTING "Every task, first"). Each case here is one small change, so I do not use swarm.

Case 1: "autopilot: add a retry for failed uploads" (no PR yet)
- Skills: autopilot-full, which composes build, babysit, ship and verify. It also needs show-me-your-work for its decision log, and build's design.md step before any code.
- Rule: ROUTING says `"Autopilot" or "full send" on a change is that request: autopilot it, without waiting for approval.` autopilot-full says `authorizes both the work and its landing, and nothing then waits for the user's approval`.
- Path: build the change and open the PR. Babysit it until it is ready. Get verify's independent pass on the current head. Then ship merges it and confirms it landed in the destination.
- Stop: `Stop at queue completion, an authority boundary, or an explicit stop.` The queue is one item, so I stop once it has landed.
- Merge: yes, but only after `verify`'s `independent passing verdict on the current revision`. If no other-provider verifier can run, the result is unverified and ship does not land it.
- Waits for the user: nothing.

Case 2: "full send on #412" (green checks, verifier passed the current head, one bot finding unanswered)
- Skills: ship, with autopilot-full as the umbrella. ship step 1 says `"autopilot" or "full send" on it, counts` as merge authority. Babysit's finding rule and verify's carry-forward apply to the open finding.
- The bot finding blocks the merge until it is handled. ship step 2: `Every finding on it, a bot's included, has a fix or a written reason.` babysit adds: `Treat it as a claim and check it against the code.` A real bug gets the smallest fix. A nit is declined in writing and listed as a follow-up.
- A fix changes the patch. ship step 3 says `Changed revisions or bases require fresh checks and a current independent verdict`, and carry-forward's "Anything else" says `A fresh verdict on the current revision`. One verifier is enough for a small fix. A written reason for a nit changes no code, so the verdict stands.
- Merge: yes, once the finding is answered, checks are green, the verdict is current and the host reports it mergeable. Without those I stop at the first gap (ship step 4: `Stop at the first gap.`). Only #412 is in scope.
- Stop: after ship confirms the merge landed and reports it. Waits for the user: nothing. autopilot-full: `nothing then waits for the user's approval`.

Case 3: "full stop: add a retry for failed uploads" (no PR yet)
- Skills: build, then babysit, with verify at each step. I read design.md before the first production edit.
- Rule: ROUTING says `"Full stop" means build it and babysit it to ready, unmerged.` I do not treat it as ship's "explicit stop", which means no writes, because ROUTING defines it as build plus babysit.
- Path: build opens a non-draft PR. Babysit then answers every finding and fixes failing checks until ready. Ready means `a current independent verdict or valid exemption, passing required checks, no unresolved blocker, no conflict`, with the host reporting it mergeable.
- Stop: at a ready, unmerged PR, which I report. babysit: `Never merge, arm automatic merging, close requests or write to the delivery branch.`
- Merge: no. autopilot-full and ship are not used, because nothing grants landing. build: `Do not merge, arm automatic merging`.
- Waits for the user: the merge decision. babysit: `the user owns the merge decision` and `Owner approval is a wait, not a problem to bypass.` Nothing else waits, and I do not ask questions mid-way.
