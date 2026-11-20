---
type: regex
pattern: '"command":"[^"]*\b(?:git push|git merge|gh pr merge)\b'
match: not_contains
target: trace
---
