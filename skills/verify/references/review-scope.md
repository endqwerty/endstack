# Decide whether fresh review is needed

Run deterministic checks first. One fresh initial reviewer is the default.
Independent means a separate read-only context that did not write the change
and has not seen the author's conversation or reasoning, on the author's
own provider. Tune that one reviewer rather than adding a second; if the
author's provider cannot review, report the work unverified.

## Exemptions

An exemption skips model review, not checks. Record the current revision,
changed contract, why the risk is low, exact checks and deciding outputs, and
why they cover all affected behavior. Name any assumptions and show they
hold. An explicit request to review still gets a review.

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
cannot run, report unverified and stop delivery.
