---
type: regex
pattern: 'transition(?:-property)?\s*:\s*all\b|\btransition-all\b'
match: not_contains
target:
  source: file
  path: index.html
---
