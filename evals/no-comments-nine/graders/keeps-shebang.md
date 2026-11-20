---
type: regex
pattern: '^#!/usr/bin/env node'
match: contains
target:
  source: file
  path: src/app.ts
---
