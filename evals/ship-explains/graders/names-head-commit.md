---
type: regex
pattern: 'head commit|current (?:head|revision|commit)|that (?:exact |same )?(?:commit|revision)|pinned|match-head'
match: contains
target: last_message
flags: i
---
