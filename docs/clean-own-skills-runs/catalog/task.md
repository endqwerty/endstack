# Dry run: routing for a review request

Each arm got one ROUTING.md text (old: `05cad93:ROUTING.md`, new: this branch) and
the same scenario, with no other context, and was asked which skills it would
load and why, without doing the review.

Scenario: "Review the diff on branch fix/retry-backoff against main before I
merge it. It changes src/queue/retry.ts (exponential backoff with jitter,
about 60 lines) and adds a test in test/retry.test.ts. Tell me if anything is
wrong."

## Result

Old: opens `swarm` as a mandatory first decision (then declines to fan out),
`verify`, `unslop`; rejects `how`/`why`/`teach` on its own judgment.
New: opens `verify`, `unslop` only; `swarm` is not a step. Neither arm loaded
the explanation skills in this one-shot run, so the audit's measured
review-thread loads of how/why/teach were not reproduced here; the new text
removes the trigger ("Explaining code ... are tasks") that the audit blames.
Outputs: out-old.md, out-new.md.
