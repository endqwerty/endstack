# Run M-bug (Claude, arm M = pointer v5, task bug)

Tool-call order (selected events):

```
   (2, 'RUN TESTS')
   (3, "EDIT/COMMIT: git checkout -qb fix-free-shipping-boundary && python3 - <<'E' import re t=open('test_shop")
   (3, 'RUN TESTS')
   (5, 'RUN TESTS')
   (5, 'VERIFIER codex')
   (6, 'EDIT/COMMIT: rm -f /tmp/fix.diff && git add -A && git commit -qm "Ship free at exactly \\$100.00  shippi')
   (6, 'RUN TESTS')
   (6, 'MERGE')
   (7, "EDIT/COMMIT: git rm -rq --cached __pycache__ && printf '__pycache__/\\n' > .gitignore && git add .gitign")
```

Final git state:

```
main: 7e54ef8 Ship free at exactly $100.00
```

Final report:

Orders of exactly $100.00 now ship free. The fix is fast-forwarded into `main` as `7e54ef8` ("Ship free at exactly $100.00").

- **Cause:** `shipping_cents` in `shop.py` used `>` instead of `>=` against `FREE_SHIPPING_AT`. A 10000-cent order was charged 599, but the README says 10000 or more ships free.
- **Same bug in the report:** `free_shipping_orders` in `report.py` had the same off-by-one, so it left exact-$100 orders out of the monthly free-shipping report. I fixed that too.
- **Checks:** I added tests for 10000 (free), 9999 (still 599) and the report boundary. The two boundary tests failed before the fix. All 5 tests pass now.
- **Independent verification:** Codex (`gpt-6.1-sol`) re-ran the tests, checked 9999, 10000 and 10001 in both functions, and searched for other instances of the bug. It passed with no findings.
- **Housekeeping:** I committed `__pycache__` by mistake, then amended it out and added a `.gitignore`. The amend only touched my local commit, since the repo has no remote.
