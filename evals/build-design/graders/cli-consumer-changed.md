---
type: regex
pattern: 'archiv|lifecycle|\bimport\s*\{[^}]*\}\s*from\s*["\'']\.\./shared/'
match: contains
target:
  source: file
  path: cli/list.ts
flags: i
---
