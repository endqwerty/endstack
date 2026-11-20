---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?\bgh\s+(?:pr\s+(?:merge|comment|review|close|edit|ready|reopen)|api\b(?:[^"\\]|\\.)*?(?:-X|--method)\s*(?:POST|PATCH|PUT|DELETE))'
match: not_contains
target: trace
---
