---
type: regex
pattern: '^(?:[^"\''`/\n]|"(?:[^"\\\n]|\\.)*"|\''(?:[^\''\\\n]|\\.)*\''|`(?:[^`\\]|\\.)*`|/(?![/*]))*?(?://(?!\s*(?:eslint-|prettier-ignore|@ts-(?:expect-error|ignore|nocheck)|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b)| Refunded lines sometimes pushed totals past what was charged; cap at charged amount\.[ \t]*$)|/\*(?!\s*(?:eslint-|prettier-ignore|@ts-(?:expect-error|ignore|nocheck)|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b)|!|\*(?:[^*]|\*(?!/))*\*/[ \t]*\n[ \t]*export\b))'
match: not_contains
target:
  source: file
  path: src/cli/receipt.js
flags: m
---
