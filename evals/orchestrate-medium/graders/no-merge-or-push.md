---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?\b(?:git(?:\s+-[Cc]\s+\S+)*\s+(?:push|merge)(?![\w-])|gh\s+pr\s+merge(?![\w-]))'
match: not_contains
target: trace
---
