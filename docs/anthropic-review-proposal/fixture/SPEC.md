# Quota change

Preserve can_reserve's public behavior while adding restore(snapshot, limit).
can_reserve allows a reservation up to and including the limit. Its callers
supply nonnegative integer used/amount/limit values, with used <= limit.
restore is a new import boundary. Snapshot used values are schema-validated
integers, but their range has not been checked. Accept 0 <= used <= limit and
return used, or raise ValueError otherwise. limit is a nonnegative integer.
No persistence, network, concurrency, or additional parser exists here.

Run python3 smoke.py from this directory. These are smoke checks, not a
claim of exhaustive coverage. Review the full change and the spec.

Unverified suggestions supplied separately for triage:
- Rename used to consumed for clarity.
- Add a defensive type check for a future parser that might supply strings.
- The import path may accept a snapshot whose usage exceeds the limit.

For each suggestion, report whether it warrants an in-scope fix and why.
Report other findings only when you can substantiate them. No quota of findings.
