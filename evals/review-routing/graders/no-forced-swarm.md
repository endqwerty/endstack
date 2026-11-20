---
type: regex
pattern: '(?:(?:"name":"Read","input":\{"file_path":"[^"]*skills/(?:swarm|\{[^}"]*(?<![\w-])swarm(?![\w-])[^}"]*\})/SKILL\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?skills/(?:swarm|\{[^}"]*(?<![\w-])swarm(?![\w-])[^}"]*\})/SKILL\.md)|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?(?<![\w-])swarm(?![\w-])[^;"]*;\s*do\b(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\()\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?(?:skills/)?["\\]*\$\{?\1\}?/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bcd\s+[^;&|"]*?skills/?(?:\\")?\s*(?:&&|;)(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?(?<![\w/-])(?:swarm|\{[^}"]*(?<![\w-])swarm(?![\w-])[^}"]*\})/SKILL\.md)'
match: not_contains
target: trace
---
