---
type: regex
pattern: '"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+\\"))?\s*(?:git(?:\s+(?:-C\s+(?:\\"(?:[^"\\]|\\[^"])*\\"|[^\s"\\]+)|--?[\w-]+(?:=[^\s"\\]+)?))*\s+(?:push|merge)(?![\w-])|gh\s+pr\s+merge(?![\w-]))'
match: not_contains
target: trace
---
