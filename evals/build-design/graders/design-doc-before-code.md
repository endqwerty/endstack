---
type: regex
pattern: '^(?:(?!(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*(?<![\w.-])(?:shared|server|web|cli)/(?![^"\n]*\.test\.ts)[^"\n]*\.ts"|\*\*\* (?:Add|Update) File: [^\n"\\]*(?<![\w.-])(?:shared|server|web|cli)/(?![^"\n]*\.test\.ts)[^"\n]*\.ts|"path":"[^"]*(?<![\w.-])(?:shared|server|web|cli)/(?![^"\n]*\.test\.ts)[^"\n]*\.ts"))[\s\S])*(?:(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*(?<![\w.-])docs/design/[^"\n]*\.md"|\*\*\* (?:Add|Update) File: [^\n"\\]*(?<![\w.-])docs/design/[^"\n]*\.md|"path":"[^"]*(?<![\w.-])docs/design/[^"\n]*\.md"))'
match: contains
target: trace
---
