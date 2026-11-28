---
type: regex
pattern: 'class="[^"]*\b(?:eyebrow|kicker|overline)\b'
match: not_contains
target:
  source: file
  path: index.html
flags: i
---
