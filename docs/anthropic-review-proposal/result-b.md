# Review b: quota.py — verdict ISSUES

Policy: `policy.md` (verify, Verifier role) and `references/review-rubric.md`.
I changed no input file. Running `smoke.py` created `b/__pycache__/quota.cpython-315.pyc`.
I deleted it, then hashed all eight inputs again. The hashes were unchanged.

## What I judged

There is no commit history, so this table identifies each input by its SHA256.

| File | SHA256 |
|---|---|
| quota.py (head) | d2feb59975c7487f6574146f69e183de2698946ddc0a94bf681058290828fd88 |
| base.py (base) | 82f18c5d905f6e9aaa387f6624e4058d3a16d32e819a91233de95aabccbad019 |
| change.diff (patch) | e8dac6a8dc6520d126f409926ced1e7c1f67f4788efec4557e2aedc561144e76 |
| SPEC.md | b0aeb337b1987a5be00281dd6c85b0dbfe2c48c6c37509db59900f28d7dc32be |
| policy.md | 588eda8a23160dedfb49777a8c29998487da644c9e051184de723b470e25b9b4 |
| references/review-rubric.md | bb8b479240091cd55b3d916514eef892684e62e5d27427ab78ee4dda4ce97e2d |
| references/carry-forward.md | fdf8affa94d804a2262ba60ed098211f3e030884c5d975b6613f72ace0c78387 |
| smoke.py | c6c9f2261611926ef028f6b0c253cfcb1cca18af277556385c9781a372ec0d37 |

`change.diff` is identical to `diff -u base.py quota.py` once the file headers are removed. I compared them and got: "change.diff body == diff base.py quota.py".

## Commands and the output that decides each check

1. `cd b && python3 smoke.py` (Python 3.15.1) prints `4 smoke checks passed`, rc=0. **PASS.**
   It passes because none of the four checks tests a limit boundary or `used > limit`.
2. A probe script loaded base.py and quota.py by file path and called both functions:
   ```
   can_reserve (7, 3, 10) base= True head= False
   can_reserve (0, 0, 0) base= True head= False
   can_reserve (10, 0, 10) base= True head= False
   can_reserve (0, 10, 10) base= True head= False
   can_reserve (8, 3, 10) base= False head= False
   can_reserve (2, 3, 10) base= True head= True
   restore used=0 limit=10 -> 0
   restore used=10 limit=10 -> 10
   restore used=11 limit=10 -> 11
   restore used=1 limit=0 -> 1
   restore used=-1 limit=10 -> ValueError(negative usage)
   restore used=0 limit=0 -> 0
   ```

## The facts the change's safety rests on

- **S1. `can_reserve` still allows `used + amount == limit`.** **Disproved** (finding F1).
- **S2. `restore` raises for every imported `used` outside `0..limit`.** **Disproved** (finding F2).

## Confirmed findings, ranked

### F1. Blocker: `can_reserve` now rejects a reservation that exactly reaches the limit

- **Where:** `quota.py:2`, which the diff changed from `<=` to `<`.
- **Trigger:** any call where `used + amount == limit`, for example `can_reserve(7, 3, 10)`.
- **Expected:** `True`. SPEC.md says the reservation is allowed "up to and including the limit", and the change must preserve public behaviour. Base returns `True`.
- **Actual:** `False` (probe output above). With `limit=0`, even `can_reserve(0, 0, 0)` returns `False`.
- **Rank:** Blocker, because the intended case is wrong. Existing callers that use ordinary values reach it. This is a regression the change introduced, not a defect in base.
- **Cheapest check that catches it again:** `assert can_reserve(7, 3, 10)`.

### F2. Blocker: `restore` accepts a snapshot whose usage is above the limit

- **Where:** `quota.py:5-9`. `limit` is accepted but never read. The only guard is `used < 0`.
- **Trigger:** `restore({"used": 11}, 10)`, or `restore({"used": 1}, 0)`.
- **Expected:** `ValueError`. SPEC.md says: "Accept 0 <= used <= limit and return used, or raise ValueError otherwise."
- **Actual:** the call returns `11` or `1` (probe output above).
- **Rank:** Blocker, because half of the stated `restore` contract is missing. If this were judged only by what reaches it, it would still be at least a should: imported data reaches it at a new import boundary whose range SPEC.md says "has not been checked". It is a trust-boundary and data-integrity defect, so it can never be a nit.
- **Downstream effect:** if the restored value goes back into `can_reserve` as `used`, it breaks that function's documented precondition `used <= limit`.
- **Cheapest checks that catch it again:**
  - `restore({"used": 11}, 10)` raises `ValueError`;
  - `restore({"used": 10}, 10) == 10`, to keep the inclusive upper bound.

## Triage of the three unverified suggestions in SPEC.md

1. **"Rename used to consumed for clarity."** No fix. This is naming and style, which the rubric says to skip. `can_reserve` is public, so renaming its parameter would also risk breaking callers that pass `used` by keyword.
2. **"Add a defensive type check for a future parser that might supply strings."** No fix. It guards against hypothetical future code. SPEC.md says "No ... additional parser exists here", and the snapshot values are already schema-validated integers. The rubric says to skip guards for hypothetical future code.
3. **"The import path may accept a snapshot whose usage exceeds the limit."** **Confirmed, in scope.** I reproduced it and it is finding F2. It needs a fix.

## Other candidates I looked at and did not report

- **A missing `"used"` key raises `KeyError`.** Not reported. The snapshot is schema-validated, so this path has no current trigger.
- **`bool` values, and an unvalidated `limit` in `restore`.** Not reported. SPEC.md says `limit` is a nonnegative integer and the snapshot values are integers. Breaking either takes contrived input, which makes it at most a nit, and I found no current path that reaches it.
- **Persistence, network and concurrency.** SPEC.md says none exist, so I found nothing to trace.

## Not checked

- Real callers of `can_reserve` and `restore`. None were supplied, so I checked the contract only against SPEC.md and these probes.
- The schema validation that SPEC.md says happens upstream of `restore`. I relied on its stated guarantee (integers, key present) and did not inspect it.
- Any Python version other than 3.15.1.

## Verdict: ISSUES

The required smoke check passes. Both safety facts are disproved, and two blockers are open: F1 and F2.

## What should happen next under the policy

- **Author fixes.** The author fixes F1 and F2 and adds the cheapest check for each:
  - the boundary assert for `can_reserve`;
  - the two `restore` asserts, one for over-limit and one for the inclusive limit.

  Then the author reruns `smoke.py`. The author declines suggestions 1 and 2 without making edits or starting another round for them.
- **Re-review.** Under carry-forward ("Anything else"), the fixed revision needs a fresh verdict. One verifier is enough for a small fix like this. It should be scoped to the change since this verdict and what that change affects (`can_reserve` and `restore`), with F1 and F2 given as the open findings. Adding more reviewers to look for extra findings is not warranted.
- **Round count.** This is round 1, so the round cap does not apply yet. Delivery waits until an independent pass on the fixed revision covers every required check and both safety facts.
