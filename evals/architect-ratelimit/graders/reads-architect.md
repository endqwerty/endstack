---
type: regex
pattern: '(?:"file_path":"[^"]*skills/architect/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/architect/SKILL\.md|\bfor \w+ in [^;\n]*\barchitect\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\barchitect\b[^}\n]*\}/SKILL\.md)'
match: contains
target: trace
---
