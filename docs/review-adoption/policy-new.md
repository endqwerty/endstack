# FILE skills/verify/SKILL.md
---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

Both roles read the whole diff, delegated work included, and the
[rubric](references/review-rubric.md), never a summary.

## Author

1. Before editing, write checks on the real surface. A bug gets a failing check first.
2. Run the checks first on the real artifact; keep deciding lines.
   Green tests do not prove the contract.
3. Apply [review scope](references/review-scope.md). Unless exempt, ask
   one fresh read-only verifier. Without one, report unverified.
4. Give it the task, checks and revision range, not your conclusions;
   for a re-review, the change since the last verdict, what it affects
   and open findings.
5. Re-rank findings. Fix blockers and shoulds with the cheapest check
   catching them again; rerun affected checks. Decline nits without edits or another round.
   [Carry-forward](references/carry-forward.md) governs fixes.
   Deliver only with every required check and safety fact proven on this
   revision, a fresh pass or valid exemption, no blocker or should open.
6. Open after two rounds: stop and rethink the approach or scope.
   Then at most two more; still open, stop delivery, report both sides.

## Verifier

- Run every check yourself; reproduce a failure, suspecting your
  method first. Answer each pass, issues or not checked, with deciding
  lines; an unrun check is not checked.
- Name the fact its safety rests on; prove it on the real code or mark
  it unproven.
- Try to break it: inputs, failure paths, callers, what the diff
  omits. A base defect is the base's unless the change copies or newly
  reaches it.
- Name what reaches each issue and rank it. Blocker: the intended case
  is wrong. Should: ordinary use, a caller, stored or imported data, a
  race or a setting reaches it. Nit: contrived input giving only a wrong
  result or warning, wording, extra tests or guards, small costs, what
  only later code makes. Data loss, security or a trust boundary is never
  a nit.
- Name the revision and patch judged. Change nothing.


# FILE skills/verify/references/carry-forward.md
# When an earlier verdict still stands

A verdict covers a patch: the change's diff against its base. A rebase gives
the change a new revision without changing that diff, and every request above
it in a stack moves too, so judging verdicts by revision re-verifies code
nobody changed. Judge by patch instead.

At each verdict, record the revision, the base and the patch identity: a
fingerprint of the base-to-head diff that ignores line offsets and commit
metadata, so the same diff on a new base gives the same identity. It must
keep every byte of the changed lines, whitespace included: a fingerprint that
ignores whitespace gives an indentation change, which alters behaviour in
some languages, the same identity. Compare the recorded identity with the
current one before relying on the verdict. The
author does the comparison and records it; a claim that "nothing changed"
without it carries nothing.

## Same patch on a new base

The verdict stands. Rerun the required checks at the new revision and confirm
it can still merge. If the base changed something the patch calls or depends
on (a caller, a function it calls, a shared type, a dependency version), also
run the change's own checks on the combined result: a pass keeps the verdict,
a failure is a finding and needs a fresh verdict. A rebase that needed a
conflict resolution changed the patch; the next sections apply.

## Patch changed only in tests, docs or lint configuration

Two parts, both needed:

- **The earlier results.** Each check the verifier ran against the built
  change still stands if what it ran builds the same at both revisions apart
  from noise. Noise is a difference that also appears between two builds of
  the earlier revision, or an embedded revision id. Report each kind of noise
  with its files, so a reader can check the call. A check with no build
  output, such as a running server or a manual drive, cannot show this:
  rerun it.
- **The new part.** The changed tests, docs or configuration get fresh checks
  and an independent review scoped to them, because the earlier verdict never
  saw them.

An agent's rules or skills, and anything else a tool or agent reads as
instructions, are behaviour here, not docs.

## Prose nothing reads as instructions

An edit only to prose that no tool or agent reads as instructions (not a lint
directive, not an agent's rules or skills) keeps the verdict. Record that
evidence and rerun the required checks.

## Anything else

A fresh verdict on the current revision. It covers what changed since the
last verdict and what that can affect, with the earlier findings. One
verifier is enough after a conflict resolution or a small fix; a full review
again is for new behaviour, a redesign or a large new diff.

Never stand in for the comparison with matching commit messages, a summary
of the change, or a passing check from an older revision.


# FILE skills/principles/references/boundary-discipline.md
# Boundary Discipline

Place validation, type narrowing, and error handling at system boundaries. Pass validated domain values inward and trust the guarantees actually established. Business logic lives in pure functions. The shell is thin and mechanical.

**Why:** Scattered validation is noisy, redundant, and gives a false sense of safety. Keep logic out of framework wiring so it can be tested without the framework.

**The pattern:**
- **At boundaries** (CLI args, config files, external APIs, network protocols): validate, return errors, handle defensively.
- **Inside the system:** typed data, error propagation, no re-validation. Trust the types.
- **Across the boundary.** Expose domain concepts, not the boundary's private representation. Keep general-purpose mechanism inside and special-purpose policy at the edge.

**Applications:**

Validation and error handling:
- Validate config at parse time (the boundary), not inside business logic
- Parse raw data into domain types at the boundary
- Do not re-export transport, storage, framework, or wire types through the public surface
- Validate unknown values once at the boundary that owns them. Pass typed values inward instead of repeating object and property-existence checks.
- Do not defensively revalidate guarantees established by a schema, validating constructor or internal type. A cast or type annotation does not validate external data. Shape validation does not establish authorization or mutable business state.
- A fresh import or external read is a new boundary. Checking a valid union's variant or a changing business condition is ordinary logic, not redundant validation.
- Catch errors where you can recover, translate them into the boundary's error contract, or add necessary context. Otherwise let them propagate. Keep the protected operation narrow, preserve the original cause, and do not turn unexpected failures into successful-looking defaults. Use finally for cleanup even when no catch is needed.

Code organization:
- Business logic in pure functions with no framework dependencies
- Parse functions: pure transforms from raw bytes to typed state
- Prompt construction: structured state in, string out
- Scoring and assessment: pure transforms from state to results

**The tests:**
- What guarantee already holds, and what new unvalidated path reaches this check?
- Can this be pure logic? Keep it free of framework wiring, then apply the [reader-load rule](minimize-reader-load.md) to decide whether extraction helps.


# FILE skills/principles/references/minimize-reader-load.md
# Minimize Reader Load

Maintainability is the work a reader must do to understand code. Track two axes: **layers to trace** (indirections between the question and the answer) and **state to hold** (hidden or mutable context the reader must keep in their head). LOC, cyclomatic complexity, and "clean architecture" are proxies. Reader load is the thing that matters. The two axes are independent. A flat file with 50 globals can be as hard to reason about as a 6-layer adapter stack. Guard both. This is the human analog of [Guard the Context Window](guard-the-context-window.md). Working memory is finite for readers too.

- **Collapse layers** that cost more than they save. Do not extract single-use helpers preemptively. Inline the logic unless the helper is reused, hides a complex boundary, or has a clear independent name that improves the caller. One caller alone is not a reason to remove a useful helper. Judge the reading saved against the jump to another function.
- **Make adjacent layers change the abstraction.** A layer that repeats the same methods and arguments adds reader load without compression. Collapse pass-through layers.
- **Demand interface compression.** A broad interface that hides little complexity makes readers learn both the surface and the implementation. Prefer boundaries that hide meaningful decisions.
- **Shrink state scope:** prefer pure functions (returns over mutations), locals over fields, fields over module state, and module state over globals. Derive instead of sync.
- **Name the invariant at the boundary,** not in every consumer, so the reader learns it once.
- Before adding a layer or a piece of state, ask: does it reduce reader load elsewhere by at least as much?

**The test:** can a new reader answer "where does X come from?" and "what can change X?" in under 30 seconds? If not, cut layers or cut state.


# FILE skills/principles/references/type-system-discipline.md
# Type System Discipline

Make the compiler reject impossible states, mismatched primitives, and unhandled variants. Prefer defining errors and special cases out of existence over proliferating handlers. For TypeScript syntax, see the `typescript-best-practices` skill.

- **Make illegal states unrepresentable.** Model variants as sum types (discriminated unions, enums with payloads, sealed classes), not as a bag of optional fields where contradictory combinations compile. `{ completed: boolean; completedAt?: Date }` admits `completed: true` with no date. Derive the boolean from `completedAt`, or model `{ kind: 'open' } | { kind: 'done'; at: Date }`. If you can write a comment explaining when a combination of fields is valid, split it into a sum type.
- **Types are constructions, not restrictions.** Build the type up from the values you want instead of carving them out of a looser type with checks. A non-empty list is a head plus a rest. A valid time range is a start plus a duration. Choose the shape that cannot build the illegal value and expose the interface callers need on top.
- **Brand semantic primitives.** `UserId` and `OrderId` are strings underneath but should not be interchangeable. Give each its own type, such as a branded intersection in TypeScript or a newtype elsewhere. Validate once at creation, trust the type downstream. If two arguments share a primitive type but mean different things, brand them.
- **External data is untyped until parsed.** RPC payloads, JSON, IPC messages, CLI args, config files, environment variables, database rows. Have a parse function at every boundary that turns unstructured input into the typed model. The **boundary-discipline** principle skill says where to put validation.
- **Don't lie to the type system.** Casts, unsafe coercions, and assertion functions that bypass the compiler are latent runtime crashes. If the compiler can't prove a fact, prove it (validate, narrow, refine the model) or accept that the cast is a hazard. Trace each `any`, `as`, or `assertNotNull` to the boundary and validate there.
- **Exhaustive matching is the compiler's job.** A match on a sum type must fail compilation when a new variant is added without handling, so the compiler tells the next agent where to add a case. Use your language's idiom: a `never`-typed binding in TypeScript, an unannotated `match` in Rust, `-Wincomplete-patterns` in Haskell, sealed-class match exhaustiveness in Kotlin.
- **Derive types from authoritative schemas.** When a protocol buffer, OpenAPI spec, GraphQL schema, database migration, design-token file, or another file owns a shape, derive from it instead of hand-rolling a parallel type. See [Encode Lessons in Structure](encode-lessons-in-structure.md).
- **Strengthen a type only where partiality appears.** A runtime assertion, null check, or "this should never happen" throw marks the place a type is too weak. Push that check up into the type. Then stop. The type system's job is to track the cases each use site must handle, not to describe the data as precisely as possible. Prefer total functions. `sum` of an empty list is 0, so it takes the plain list. `head` of an empty list has no answer, so it demands the non-empty one. If nothing would otherwise panic, keep the plain type.


# FILE skills/verify/references/review-scope.md
# Decide whether fresh review is needed

Run deterministic checks first. One fresh initial reviewer is the default.
Independent means a separate read-only context that did not write the change
and has not seen the author's conversation or reasoning. The same provider
or model family qualifies. A different family is optional when a specific
risk or uncertainty makes another perspective useful; it is not a gate.
The author reviewing their own work never substitutes for fresh review.

## Exemptions

An exemption skips model review, never required checks or host protections.
Record the current revision, changed contract, why the risk is low, exact
checks and deciding outputs, and why they cover all affected behavior. Name
any assumptions and show they hold. A project may require stricter review.
An explicit request to review still gets a review.

Exempt changes may include ordinary prose or comments with no instruction or
contract effect, verified mechanical edits, and small bounded behavior changes
whose full affected contract is established by deterministic evidence, such
as an exhaustive finite input check. Size, a green test suite, a snapshot,
static types or the author's confidence alone do not justify an exemption.
An exemption has no unresolved safety fact or missing required evidence.

Do not exempt changes to agent instructions, security or authorization,
money, persistent data or migrations, production deployment, concurrency,
or external contracts. Use a fresh reviewer whenever coverage, reachability
or the risk classification needs unresolved judgment. If required review
cannot run, report unverified and stop delivery. Do not lower the risk merely
to bypass an unavailable reviewer.

A new behavior change needs a new exemption decision or a fresh verdict.
A verdict already obtained follows the existing carry-forward rules.


# FILE skills/verify/references/review-rubric.md
# Review the contract, filter the findings

Give the reviewer the requirements, relevant project rules, full diff, base
and head, check commands and results. Let it inspect surrounding code,
callers, stored data and imports. Exclude the author's conversation,
reasoning and desired verdict. Fresh context does not mean diff-only access.

Run required deterministic checks before review. Fix their failures first;
if one cannot run, record that gap. A requested review can investigate the
gap, but cannot turn it into a pass. The verifier still runs every required
check when review is required. Report commands, decisive output and revision;
omit routine passing logs, while retaining full logs when needed to diagnose.

Check the requirements and relevant regression, security, data and failure
paths, including omissions in the diff. Do not limit safety review to a
flawed or incomplete spec. For each candidate finding, trace a current path
to an observable failure and check the claim against the code before
reporting it. Supply the location, trigger, expected and actual behavior,
and a reproducer or a concrete code trace. A code trace supports a finding;
it does not replace an unrun required check.

Skip style, naming, optional refactors, redundant tests and guards for
hypothetical future code. A required compatibility or safety property is
not style. Factual errors in evidence or requirements are correctness
defects, not wording nits. Report blockers and shoulds with evidence, not
a minimum count.
Put a missing check or unresolved safety fact under not checked, not among
confirmed defects. Do not label an evidenced security or data-loss path a
nit because it is unusual. No findings is a valid result, but not checked
still prevents a passing verdict when evidence is required.

One first pass is the default, not a one-pass approval guarantee. Re-review
only for fixes or new evidence that the carry-forward rules require, scoped
to the changed behavior and its dependents. An unresolved required fact
needs evidence, not another unfocused search. Preserve stricter project
review requirements and the existing round cap. Do not add a reviewer just
to seek more findings or reconsider a declined style suggestion.

For validation, helpers and catches, apply the
[boundary](../../principles/references/boundary-discipline.md) and
[reader-load](../../principles/references/minimize-reader-load.md) rules.
Name the existing guarantee before removing validation, the reachable
unvalidated path before adding it, and the concrete readability or recovery
benefit before requesting a helper or catch.
