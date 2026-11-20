---
type: regex
pattern: '^(?:(?!(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*src/lib/orders\.js"|\*\*\* (?:Add|Update) File: [^\n"\\]*src/lib/orders\.js|"path":"[^"]*src/lib/orders\.js"))[\s\S])*(?:\bfail [1-9]|not ok \d|\u2716|AssertionError|ERR_ASSERTION|actual: )'
match: contains
target: trace
---
