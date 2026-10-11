# Run F-review (arm F, task review)

Tool-call order (selected events):

```
   (2, 'RUN TESTS')
```

Final git state:

```
main: f925960 initial shopkit
branches: change main 
```

Final report:

**The `change` branch is safe to merge.** I changed nothing.

- **Merge:** `change` is one commit (`04a43e0`) on top of `main` (`f925960`). It fast-forwards cleanly, which is what the project rules call for.
- **Scope:** The commit touches only `shop.py` and `test_shop.py`.
- **Tests:** I exported the branch to a scratch directory and ran `python3 -m unittest`. All 4 tests pass. `main` currently passes its 2.
- **Behavior change:** Free shipping now starts at exactly $100.00 (`>=` instead of `>`). The commit message and the new `test_exact` test both say this is intended.
- **New feature:** `shipping_cents` takes an optional `express=False` argument that adds $15.00. The old one-argument calls behave as before. The new test covers a $5.00 order with express, which comes to $20.99.
- **Express on free orders:** Express still costs $15.00 on an order that qualifies for free shipping. The docstring states this.
- **Other callers:** The repo has no other callers of `shipping_cents` to break.

I didn't run an independent verifier model. For a change this small I read the diff and ran the tests myself.
