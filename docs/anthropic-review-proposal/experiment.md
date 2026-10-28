# Review-rubric experiment

Run on 2026-10-27 against endstack baseline
`6136a6b5cf83cf4361ddda03c8b445375d22aa5a`. The proposal is not installed.

## Method

The [acceptance checks](acceptance.md) were written before drafting the
proposal. One independent Claude Opus 5.5 reviewer at high effort per arm,
launched concurrently in fresh contexts with no parent history. Both got
identical files from [fixture/](fixture/), except `fixed.py`, which was created
after the reviews. They received the [current policy](current-policy.md) or
[proposed policy](proposed-policy.md), the same
[carry-forward reference](references/carry-forward.md), and, for B only, the
[proposed rubric](references/review-rubric.md). Their source folders were separate.
They shared a machine and the enclosing repository's inherited instructions.
No performance measurement was made.

The task was to review the supplied before/after files against SPEC.md, run
the smoke checks and useful local probes, triage its three suggestions, and
state what edits and further review the policy required. It forbade reading
the sibling arm, research or answer key, modifying inputs, or spawning agents.
The reports record input SHA256s. They agree with the committed fixture.
The literal task template is in [brief.md](brief.md).

The parent chose the fixture and wrote the policy, so this is a small authored
test, not a blind sample of production changes. One defect was suggested in
SPEC.md; the exact-limit regression was not. The parent withheld
[contract_checks.py](contract_checks.py) and independently ran its two
assertions before collecting the reports. Both failed as expected, while
the four smoke checks passed. Afterward, a fixed example passed both assertions.
See [contract-results.txt](contract-results.txt).

## Observed results

| Check | A: current policy | B: proposal |
| --- | --- | --- |
| Inclusive limit regression | Reproduced, blocker | Reproduced, blocker |
| Over-limit imported value accepted | Reproduced, should | Reproduced, blocker |
| Rename a public parameter | Declined, no edit or new round | Declined, no edit or new round |
| Guard for a nonexistent future parser | Declined, no edit or new round | Declined, no edit or new round |
| Next action | Fix both defects, add cheap regressions, scoped independent recheck | Same |
| Unavailable callers or upstream schema | Listed as not checked | Listed as not checked |

Raw reports: [A](result-a.md), [B](result-b.md). Both runs required fixes for
the same two defects. The different rank on the import defect changes no
delivery decision, because both blocker and should require a fix. Both also
noticed that a parameter rename could break keyword callers, so the naming
suggestion is not a pure style-only control. That limits what this experiment
shows about style suppression.

There is no demonstrated improvement in these outcomes and no cost saving
measured. The candidate makes the expected behavior explicit but the current
text already produced it. Both reviewers had fresh context, so this does not
measure the effect of context isolation itself or compare provider families.

## Reproduce the deterministic checks

From the repository root:

```sh
python3 -B docs/anthropic-review-proposal/fixture/smoke.py
python3 -B docs/anthropic-review-proposal/contract_checks.py docs/anthropic-review-proposal/fixture/quota.py
python3 -B docs/anthropic-review-proposal/contract_checks.py docs/anthropic-review-proposal/fixture/fixed.py
python3 scripts/check-skills.py
python3 scripts/check-routing.py
git apply --check docs/anthropic-review-proposal/verify.patch
```

Expected: smoke passes, the buggy fixture exits 1 with two assertion
failures, the fixed fixture passes both, each checker prints `0 problem(s)`,
and patch validation exits 0. The intentionally failing fixture is evidence,
not a required production check.

Before independent review, the parent applied the tested draft patch to a
temporary copy of all skills and
routing, ran both checkers there (`0 problem(s)` each), and compared the
result byte-for-byte with proposed-policy.md and the tested rubric. The proposed core is 2,162
bytes, under the 2,200-byte checker limit. Active skill files were unchanged.

## Not exercised

- A fully clean candidate review, or a style-only diff with no compatibility
  consequence. The policy permits no findings, but that outcome was not tested.
- Live deployment, concurrency, security, data loss, or an incomplete spec.
- A fix followed by an actual second model review or the round cap.
- Reviewer recall, incident rates, token use, or elapsed-time savings.
- Enforcement of a Stop hook, imported upstream schema validation, or a
  reviewer accepting deterministic evidence without rerunning it.

The parent read the complete reports and reran the decisive contract checks.
B reported that it wrote its report at the end rather than incrementally;
both runs nevertheless completed and left their evidence. This does not
test interrupted-run recovery.

## Independent review correction

[Round 1](review-round-1.md), Claude Opus 5.5 at high effort, passed the source
audit and mechanical evidence but found one should in the proposal: the
blanket ban on nit fixes could suppress factual corrections to evidence.
The final patch adds one exception in [final-rubric.md](final-rubric.md):
factual errors in evidence or requirements are correctness defects, not
wording nits. The paired runs above used the earlier rubric, retained in
references/review-rubric.md. They are not claimed as a run of the final text.

Two nits were considered without more policy edits. The core's "full diff"
still includes delegated changes; the reviewer agreed the duty is preserved.
The proposed one-first-pass default is a recommendation pending Daniel's
choice, now stated explicitly in the report. It is not installed policy.
