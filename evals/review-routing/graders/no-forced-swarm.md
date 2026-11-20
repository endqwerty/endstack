---
type: regex
pattern: '(?:"file_path":"[^"]*skills/swarm/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/swarm/SKILL\.md|\bfor \w+ in [^;\n]*\bswarm\b[^;\n]*;\s*do\b[^\n]*skills/\$\{?\w+\}?/SKILL\.md|skills/\{[^}\n]*\bswarm\b[^}\n]*\}/SKILL\.md)'
match: not_contains
target: trace
---
