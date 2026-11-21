---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?watch_pr\.py(?:[^"\\;|&]|\\.)*?--timeout(?:\s+|=)(?:\\"|'')?(?!(?:[1-9]\d*h|(?:[6-9]\d|[1-9]\d{2,})m)(?![\w.]))'
match: not_contains
target: trace
---
