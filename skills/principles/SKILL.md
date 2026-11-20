---
name: principles
description: Engineering principles for design, implementation, debugging and review decisions.
disable-model-invocation: true
---

# Principles

Read this whole index before a design, implementation, debugging or review decision. When an entry applies, read its reference before the step it governs; do not preload the references.

**Core**

- [Laziness Protocol](references/laziness-protocol.md) — when refactoring or considering new layers and signal threading: bias to deletion and the smallest change that solves the problem.
- [Foundational Thinking](references/foundational-thinking.md) — before choosing core data structures or sequencing scaffold and feature work: settle types and shared state before logic.
- [Redesign From First Principles](references/redesign-from-first-principles.md) — when integrating a new requirement into an existing design.
- [Attack the Premise](references/attack-the-premise.md) — when two fixes sharing a premise fail the same gate: test the premise before another fix.
- [Subtract Before You Add](references/subtract-before-you-add.md) — when sequencing additions, refactors, or rewrites.
- [Minimize Reader Load](references/minimize-reader-load.md) — when code takes too many layers or too much hidden state to trace.
- [Experience First](references/experience-first.md) — when choosing product, user experience, or feature scope tradeoffs.
- [Exhaust the Design Space](references/exhaust-the-design-space.md) — when a novel interaction or architecture has no established precedent.
- [Build the Lever](references/build-the-lever.md) — when the work is more than a couple of obvious edits: build the tool that does or proves it; the bar is triviality, not repetition.

**Architecture**

- [Model the Domain](references/model-the-domain.md) — when stateful logic branches or repeats shape assumptions.
- [Boundary Discipline](references/boundary-discipline.md) — when placing validation, error handling, or framework adapters.
- [Type System Discipline](references/type-system-discipline.md) — when designing types, function signatures, or statically typed code.
- [Make Operations Idempotent](references/make-operations-idempotent.md) — when operations must survive crashes, restarts, and retries.
- [Migrate Callers Then Delete Legacy APIs](references/migrate-callers-then-delete-legacy-apis.md) — when replacing an internal API without external compatibility obligations.
- [Separate Before Serializing Shared State](references/separate-before-serializing-shared-state.md) — when concurrent actors might mutate the same object.

**Verification**

- [Fix Root Causes](references/fix-root-causes.md) — when debugging symptoms.
- [Sequence work into verifiable units](references/sequence-verifiable-units.md) — when ordering multi-step work, commits, or pull requests.
- [Test Behavior, Not Implementation](references/test-behavior-not-implementation.md) — when writing, changing, or keeping a test.
- [Explain the Number](references/explain-the-number.md) — before measuring, trusting, reporting, or acting on a number: find what limits it and rule out that it measured something else.

**Delegation**

- [Guard the Context Window](references/guard-the-context-window.md) — when large payloads, repeated reads, or broad phases fill context: route bulk output to files or helpers.
