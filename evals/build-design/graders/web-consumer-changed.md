---
type: regex
pattern: 'archiv|lifecycle|\bimport\s*\{[^}]*\}\s*from\s*["\'']\.\./shared/'
match: contains
target:
  source: file
  path: web/taskList.ts
flags: i
---
