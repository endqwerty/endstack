---
type: regex
pattern: '<h[1-3]\b[^>]*>\s*(?:<[^>]+>\s*)*(?:0[1-9]\b|\[\s*0[1-9]|(?:I|II|III|IV|V)\.\s)'
match: not_contains
target:
  source: file
  path: index.html
---
