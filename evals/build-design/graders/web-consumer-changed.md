---
type: regex
pattern: '^(?![ \t]*(?://|/\*|\*))(?:(?!//)[^\n])*?(?:\bimport\s+(?!type\b)(?:[\w$]+\s*(?:,\s*)?)?(?:\*\s*as\s+[\w$]+|\{\s*(?:type\s+[\w$]+\s*,\s*)*(?!type\s)[\w$]+[^}]*\})?\s*from\s*["\'']\.\./shared/|\brequire\(\s*["\'']\.\./shared/|\??\.(?:archived|archivedAt|isArchived|lifecycle)\b|\.(?:status|state)\s*[!=]==?\s*["\'']archived["\''])'
match: contains
target:
  source: file
  path: web/taskList.ts
flags: m
---
