---
type: regex
pattern: '(?:"file_path":"[^"]*skills/swarm/SKILL\.md"|\b(?:cat|sed|head|nl|less|awk|bat)\b[^"\n]*skills/swarm/SKILL\.md)'
match: not_contains
target: trace
---
