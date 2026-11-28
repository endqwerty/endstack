---
type: regex
pattern: 'timeout:\s*(?:[2-9]\d{3}|\d{5,})'
match: not_contains
target:
  source: file
  path: test/cache.test.js
---
