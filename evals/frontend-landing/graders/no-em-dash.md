---
type: regex
pattern: '—|&mdash;|&#8212;|&#x2014;'
match: not_contains
target:
  source: file
  path: index.html
flags: i
---
