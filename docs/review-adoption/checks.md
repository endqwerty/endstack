# Adoption checks and design

Recorded before editing active skills. Scope is the accepted review defaults,
provider-optional fresh review, justified exemptions, and the four coding
rules as refined in the conversation. Land the existing endstack PR, then
update homelab's shared gate and pin and sync both machines.

Design: keep review policy in verify and its references; keep coding judgment
in Boundary Discipline and Minimize Reader Load. All delivery skills already
consume verify. Remove contradictory unconditional trust/extraction wording.
No new skill, parser or hook. Subtract Before You Add keeps this within the
existing skills; Boundary Discipline owns validation and error handling;
Minimize Reader Load permits useful single-use helpers. One author keeps the
shared policy coherent. No unrelated project policies change.

Completion checks:
- Both skill/routing checkers and their unit tests pass.
- Fresh paired dry runs using old and new text, same scenarios, report actual
  differences and limits, not estimated savings.
- Scenarios distinguish valid schema-backed values from raw casts, fresh
  imports, authorization and stale state; useful single-use helpers from
  speculative extraction; recovery/translation/finally from swallowed errors.
- Exemptions require current deterministic evidence for the full changed
  contract, low risk, no unresolved facts and no stricter project requirement.
  Agent rules, security, auth, money, persistent-data, deployment, concurrency
  and external-contract changes still require review. Small size is no proof.
- A same-provider fresh reviewer qualifies; the author session does not.
- Missing required checks block delivery, including exempt changes.
- Independent verification covers the active policy and homelab gate before
  landing. After landing, sync uses the exact merged source revision.
- Confirm host mergeability, rebase merge, verify main, sync/check locally and
  on omarchy. Record any unavailable machine explicitly.

## Dry run

Two fresh Claude Opus 5.5 high-effort paper runs, one per policy. Old bundle
comes from `be7d5ad`; new bundle is retained with its hashes in the reports.
Both received the same [12 cases](scenarios.md), no author reasoning, no
sibling policy, and no runtime task. [Old report](result-old.md),
[new report](result-new.md), [old input](policy-old.md), [new input](policy-new.md).
One sample per side, no token or reliability claim.

Observed differences: old text rejects the same-provider reviewer and requires
review of the exhaustive three-value transform; new text accepts the fresh
reviewer and permits the evidenced exemption. Both reject exemption for auth
and instructions, keep required checks, remove repeated schema checks, keep
parseConfig and reject processValue. New text explicitly covers finally,
current authorization/state and actionable factual corrections. Old text left
those less settled. No runtime behavior or workflow quality was measured.

After these runs, carry-forward's anything-else section was aligned explicitly
with the new exemption policy. The paired bundle retains its earlier wording;
that clarification is checked by final independent review rather than claimed
as a paired run. Related arena, figure-it-out and trail roles also use the new
fresh-context definition; their complete workflows were not exercised here.

These are accepted preferences. Their enforcement is agent judgment against
real guarantees and evidence, not a new syntax gate:

| User wording | Applied judgment |
| --- | --- |
| "deterministic checks first, one fresh initial reviewer by default, and evidence-backed findings only" | verify and its rubric |
| "I'm okay with lifting it" | same-provider fresh review qualifies |
| "definitely allow exemptions when appropriate" | explicit low-risk scope and current evidence |
| "Validate unknown values once at the boundary that owns them" | boundary ownership and established guarantee |
| "Do not extract single-use helpers preemptively" | readability benefit and meaningful boundary |
| "Avoid try/catch where possible" followed by approval of the refined wording | recovery, boundary contract or necessary context, otherwise propagation |

## Independent review corrections

The first fresh verification found three shoulds: ship still restricted
exemptions to nonbehavioral work, the router still stopped at a missing
second provider, and the global gate omitted passing/current-revision wording.
Ship now defers to verify's documented scope. Paper ship check: an exhaustive
low-risk transform with recorded complete evidence may land under the
exemption; auth and agent-rule changes still need a fresh passing verdict;
missing required checks and unresolved findings block both paths. This is
a rule application, not an observed hosted exempt merge.

Homelab's new regression first failed twice, once for each sole available
provider (`unexpectedly None`). The router now falls back to the available
provider with a fresh-context requirement and native-subagent routing when
appropriate. Cross-provider preference and allowance/exclusion limits remain.
The shared gate explicitly requires a passing verdict on the current revision.
