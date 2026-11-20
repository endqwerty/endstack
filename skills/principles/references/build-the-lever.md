# Build the Lever

Build the tool that does or proves the work (a codemod, script, generator, or rerunnable check) when it saves total work or makes the result checkable, after checking for an existing one. Skip it for a couple of obvious edits, or when a safe one-off command does the job.

- Do the first unit by hand, then build the tool and prove it by rerunning it on that unit. Make it safe to rerun.
- A deterministic tool beats fan-out. When you do hand work to separate workers, write the recipe, the verification contract, and the fences as one skill they read and cannot edit.
- Commit it when the work outlives the session. Build the smallest script that does or proves the job, never a framework.
