---
type: regex
pattern: '(?:"file_path":"[^"]*skills/(?:how|why)/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/(?:how|why)/SKILL\.md|\bfor \w+ in [^;\n]*\b(?:how|why)\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\b(?:how|why)\b[^}\n]*\}/SKILL\.md)'
match: not_contains
target: trace
---
