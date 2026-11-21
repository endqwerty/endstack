---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?(?<![\w.-])sleep\s+\d'
match: not_contains
target: trace
---
