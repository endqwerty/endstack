# bug-with-first-wording-1

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Bash cd  && git ls-files && grep -rn "strip\|expire" --include=*.py . | head -40; ls skills-S
 1 Bash cd  && cat AGENTS.md jobs.py report.py test_jobs.py; cat ../../skills-S/tdd/SKILL.md
 2 Bash cd  && git checkout -qb fix-expired-job-report && python - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         queue =
 3 Edit test_jobs.py
 4 Bash cd  && python3 -m unittest 2>&1 | tail -6; git commit -qam "Add failing test: report after expire and drain  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
 5 Bash cd  && sed -i 's/^        job.failed = True$/        job.failed = True\n        job.error = "expired"/; s/^                job.failed = True$/                job.failed = True\n                job.err
 6 Edit jobs.py
 7 Edit jobs.py
 8 Bash cd  && git diff --stat && python3 -m unittest 2>&1 | tail -4 && git commit -qam "Record an error when expire and drain fail a job  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git log
 9 Bash cd  && python3 -m unittest 2>&1 | head -20
10 Edit jobs.py
11 Bash cd  && python3 -m unittest 2>&1 | tail -4; git status --short
12 Bash cd  && git commit -qam "Keep the original error when drain meets an already failed job  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git log --oneline | head -4
```

Commits, newest first:

```
2066905 Keep the original error when drain meets an already failed job
17822b0 Record an error when expire and drain fail a job
2be932b Add failing test: report after expire and drain
203830d jobkit base
```

Final reply:

I fixed the crash on branch `fix-expired-job-report`, in three commits. All 6 tests pass. The change is unverified, because no independent verifier can run in this sandbox.

Here is the pull request description. I did not push or open a pull request, since the repo has no remote.

## Fix report crash after a job is expired

**Why:** `render()` calls `job.error.strip()` for every failed job. `Queue.expire()` and `Queue.drain()` set `failed = True` directly and never set `error`. Rendering a report after either call therefore raised `AttributeError: 'NoneType' object has no attribute 'strip'`.

**What:** The change is in `jobs.py`. Start reading at `Queue.expire` and `Queue.drain`.
- `expire` now sets `error = "expired"`.
- `drain` now sets `error = "drained"`. It skips jobs that are already failed, so it no longer overwrites their real error. My first attempt overwrote the error on an expired job, and the new test caught it.

**Why this approach:** Every failed job should have an error, as it does when it fails through `Job.fail()`. I fixed the places that break that, not `render()`. I turned down making `render()` tolerate `None` because that would hide jobs that fail with no reason recorded.

**Checks:**
- `test_report_after_expire_and_drain` is new. It expires one job, drains the queue, and renders the report.
- Before the fix, it failed with `AttributeError: 'NoneType' object has no attribute 'strip'`.
- After the fix: `Ran 6 tests ... OK`.
- Verifier: none. No independent verifier ran, so the change is unverified.
- Not checked: other callers that might set `failed` directly. I found none in the repo.

**Commits:**
1. `2be932b` adds the failing test.
2. `17822b0` sets the error in `expire` and `drain`.
3. `2066905` makes `drain` skip jobs that are already failed.

I committed the second commit before running the tests, and the tests were red at that point. The third commit fixes that, so only the final state is green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
