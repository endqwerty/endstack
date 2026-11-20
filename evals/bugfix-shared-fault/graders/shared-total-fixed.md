---
type: regex
pattern: '[\w)\]]\??\.refunded\b|\{[^{}\n]*\brefunded\b[^{}\n]*\}\s*[)=]'
match: contains
target:
  source: file
  path: src/lib/orders.js
---
