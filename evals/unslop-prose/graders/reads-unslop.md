---
type: regex
pattern: '(?:"file_path":"[^"]*skills/unslop/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/unslop/SKILL\.md|\bfor \w+ in [^;\n]*\bunslop\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\bunslop\b[^}\n]*\}/SKILL\.md)'
match: contains
target: trace
---
