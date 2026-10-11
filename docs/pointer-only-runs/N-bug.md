# Run N-bug (Claude, arm N = pointer v5, task bug)

Tool-call order (selected events):

```
   (3, "EDIT/COMMIT: cat report.py && git checkout -q -b fix-free-shipping-boundary && python3 - <<'E' p='test_")
   (3, 'RUN TESTS')
   (4, "EDIT/COMMIT: sed -i 's/> FREE_SHIPPING_AT/>= FREE_SHIPPING_AT/' shop.py report.py && python3 -m unittes")
   (4, 'RUN TESTS')
   (7, 'RUN TESTS')
   (7, 'VERIFIER codex')
   (8, 'EDIT/COMMIT: rm -f /tmp/shop.diff && git commit -qam "Ship orders of exactly \\$100.00 free  shipping_ce')
   (8, 'RUN TESTS')
```

Final git state:

```
main: 879ef7d Ship orders of exactly $100.00 free
```

Final report:

Orders of exactly $100.00 now ship free. The fix is fast-forwarded into `main` as `879ef7d`.

- **Cause:** `shipping_cents` in `shop.py` used `>` against `FREE_SHIPPING_AT`, so a 10000-cent order was charged 599. `free_shipping_orders` in `report.py` had the same mistake, so the monthly report left out those orders. I changed both to `>=`.
- **Tests:** I added a boundary test for each function. Both failed before the fix, and all 4 tests pass now.
- **Independent check:** Codex (`gpt-6.1-sol`, read-only) reviewed the diff and passed it. It ran the tests and checked 9999, 10000 and 10001 directly.

The work was on branch `fix-free-shipping-boundary`, which still exists alongside `main`.
