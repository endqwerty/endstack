---
type: regex
pattern: '<img\b[^>]*\bsrc\s*=\s*["'']?https?:|url\(\s*["'']?https?://(?!fonts\.)'
match: not_contains
target:
  source: file
  path: index.html
flags: i
---
