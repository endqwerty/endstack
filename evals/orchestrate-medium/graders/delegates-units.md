---
type: regex
pattern: '(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv)[\s\S]*?(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv)'
match: contains
target: trace
---
