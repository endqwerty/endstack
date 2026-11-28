# blast-radius import notes (2026-11-27)

Source: `candidates/blast-radius/SKILL.md` (pstack at `978ca6e`).

Kept: the role (find breakage outside the diff, not list callers), the "don't
trust your own writeup" stance, the five-step certainty ladder, the one fact
the change is safe because of, looking where search stops, honest risks with
cleared ones listed apart, proving the fact by running real code, an arena for
a wide change, the handback shape and the unslop and privacy line.

Changed for portability: "`why` step 2" became "`why`", since `why` no longer
numbers its steps; "grep" became "search"; "Solid versus React" became "the
framework's render and effect order"; an installed or vendored copy joins the
list of things a symbol search misses; the arena step links the skill.

Added: a one-way or two-way door section (what outlives a revert, and how to
make the one-way core two-way), a step that calls the door, a rigor table that
combines radius and door, and Door and Rigor entries in the handback. Behind a
one-way door, running the real code is the floor for the safety fact. The
description now names the door so the skill triggers on "is this a one-way
door" as well as "what could this break".
