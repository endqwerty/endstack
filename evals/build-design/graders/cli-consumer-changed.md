---
type: regex
pattern: '!t\.done && !t\.deletedAt\)'
match: not_contains
target:
  source: file
  path: cli/list.ts
---
