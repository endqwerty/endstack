---
type: regex
pattern: '(?:(?:"name":"Read","input":\{"file_path":"[^"]*skills/(?:formal-verification|\{[^}"]*(?<![\w-])formal-verification(?![\w-])[^}"]*\})/SKILL\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&#]|\\(?!n)[\s\S])*?skills/(?:formal-verification|\{[^}"]*(?<![\w-])formal-verification(?![\w-])[^}"]*\})/SKILL\.md)|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?(?<![\w-])formal-verification(?![\w-])[^;"]*;\s*do\b(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&#]|\\(?!n)[\s\S])*?(?:skills/)?["\\]*\$\{?\1\}?/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bcd\s+[^;&|"]*?skills/?(?:\\")?\s*(?:&&|;)(?:(?:[^"\\]|\\.)*?(?:[;&|(]|\\n|-lc\s+(?:\''|\\")|\bdo\b|\bthen\b|\$\())?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\b(?:[^"\\;|&#]|\\(?!n)[\s\S])*?(?<![\w/-])(?:formal-verification|\{[^}"]*(?<![\w-])formal-verification(?![\w-])[^}"]*\})/SKILL\.md)'
match: contains
target: trace
---
