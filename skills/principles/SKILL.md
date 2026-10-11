---
name: principles
description: Apply engineering principles when making design, implementation, debugging or review decisions. Select the relevant principle by its situation and read only its full reference.
disable-model-invocation: true
---

# Principles

Use this index to select the principle that applies to the decision at hand. Open only that principle's reference when it applies; do not preload the collection.

- [Attack the Premise](references/attack-the-premise.md) — when two fixes sharing a premise fail the same gate.
- [Boundary Discipline](references/boundary-discipline.md) — when placing validation, error handling, or framework adapters.
- [Build the Lever](references/build-the-lever.md) — when non-trivial work needs a rerunnable edit or proof.
- [Encode Lessons in Structure](references/encode-lessons-in-structure.md) — when an instruction or correction recurs.
- [Exhaust the Design Space](references/exhaust-the-design-space.md) — when a novel interaction or architecture has no established precedent.
- [Experience First](references/experience-first.md) — when choosing product, user experience, or feature scope tradeoffs.
- [Explain the Number](references/explain-the-number.md) — before trusting, reporting, or acting on a measured number.
- [Fix Root Causes](references/fix-root-causes.md) — when debugging symptoms or failures after restart.
- [Foundational Thinking](references/foundational-thinking.md) — before choosing core data structures or sequencing scaffold and feature work.
- [Guard the Context Window](references/guard-the-context-window.md) — when large payloads, repeated reads, or broad phases fill context.
- [Laziness Protocol](references/laziness-protocol.md) — when refactoring or considering new layers and signal threading.
- [Make Operations Idempotent](references/make-operations-idempotent.md) — when operations must survive crashes, restarts, and retries.
- [Migrate Callers Then Delete Legacy APIs](references/migrate-callers-then-delete-legacy-apis.md) — when replacing an internal API without external compatibility obligations.
- [Minimize Reader Load](references/minimize-reader-load.md) — when code takes too many layers or too much hidden state to trace.
- [Model the Domain](references/model-the-domain.md) — when stateful logic branches or repeats shape assumptions.
- [Never Block on the Human](references/never-block-on-the-human.md) — when tempted to seek permission for reversible work.
- [Outcome-Oriented Execution](references/outcome-oriented-execution.md) — during planned rewrites with explicit verification boundaries.
- [Redesign From First Principles](references/redesign-from-first-principles.md) — when integrating a new requirement into an existing design.
- [Separate Before Serializing Shared State](references/separate-before-serializing-shared-state.md) — when concurrent actors might mutate the same object.
- [Sequence work into verifiable units](references/sequence-verifiable-units.md) — when ordering multi-step work, commits, or pull requests.
- [Subtract Before You Add](references/subtract-before-you-add.md) — when sequencing additions, refactors, or rewrites.
- [Test Behavior, Not Implementation](references/test-behavior-not-implementation.md) — when writing, changing, or keeping a test.
- [Type System Discipline](references/type-system-discipline.md) — when designing types, function signatures, or statically typed code.
