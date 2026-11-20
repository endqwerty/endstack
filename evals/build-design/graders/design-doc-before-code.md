---
type: regex
pattern: '^(?:(?!(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*(?<![\w.-])(?:shared|server|web|cli)/(?![^"\n]*\.test\.ts)[^"\n]*\.ts"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*(?<![\w.-])(?:shared|server|web|cli)/(?![^"\n]*\.test\.ts)[^"\n]*\.ts"))[\s\S])*(?:(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*(?<![\w.-])docs/design/[^"\n]*\.md"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*(?<![\w.-])docs/design/[^"\n]*\.md"))'
match: contains
target: trace
---
