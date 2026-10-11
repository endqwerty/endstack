---
name: arena
description: "Compare N candidates for the same task, pick a base, and graft the strongest parts of the others into it. Run candidates in parallel when separate workers are available. Use for 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

Track progress with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Choose runners suited to the task, with different model families for judgment-sensitive work if available. Use more runners for multiple design directions; the same family can fill several seats for generation-bound work.
4. Give each candidate its own isolated output location, preferably a separate checkout. Separate writable state before coordinating it.

## Phase B: Fan out

If the harness has separate workers, launch all N in parallel, each with the same task, shared grounding, its own output path, and instructions to produce the artifact and a short rationale naming alternatives considered and rejected. Otherwise produce candidates yourself in sequence and disclose that they are not independent attempts.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all candidates complete, give a read-only judge the rubric and candidates by path label. Prefer a different model family than yours, if available; otherwise say the judge is not independent. Use a separate worker if the harness has one, otherwise apply the judge lens yourself in sequence and disclose this. The judge scores each criterion and recommends a base with rationale. It may run alongside your reading in Phase D, never while candidates are writing.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, favoring the design that is easiest to extend.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, by redesigning from first principles, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, using [verify](../verify/SKILL.md) for the independent check. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
