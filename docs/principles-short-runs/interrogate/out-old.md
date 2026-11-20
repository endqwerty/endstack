# Interrogate: feature vs master (fx-old)

Note: no separate workers were available. I played Reviewer A (correctness/rubric), Reviewer B (code-quality lens) and the lead myself, in sequence. This is not an independent panel, and all reviewers share one model family, so the diversity signal is absent.

### Intent
> Add input validation to `page()` so it raises ValueError when page_no < 1 or size < 1 (per the new docstring), and add `page_count(n_items, size)` returning the number of pages needed for n_items. Source: commit message "Validate page size and add page_count", the diff, and the docstrings.

### Reviewers
- Reviewer A (correctness/rubric, me, same model family as lead): 4 findings
- Reviewer B (code-quality lens, me, same model family): 2 findings (1 overlapping with A)
- Neither is independent of the other. Agreement between them is not evidence.

### Act On
1. `page_count` rounds down (A). Reproduced: `page_count(25,10)` returns 2 (should be 3), `page_count(5,10)` returns 0 (should be 1). Only exact multiples are right (`page_count(10,10)` = 1). It needs ceiling division: `-(-n_items // size)`. It also has no `size < 1` check: `page_count(5,0)` raises ZeroDivisionError, while `page()` raises ValueError for the same input. This is new code in the diff and wrong for most inputs.
2. `page_no < 1` is documented but not enforced (A, B). The docstring says it raises ValueError on page_no < 1. Reproduced: `page(range(25), 0, 10)` returns the first 10 items with no error, and `page_no=-1` returns `[]`. The contract this change introduces is therefore false, and only the size half is implemented.
3. `page()` is 1-based by its docstring but `start = page_no * size` is 0-based (A). Reproduced: `page(list(range(25)),1,10)` returns items 10..19, the second page. Page 1 is skipped and the real first page is only reachable with page_no=0. The line predates the diff, but the diff edits this docstring and function and adds the page_no >= 1 promise. Fixing item 2 without fixing this would make page_no=0 an error while page 1 still returns the wrong page, so the first page would be unreachable. Fix: `start = (page_no - 1) * size`.
   Evidence it is real: the docstring on master already said "(1-based)". It is pre-existing but must be fixed in the same change.

### Consider
- No tests were added for the new behaviour (A). `test_pager.py` has one test (length of page 2 == 10), which passes and cannot catch items 1-3. It is run with plain python3 here, since pytest is absent. Tests for the ValueError cases, page contents and `page_count` (25 -> 3, 0 -> 0, 5 -> 1) would have caught every Act On item. I put this under Consider because it is a verification gap rather than a defect, but it should go in with the fixes.

### Noted
- Bool or non-int inputs (for example float size) are not validated (A). There is no evidence any caller passes them.
- Whether `page_count(0)` should return 0 is an open spec question. Ceiling division gives 0, which is reasonable.

### Dismissed
- B: "extract a shared validation helper for size, used by both functions". This is premature abstraction for a one-line check in two places. Once `page_count` guards size inline, the duplication is trivial.
- B: "file-size or spaghetti concerns". The file is 11 lines, so no threshold applies.
- A: "page() with an empty list or a page past the end returns []". This is standard slice behaviour, and the intent does not say it should raise.

### Agreement Map
A and B agreed on item 2 only, and they are the same model, so this is weak corroboration. Items 1 and 3 were raised by A alone, but each has a reproduced trace in this review and does not rely on agreement. B's remaining finding was dismissed as a preference. Pattern: the diff is small and its defects are all about the new contract not matching the implementation. The docstring promises more than the code delivers, and the unchanged test cannot see it. Verdict: do not merge as is. Fix items 1-3 and add tests.
