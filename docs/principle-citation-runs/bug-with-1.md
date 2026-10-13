# bug-with-1

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Bash cd  && git ls-files && grep -rn "strip\|expire" --include=*.py . | head -30; ls skills-S
 1 Bash cd  && cat AGENTS.md jobs.py report.py test_jobs.py; cat ../../skills-S/tdd/SKILL.md ../../skills-S/principles/SKILL.md
 2 Bash cd skills-S/principles/references && cat fix-root-causes.md model-the-domain.md
 3 Bash cd  && git checkout -qb fix-expire-error && python - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         queue = Queue
 4 Edit test_jobs.py
 5 Bash cd  && python3 -m unittest 2>&1 | tail -6; git commit -qam "Add failing test: report after expire and drain  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
 6 Edit jobs.py
 7 Edit jobs.py
 8 Edit jobs.py
 9 Bash cd  && python3 -m unittest 2>&1 | tail -4; git commit -qam "Record an error when a job is expired or drained  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"; git log --oneline | head -3; g
```

Commits, newest first:

```
27f2e72 Record an error when a job is expired or drained
89c8388 Add failing test: report after expire and drain
203830d jobkit base
```

Final reply:

The report no longer crashes after a job is expired or drained. The fix is on branch `fix-expire-error`, in two commits. **It is unverified:** no independent verifier can run in this sandbox. I only ran the unit tests myself, and all 6 pass.

## Pull request description

**Why:** `report.render` calls `job.error.strip()` for every failed job. `Queue.expire` and `Queue.drain` set `job.failed = True` directly and never set `job.error`. The error stayed `None`, so the report raised `AttributeError: 'NoneType' object has no attribute 'strip'`.

**What it does:** Start at `jobs.py`.
- `Job.abandon(error)` is new. It sets `failed` and `error` together.
- `expire` now calls it with `"expired"`.
- `drain` now calls it with `"drained"`.

**Why this approach:** The fault was in `jobs.py`, so I fixed it there and left `report.py` alone. A `None` guard in `render` would have hidden the crash and left those jobs with no reason recorded (the `fix-root-causes` principle). I added a new method instead of calling `Job.fail`, because `fail` requires a started, unfinished job. `drain` also fails jobs that never started, which `fail` would reject.

**How it was checked:**
- The new test `test_report_after_expire_and_drain` was committed first (`89c8388`) and failed with `AttributeError: 'NoneType' object has no attribute 'strip'`, the reported error.
- After the fix (`27f2e72`), `python3 -m unittest` printed `Ran 6 tests ... OK`.
- Independent verification was not run. Nothing else is checked.

**Open:** Nothing outside the tests calls `Job.fail` or the queue methods, so I changed no other callers.

Skills that shaped the work: `tdd` (failing test committed before the fix) and `principles` → `fix-root-causes` (fix at the source, no guard in `render`). I did not run `unslop` or `verify`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
