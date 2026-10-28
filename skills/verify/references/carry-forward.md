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

Apply [review scope](review-scope.md) to the current revision. A documented
low-risk exemption may replace a new model verdict only when its full affected
contract and earlier findings are resolved by current deterministic evidence.
Otherwise get a fresh verdict covering what changed since the last verdict
and what that can affect, with the earlier findings. One
verifier is enough after a conflict resolution or a small fix; a full review
again is for new behaviour, a redesign or a large new diff.

Never stand in for the comparison with matching commit messages, a summary
of the change, or a passing check from an older revision.
