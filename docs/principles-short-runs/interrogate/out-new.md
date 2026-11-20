# Interrogate: branch `feature` vs `master` (fx-new)

Note: no separate workers, so I played three adversaries in sequence in copies (adv1 = page, adv2 = page_count, adv3 = edge/type probes). The findings are not independent.

## Intent
Make `page` a real 1-based pager that rejects page_no < 1 and size < 1 with ValueError, as its new docstring says. Add `page_count(n_items, size)` returning the number of pages needed to hold n_items.

## Findings (verified by rerunning in fx-new)

1. `page` is still 0-based and does not validate page_no (found by adv1)
   - Command: `python3 -c "from pager import page; L=list(range(25)); print(page(L,1)[:3], page(L,0)[:3]); print(page(L,-1))"`
   - Output: `[10, 11, 12] [0, 1, 2]` then `[]`. No ValueError for page_no 0 or -1.
   - Required: `page(L,1)` starts at 0, and `page(L,0)` and `page(L,-1)` raise ValueError. The code has `start = page_no * size` (should be `(page_no - 1) * size`) and no page_no check. Only the size check was added, so the docstring is wrong.

2. `page_count` rounds down (found by adv2)
   - Command: `python3 -c "from pager import page_count as c; print(c(25,10), c(5,10), c(0,10))"`
   - Output: `2 0 0`
   - Required: `3 1 0`. 25 items need 3 pages and 5 items need 1. Floor division `//` drops the partial last page (needs ceiling).

## Dropped
- adv1: 0 dropped.
- adv2: 1 dropped. `page_count(5, 0)` raises ZeroDivisionError, not ValueError. It is real, but the intent only specifies validation for `page`, so it does not clearly break the intent.
- adv3: 2 dropped. `page(L, 'a')` raises TypeError, and `page([], 1)` returns `[]`. Both are expected behavior. `page(..., size=0)` correctly raises ValueError, so the size validation works.

Also noted: the only test (`test_pager.py::test_size`) passes on either indexing and has no coverage for page_no, page_count or ValueError.
