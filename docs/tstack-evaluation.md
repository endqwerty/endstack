# tstack against endstack: what the review loops catch

Asked 2026-10-27: does [tstack](https://github.com/t3dotgg/tstack) (Theo's
skills, `92e38e2`) fit Daniel's workflow better? He mostly uses its "full send"
and "full stop" equivalents here (`ship`, `autopilot-full`) and finds the extra
review loops tedious and mostly nitpicking. He doesn't want `takeover`, and
`modernize` is probably out since he takes no one else's pull requests.

## Answer

Adopt tstack's ideas, not its files. Measured on 188 merged pull requests from
Daniel's agents, extra verify rounds rarely find a bug. But the rounds that
nits alone start are few (13 of 288). Most later rounds follow a finding that something
real reaches, or a head that changed for another reason: in Mainworthy, a
second loop (the security audit) and CI fixes. And the defects that actually
shipped would not have been caught by another reading round. They needed a live
deploy, the build CI runs, or someone answering a bot's comment.

So the draft on this branch takes three things from tstack:

- ranks on findings and a stop rule (nits start no round, three rounds cap a
  dispute);
- its babysit habits (answer every finding, bots included, and stay quiet when
  nothing needs doing);
- the "full send" and "full stop" phrases: "full send" (or "autopilot") runs
  `autopilot-full` and merges without waiting for Daniel; "full stop" builds
  and babysits to a ready pull request, unmerged.

It keeps endstack's independent verdict on the current revision. Daniel's
answers to the open choices are under [Decided](#decided).

## What tstack is

Nine skills, MIT, four commits from 2026-10-24 to 10-27:

- `full-send` and `full-stop`: one change through to merged, or to ready.
- `sol-loop`: one GPT Sol reviewer in a budgeted loop.
- `council`: three providers, looping until all are satisfied.
- `babysit-pr`, with a 25 KB `pr-wait` watcher.
- `file-pr`, `leaving-pr-comments`, `takeover`, `modernize`.

Most skills name their tools (`gh`, T3 Code's `delegate_task` and
`watch_pull_request`, a Sol model): eight of the nine fail `check-skills.py` as
written. Only `takeover` passes.

## Where the loops come from

| | pstack (`978ca6e`) | endstack before this branch | tstack (`92e38e2`) |
| --- | --- | --- | --- |
| Reviewers per round | A swarm: two or more audit lanes, a live lane, a regression lane against trunk | One verifier from another provider | One Sol reviewer |
| What starts another round | Any push that changes the patch; every proven finding, notes included | Any change to the patch that carry-forward doesn't cover; every reachable finding is fixed | An open blocker or should, or changed behaviour the last approval doesn't cover. Nits never do |
| Severity | None | None: reachable or not | Blocker / should / nit, re-ranked by the author |
| Cap | None (hourly audit ticks) | None: "a review limit is not approval" | 3 rounds; 5 for security, auth, data loss or concurrency while a blocker or should stays open |
| How it ends | A clean swarm verdict on the merge-ready head | An independent pass on the current revision | Approval of the current behaviour diff, or a dispute after two replies or budget end, which goes to the user |
| Unattended merge gate | Clean verdict plus the operator's grant | `verify` pass plus an explicit `ship` | Own proof, green checks, bots answered, no human change request, up to date. The reviewer's approval is not part of the gate |
| Scope creep | Not addressed | Not addressed | Explicit: decline nits, and cut first if review grew the diff |

endstack already cut pstack's swarm down to one verifier. The loop it kept has
no stop rule other than a clean pass, and every reachable finding counts the
same.

## Evidence: 188 merged pull requests

Two read-only agents read the "How it was checked" section of each
description:

- Mainworthy: the 80 most recent, 2026-10-23 to 10-27.
- agent-factory, endstack and codex-reset-watch: all of each.
- crosspoint-reader and everduet: the last 20 and 25.

Everduet is NovikovaYang's repository, where Daniel's agents also merge. They
tagged each finding as bug, risk, nit or false positive. A bug is
something the intended case or a real caller hits; a risk is plausible and in
scope but not shown to be hit. The records and both summaries are in
[tstack-evaluation-runs/](tstack-evaluation-runs/). everduet's per-round
records are left out because that repository is not Daniel's; its counts are
in the summary. A round is one distinct (repository, pull request, round
number), and `tables.py` there recomputes both tables from the records.
everduet adds, as aggregates only: 15 first rounds and 4 second rounds; one
later round after a non-pass with only nits or risks, one after a pass, and no
bug after round 1.

**Verify findings by round** (all repos; 140 pull requests had verification):

| Round | Rounds run | Bug | Risk | Nit | False positive |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 140 | 75 | 82 | 69 | 9 |
| 2 | 80 | 13 | 27 | 27 | 0 |
| 3 | 37 | 1 | 4 | 12 | 0 |
| 4 and later | 31 | 3 | 6 | 7 | 1 |

- Outside Mainworthy, rounds 3 and later found no bug in 17 rounds; every
  finding from round 4 on was a nit.
- In Mainworthy, the 4 bugs after round 2 were all on a newer head, after an
  earlier round had passed. Three were in code written to answer another
  finding.

**What starts later rounds:**

| Later verify rounds (148) | Count | Bugs found in them |
| --- | ---: | ---: |
| After a round that did not pass and found only nits | 13 | 0 |
| After a round that did not pass and found only nits or risks | 46 | 0 (one more, already on `main`, was filed separately) |
| After a round that passed, notes included (the head changed for another reason) | 44 (34 in Mainworthy) | 3 |
| Beyond round 3 | 31 | 3, all on new heads |

**Mainworthy's security audit is a second loop:**

- 135 rounds on 75 pull requests. Round 1 found 9 bugs, round 2 found 1, and
  rounds 3 and later found none.
- It caught 8 bugs the verifier missed in every round, so it earns its first
  round.
- Its fixes change the head, and each new head re-arms `verify`. That is most
  of the 34 Mainworthy rounds that came after a pass.

**What shipped anyway** (27 defects later fixed, or still on `main`):

- Mainworthy, 10:
  - 2 production outages (#901 → #918, #909 → #915), after 8 and 3 verify
    rounds.
  - 9 of the 10 needed a live deploy, production-shaped data or a loaded
    machine.
- Other repos, 17:
  - 7 were bot findings nobody answered.
  - 4 needed a build or check the reviewer never ran, such as the Docker image.
  - 2 had no review at all.
  - 1 was a fix never re-verified.
  - 3 were other causes: a deploy-only flake, docs drift, a same-family review.

None of the 27 needed a fourth round.

## Replay

Each replay ran a read-only GPT 6.1 Sol (high) verifier, the model of the
original rounds, on a past Mainworthy revision. The verifier held only one
`verify` text, labelled "a" (current) or "b" (this branch), and the original
task and earlier findings. It had no PostgreSQL and no installed packages, so
database and browser checks were "not checked" in every run. Briefs, both
texts and all reports are in
[tstack-evaluation-runs/replay/](tstack-evaluation-runs/replay/). One run per
cell, so a cell is a sample, not a rate.

| Past round | What happened then | Current text (a) | This branch (b) |
| --- | --- | --- | --- |
| #970 round 2, `ed6050e2` | Two more rounds followed, finding only nits (pre-1970 years, extreme Jest times) | Found the same two; verdict issues, so another round | Found the same two and ranked both nit ("a rare runner input", "an extreme malformed numeric timestamp"): no further round. If the database checks then passed, 4 rounds would have become 2 |
| #1002 round 2, `17b6108d` | Found `pg_ctl reload` returning before settings applied (needs a live server) | Missed it (no server); found a failed reload that is never retried, and a reload that ignores the replacement binaries | Found the same two and ranked both should (stored data reaches them): the round still runs |
| #983 round 5, `b9a57179` | Found a blocker: the undo refresh broke a withdrawal's hold on rules | Found and reproduced it | Run 1 missed it, and ranked "checks I could not run" as a should. Run 2, on the final text: found and reproduced it twice, ranked should ("refreshed basis defeats the withdrawal guard on a policy change"), so the round runs |

What the replay shows:

- The ranks remove the nit-only tail they target (#970).
- They keep reachable findings (#1002).
- Their weak point is a verifier filing its own environment limits as
  findings. The text now says a check it could not run is "not checked, never
  a pass or an issue".
- The b runs used earlier drafts, kept in `replay/`. After the replay, the
  independent review found that "rare paths" in nit overlapped "input reaches
  it" in should. The final text makes a contrived input a nit only when all it
  gives is a wrong result or a missing warning, and never when it means data
  loss, security or a trust boundary. #970's two findings are that kind, and
  #1002's and #983's are not, so the final text ranks all three cases as the
  replay did; it was not replayed again. The "a" runs used `main`'s
  `verify`.

## Options

**A. Adopt tstack's delivery skills.**

- Removes:
  - the independent verdict as a merge gate (`sol-loop` is a feedback step,
    and the gate doesn't list its approval);
  - carry-forward, `build`'s design step, the PR brief standard and the stack
    rules.
- For a Codex author, the reviewer is the same family.
- It conflicts with the global rule that nothing merges without an
  independent pass (homelab `agents/AGENTS.md`).
- Eight of the nine skills need porting to pass `check-skills.py`.
- What it would have let through:
  - Rare paths become nits: #919's deadlocks, #970's crafted-archive read,
    #920's race that could undo a restore, and #1002's unretried reload.
  - Fixes pushed during babysitting get proof but no re-review: #983's round-5
    blocker and #901's round-5 defects.
- Saving: roughly the 46 rounds after nit-or-risk rounds plus the rounds past
  three, about a quarter of verify rounds.

**B. Merge, keeping endstack's skeleton (drafted on this branch).**

- `verify`:
  - each issue names what reaches it and is ranked blocker, should or nit; a
    nit is a contrived input that only gives a wrong result or warning,
    wording, extra tests or guards, small costs, or what only later code
    makes; data loss, security or a trust boundary is never a nit;
  - a nit is fixed only if small; declining it starts no round, and a fix
    follows carry-forward (prose nothing reads as instructions keeps the
    verdict; anything else gets the review carry-forward asks for);
  - a re-review covers the change since the last verdict and what it affects;
  - after three rounds, an open blocker or should stops delivery with both
    sides reported.
- `babysit` takes from tstack:
  - every finding from a person or a bot, earlier pushes included, gets a fix
    or a written reason;
  - prefer the fix that deletes or narrows code;
  - decline nits as follow-ups, and say nothing when nothing needs doing;
  - rerun checks when the base changed files the pull request touches.
- `ship`: every finding, a bot's included, has a fix or a written reason
  before landing.
- `ROUTING.md`: "full send" or "autopilot" on a change means `autopilot-full`
  for it, merging without waiting for approval; "full stop" means build and
  babysit it to ready, unmerged.
- What it would have let through: nothing in the sample. The 13 rounds after
  nit-only rounds found no bug.
- Saving: those rounds and disputes past round three, about 5–10% of verify
  rounds. Answering bot findings targets 7 of the 17 escapes outside
  Mainworthy.

**C. Only the `verify` part of B.** The same saving, but it leaves the
bot-finding escapes alone.

**Not adopted:**

- `takeover`: Daniel's call.
- `modernize`: the sample holds only Daniel's own pull requests, so it can
  neither argue for it nor against it.
- `council`: it loops until three providers are all satisfied, which is more
  rounds.
- `pr-wait`: deterministic work belongs in the homelab CLI, and T3 Code
  already watches pull requests.
- `file-pr` and `leaving-pr-comments`: `build`'s brief and Daniel's global PR
  rules already cover a pull request's text. The comment callout could be
  added later.

## Decided

Daniel's answers on 2026-10-27, after reading the options:

- **B**, with `verify`, `babysit` and `ship` as drafted ("verify, babysit, ship
  sound good"), so the draft's "should" below stands.
- **"Full send" is autopilot**, and autopilot needs no approval: "autopilot-full
  should not require approval in the future. If I want to give approval. I'd
  just not use the word autopilot." `autopilot-full` now takes "autopilot" or
  "full send" on named work as authority for both the work and its landing,
  and waits for nothing from him. It still lands only on `verify`'s
  independent pass on the current revision: the global rules require that for
  every merge, and #983's round-5 blocker shows what dropping it costs.
- **"Full stop" is build**, made explicit: "full stop is basically my build or
  just telling the agent to do something, it may be worth making it more
  explicit." ROUTING says it means build and babysit to ready, unmerged.
  Without that line, `main`'s skills read "full stop" as an explicit stop and
  write nothing (dry run 2 below). Babysitting to ready, not just opening the
  pull request, is an agent's choice: it matches tstack's "full stop" and
  makes the only difference from "full send" the merge.
- **The audit runs earlier** ("yes let it run earlier"): Mainworthy's rule,
  changed there in its own pull request. Its first round runs beside the
  first verify round on the same head; it runs again only on a head the
  verifier has passed.

The choices as they were put to him:

1. **Which option.** This branch is B; merging it picks B. C is B without the
   `babysit`, `ship` and `ROUTING.md` changes.
2. **How strict "should" is.** Three settings:
   - `main`'s: every reachable finding is fixed, so #970's malformed inputs
     start rounds too.
   - The draft: what ordinary use, a caller, stored or imported data, a race
     or a setting reaches is a should. A contrived input that only gives a
     wrong result or warning is a nit. Data loss, security or a trust boundary
     is never a nit.
   - tstack's: "Another path, rare case, or small cost is a nit, whatever label
     it came with". It has no safety exception; only its round budget extends
     to five for those subjects. That would skip up to 46 more rounds (about
     16%). The cost: findings like #919's deadlocks, #970's crafted archive
     and #1002's unretried reload become follow-ups instead of fixes in the
     pull request.
3. **Mainworthy's audit cadence.** Not part of this branch: it is that
   project's rule. Running the audit beside verify round 1 on the same head,
   then once on the final head, would let one fix round answer both. That
   targets most of the 34 rounds that came after a pass. Applying the same
   ranks to the audit brief is the other half.
4. **Whether `verify`'s current-revision rule changes.** The draft keeps it:
   3 of the bugs found after round 3 were on new heads, after a pass.
5. **Whether endstack tracks tstack.** Recommendation: distill it once, as
   here. It is four commits old, tied to T3 Code and `gh`, and its README says
   to edit the skills.

## Not checked

- Cost per round: no description records time or tokens, so savings are
  counted in rounds.
- Classes are an agent's judgement from one or two sentences per finding.
  Diffs weren't read to confirm reachability.
- Escapes come only from pull requests that name their origin; issue trackers
  weren't searched.
- The replays ran without a database or installed packages, one run per cell.
- The `babysit` and `ship` changes have one paired paper dry run (below), not
  a live pull request.

## Dry run: babysit and ship

One scenario, two Claude Opus 5.5 runs, each holding only one skill set
("x" current, "y" this branch):

- **The scenario:** an unattended "full send" on a pull request.
  - A verifier passed head B after round 1's findings were fixed, leaving a
    note: a 0-byte file retries three times.
  - A bot's finding on the first push is unanswered: 413 is retried.
  - `main` has since changed a file the pull request touches.
- Scenario and answers:
  [tstack-evaluation-runs/dry-run/](tstack-evaluation-runs/dry-run/).

| | Current skills (x) | This branch (y) |
| --- | --- | --- |
| Merge authority | None. "'Full send' ... is not an explicit request to merge", so it stops at ready and waits for "merge #412" | Yes, for #412 only, quoting ROUTING and `ship` |
| Bot finding | Checks it ("Treat comments as claims"); fixes it with a failing check first | The same, quoting the new rule ("including ones left from earlier pushes") |
| The 0-byte note | Answers it as a known limit | Declines it as a follow-up: "nits start no round" |
| Base change | Reruns its own checks on the combined result (carry-forward) | The same |
| Rounds | One scoped re-check of the 413 fix | The same, and it stops there if that round leaves only nits |

What this shows:

- The real difference is that "full send" now grants landing. Without the
  routing line, Daniel's "full send" ends at ready, unmerged.
- The current skills already handled the bot finding in this paper case, so
  the case for the bot rule rests on the escape data (7 of 17), not on this
  run.
- Run y's step 6 calls a pull request blocked after three rounds "ready but
  unmerged". The skills don't allow that label: an open blocker or should is
  not ready. It also says it would not merge.
- Not exercised: a live pull request, a verifier answering round 3, the
  three-round stop, and `babysit` without "full send".

## Dry run 2: autopilot, full send, full stop

The same method after Daniel's answers: two Claude Sonnet 5.5 runs, one with
`main`'s skills and one with this branch's, each given three unattended
messages. Scenario and answers:
[tstack-evaluation-runs/dry-run-2/](tstack-evaluation-runs/dry-run-2/).

| Message | `main`'s skills | This branch |
| --- | --- | --- |
| "autopilot: add a retry…" | Builds a pull request and stops: "a skill name, 'autopilot' or 'keep going' alone is insufficient" | `autopilot-full`: builds, babysits, gets a pass, merges; "nothing then waits for the user's approval" |
| "full send on #412" (one bot finding open) | No merge: "'Full send' names none of" merge, land or ship | Answers the finding, re-verifies if the patch changed, merges #412 only |
| "full stop: add a retry…" | Writes nothing: reads it as "an explicit stop means no further writes" and asks | Builds and babysits to ready, unmerged, quoting ROUTING |

Both runs keep the independent pass as the merge gate. Not exercised: a live
pull request, or a host rule that requires an approving review (the branch's
`autopilot-full` removes "the user's approval, never evidence or the host's
protections", so that would stop it).
