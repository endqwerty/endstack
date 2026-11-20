---
type: regex
pattern: '(?=[\s\S]*(?:\b(?:e-?)?mail|mailSummary|summary\.js))(?=[\s\S]*(?:\binvoice|invoiceHtml))'
match: contains
target: last_message
flags: i
---
