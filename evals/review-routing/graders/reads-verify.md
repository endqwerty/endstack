---
type: regex
pattern: '(?:"file_path":"[^"]*skills/verify/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/verify/SKILL\.md|\bfor \w+ in [^;\n]*\bverify\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\bverify\b[^}\n]*\}/SKILL\.md)'
match: contains
target: trace
---
