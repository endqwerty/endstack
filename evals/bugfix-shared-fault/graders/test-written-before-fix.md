---
type: regex
pattern: '^(?:(?!(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*/src/[^"]*\.js"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*/src/[^"]*\.js"))[\s\S])*(?:(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*/test/[^"]*\.test\.js"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*/test/[^"]*\.test\.js"))'
match: contains
target: trace
---
