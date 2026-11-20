---
type: regex
pattern: '^(?:[^"\''`/\n]|"(?:[^"\\\n]|\\.)*"|\''(?:[^\''\\\n]|\\.)*\''|`(?:[^`\\]|\\.)*`|/(?![/*]))*?(?://(?!\s*(?:eslint-|prettier-ignore|@ts-(?:expect-error|ignore|nocheck|check)|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b)| Refunded lines sometimes pushed totals past what was charged; cap at charged amount\.[ \t]*$)|/\*(?!\s*(?:eslint-|prettier-ignore|@ts-(?:expect-error|ignore|nocheck|check)|istanbul ignore|c8 ignore|Copyright\b|SPDX-License-Identifier|@license\b)|!|\*(?:[^*]|\*(?!/))*\*/[ \t]*\n[ \t]*(?:export\b|(?:(?:public|private|protected|static|async|readonly|override|abstract|declare|get|set)\s+)*(?!(?:if|for|while|switch|catch|return|function|await|new|typeof|delete|void|throw|else|do|try|const|let|var)\b)[\w$#]+\s*(?:<[^>\n]*>)?\s*\([^\n]*\)\s*(?::[^\n{]*)?\{[ \t]*$|(?:(?:public|private|protected|static|async|readonly|override|abstract|declare|get|set)\s+)+[\w$#]+[^\n]*;[ \t]*$|(?:readonly\s+)?(?!(?:if|for|while|switch|catch|return|function|await|new|typeof|delete|void|throw|else|do|try|const|let|var)\b)[\w$]+\??\s*:\s*[^\n;,]+;?[ \t]*$)))'
match: not_contains
target:
  source: file
  path: src/cli/receipt.js
flags: m
---
