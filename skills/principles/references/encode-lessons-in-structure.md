# Encode Lessons in Structure

When an instruction or correction recurs, encode it as a lint rule, type, metadata flag, runtime check, or script instead of more text, and delete the instruction.

- Classify first. Encode only a defect against something still wanted. A preference stays a plain instruction, open to change; an experiment gets the condition that ends it.
- Pick the strongest mechanism the recurrence justifies: an unrepresentable state, then a lint or banned API that fails CI, then a canonical helper, then a runtime check. A guard must cost less than the mistake it stops.
- If the lesson needs judgment and cannot be encoded, make the instruction more prominent and add an example of the failure mode.

If the fix is structural, only use the structural fix. The instruction is the symptom.
