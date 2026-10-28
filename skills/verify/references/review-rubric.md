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
