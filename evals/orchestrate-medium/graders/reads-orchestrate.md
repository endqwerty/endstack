---
type: regex
pattern: '(?:"name":"Read","input":\{"file_path":"[^"]*skills/orchestrate/SKILL\.md"|(?:"command":"|"command":"(?:[^"\\]|\\.)*?(?:[;&|(]\s*|\\n\s*|-lc\s+(?:''|\\")|\bdo\s+|\bthen\s+))(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?(?:skills/|\$\{?\w+\}?/|(?<=[\s"''/]))(?:orchestrate|\{[^}"]*(?<![\w-])orchestrate(?![\w-])[^}"]*\})/SKILL\.md|"command":"(?:[^"\\]|\\.)*?\bfor\s+(\w+)\s+in\s+[^;"]*?(?<![\w-])orchestrate(?![\w-])[^;"]*;\s*do\s+(?:sudo\s+)?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?\$\{?\1\}?/SKILL\.md)'
match: contains
target: trace
---
