---
type: regex
pattern: '"name":"Read","input":\{"file_path":"[^"]*gemini-frontend-design/SKILL\.md"|"name":"Skill","input":\{"skill":"[^"]*gemini-frontend-design|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?gemini-frontend-design/SKILL\.md'
match: contains
target: trace
---
