---
type: regex
pattern: '(?:"file_path":"[^"]*skills/ship/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/ship/SKILL\.md|\bfor \w+ in [^;\n]*\bship\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\bship\b[^}\n]*\}/SKILL\.md)'
match: contains
target: trace
---
