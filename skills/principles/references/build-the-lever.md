# Build the Lever

When the work isn't trivial, build the tool that does it instead of doing it by hand.

A codemod, generator, or script does the work the same way every time and reruns for free. The tool is one artifact a reviewer can read and rerun to check the work. Hand-done changes can only be re-verified by redoing them. A deterministic script turns "trust me" into "run this".

Build the lever when it saves total work or makes the result checkable, after checking for an existing tool that already does it. Skip it for a couple of obvious edits, or when a safe one-off command does the job.

- Do the first unit by hand to learn the recipe, then build the tool. Prove it by rerunning it on that unit and diffing against your hand-done version. Make the lever safe to rerun.
- Codemod or script for edits, generator for repetitive files, a dump-to-sqlite query for analysis, a rerunnable check for verification.
- A deterministic lever beats fan-out. If the tool can process every unit in one pass, run it yourself. Don't distribute work to separate workers to hand-apply what a script can do.
- When the harness has separate workers and you distribute work to them, write the lever as a skill they all read: the recipe, the verification contract, and the do-not-touch fences in one artifact. Keep it outside the workers' write scope so they can't quietly edit the contract. If separate workers are unavailable, do the work yourself in sequence and say so.
- Commit the lever when the work outlives the session.

Every lever is code someone maintains: say what repeated work it removes. Per the [Laziness Protocol](laziness-protocol.md), build the smallest script that does or proves the job, never a framework.

Distinct from [Encode Lessons in Structure](encode-lessons-in-structure.md), which makes a recurring instruction a durable guardrail. This is throughput and reviewability on the work in front of you. For scripting the verification itself, see [Prove It Works](../../verify/SKILL.md).
