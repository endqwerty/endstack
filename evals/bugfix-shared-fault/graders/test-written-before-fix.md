---
type: regex
pattern: '^(?:(?!(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*src/lib/orders\.js"|\*\*\* (?:Add|Update) File: [^\n"\\]*src/lib/orders\.js|"path":"[^"]*src/lib/orders\.js"))[\s\S])*(?:(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*(?<![\w.-])test/[^"\n]*\.test\.js"|\*\*\* (?:Add|Update) File: [^\n"\\]*(?<![\w.-])test/[^"\n]*\.test\.js|"path":"[^"]*(?<![\w.-])test/[^"\n]*\.test\.js"))'
match: contains
target: trace
---
