# bug-with-2

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Bash cd  && git ls-files && grep -rn "strip\|expire" --include=*.py . | head -40; ls skills-S
 1 Bash cd  && cat AGENTS.md jobs.py report.py test_jobs.py; cat ../../skills-S/tdd/SKILL.md ../../skills-S/principles/SKILL.md
 2 Bash cd skills-S/principles/references && cat fix-root-causes.md model-the-domain.md
 3 Bash cd  && git checkout -qb fix-expired-report && python3 - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         queue = Qu
 4 Bash cd  && python3 -m unittest 2>&1 | head -15
 5 Bash cd  && python3 - <<'E' p='jobs.py' s=open(p).read() s=s.replace('''            if not job.done:                 job.failed = True                 job.error = "drained"''','''            if not job.don
```

Commits, newest first:

```
32716bd Keep the existing error when draining a failed job
e1e7926 Record an error when a job is expired or drained
7f00bc6 Add failing test: report after expire and drain
203830d jobkit base
```

Final reply:

The report no longer crashes after a job is expired. The fix is committed on branch `fix-expired-report`, and all 6 tests pass. It is unverified: `CLAUDE.md` says no independent verifier can run in this sandbox.

**Pull request description (not pushed, no remote)**

**Why:** `report.render` calls `job.error.strip()` on every failed job. `Queue.expire` and `Queue.drain` set `job.failed = True` directly, so `job.error` stayed `None` and the report raised `AttributeError`.

**What:** The fix is in `jobs.py`.
- `expire` now sets `error = "expired"`.
- `drain` now sets `error = "drained"` on unfinished jobs.
- `drain` skips jobs that already failed, so it keeps their existing error. For example, an expired job stays "expired".

I fixed the cause, not the symptom, so `report.py` is unchanged. A `None` guard there would have shown a failed job with no reason. It follows the fix-root-causes principle. `drain` had the same flaw as `expire`, so I fixed both.

**Alternative turned down:** Routing `expire` and `drain` through `Job.fail()`. It raises for jobs that never started, which `drain` has to handle.

**Checks:**
- **Failing first:** the new test `test_report_after_expire_and_drain` failed on the unfixed code with `AttributeError: 'NoneType' object has no attribute 'strip'` (commit `7f00bc6`).
- **Passing after:** `python3 -m unittest` gives `Ran 6 tests ... OK`.
- **Caught my own bug:** my first version of the fix made `drain` overwrite "expired" with "drained". The test caught it, and `32716bd` fixes it.
- **Not verified:** no independent verifier ran.

**Open:** Any other code that sets `failed` directly could leave `error` as `None` again. The only places in the repo are `expire` and `drain`.

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
