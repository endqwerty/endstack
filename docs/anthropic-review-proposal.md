# A narrower review policy

Historical research and proposal. The [adoption record](review-adoption/checks.md)
and active skills supersede the open choices below after Daniel approved
provider-optional fresh review, appropriate exemptions and the coding defaults.

Proposal, 2026-10-27. This document and its patch are review material, not
active instructions. Nothing here changes the installed skills or merge gate.

Adopt explicit context isolation and filter unsupported or stylistic findings
before the author edits. Keep one initial verifier and the existing rules for
reviewing fixes. The evidence does not justify removing cross-provider review
or exempting more behavior changes yet. Those remain Daniel's choices.

## What Anthropic actually says

The sources below were opened on 2026-10-27. Gemini combines several different
workflows into one recommendation. The defensible parts are narrower:

| Claim | Primary-source result |
| --- | --- |
| A fresh reviewer should not inherit the writer's reasoning | Explicit in [Best practices](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run). It does not establish that model diversity adds no value. |
| Review against the specification and skip style | Explicit in [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec). |
| Use executable checks and Stop hooks | Explicit [typecheck example](https://code.claude.com/docs/en/best-practices#enforce-the-check-with-a-stop-hook), not an automatically configured test suite. |
| `/verify` runs the app and inspects the result | [Documented](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run). This is Anthropic's command, not endstack's `verify` skill. |
| One reviewer is Anthropic's universal recommendation | Unsupported. [Building effective agents](https://www.anthropic.com/research/building-effective-agents) includes multiple vulnerability-review prompts as a useful voting workflow. It recommends starting simple, not banning multiple reviewers. |
| Managed review finds, then filters | Confirmed in [Code Review](https://code.claude.com/docs/en/code-review). Several agents inspect changes and surrounding code; verification filters findings. These sources do not establish Gemini's specific Haiku/Sonnet staffing claim. |
| Local review always means one narrowly scoped pass | Too broad. [Local review](https://code.claude.com/docs/en/code-review-local) varies coverage with model and effort and can include simplification and efficiency. Our narrower scope needs a custom rubric. |
| Separate agents must write tests and implementation, with immutable tests | Not established by the current sources checked. The older [engineering article URL](https://www.anthropic.com/engineering/claude-code-best-practices) redirects to current best practices; its historical wording was not verified here. Do not attribute the strict split or mandatory hook on this evidence. |
| Strip passing logs, always reset to a spec checkpoint, keep instructions under 100 lines, and use exactly 3–4 worktrees | The checked sources support concise instructions, evidence and independent parallel work, but do not establish these exact prescriptions. Treat them as Gemini's techniques, not Anthropic requirements. |
| This shifts 80% of verification to scripts and makes review much cheaper | No supporting measurement in the checked sources. No cost estimate is made here. |

The strongest corrective source is the Claude Code team's
[October 15 review article](https://claude.dev/blog/solving-code-review-at-anthropic/).
It describes executable verification followed by a fresh-context review,
additional automated review layers, and separate agents that validate findings.
It also describes noise filters, a round cap, and narrower re-review. Its
at-most-one-human goal is not a limit of one model reviewer. This supports
filtering and convergence without a universal reviewer count. The article
recommends judging efficiency alongside reverts and incidents.

## What our current rules already cover

Baseline: endstack `6136a6b5cf83cf4361ddda03c8b445375d22aa5a` and locally read
homelab `ed99a59`. The [verify skill](../skills/verify/SKILL.md) already puts
author checks before one cross-provider verifier, excludes author conclusions
from the brief, requires a reachable path for findings, and limits repeated
rounds. [Carry-forward](../skills/verify/references/carry-forward.md) already
scopes review of small fixes and handles unchanged patches.

The duplication is explicit: the verifier must run every required check
again. That can be deliberate independent evidence, not wasted model judgment.
Accepting revision-bound CI evidence instead is a separate future change;
this proposal does not relax that requirement.

The remaining gaps are fresh context rather than merely a neutral brief,
filtering before reporting, and the invitation to fix a nit if it is small.
The proposal changes those. Its one-first-pass wording implements the
recommended option for the still-open extra-pass choice; it is not neutral
between those options and is not active policy. `check-skills.py` already checks names, sizes,
frontmatter and links. `check-routing.py` checks routing coverage and merge
triggers. Neither proves that an agent follows a review policy.

## What recent reviews actually caught

A read-only Claude Sonnet 5.5 worker inspected four recent merged endstack
pull requests. The parent checked the linked repository evidence. The four
PRs had no hosted review comments, so their descriptions and committed reports
are the evidence, not independently reproduced reviewer transcripts.

| Evidence | Why it matters to the proposed filter |
| --- | --- |
| [#18](https://github.com/endqwerty/endstack/pull/18), `d0abbec`: a whitespace-insensitive fingerprint treated behaviorally different Python patches as equal | A behavior defect, not a formatting nit. Keep it. The reproduction is in [carry-forward evidence](verify-carry-forward.md), not newly rerun here. |
| [#23](https://github.com/endqwerty/endstack/pull/23), `a7b75cd`: rare-path nits overlapped the definition of should | An instruction contract conflict. Keep it; agent instructions are behavior. |
| [#23](https://github.com/endqwerty/endstack/pull/23), `6b862b3`: moving text dropped the author's obligation to read a child's diff | An omitted responsibility that mechanical checks cannot prove. Keep it. |
| [#21](https://github.com/endqwerty/endstack/pull/21), `41f5662`: a report attributed four guards to findings, although one came from the author | Factual accuracy, not style. A skip-style rule must still allow correction of false evidence. |
| [#22](https://github.com/endqwerty/endstack/pull/22) | No findings reported. A reviewer need not invent work. |

The earlier [reachable-findings study](verify-reachable-findings.md) supplies
a counterexample to speculative guards: a concern about value-derived
instance keys when the keys were literal. It also records why imported data
must remain in scope even when ordinary callers are safe. These are historical
examples, not fresh replays. The [tstack study](tstack-evaluation.md) does not
supply per-round token or time measurements; its estimates are not reused as
cost evidence here.

## Exact proposal

[verify.patch](anthropic-review-proposal/verify.patch) changes only
`skills/verify/SKILL.md` and adds `references/review-rubric.md`. It is not
applied. It retains the current trigger, provider requirement, independent
execution of required checks, carry-forward rules and two-round rethink,
with at most two further rounds. No new skill, hook or reviewer committee. The shorter "full diff" line
drops the explicit "a subagent's included, never a summary" reminder, although
the full-diff obligation remains. This wording choice is included in the
unapplied proposal for review.

The rubric supplies requirements, project constraints, the full diff, base
and head, check evidence, and access to surrounding code. It excludes the
author's conversation and preferred conclusion. It asks for relevant
regression and safety paths as well as specification compliance. A flawed
specification must not hide a security or data-loss defect.

A reported defect needs a location, a current trigger, expected and actual
behavior, and a reproducer or a concrete code trace. Unrun required checks
and unresolved safety facts remain `not checked`. They cannot become passes
or fabricated defects. The final rubric explicitly treats factual errors
in evidence or requirements as correctness defects, not wording nits. Style
and hypothetical future guards prompt no edits
and no review round. Existing external comments still receive a written
disposition under `babysit` and `ship`.

The reference keeps the core skill within its size limit. This reduces
requested review work, not prompt length. **Subtract Before You Add** shaped
the decision to remove nit fixes rather than add another reviewer to judge them.

## Dry run and limits

The [experiment record](anthropic-review-proposal/experiment.md) contains the
predeclared checks, fixture, policies, reviewer reports and reproduction
commands. It compares current and proposed text in fresh contexts on the
same small Python change. The parent withheld two contract assertions from
the reviewers. They fail on the supplied implementation although its smoke
checks pass. **Test Behavior, Not Implementation** shaped those assertions:
exact-limit acceptance and rejection of an over-limit import.

This is a narrow rubric check, not a production reliability benchmark. It
establishes neither savings nor provider equivalence, recall or safe
exemptions. Equal outcomes are reported as equal, not as an improvement.
Independent review found a factual-correction gap in the tested draft. The
experiment record separates that draft from the corrected final rubric.
The [scoped independent recheck](anthropic-review-proposal/review-round-2.md)
passed the final patch and its paper regression cases.

## Choices left to Daniel

1. **Provider independence.** Keep the current requirement, or permit a fresh
   session from the same family. Recommendation: keep it for now; these sources
   explain isolation but do not compare its defect detection with diversity.
   Changing it needs both `verify` and homelab's global verifier/routing rules
   updated together. Reverting those changes restores the requirement.
2. **Exemptions.** Keep today's nonbehavioral exemptions, or define a broader
   class covered by deterministic evidence alone. Recommendation: keep today's
   scope until real misses and coverage justify a particular exemption. Agent
   instructions, migrations, auth and money do not become exempt just because
   their diffs are small. Any exemption needs matching global rules.
3. **Additional passes.** Default to one initial pass with targeted rechecks,
   or require extra independent coverage for named risks. Recommendation: retain
   stricter project requirements and add a pass only for a specified unresolved
   risk or relevant new behavior. A second search with no new question is not
   evidence. The patch keeps the existing round and carry-forward rules.

No Stop hook is installed. Hook ownership and commands belong in homelab or
the affected project, and this repository already has deterministic checkers.
If adopted later, the patch can be reverted without a data migration. Changing
the provider gate or exemptions is outside the patch and remains undecided.
