---
type: regex
pattern: 'orderTotalCents\(|[\w)\]]\??\.refunded\b'
match: contains
target:
  source: file
  path: src/web/invoice.js
---
