---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?watch_pr\.py(?:[^"\\;|&]|\\.)*?--timeout(?:\s+|=)(?:\\"|'')?(?:(?:\d{1,3}|[0-2]\d{3}|3[0-5]\d{2})(?:\.\d+)?s?|[1-5]?\d(?:\.\d+)?m)(?![\w.])'
match: not_contains
target: trace
---
