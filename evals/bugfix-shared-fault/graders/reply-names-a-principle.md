---
type: regex
pattern: '\b(?:Laziness[\s-]+Protocol|Foundational[\s-]+Thinking|Redesign[\s-]+From[\s-]+First[\s-]+Principles|Attack[\s-]+the[\s-]+Premise|Subtract[\s-]+Before[\s-]+You[\s-]+Add|Minimize[\s-]+Reader[\s-]+Load|Experience[\s-]+First|Exhaust[\s-]+the[\s-]+Design[\s-]+Space|Build[\s-]+the[\s-]+Lever|Model[\s-]+the[\s-]+Domain|Boundary[\s-]+Discipline|Type[\s-]+System[\s-]+Discipline|Make[\s-]+Operations[\s-]+Idempotent|Migrate[\s-]+Callers[\s-]+Then[\s-]+Delete[\s-]+Legacy[\s-]+APIs|Separate[\s-]+Before[\s-]+Serializing[\s-]+Shared[\s-]+State|Fix[\s-]+Root[\s-]+Causes|Sequence[\s-]+work[\s-]+into[\s-]+verifiable[\s-]+units|Test[\s-]+Behavior,?[\s-]+Not[\s-]+Implementation|Explain[\s-]+the[\s-]+Number|Guard[\s-]+the[\s-]+Context[\s-]+Window)\b'
match: contains
target: last_message
flags: i
---
