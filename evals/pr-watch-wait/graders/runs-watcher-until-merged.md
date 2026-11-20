---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?watch_pr\.py(?:[^"\\]|\\.)*?--until(?:\s+|=)(?:\\"|'')?(?:[\w-]+,)*merged\b'
match: contains
target: trace
---
