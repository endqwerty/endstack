def page(items, page_no, size=10):
    """Return page `page_no` (1-based) of `items`. Raise ValueError on page_no < 1 or size < 1."""
    if size < 1:
        raise ValueError("size must be >= 1")
    start = page_no * size
    return items[start:start + size]


def page_count(n_items, size=10):
    """Number of pages needed for n_items."""
    return n_items // size
