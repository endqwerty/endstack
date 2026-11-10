---
name: arena
description: Compare several attempts at one artifact, pick a base and graft in the best parts of the rest.
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

If a runner cannot start, use an available replacement only when the task and harness permit it; otherwise drop the seat and say why. Keep at least two independent candidates for a comparison unless the user specified one. If that is impossible, report the comparison incomplete. If a started candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all candidates complete, give a read-only judge the rubric and candidates by path label. Use fresh context independent of the candidate authors. A different model family is optional. Use a separate worker if the harness has one, otherwise apply the judge lens yourself in sequence and disclose this. The judge scores each criterion and recommends a base with rationale. It may run alongside your reading in Phase D, never while candidates are writing.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, favoring the design that is easiest to extend.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, by redesigning from first principles, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, do not ship it yet: shared training can make agreement a shared blind spot. Run one dissenter per comparison, briefed with the consensus and asked for the strongest opposite or a far different shape, and score it on every criterion of the same rubric, as in Phase D. Make the dissent the base only when that full comparison favours it; otherwise keep the consensus and graft what the dissent found, or report the trade-off it exposed. Reframe only when the dissent shows the rubric itself missed a requirement, at most once, then deliver with the open question named. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, using [verify](../verify/SKILL.md) for the independent check. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence, the dissenter and what it changed, any dropouts, and the verification result.
