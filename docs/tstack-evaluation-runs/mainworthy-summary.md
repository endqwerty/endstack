# Review rounds in endqwerty/mainworthy: what each round caught

Sample: the 80 most recent merged PRs, [#854](https://github.com/endqwerty/mainworthy/pull/854) to [#1011](https://github.com/endqwerty/mainworthy/pull/1011) (2026-10-23 to 2026-10-27). Data: `mainworthy.jsonl` (304 records, one per verify or audit round) and `mainworthy-escapes.jsonl`. Classes are my judgement from the PR descriptions and commit headlines, applied strictly as the brief defines them. I did not read the fix diffs.

## Bottom line

- **The claim is half right.** Rounds after the first rarely find a bug: 10 of the 50 later-round findings are bugs, and 62 of the 96 later rounds found nothing. But nits are not most of what later rounds find. Nits are about a third of the findings in every round (32 of 97 in round 1, 17 of 50 later). Risks are the largest share (22 of 50), and half of them come from two PRs: [#919](https://github.com/endqwerty/mainworthy/pull/919) (deadlocks) and [#898](https://github.com/endqwerty/mainworthy/pull/898) (a design record). The clearest nitpick run is [#970](https://github.com/endqwerty/mainworthy/pull/970) (5 nits on malformed input after round 1).
- **Real bugs do turn up after round 1.** 8 PRs had a bug found in round 2 or later. In at least 3 of them ([#1002](https://github.com/endqwerty/mainworthy/pull/1002), [#983](https://github.com/endqwerty/mainworthy/pull/983), [#932](https://github.com/endqwerty/mainworthy/pull/932)) the bug was in code written to fix an earlier finding. Later rounds mostly re-check new code (fixes, audit answers, CI changes), not the same code a second time.
- **Under the proposed caps:**

  | Cap | PRs that would have merged with a bug the loop actually found |
  | --- | --- |
  | (a) stop after round 1 | 8 (7 without the design record #898) |
  | (b) stop at the first round that finds no bug | 4 |
  | (c) at most 3 rounds | 3 |

  All three caps lose [#983](https://github.com/endqwerty/mainworthy/pull/983) round 5 (a blocker) and [#901](https://github.com/endqwerty/mainworthy/pull/901) round 5 (missing evidence samples in the product). Both were found on a new head, after a passing round. A rule that verifies the final head again whenever code changes after a pass would still catch both.
- **Extra verify rounds would not have prevented any escape.** Of the 10 defects that sampled PRs shipped, 2 took production down ([#901](https://github.com/endqwerty/mainworthy/pull/901) → [#918](https://github.com/endqwerty/mainworthy/pull/918), [#909](https://github.com/endqwerty/mainworthy/pull/909) → [#915](https://github.com/endqwerty/mainworthy/pull/915)), even after 8 and 3 verify rounds. Nine needed a live deploy, production-shaped data or a loaded machine. Only one ([#965](https://github.com/endqwerty/mainworthy/pull/965)) looks catchable by a reviewer reading the code.
- **The security audit catches different things.** It found 8 bugs that the verifier missed in every round, including [#919](https://github.com/endqwerty/mainworthy/pull/919)'s duplicated evidence after 4 verify rounds. It also produced most of the false positives (15 of 18), mostly trust-model points and the copyright line in `NOTICE`.

## Counts

- 80 PRs. 73 had independent verification. 7 had none: 4 docs-only ([#956](https://github.com/endqwerty/mainworthy/pull/956), [#958](https://github.com/endqwerty/mainworthy/pull/958), [#959](https://github.com/endqwerty/mainworthy/pull/959), [#883](https://github.com/endqwerty/mainworthy/pull/883)) and 3 test-only, which the repository's rules exempt ([#998](https://github.com/endqwerty/mainworthy/pull/998), [#924](https://github.com/endqwerty/mainworthy/pull/924), [#922](https://github.com/endqwerty/mainworthy/pull/922)). All 7 had a Daybreak audit. 75 PRs had an audit.
- 169 verify rounds and 135 audit rounds in total.
- No PR has a review bot. The `reviews` field is empty on every PR, and the few PR comments are the author's (audit transcripts and screenshots).

**Verify rounds per PR** (73 PRs)

| Rounds | 1 | 2 | 3 | 4 | 5 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRs | 28 | 20 | 14 | 5 | 3 | 1 | 1 | 1 |

**Audit rounds per PR** (75 PRs): 1 round: 40; 2: 20; 3: 11; 4: 1; 5: 2; 8: 1.

## Findings by round (bugs that already existed on `main` excluded)

**Verify**

| Round | Rounds run | Rounds with any finding | Rounds with a bug | bug | risk | nit | false positive |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 73 | 51 | 24 | 34 | 29 | 32 | 2 |
| 2 | 45 | 16 | 5 | 6 | 13 | 8 | 0 |
| 3 | 25 | 8 | 1 | 1 | 3 | 6 | 0 |
| 4+ | 26 | 10 | 3 | 3 | 6 | 3 | 1 |

All later rounds together (2 and up): 50 findings, of which 10 bugs (20%), 22 risks (44%), 17 nits (34%) and 1 false positive. In round 1 the split is 35% bugs, 30% risks, 33% nits.

Seven PRs account for 33 of the 50 later-round findings: [#919](https://github.com/endqwerty/mainworthy/pull/919) (7, mostly deadlock risks), [#970](https://github.com/endqwerty/mainworthy/pull/970) (6, five of them nits), [#898](https://github.com/endqwerty/mainworthy/pull/898) (6, a design record), [#1002](https://github.com/endqwerty/mainworthy/pull/1002) (4), [#983](https://github.com/endqwerty/mainworthy/pull/983) (4), [#947](https://github.com/endqwerty/mainworthy/pull/947) (3), [#932](https://github.com/endqwerty/mainworthy/pull/932) (3). Of the 45 PRs that had a second round, 26 found nothing after round 1.

**Daybreak audit**

| Round | Rounds run | Rounds with any finding | bug | risk | nit | false positive |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 75 | 23 | 9 | 15 | 2 | 10 |
| 2 | 35 | 7 | 1 | 8 | 0 | 3 |
| 3 | 15 | 5 | 0 | 4 | 0 | 1 |
| 4+ | 10 | 4 | 0 | 2 | 1 | 1 |

Audit bugs the verifier never reported: [#919](https://github.com/endqwerty/mainworthy/pull/919) (MCP retry duplicates evidence), [#964](https://github.com/endqwerty/mainworthy/pull/964) (an unmounted volume looks like a deleted checkout, so its clusters get removed), [#886](https://github.com/endqwerty/mainworthy/pull/886) (a stale page cannot sign out), [#932](https://github.com/endqwerty/mainworthy/pull/932) (identifiers in the public CI log), [#947](https://github.com/endqwerty/mainworthy/pull/947) (the Worker sends the secret to another host), [#941](https://github.com/endqwerty/mainworthy/pull/941) (Coolify's `wget` health check fails on 503), [#918](https://github.com/endqwerty/mainworthy/pull/918) (container test expects the old database name), [#983](https://github.com/endqwerty/mainworthy/pull/983) round 2 (stale reopened question). Two more were duplicates of verify findings ([#1006](https://github.com/endqwerty/mainworthy/pull/1006), [#941](https://github.com/endqwerty/mainworthy/pull/941)).

## Last verify round that found a bug, per PR (73 PRs)

| Last round with a bug | none | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| PRs | 47 | 18 | 4 | 1 | 1 | 2 |

The 8 PRs with a bug after round 1, and whether the bug was in the code that round 1 saw:

- [#1002](https://github.com/endqwerty/mainworthy/pull/1002) round 2: `pg_ctl reload` returned before the settings applied. This was in the fix for a round-1 finding.
- [#985](https://github.com/endqwerty/mainworthy/pull/985) round 2: F3, a remote edit to indentation hidden, then overwritten. Rare data loss; the descriptions don't say whether round 1's code had it.
- [#983](https://github.com/endqwerty/mainworthy/pull/983) round 5: a blocker in the fix for audit round 2's finding. Rounds 2 and 4 had passed earlier heads.
- [#947](https://github.com/endqwerty/mainworthy/pull/947) round 2: the CI planner could not read the domain mapping, and certificate renewal would fail. Round 1's verdict is not recorded, so this may in effect have been round 1 for the domain-mapping design.
- [#932](https://github.com/endqwerty/mainworthy/pull/932) round 4: a `:` mask that garbles logs, in masking code added for audit round 1. Low severity.
- [#911](https://github.com/endqwerty/mainworthy/pull/911) rounds 2 and 3: budgets that still failed instead of warning. They were there in round 1 and it missed them, because each round found only part of them.
- [#901](https://github.com/endqwerty/mainworthy/pull/901) round 5: missing evidence samples, on a head reached after rounds 3 and 4 passed and more CI-driven commits followed.
- [#898](https://github.com/endqwerty/mainworthy/pull/898) round 2: a design-record flaw (no code).

## Caps: PRs that would have merged with a bug the loop found

These count bugs found by verify rounds. Audits keep running under every cap; capping audits the same way would lose only [#983](https://github.com/endqwerty/mainworthy/pull/983) audit round 2 (low severity).

- **(a) Stop after round 1:** 8 PRs, the 8 listed above.
- **(b) Stop at the first round that finds no bug** (a clean pass counts as no bug): 4 PRs.
  - [#983](https://github.com/endqwerty/mainworthy/pull/983) stops at round 2 and loses round 5's blocker.
  - [#901](https://github.com/endqwerty/mainworthy/pull/901) stops at round 1, which found only risks and nits, and loses round 5.
  - [#932](https://github.com/endqwerty/mainworthy/pull/932) has no verdict recorded for round 2 and loses round 4's low-severity bug.
  - [#947](https://github.com/endqwerty/mainworthy/pull/947) has no verdict recorded for round 1, so it counts only if round 1 found no bug.

  In all 4, the late bug was on a newer head than the passing round. "Stop the loop" loses them only if code that changes after a pass is never verified again.
- **(c) At most 3 rounds:** 3 PRs ([#983](https://github.com/endqwerty/mainworthy/pull/983), [#932](https://github.com/endqwerty/mainworthy/pull/932), [#901](https://github.com/endqwerty/mainworthy/pull/901)). Each had 7 to 9 rounds, mostly because the head kept changing: audit answers, CI fixes, rebases.

Stopping after round 1 would also have lost risks found later in 12 PRs. Most serious are [#919](https://github.com/endqwerty/mainworthy/pull/919)'s round 2 and 3 deadlocks (each ends as a retryable `busy`, never a wrong write), [#970](https://github.com/endqwerty/mainworthy/pull/970)'s N3 (a crafted archive breaks a read) and [#920](https://github.com/endqwerty/mainworthy/pull/920)'s D4 (a narrow race that could undo a recorded restore).

## Escapes

Fix PRs whose description says they fix a defect from an earlier PR:

| Origin | Fix | What | Could another round have caught it? |
| --- | --- | --- | --- |
| [#901](https://github.com/endqwerty/mainworthy/pull/901) | [#918](https://github.com/endqwerty/mainworthy/pull/918) | Production down: `postgres` resolved to Coolify's own database | No. 8 verify + 4 audit rounds passed; it needed a real Coolify deploy |
| [#909](https://github.com/endqwerty/mainworthy/pull/909) | [#915](https://github.com/endqwerty/mainworthy/pull/915) | Production down: retired-demo cleanup slices grew to 7 s, then one hung | No. Measured on a 1.09 GB synthetic copy; it needed production-shaped data |
| [#932](https://github.com/endqwerty/mainworthy/pull/932) | [#936](https://github.com/endqwerty/mainworthy/pull/936) | First GCP apply failed: no quota project | No round of 7 did; #936's verifier found the sibling gap by reading provider source |
| [#932](https://github.com/endqwerty/mainworthy/pull/932) | [#938](https://github.com/endqwerty/mainworthy/pull/938) | Preview database drift on every apply | No. Needed a live apply |
| [#939](https://github.com/endqwerty/mainworthy/pull/939) | [#940](https://github.com/endqwerty/mainworthy/pull/940) | Job service's first start failed: SQL proxy probed on the wrong port | No. The verifier said the real start was not checked |
| [#932](https://github.com/endqwerty/mainworthy/pull/932)/[#944](https://github.com/endqwerty/mainworthy/pull/944) (my attribution) | [#965](https://github.com/endqwerty/mainworthy/pull/965) | iPhone passkeys broken since cutover: `MAINWORTHY_APPLE_APPS` never set on Cloud Run | Possibly, by any round that compared settings between Coolify and Cloud Run; none did |
| [#943](https://github.com/endqwerty/mainworthy/pull/943)/[#944](https://github.com/endqwerty/mainworthy/pull/944) (my attribution) | [#947](https://github.com/endqwerty/mainworthy/pull/947) | External `/healthz` on run.app answered by Google's own 404 | No. Needed a live Cloud Run request |
| [#910](https://github.com/endqwerty/mainworthy/pull/910) | [#913](https://github.com/endqwerty/mainworthy/pull/913) | New browser test raced Chromium's port file | No. Did not reproduce locally |
| [#875](https://github.com/endqwerty/mainworthy/pull/875) | [#892](https://github.com/endqwerty/mainworthy/pull/892) | New case-loading test flaky under load | No |
| [#865](https://github.com/endqwerty/mainworthy/pull/865) | [#897](https://github.com/endqwerty/mainworthy/pull/897) | New draft-project-live test raced | No. Needed load or an injected delay |

Also recorded in the file:

- Shipped knowingly: [#970](https://github.com/endqwerty/mainworthy/pull/970)'s N6, found in round 4, filed as #973 and fixed in [#982](https://github.com/endqwerty/mainworthy/pull/982).
- Origin unclear: the lifetime test flake fixed by [#1002](https://github.com/endqwerty/mainworthy/pull/1002).
- Origins outside the sample: [#838](https://github.com/endqwerty/mainworthy/pull/838) → [#857](https://github.com/endqwerty/mainworthy/pull/857), [#830](https://github.com/endqwerty/mainworthy/pull/830) → [#886](https://github.com/endqwerty/mainworthy/pull/886), [#815](https://github.com/endqwerty/mainworthy/pull/815) → [#865](https://github.com/endqwerty/mainworthy/pull/865).

The 3 test-race escapes are cheap. The 2 outages, the 3 failed applies and the `/healthz` miss came from environments that no review round touched.

## Representative findings from round 2 or later (verbatim)

**bug**
- [#983](https://github.com/endqwerty/mainworthy/pull/983) round 5: "The undo refresh broke the withdrawal's hold on rules"
- [#901](https://github.com/endqwerty/mainworthy/pull/901) round 5: "Round 5, on `dcd6e411`, found two defects: flaky evidence missing a sample whose target was not preloaded, and a 404 instead of 401 when a session expired during admission."
- [#947](https://github.com/endqwerty/mainworthy/pull/947) round 2: "certificate renewal needs Cloudflare's "Always Use HTTPS" off"
- [#1002](https://github.com/endqwerty/mainworthy/pull/1002) round 2: "`pg_ctl reload` returned before the settings applied (fixed in `d03d888b`)"
- [#985](https://github.com/endqwerty/mainworthy/pull/985) round 2: "`eef608de`, issues: F3 (remote indentation inside preconditions got hidden, then overwritten)."

**risk**
- [#919](https://github.com/endqwerty/mainworthy/pull/919) round 3: "**Issues, two more `40P01` deadlocks, both reproduced live:** `plan` assigning another actor, and `decide` adopting a proposal by another actor."
- [#970](https://github.com/endqwerty/mainworthy/pull/970) round 2: "N3 (P2) the CHECK let `ended_at` exceed 2^53 − 1, and an imported archive with it made the results read fail"
- [#983](https://github.com/endqwerty/mainworthy/pull/983) round 7: "13% slower per file than `main`"
- [#920](https://github.com/endqwerty/mainworthy/pull/920) round 2: "Found D4: a second move before the lookup answered left the retry promise on screen, and `u` then sent a new restore that could undo the recorded one."
- [#932](https://github.com/endqwerty/mainworthy/pull/932) round 6: "One Low defect: an IPv4 address followed by a port or after a colon (`dial tcp 10.20.30.40:5432`) was printed unredacted."

**nit**
- [#970](https://github.com/endqwerty/mainworthy/pull/970) round 3: "N5 (P3) years 0070–0099 became 1970–1999 through `Date.UTC`."
- [#970](https://github.com/endqwerty/mainworthy/pull/970) round 4: "Note N6 (P3): a file missing its times can hide a later file's reversed-time warning; results and span are right either way."
- [#911](https://github.com/endqwerty/mainworthy/pull/911) round 4: "It noted two stale comments, fixed in `fc91453a` (prose only)."
- [#1002](https://github.com/endqwerty/mainworthy/pull/1002) round 3: "One P2: the wait's 10 s deadline is checked between queries, so a server frozen mid-query (the verifier paused it with a signal) holds the call until it resumes."
- [#874](https://github.com/endqwerty/mainworthy/pull/874) round 3: "R3-1 (test coverage): numbering reads at reply time passed every test."

**false positive** (verify had only one after round 1; the other four are from audit rounds 2 and up)
- [#983](https://github.com/endqwerty/mainworthy/pull/983) verify round 7: "the conflict's hash, answered below"
- [#968](https://github.com/endqwerty/mainworthy/pull/968) audit round 6: "The commit rechecks the person's name and password hash, not the email address typed, so removing the address while a sign-in with it runs does not stop that sign-in."
- [#962](https://github.com/endqwerty/mainworthy/pull/962) audit round 2: "Round 2 confirmed the depth bound but still flagged distinct filenames creating many folders."
- [#958](https://github.com/endqwerty/mainworthy/pull/958) audit round 2: "One low finding identified the existing copyright holder in `NOTICE:2`, its app metadata, and test mirrors."
- [#947](https://github.com/endqwerty/mainworthy/pull/947) audit round 3: "One Low, answered as before: the owner's name in `NOTICE` and the app's metadata is the copyright line `AGENTS.md` and decision 0025 allow, predating this change."

## What the descriptions don't let me determine

- **Findings that aren't itemised.** [#932](https://github.com/endqwerty/mainworthy/pull/932) rounds 1–3 ("B1 and F1 to F7… Among them" three), [#963](https://github.com/endqwerty/mainworthy/pull/963) ("F1–F6"), [#898](https://github.com/endqwerty/mainworthy/pull/898) ("ten issues", "seven more"), [#1011](https://github.com/endqwerty/mainworthy/pull/1011) ("all three findings", one described), [#859](https://github.com/endqwerty/mainworthy/pull/859) audit ("two Mediums", no detail). I recorded the named ones and one placeholder `risk` for the rest. The real class mix there is unknown.
- **Missing verdicts or revisions.** Verdicts: [#947](https://github.com/endqwerty/mainworthy/pull/947) r1, [#932](https://github.com/endqwerty/mainworthy/pull/932) r2, [#921](https://github.com/endqwerty/mainworthy/pull/921) r1, [#859](https://github.com/endqwerty/mainworthy/pull/859) audit r2. Revisions: [#967](https://github.com/endqwerty/mainworthy/pull/967) r1, [#963](https://github.com/endqwerty/mainworthy/pull/963) r1, [#931](https://github.com/endqwerty/mainworthy/pull/931) r1–2, [#930](https://github.com/endqwerty/mainworthy/pull/930) r1–2, [#923](https://github.com/endqwerty/mainworthy/pull/923) r2.
- **Rounds aren't comparable.** A "round" may be a full review, a scoped review of one fix commit, a landing recheck after a rebase, or a late review of an old revision ([#923](https://github.com/endqwerty/mainworthy/pull/923)). Verifiers differ (Sol, Opus, Gemini Argon, once GPT 6 Luna). Some PRs fixed the last finding and never had it re-verified ([#1000](https://github.com/endqwerty/mainworthy/pull/1000), [#934](https://github.com/endqwerty/mainworthy/pull/934), [#865](https://github.com/endqwerty/mainworthy/pull/865), [#864](https://github.com/endqwerty/mainworthy/pull/864)).
- **Fix-induced or not.** Whether a later-round bug was already in round 1's code is stated or inferable for 4 of the 8 PRs only.
- **Classification calls a reader might make differently:**
  - Test-coverage regressions in test-only PRs are counted as bugs ([#1011](https://github.com/endqwerty/mainworthy/pull/1011), [#1005](https://github.com/endqwerty/mainworthy/pull/1005)), and so are failures that turned the check red, which CI would also have caught ([#909](https://github.com/endqwerty/mainworthy/pull/909), [#886](https://github.com/endqwerty/mainworthy/pull/886)). Every one of these was found in round 1, so they don't change the cap results.
  - Changelog-filename and lint failures are counted as nits.
  - [#898](https://github.com/endqwerty/mainworthy/pull/898) is a design record; I classed its design flaws as if they were code.
- **Escapes are incomplete.** I searched only PR bodies (sampled PRs and their successors up to #1011; #1012 is still open), not issues. A defect fixed without naming the PR that caused it is missed, and two attributions in the table are mine.
- **Severity and cost.** The descriptions give no review time or token cost per round, so the cost side of a cap can't be measured from this data.
