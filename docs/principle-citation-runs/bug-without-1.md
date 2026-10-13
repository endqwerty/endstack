# bug-without-1

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Bash cd  && git ls-files && grep -rn "strip\|expire" --include=*.py . | head -30; ls skills-N
 1 Bash cd  && cat AGENTS.md jobs.py report.py test_jobs.py; cat skills-N/tdd/SKILL.md
 2 Bash cd  && git checkout -q -b fix-expire-report-crash && python3 - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         que
 3 Bash cd  && python3 - <<'E' p='jobs.py' s=open(p).read() s=s.replace('''        job.failed = True      def drain''','''        job.failed = True         job.error = "expired"      def drain''') s=s.replace
 4 Bash cd  && git commit -qam "Record an error when a job is expired or drained  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git log --oneline -1
```

Commits, newest first:

```
d1ba085 Record an error when a job is expired or drained
203830d jobkit base
```

Final reply:

I fixed the crash and committed it on branch `fix-expire-report-crash` (`d1ba085`). The change is unverified, because this sandbox can't run an independent verifier.

**Pull request description**

**Why:** `report.render` builds `"failed: " + job.error.strip()` for every failed job. `Queue.expire` and `Queue.drain` set `failed = True` but never set `error`, so the report crashed with `AttributeError: 'NoneType' object has no attribute 'strip'` for any expired or drained job.

**What:** In `jobs.py`, `expire` now sets `error = "expired"`. `drain` sets `error = "drained"` only when the job has no error yet, so a real failure message isn't overwritten. Start reading at `jobs.py`, `Queue.expire` and `Queue.drain`.

**Why this approach:** The bug is that a failed job can exist with no error. I fixed that where the state is set. I turned down a `None` check in `report.py` because it would hide the missing reason.

**Checks:**
- I added `test_report_after_expire_and_drain`, which expires one job, drains the queue and renders the report.
  - Before the fix, the suite ran 6 tests with `FAILED (errors=1)`. I didn't capture the traceback, but `errors=1` means the new test raised rather than failed an assertion.
  - After the fix, `python3 -m unittest` ran 6 tests and all passed.
- **Not checked:** no independent verification. The wording of the "expired" and "drained" messages is my choice, so change it if you want different text.

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
