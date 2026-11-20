---
type: regex
pattern: 'Returns the order total in cents\. Throws if any order is negative\.'
match: contains
target:
  source: file
  path: src/app.ts
---
