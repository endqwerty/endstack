---
type: regex
pattern: '(?:"name":"Read","input":\{"file_path":"[^"]*skills/test-design/references/property-and-model-testing\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?(?:skills/test-design/)?references/property-and-model-testing\.md)'
match: contains
target: trace
---
