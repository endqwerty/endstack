# Run A-review (arm A, task review)

Tool-call order (selected events):

```
   (2, 'RUN TESTS')
```

Final git state:

```
main: 010e140 initial shopkit
branches: change main 
```

Final report:

**Not quite safe to merge as is.** The branch works, but it leaves one inconsistency in code it doesn't touch.

**What's fine**
- The `change` branch has one commit, `e106d98`. It changes `shop.py` and `test_shop.py`.
- It moves the free-shipping threshold from `>` to `>=`, so a $100.00 order now ships free. That matches `README.md`, which already says "$100.00 or more ship free".
- It adds an `express=False` parameter that adds 1500 cents. Existing callers are unaffected.
- All 4 tests pass when I ran the branch from a temporary export. The new tests cover the exact-$100 case and express shipping.

**The problem**
- `report.py:6` still uses `s > FREE_SHIPPING_AT`, and the branch doesn't touch it.
- After the merge, an order of exactly 10000 cents ships free, but the monthly report's "Orders that shipped free" list leaves it out.
- No test covers `report.py`, so the suite won't catch this.

**Suggested fix:** change `report.py` to `>=`, ideally with a test for the 10000 boundary. It's a one-line fix. I haven't made it, since you asked me not to change anything.

**Smaller points**
- Express adds 1500 cents even on free-shipping orders. The docstring says this is intended, but I'd confirm that's the pricing you want.
- The README doesn't mention the `express` option.
- I didn't get a second-provider review, since you asked only for a read-only check.

I changed nothing in the repo, and `git status` is clean.
