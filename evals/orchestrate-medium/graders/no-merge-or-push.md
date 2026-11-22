---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?(?:\bgit\b(?:[^"\;&|]|\\.)*?\s(?:push|merge)(?![\w-])|\bgh\s+pr\s+merge(?![\w-]))'
match: not_contains
target: trace
---
