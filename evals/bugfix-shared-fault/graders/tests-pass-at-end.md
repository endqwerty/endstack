---
type: regex
pattern: '(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*/src/[^"]*\.js"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*/src/[^"]*\.js")(?![\s\S]*(?:"name":"(?:Write|Edit|MultiEdit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*/src/[^"]*\.js"|"type":"file_change","changes":\[[^\]]*"path":"[^"]*/src/[^"]*\.js"))[\s\S]*?(?:"id":"(toolu_\w+)","name":"Bash","input":\{"command":"(?:[^"\\]|\\.)*?(?:\bnode\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?--test\b|\bnpm\s+(?:run\s+)?test\b)(?:[^"\\]|\\.)*?"[\s\S]*?(?:\{"tool_use_id":"\1","type":"tool_result","content":"(?:[^"\\]|\\.)*?(?:\u2139|\\u2139|#) fail 0\b|"type":"tool_result","content":"(?:[^"\\]|\\.)*?(?:\u2139|\\u2139|#) fail 0\b(?:[^"\\]|\\.)*?"(?:,"is_error":(?:true|false))?,"tool_use_id":"\1")|"type":"command_execution","command":"(?:[^"\\]|\\.)*?(?:\bnode\b(?:[^"\\;|&]|\\(?!n)[\s\S])*?--test\b|\bnpm\s+(?:run\s+)?test\b)(?:[^"\\]|\\.)*?","aggregated_output":"(?:[^"\\]|\\.)*?(?:\u2139|\\u2139|#) fail 0\b)'
match: contains
target: trace
---
