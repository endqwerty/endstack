---
type: regex
pattern: '(?:(?:"name":"Read","input":\{"file_path":"[^"]*skills/(?:unslop|\{[^}"]*(?<![\w-])unslop(?![\w-])[^}"]*\})/SKILL\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?skills/(?:unslop|\{[^}"]*(?<![\w-])unslop(?![\w-])[^}"]*\})/SKILL\.md)|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?(?<![\w-])unslop(?![\w-])[^;"]*;\s*do\b(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\()\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?(?:skills/)?["\\]*\$\{?\1\}?/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bcd\s+[^;&|"]*?skills/?(?:\\")?\s*(?:&&|;)(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?(?<![\w/-])(?:unslop|\{[^}"]*(?<![\w-])unslop(?![\w-])[^}"]*\})/SKILL\.md)'
match: contains
target: trace
---
