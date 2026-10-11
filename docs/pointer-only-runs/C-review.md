# Run C-review (arm C, task review)

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

**It is safe to merge.** I haven't changed anything.

- **Fast-forward:** `change` is one commit (`e106d98`) directly on top of `main` (`010e140`), so `main` can fast-forward to it.
- **Tests:** `python3 -m unittest` passes, 4 of 4. I ran it in a temporary checkout of `change` and removed the checkout afterwards. `git status` is clean.
- **What changed:** the diff touches only `shop.py` and `test_shop.py`.
  - **Free shipping:** the threshold moves from `> $100.00` to `>= $100.00`, so an order of exactly $100.00 now ships free. This is the intended change, and a new test covers it.
  - **Express:** a new `express=False` parameter adds a flat $15.00. The surcharge applies even on free-shipping orders, which the docstring says and a test checks.
- **Callers:** nothing else in the repo calls `shipping_cents`, and the new parameter defaults to the old behavior, so no existing code breaks.

The tests don't cover express on an order above the free-shipping threshold (the result should be 1500). The code handles it correctly, so this is a minor gap.
