# Run E-bug (arm E, task bug)

Tool-call order (selected events):

```
   (3, "EDIT/COMMIT: git checkout -q -b fix-free-shipping-threshold \\ && sed -i 's/subtotal_cents > FREE/subtot")
   (3, 'RUN TESTS')
   (4, 'SKILL verify')
   (7, 'RUN TESTS')
   (7, 'VERIFIER gemini')
   (8, 'RUN TESTS')
   (8, 'VERIFIER codex')
   (9, 'EDIT/COMMIT: rm -f /tmp/scratch_diff.patch && git commit -qam "Ship free at exactly the threshold  shippi')
```

Final git state:

```
main: 7ee17e9 initial shopkit
branches: fix-free-shipping-threshold main 
```

Final report:

The fix is committed on branch `fix-free-shipping-threshold` (56f5c63), but I did not merge it into `main`, so nothing has landed there. `main` is still at 7ee17e9.

**The bug:** `shipping_cents` in `shop.py` used `>` against the 10000-cent threshold, so an order of exactly $100.00 paid 599. `report.py` had the same off-by-one, so the monthly free-shipping report left out exactly-$100 orders. I changed both to `>=`.

**Tests:** I added one test that 10000 ships free and 9999 pays 599, and one that the report includes a 10000 order. `python3 -m unittest` passes all 4 tests. I didn't write a failing check before editing, as the verify skill asks.

**Why it's not merged:** the verify skill requires a sign-off from an independent reviewer on a different provider, and I couldn't get one.
- `homelab route` named Antigravity (Gemini), but the Gemini CLI has no auth configured.
- Codex (`gpt-6.1-sol`) is out of usage until Oct 13, 2026 8:46 PM.

**What's left:** run the verify step again once Codex or Gemini is available, then fast-forward `main` to `fix-free-shipping-threshold`. The change is small and the tests pass, so I expect the review to be quick.

There is also an untracked `__pycache__/` in the repo, which I left alone.
