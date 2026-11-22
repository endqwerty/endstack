---
type: regex
pattern: '(?:"name":"Read","input":\{"file_path":"[^"]*skills/orchestrate/SKILL\.md"|"command":"(?:(?:[^"\\]|\\.)*?(?:[\s;&|(]|\\n|\\"))?(?:cat|sed|head|tail|nl|less|more|awk|bat)\s(?:[^"\\;|&]|\\")*?(?:skills/|\$\{?\w+\}?/|(?<=[\s"]))(?:orchestrate|\{[^}"]*(?<![\w-])orchestrate(?![\w-])[^}"]*\})/SKILL\.md)'
match: not_contains
target: trace
---
