---
name: interrogate
description: Challenge a change or design adversarially with several independent reviewers.
disable-model-invocation: true
---

# Interrogate

Convene a panel of separate reviewers to adversarially review code changes. The adversarial signal comes from model diversity, not assigned personas. The deliverable is a synthesized verdict. Do NOT auto-apply changes.

## Step 1, Scope

Identify what to review from context:

- If the user points at specific files or a diff, use that.
- If on a feature branch, gather the full changeset against the appropriate base branch.
- If the user's message references recent work, gather the relevant files.

Package the diff or file contents with any surrounding context files the reviewers need to understand the code.

## Step 2, Intent

Before convening reviewers, state the intent in one clear paragraph from the user's message, commit messages, the PR description if one exists, and the code. If you're unsure about the intent, ask the user before proceeding.

## Step 3, Convene the panel

Give the same brief to separate read-only reviewers in parallel, if the harness supports it, labeled Reviewer A, B and so on. Use different model families if available: diversity, not assigned personas, provides the adversarial signal. Prefer at least two reviewers. If the harness lacks separate workers, apply the review yourself in sequence and report that this is not an independent panel. If diverse families are unavailable, disclose the limit.

Read the [reviewer prompt](references/reviewer-prompt.md), [rubric](references/rubric.md), and [code-quality lens](references/code-quality-review.md) on demand. Fill the same template for every reviewer with the intent, code and both lenses.

## Step 4, Synthesize

As results come back, build a unified picture. Parse every reviewer's findings. Merge findings that describe the same issue differently, and note which models raised each one. Findings two or more models raised independently are the highest signal. Read a lone model's finding, but weight it accordingly. Note disagreements. If one model flags something and another explicitly says the opposite, that is context for the verdict.

## Step 5, Lead Judgment

You are the lead reviewer, a pragmatic senior engineer, not a neutral aggregator. Read the [lead-judgment framework](references/lead-judgment.md) for the full framework. Put every finding in one of four buckets, with the model(s) that raised it and a one-line rationale.

- **Act on**. Real issues affecting correctness, security, or maintainability given the actual goals. They would block a real PR.
- **Consider**. Legitimate, but you're not sure they outweigh the cost of addressing them now. Worth the user's attention.
- **Noted**. Technically valid but not actionable. Context-dependent, premature optimization, or low-impact at this stage.
- **Dismissed**. Wrong, nitpicky, or missing context, with a brief reason.

A finding goes in Act on or Consider only when it shows what reaches it: a reproducer, or a trace that names each step from a caller, input or setting to the failure, through the real code or, for a design, through the sketch and the code it would run on. Agreement among reviewers draws attention but is not that evidence. Without it the finding is Noted, however serious it sounds, and one the code rules out is Dismissed. One on data loss, security or a trust boundary that can be neither shown nor ruled out goes in Consider, marked unproven, with the check that would settle it.

## Output Format

### Intent
> [The stated intent paragraph from Step 2]

### Reviewers
- Reviewer [label]: [reviewer identity and independence limits], [N findings] (one bullet per reviewer)

### Act On
[Each: description, which reviewers raised it, why it matters.]

### Consider
[Each: description, which reviewers raised it, the tradeoff.]

### Noted
[Brief list.]

### Dismissed
[Each with a brief rationale.]

### Agreement Map
[Where reviewers agreed and diverged, and what that pattern tells us.]

For the single independent delivery check, use [verify](../verify/SKILL.md). This panel reports a verdict and does not auto-apply changes.
