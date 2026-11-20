# Create a verify skill

Write the verify skill for an agent who reads it cold, mid-change, and has never seen your work. Apply the target, tool and quality rules in [the skill](../SKILL.md) first.

### Generate the verify skill

Write a project-local skill with frontmatter that names the area and says when to use it. Without frontmatter, the skill never registers. From the skill alone, the next agent must be able to tell whether a change touches the verified code, run the check, tell a real bug from a modeling error, and update the verification when a change is intended. Put the coverage record and the sync commit in the skill, and tell the next agent to move the sync commit forward only after it confirms that the verification describes the code at the new commit. Use this repo's real commands, paths, and nouns, and leave no placeholders.

If the check is a TLA+ model, tell the next agent to read every result with the `statechart` skill. It shows each invariant violation the checker finds as its shortest path in plain words, and when the check passes it draws how the system moves between states. Refer to `statechart` by name. Its commands, options and file paths change between releases and machines, so copy none of them into the generated skill or its scripts.

### Prove it before you hand off

Follow the generated skill once, as the next agent would, on a scratch change that breaks the property in the real code. It must catch the break. Then drop the scratch change and confirm that the check is back where it started: passing, or failing only on the findings you will report. A verify skill that was never run is a draft. If the skill misses the break or a step does not run, fix the skill or the verification, not the scratch change.

### Hand off

Tell the user what you verified, which tool you used and why, the bounds, what the check found in plain words, how to run it, and what it does not cover. Suggest a second target only if you found a close one. Point the user at this skill's maintain pass for bringing the verification back in line after changes that did not recheck it.
