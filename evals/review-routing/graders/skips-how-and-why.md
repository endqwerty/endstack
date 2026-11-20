---
type: regex
pattern: '(?:"file_path":"[^"]*skills/(?:how|why)/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/(?:how|why)/SKILL\.md)'
match: not_contains
target: trace
---
