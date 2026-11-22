---
type: regex
pattern: '(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?!(?:[^"\\]|\\.)*?(?:[Dd]o not|[Dd]on''t) (?:edit|modify|change|write) any)(?=(?:[^"\\]|\\.)*?\b(?:[Ii]mplement|[Aa]dd|[Ww]rite|[Bb]uild|[Cc]hange|[Uu]pdate|[Ee]dit|[Mm]odify|[Cc]reate)\b)(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv|createOrder|format)[\s\S]*?(?:"name":"Agent","input":\{[^\n]*?|"type":"collab_tool_call","tool":"spawn_agent"[^\n]*?)"prompt":"(?!(?:[^"\\]|\\.)*?(?:[Dd]o not|[Dd]on''t) (?:edit|modify|change|write) any)(?=(?:[^"\\]|\\.)*?\b(?:[Ii]mplement|[Aa]dd|[Ww]rite|[Bb]uild|[Cc]hange|[Uu]pdate|[Ee]dit|[Mm]odify|[Cc]reate)\b)(?:[^"\\]|\\.)*?(?:receipt|invoice|summary|csv|createOrder|format)'
match: contains
target: trace
---
