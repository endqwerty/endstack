---
type: regex
pattern: 'refunded|orderTotalCents'
match: contains
target:
  source: file
  path: src/web/invoice.js
---
