---
type: regex
pattern: '^(?![\s\S]*!\s*t\.done\s*&&\s*!\s*t\.deletedAt\s*\))[\s\S]*?(?:\bimport\s+(?!type\b)(?:[\w$]+\s*(?:,\s*)?)?(?:\*\s*as\s+[\w$]+|\{\s*(?:type\s+[\w$]+\s*,\s*)*(?!type\s)[\w$]+[^}]*\})?\s*from\s*["\'']\.\./shared/|\brequire\(\s*["\'']\.\./shared/|\??\.(?:archived|archivedAt|isArchived|lifecycle)\b|\.(?:status|state)\s*[!=]==?\s*["\'']archived["\''])'
match: contains
target:
  source: file
  path: cli/list.ts
---
