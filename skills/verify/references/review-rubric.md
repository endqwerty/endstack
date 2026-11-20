# Review the contract, filter the findings

Give the reviewer the requirements, relevant project rules, full diff, base
and head, check commands and results. Let it inspect surrounding code,
callers, stored data and imports. Exclude the author's conversation,
reasoning and desired verdict.
When the change has a design doc, its *Behaviour* scenarios are requirements:
each one the change adds or edits has its named check run on this revision,
and behaviour the diff changes has its scenarios updated in the same diff.

Fix failures of required deterministic checks before review; if one cannot
run, record that gap. A requested review can investigate the gap, but cannot
turn it into a pass. The verifier still runs every required check when review
is required.

Do not limit safety review to a flawed or incomplete spec. For each candidate
finding, trace a current path to an observable failure and check the claim
against the code before reporting it. Supply the location, trigger, expected
and actual behavior, and a reproducer or a concrete code trace. A code trace
supports a finding; it does not replace an unrun required check.

That evidence is what "show what reaches it" means: a check that fails on
this revision, or a trace that names each step through the real code from a
caller, input or setting to the failure. A finding with neither is a nit; one
the code rules out is no finding. One on data loss, security or a trust
boundary that can be neither shown nor ruled out goes under not checked
instead, with the check that would settle it.

Skip style, naming and optional refactors. A required compatibility or safety
property is not style; factual errors in evidence or requirements are
defects. Put a missing check or unresolved safety fact under not checked, not
among confirmed defects; not checked prevents a passing verdict when evidence
is required.

Re-review only as [carry-forward](carry-forward.md) requires, scoped to the
changed behavior and its dependents; do not add a reviewer to seek more
findings.

For validation, helpers and catches, apply the
[boundary](../../principles/references/boundary-discipline.md) and
[reader-load](../../principles/references/minimize-reader-load.md) rules:
name the existing guarantee before removing validation, the reachable
unvalidated path before adding it, and the concrete benefit before requesting
a helper or catch.
