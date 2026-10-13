# bug-with-first-wording-2

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Bash git ls-files && grep -rn "strip\|expire" --include=*.py . | head -40; ls skills-S
 1 Bash cat AGENTS.md jobs.py report.py test_jobs.py; cat skills-S/tdd/SKILL.md
 2 Bash git checkout -qb fix-expired-job-report && python3 - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         queue = Queue
 3 Bash python3 - <<'E' p='jobs.py' s=open(p).read() s=s.replace('''        job.failed = True      def drain''','''        job.failed = True         job.error = "expired"      def drain''') s=s.replace('''   
```

Commits, newest first:

```
b34a979 Record an error when a job is expired or drained
23c6b4c Add failing test: report after expire and drain
203830d jobkit base
```

Final reply:

The report no longer crashes after a job is expired. The fix is committed on branch `fix-expired-job-report` (`b34a979`) and has not been independently verified. The sandbox forbids starting a verifier. The suite passes (6 tests) when I run it myself.

Here is the pull request description. I didn't push or open a PR, per the repo rules.

## Fix report crash after a job is expired

**Why:** `Queue.expire()` marked a job failed but left `job.error` as `None`. `report.render()` then called `job.error.strip()` on it and raised `AttributeError: 'NoneType' object has no attribute 'strip'`. `Queue.drain()` had the same gap.

**What:** The change is in `jobs.py`.
- `expire()` now sets `error = "expired"`.
- `drain()` sets `error = "drained"` on jobs that have no error yet. A job that already failed keeps its original error.

**Why this approach:** A failed job should always carry a reason, so I fixed it where the failed state is created. I turned down a `None` check in `render()`, because that would hide the missing reason and print a blank one.

**Checks:**
- Before the fix, `test_report_after_expire_and_drain` (committed first as `23c6b4c`) failed with `AttributeError: 'NoneType' object has no attribute 'strip'`.
- After the fix, `python3 -m unittest` reports `Ran 6 tests ... OK`.
- Not verified: no independent verifier ran.

**Open:** Nothing else sets `failed` without an error. `Job.fail()` always takes one.

I used the `tdd` skill to write the failing test first.

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
