# Independent verdict: Anthropic review proposal

Verifier: Claude Opus 5.5 (read-only, fresh context; same family as the dry-run
reviewers, see limits). Judged endstack worktree t3-c14452ee, base
`6136a6b5cf83cf4361ddda03c8b445375d22aa5a`, head
`606bf73093108b69a14eedad844f2749da7f8948` (HEAD at review, working tree
clean). Full diff read: 21 files, 872 insertions, no deletions.
Patch judged: `docs/anthropic-review-proposal/verify.patch` at head.

(In progress; sections appended as confirmed.)

## Mechanical and fixture checks

| Check | Result | Deciding evidence |
| --- | --- | --- |
| smoke.py on quota.py | pass | `4 smoke checks passed`, rc=0 |
| contract_checks.py on buggy quota.py | pass (fails as required) | `FAILED (failures=2)`, rc=1; both tests FAIL |
| contract_checks.py on fixed.py | pass | `Ran 2 tests ... OK`, rc=0 |
| check-skills.py at head | pass | `0 problem(s)` |
| check-routing.py at head | pass | `0 problem(s)` |
| `git apply --check verify.patch` | pass | rc=0 |
| Patch applied to temporary `git archive HEAD` copy | pass | both checkers `0 problem(s)`; `cmp` patched SKILL.md == proposed-policy.md; patched rubric == committed rubric; core 2,162 bytes vs `CORE_MAX = 2200` |
| Input hashes vs reports | pass | base.py 82f18c5d…, quota.py d2feb599…, change.diff e8dac6a8…, SPEC.md b0aeb337…, smoke.py c6c9f226…, current-policy cb5d6035… (A), proposed-policy 588eda8a… (B), rubric bb8b4792…, carry-forward fdf8affa… all match the reports' tables |
| Committed carry-forward copy == active `skills/verify/references/carry-forward.md` | pass | `diff` empty |
| Active skills, ROUTING.md, scripts, AGENTS.md unchanged base..head | pass | `git diff --stat 6136a6b 606bf73 -- skills ROUTING.md scripts AGENTS.md` empty |
| Global rules unchanged | pass | `~/.claude/CLAUDE.md` byte-identical to homelab `agents/AGENTS.md`; homelab ed99a59..538b15a touches only CHANGELOG.md and workstation.md |
| Committed result-a/result-b == /tmp originals | pass | `cmp` identical |
| Temporary copy removed | done | literal path deleted |

## Primary-source claims (opened independently, 2026-10-27)

Pass. Each row of the proposal's claim table matches the source:

- Best practices (code.claude.com/docs/en/best-practices): under "Give Claude a
  check to run", "/code-review reviews the diff in a fresh subagent that never
  saw your conversation. It isn't swayed by the reasoning that produced the
  code." and "run /verify ... which has Claude build and run the app and look at
  the result." "Review against your spec": "report gaps that affect correctness
  and skip style" / "Don't drop the `skip style` part". "Enforce the check with
  a Stop hook": typecheck example, exit code 2. No 100-line limit (it cites the
  memory guide's "under 200"), no 3-4 worktree count, no log stripping, no
  test-writer/implementer split or immutable tests. Also "same model ... a fresh
  pair of eyes ... not a smarter answer", which does not rank isolation above
  diversity.
- Code Review: "Several agents read each change alongside the surrounding
  code"; "A verification step checks findings against the code"; "Code Review
  chooses the Claude models"; no Haiku/Sonnet staffing named.
- Local review: "Depending on your model and effort level, the review also
  covers reuse, simplification, and efficiency cleanups."
- Building effective agents: voting example "Reviewing a piece of code for
  vulnerabilities, where several different prompts review and flag the code";
  "finding the simplest solution possible, and only increasing complexity when
  needed". No ban on multiple reviewers.
- claude.dev review article: dated October 15, 2026; fresh-context subagent
  review after runnable checks; separate security review; "a separate group
  votes on each finding"; style/cleanup filters A/B tested; "After three
  rounds ... reconsider the approach"; "Diff-only re-review"; "at most one human
  in the loop"; "Revert and incident rates are the guardrail".
- Old engineering URL: HTTP 308 to code.claude.com/docs/en/best-practices, as
  stated.
- Gemini's text (from the task's first user message, read only for the claims
  column): every recommendation it attributes to Anthropic appears in the table
  with a correct status.

## Recent-review evidence

Pass for the checked rows. d0abbec, a7b75cd, 6b862b3, b1214ee exist locally
and match their descriptions. 41f5662 is not in local history (rebased away),
but PR #21's body records "Round 1 on `41f5662`: issues ... the record
attributed all four guards to findings, when one was the author's", which
matches. #22 hosted content: not checked.

## Confirmed findings on the proposal and patch

### F1. Should: the patch forbids the edit the proposal says must stay allowed

- Contract: docs/anthropic-review-proposal.md, #21 row: "Factual accuracy, not
  style. A skip-style rule must still allow correction of false evidence."
- Patch: step 5 becomes "Decline nits without edits or another round." The
  nit definition it keeps still includes "wording". The rubric's only carve-out
  is "A required compatibility or safety property is not style."
- Reach: the #21 finding itself. A misattribution in a committed evidence
  record is not "the intended case is wrong" and is not reached by "ordinary
  use, a caller, stored or imported data, a race or a setting", so a verifier
  following the tiers literally ranks it a nit ("wording"). Today "Fix a nit
  only if small" lets the author correct it; under the patch the author must
  decline it. Most endstack verify PRs ship an evidence record like this, so
  ordinary use reaches it. The dry run did not test this case (its fixture has no
  evidence document).
- Cheapest fix: one rubric or tier sentence saying that a false factual claim in
  evidence, a report or an instruction is a should, not wording. Or keep the
  small-nit allowance for factual corrections only.

### F2. Nit: the patch drops "a subagent's included, never a summary" without saying so

- Current line 8: "Both roles read the whole diff, a subagent's included, never
  a summary." b1214ee restored it after the 6b862b3 re-review, the same case the
  proposal's #23 row says to "Keep". The patch replaces it with "Both roles read
  the full diff and [rubric]". It is the only mention of subagent diffs in
  skills/verify/.
- "Full diff" still covers a child's edits in substance, so I rank this as
  wording. But "never a summary" is an explicit guard that a recent review
  finding put back, and the proposal's lists of intended changes and of retained
  rules do not mention removing it.

### F3. Nit: the patch already contains one answer to open choice 3

- The proposal leaves "Additional passes" to Daniel, and of the patch it says
  only that "Changing the provider gate or exemptions is outside the patch."
- The patch says "Ask one read-only verifier"; the rubric says "One first pass
  is the default", "Re-review only for fixes or new evidence that the
  carry-forward rules require" and "Do not add a reviewer just to seek more
  findings". That is the recommended option. Adopting the patch picks it; it is
  not neutral. The patch is unapplied, so nothing is installed. The fix is one
  sentence in "Choices left to Daniel" saying so.

## Experiment and limits

Pass with one not-checked item. The reports support each row of the results
table: A ranks the import defect should and B ranks it blocker; both decline
the rename and the parser guard, both note the keyword-caller risk, both list
callers and upstream schema as not checked, and both call for a scoped
single-verifier recheck. Limits are stated and not overstated: no improvement,
saving, recall, provider or isolation effect is claimed, and the parent-authored
fixture and shared machine are disclosed.
- Not checked from committed evidence: "B reported that it wrote its report at
  the end rather than incrementally" (that is not in result-b.md), and that
  contract_checks.py ran "before collecting the reports". Both depend on timing
  or messages outside the committed files.
- Not exercised by the experiment and not claimed: F1's factual-correction case.

## Safety fact

Live review behaviour is unchanged because the patch is unapplied. Proven:
nothing under skills/, ROUTING.md, scripts/ or AGENTS.md changed from base to
head, and the global rules are byte-identical to homelab's agents/AGENTS.md.

## Verdict: ISSUES

The research claims, mechanical checks, fixture behaviour, patch identity,
unchanged live rules and stated limits all pass. One should (F1) is open
against the proposed patch. F2 and F3 are nits. Required checks: all pass,
except two experiment-timing claims, which are not checked.

Independence: verifier is Claude Opus 5.5. Transcript metadata shows the
author ran on Codex gpt-6-astra, so the provider differs. I read transcript
metadata and the user's first message (for Gemini's text) before writing this
verdict, but not the author's reasoning or decisions.

---

## Trail scan (separate from the verdict above; not a new code review)

Inputs: decisions.tsv (4 rows), transcript.json (88 items, hasMore=false).
Limitation: item 83, the author's own `t3_thread_read`, is cut at 50,000
characters (`textTruncated: true`). Anything only in its tail is not seen.
The other 87 items are complete.

Matches:
- The `frame` row (06:02:13Z) matches item 20, which ran before any drafting.
  The acceptance file (item 41, 06:03:59) comes before the policy and fixture
  drafts (items 42 and 45) and before the dry runs. That supports "recorded
  before drafting".
- The `evidence` row: the claude.dev article supports it (I checked this
  independently above).
- The `experiment` row ("equal"): result-a.md and result-b.md support it.
- The dry-run arms were Claude Opus 5.5 at high effort (items 48 and 58), as
  brief.md says. The research worker was claude-sonnet-5-5 at medium (item 21),
  as the proposal says.
- Timing claims I could not check from the committed files: contract_checks.py
  ran at 06:05:04Z (item 52, two FAILs) before B returned (06:06:03Z) and A
  returned (06:07:08Z). fixed.py was made afterwards (item 67, 06:07:48Z). B's
  return says "I wrote the results file in one go at the end, not finding by
  finding as asked" (item 49). All three claims are supported.

Attention flags:
1. The three later decisions.tsv rows share one timestamp (06:08:45Z, item 72).
   They were logged together after the work, not as each decision was made.
2. The log leaves out the decisions that change behaviour: removing the
   small-nit allowance, rewording line 8 (which drops "a subagent's included,
   never a summary"), and the rubric's one-pass default. The `proposal` row says
   "Retain current review gates in the unapplied patch". That holds for the
   provider gate and the trigger, but not for F1, F2 and F3.
3. The first draft of docs/anthropic-review-proposal.md (item 60, 06:07:05Z)
   was written 3 s before arm A returned (06:07:08Z). Later items (65, 67, 80,
   84) read both reports and rewrote the files, and the committed text matches
   both reports. So this is a process note, not a wrong claim.
4. /tmp/endstack-review.fiP6up/fixture/__pycache__/quota.cpython-315.pyc exists
   in the parent's scratch fixture, though not in the committed fixture. That is
   harmless, and cleanup belongs to the parent.
