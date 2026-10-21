---
name: principles
description: Engineering principles for design, implementation, debugging and review decisions.
disable-model-invocation: true
---

# Principles

Read this whole index before a design, implementation, debugging or review decision: each entry says when the principle applies and states its rule. When one applies, read its reference before the step it governs; do not preload the references.

In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose reference you read this session.

**Core**

- [Laziness Protocol](references/laziness-protocol.md) — when refactoring or considering new layers and signal threading. Bias to deletion and the smallest change that solves the problem.
- [Foundational Thinking](references/foundational-thinking.md) — before choosing core data structures or sequencing scaffold and feature work. Settle core types, data structures and what concurrent actors share before writing logic; scaffold before features.
- [Redesign From First Principles](references/redesign-from-first-principles.md) — when integrating a new requirement into an existing design. Redesign as if the requirement had been there from day one; do not bolt it on.
- [Attack the Premise](references/attack-the-premise.md) — when two fixes sharing a premise fail the same gate. Write the premise down and test it directly before writing another fix that assumes it.
- [Subtract Before You Add](references/subtract-before-you-add.md) — when sequencing additions, refactors, or rewrites. Remove dead weight first, then build on the simpler base.
- [Minimize Reader Load](references/minimize-reader-load.md) — when code takes too many layers or too much hidden state to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- [Outcome-Oriented Execution](references/outcome-oriented-execution.md) — during planned rewrites with explicit verification boundaries. Converge on the target architecture; do not preserve throwaway compatibility states.
- [Experience First](references/experience-first.md) — when choosing product, user experience, or feature scope tradeoffs. Choose the user's experience over implementation convenience.
- [Exhaust the Design Space](references/exhaust-the-design-space.md) — when a novel interaction or architecture has no established precedent. Build two or three competing sketches and compare them before committing.
- [Build the Lever](references/build-the-lever.md) — when non-trivial work needs a rerunnable edit or proof. Build the tool that does or proves the work (codemod, script, generator); the tool is what a reviewer reruns.

**Architecture**

- [Model the Domain](references/model-the-domain.md) — when stateful logic branches or repeats shape assumptions. Name the data shape first and encode it in a structure (state type, tagged union, table or registry, reducer) instead of scattered conditionals and flags.
- [Boundary Discipline](references/boundary-discipline.md) — when placing validation, error handling, or framework adapters. Guard and parse at system boundaries, trust internal types, keep business logic pure.
- [Type System Discipline](references/type-system-discipline.md) — when designing types, function signatures, or statically typed code. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.
- [Make Operations Idempotent](references/make-operations-idempotent.md) — when operations must survive crashes, restarts, and retries. Derive each step from the state that exists and apply only the difference, so a repeat or a resumed run converges.
- [Migrate Callers Then Delete Legacy APIs](references/migrate-callers-then-delete-legacy-apis.md) — when replacing an internal API without external compatibility obligations. Migrate every caller and delete the old API in one wave.
- [Separate Before Serializing Shared State](references/separate-before-serializing-shared-state.md) — when concurrent actors might mutate the same object. Eliminate the sharing first; serialize only for a real invariant.

**Verification**

- [Fix Root Causes](references/fix-root-causes.md) — when debugging symptoms or failures after restart. Reproduce, then trace back to the first place the system went wrong; fix it there and in every place with the same fault. A guard is a fix only when the state it handles is legitimate.
- [Sequence work into verifiable units](references/sequence-verifiable-units.md) — when ordering multi-step work, commits, or pull requests. Break work into small units that each end in a check, and verify each before starting the next.
- [Test Behavior, Not Implementation](references/test-behavior-not-implementation.md) — when writing, changing, or keeping a test. Assert what the code's users can observe, so the test fails when that behavior breaks and keeps passing when only the internals change.
- [Explain the Number](references/explain-the-number.md) — before trusting, reporting, or acting on a measured number. Find what limits it and rule out that it measured something other than the work.
- Prove It Works is the [verify](../verify/SKILL.md) skill.

**Delegation**

- [Guard the Context Window](references/guard-the-context-window.md) — when large payloads, repeated reads, or broad phases fill context. Route bulk output to files or helpers; keep summaries in the main thread.
- [Never Block on the Human](references/never-block-on-the-human.md) — when tempted to seek permission for reversible work. Proceed, present the result, let the human correct course.

**Meta**

- [Encode Lessons in Structure](references/encode-lessons-in-structure.md) — when an instruction or correction recurs. Encode it as a lint, type, runtime check or script instead of more text.
