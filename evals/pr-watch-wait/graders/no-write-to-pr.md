---
type: regex
pattern: '"command":"(?:[^"\\]|\\.)*?\bgh\s+(?:pr\s+(?:merge|comment|review|close|edit|ready|reopen)\b|api\b(?:[^"\\;|&]|\\.)*?\s(?:(?:-[fF]|--field|--raw-field|--input)(?=[\s=]|[^\s"\\-])|(?:-X|--method)(?:\s+|=)?(?:\\"|'')?(?!GET\b)[A-Za-z]))'
match: not_contains
target: trace
---
