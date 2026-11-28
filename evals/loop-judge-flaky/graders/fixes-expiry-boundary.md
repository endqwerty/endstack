---
type: llm
criteria: 'Does the reply say the failure comes from the expiry boundary (Date.now() minus the stored time can equal the ttl after a sleep of exactly the ttl, and the check uses a strict greater-than) or from depending on real timer precision, rather than from the test timeout, and fix that cause?'
---
