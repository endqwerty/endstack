---
type: regex
pattern: '(?:"name":"Read","input":\{"file_path":"[^"]*skills/orchestrate/SKILL\.md"|(?:"command":"|"command":"(?:[^"\\]|\\.)*?(?:[;&|(]\s*|\\n\s*|-lc\s+(?:''|\\")|\bdo\s+|\bthen\s+))(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?(?:skills/|\$\{?\w+\}?/|(?<=[\s"''/]))(?:orchestrate|\{[^}"]*(?<![\w-])orchestrate(?![\w-])[^}"]*\})/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?(?<![\w-])orchestrate(?![\w-])[^;"]*;\s*do\b(?:(?:[^"\\]|\\.)*?(?:[;&|(]\s*|\\n\s*))?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?\$\{?\1\}?/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?skills/orchestrate/SKILL\.md[^;"]*;\s*do\b(?:(?:[^"\\]|\\.)*?(?:[;&|(]\s*|\\n\s*))?\s*(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?\$\{?\2\}?(?![\w/]))'
match: not_contains
target: trace
---
