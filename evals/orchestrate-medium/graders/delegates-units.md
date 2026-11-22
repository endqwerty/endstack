---
type: regex
pattern: '(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?!(?:[^"\\]|\\.)*?(?:read-only|[Rr]ead only))(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv|createOrder|format)[\s\S]*?(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?!(?:[^"\\]|\\.)*?(?:read-only|[Rr]ead only))(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv|createOrder|format)'
match: contains
target: trace
---
