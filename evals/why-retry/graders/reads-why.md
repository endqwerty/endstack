---
type: regex
pattern: '(?:"file_path":"[^"]*skills/why/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/why/SKILL\.md|\bfor \w+ in [^;\n]*\bwhy\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\bwhy\b[^}\n]*\}/SKILL\.md)'
match: contains
target: trace
---
