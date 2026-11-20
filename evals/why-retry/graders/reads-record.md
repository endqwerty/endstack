---
type: regex
pattern: '(?:"name":"Read","input":\{"file_path":"[^"]*retry-record\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?retry-record\.md)'
match: contains
target: trace
---
