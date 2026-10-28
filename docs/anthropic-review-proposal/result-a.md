# Review result A: quota.py

**Verdict: ISSUES.** One blocker, one should. Both must be fixed before delivery.

## What I judged

These are synthetic files with no commit history, so each is identified by SHA256:

| File | SHA256 |
|---|---|
| base.py (before) | `82f18c5d905f6e9aaa387f6624e4058d3a16d32e819a91233de95aabccbad019` |
| quota.py (after) | `d2feb59975c7487f6574146f69e183de2698946ddc0a94bf681058290828fd88` |
| change.diff (patch) | `e8dac6a8dc6520d126f409926ced1e7c1f67f4788efec4557e2aedc561144e76` |
| SPEC.md | `b0aeb337b1987a5be00281dd6c85b0dbfe2c48c6c37509db59900f28d7dc32be` |
| policy.md | `cb5d6035c70eb1222c3875a5350fb5dac65d94afb155859533078b4350c9d846` |
| smoke.py | `c6c9f2261611926ef028f6b0c253cfcb1cca18af277556385c9781a372ec0d37` |

I read the whole diff, not a summary of it. `diff -u base.py quota.py` gives the same hunks as change.diff (`hunks identical`), so the patch I reviewed is the real before-to-after change. No input file was changed: I ran Python with `-B` so the inputs directory gets no `__pycache__`, and the hashes and directory listing are the same after the run.

## Safety fact

The change is safe only if two things hold:

- (a) `can_reserve` behaves exactly as base does for every caller input the spec allows;
- (b) `restore` lets a snapshot through only when `0 <= used <= limit`, which is the `used <= limit` precondition that `can_reserve` callers rely on.

**Both are disproved on the real code** (see the findings below).

## Commands and the lines that decide them

```
$ python3 -B smoke.py
4 smoke checks passed
rc=0
```
The smoke checks pass, but they test neither boundary, so they prove neither part of the safety fact.

Boundary check, comparing base with quota over every case with 0..12 values and used <= limit:
```
differing cases: 91 all at used+amount==limit: True
can_reserve(7,3,10): base True quota False
can_reserve(0,0,0):  base True quota False
```
Calling `restore` with each value:
```
restore(used=0, limit=10) -> returns 0
restore(used=10, limit=10) -> returns 10
restore(used=11, limit=10) -> returns 11
restore(used=1000000000, limit=10) -> returns 1000000000
restore(used=1, limit=0) -> returns 1
restore(used=-1, limit=10) -> ValueError(negative usage)
```
The bytecode of `restore` never loads `limit`:
`['snapshot', 'used', 'used', 0, 'ValueError', 'negative usage', 'used']`.

## Confirmed findings, ranked by the policy

### 1. BLOCKER: `can_reserve` no longer allows a reservation that reaches the limit exactly

- **Where:** `quota.py:2`. `<=` became `<`.
- **What the spec says:** "Preserve can_reserve's public behavior … allows a reservation up to and including the limit."
- **What happens:** every call where `used + amount == limit` now returns False instead of True. That is 91 of the cases in the sweep, and every differing case is one of these. For example, `can_reserve(7, 3, 10)` and `can_reserve(0, 0, 0)`.
- **What reaches it:** the function's intended case, called normally by existing callers. Under the policy that makes it a blocker.
- **How it got through:** smoke.py checks only 5/10 and 11/10, never 10/10.
- **Cheapest check that would catch it again:** `assert can_reserve(7, 3, 10)`.

### 2. SHOULD: `restore` accepts a snapshot whose usage is above the limit

- **Where:** `quota.py:5-9`. `limit` is never read, and only `used < 0` raises an error.
- **What the spec says:** restore must "accept 0 <= used <= limit and return used, or raise ValueError otherwise".
- **What happens:** `restore({"used": 11}, 10)` returns 11, as does any larger value. With `limit=0`, `used=1` is also accepted.
- **What reaches it:** imported data. `restore` is the new import boundary, and the spec says the range of `used` "has not been checked" before it arrives. Under the policy, imported data reaching an issue makes it a should. Because this is a trust boundary, it can never be ranked a nit.
- **Effect downstream:** the restored value breaks the caller precondition `used <= limit` that `can_reserve` relies on.
- **Cheapest check that would catch it again:** `restore({"used": 11}, 10)` raises ValueError. Also keep the accepted edges: `restore({"used": 10}, 10) == 10` and `restore({"used": 0}, 10) == 0`.

## The three unverified suggestions from SPEC.md

1. **Rename `used` to `consumed`. Not in scope; decline.** This is a nit, a wording change. It also renames a public keyword parameter, which would break any caller that passes `used=` by keyword, and the spec asks to preserve public behaviour. Under the policy, declining a nit starts no round.
2. **Add a defensive type check for a future parser that might supply strings. Not in scope; decline.** This is a nit: a guard against something only later code would cause. The spec says "No … additional parser exists here" and that snapshot `used` values are "schema-validated integers". If a parser is added later, that change should do its own checking.
3. **The import path may accept a snapshot whose usage exceeds the limit. Confirmed, and in scope.** This is finding 2 above, a should. It was reproduced with `restore({"used": 11}, 10)`, which returns 11.

## Not checked

- **The real callers of `can_reserve`.** None are supplied, so I judged the effect of finding 1 from the spec's contract, not from a call site.
- **Inputs the spec rules out.** I did not explore non-integer values, `bool`, a missing `"used"` key (which raises KeyError, not ValueError), a negative `limit`, or a negative `amount`. The spec guarantees each of these away, and none of them is a finding.
- **Persistence, network and concurrency.** The spec says none exist here.

## What should happen next under the policy

1. The author fixes both findings:
   - restore `<=` in `can_reserve`;
   - add the `used > limit` check that raises ValueError in `restore`.
2. Each fix gets the cheapest check that catches it again (listed under each finding above), added to the smoke checks. Then the author reruns `python3 smoke.py` and the boundary checks.
3. Decline suggestions 1 and 2. They are nits, and declining them starts no round.
4. A fresh verdict is needed, because the patch will change. Following carry-forward, "Anything else" applies: this is a small fix, so one read-only verifier from another provider, if one is available, is enough. That re-review covers the change since this verdict and what it affects, together with these two findings. A full review is not needed.
5. Delivery waits until that verdict passes every required check and the safety fact on the new revision, with no blocker or should open. This was round 1. If either finding is still open after round 2, the author must stop and rethink before going further.
