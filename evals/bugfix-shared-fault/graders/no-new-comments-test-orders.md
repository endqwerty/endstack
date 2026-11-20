---
type: regex
pattern: '^(?:[^"\''`/\n]|"(?:[^"\\\n]|\\.)*"|\''(?:[^\''\\\n]|\\.)*\''|`(?:[^`\\]|\\.)*`|/(?![/*]))*?(?://(?!\s*(?:eslint-|prettier-ignore|@ts-check\b|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b))|/\*(?!\s*(?:eslint-|prettier-ignore|@ts-check\b|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b)|!|\*(?:(?!@ts-(?:ignore|expect-error|nocheck)\b)(?:[^*]|\*(?!/)))*\*/[ \t]*\n[ \t]*(?:export\b|(?:(?:public|private|protected|static|async|readonly|override|abstract|declare|get|set)\s+)*(?!(?:if|for|while|switch|catch|return|function|await|new|typeof|delete|void|throw|else|do|try|const|let|var)\b)[\w$#]+\s*(?:<[^>\n]*>)?\s*\((?:[^;{}]|\{[^{}]*\})*?\)\s*(?::[^\n{;]*)?\{[ \t]*$|(?:(?:public|private|protected|static|async|readonly|override|abstract|declare|get|set)\s+)+[\w$#]+[^\n]*;[ \t]*$|(?:readonly\s+)?(?!(?:if|for|while|switch|catch|return|function|await|new|typeof|delete|void|throw|else|do|try|const|let|var)\b)[\w$]+\??\s*:\s*[^\n;,]+;?[ \t]*$)))'
match: not_contains
target:
  source: file
  path: test/orders.test.js
flags: m
---
