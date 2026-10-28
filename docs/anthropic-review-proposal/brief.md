# Dry-run brief

This is the task text used for each arm, with `{arm}` replaced by `a` or `b`.
Provider settings were Claude Opus 5.5, high effort, shared isolation, review
role, wait mode. The delegation mechanism passed no parent conversation.

```text
This is one isolated review experiment, not implementation. No subagents.
Use only /tmp/endstack-review.fiP6up/{arm}/ as the experiment inputs.
Read policy.md as the review policy, references as needed, SPEC.md as the
requirements, base.py and quota.py as before and after, and change.diff as
the full diff. Review quota.py under that policy and run the supplied smoke
command plus any small local checks needed. This synthetic artifact has no
commit history; identify the reviewed files by SHA256. Do not inspect sibling
directories or the repository's review research. Do not change any input
files. Save your findings as they are confirmed and your final verdict to
/tmp/endstack-review.fiP6up/result-{arm}.md. Include commands and decisive
outputs, confirmed findings ranked by the supplied policy, triage of the
three unverified suggestions from SPEC.md, and not-checked limits. State what
should happen next under the supplied policy, including whether edits or
another review are warranted. Do not perform fixes, commits, publishing, or
external messages. Return PASS/ISSUES/BLOCKED and a concise summary.
```

For a new run, replace the temporary paths with isolated copies of the
committed inputs. Do not give the reviewer fixed.py, contract_checks.py,
either result report, or this experiment's interpretation. Snapshot policies
use `references/carry-forward.md` and `references/review-rubric.md`; copy the
recorded files into those relative locations. Only B gets the latter.
