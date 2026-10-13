# bug-without-2

PROMPT: The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.

Tool calls, in order:

```
 0 Grep strip\(|expire
 1 Bash git ls-files && ls skills-N
 2 Bash cat AGENTS.md jobs.py report.py test_jobs.py; cat skills-N/tdd/SKILL.md skills-N/principles/SKILL.md
 3 Bash git checkout -qb fix-report-expired-job && python3 - <<'E' p='test_jobs.py' s=open(p).read() s=s.replace('''  if __name__''','''     def test_report_after_expire_and_drain(self):         queue = Queue
 4 Bash python3 - <<'E' p='jobs.py' s=open(p).read() s=s.replace('''    def can_retry''','''    def abort(self, error):         """Mark the job failed from outside, whether or not it started."""         self.
 5 Bash python3 -m unittest 2>&1 | head -15
 6 Bash sed -i 's/            if not job.done:/            if not job.done and not job.failed:/' jobs.py && python3 -m unittest 2>&1 | tail -3 && git commit -qam "Keep the original error when draining an alre
 7 Edit jobs.py
 8 Bash python3 -m unittest 2>&1 | tail -3 && git commit -qam "Keep the original error when draining an already failed job  Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git log --oneline -3 &
```

Commits, newest first:

```
72c5ecd Keep the original error when draining an already failed job
4a9d442 Record an error when a job is expired or drained
203830d jobkit base
```

Final reply:

The report no longer crashes after a job is expired. The fix is on branch `fix-report-expired-job` in two commits, `4a9d442` and `72c5ecd`. All 6 tests pass, but nobody independent has checked it, because no verifier can run in this sandbox.

I used `tdd`, with `principles` and `unslop` for the write-up.

**Pull request description**

**Why:** `Queue.expire` and `Queue.drain` marked jobs as failed without setting `job.error`. `report.render` then called `job.error.strip()` on `None` and raised `AttributeError: 'NoneType' object has no attribute 'strip'`. `drain` had the same bug.

**What:** Start reading at `jobs.py`.
- I added `Job.abort(error)`, which marks a job failed and records the reason. It works whether or not the job has started.
- `expire` now records `"expired"`.
- `drain` now records `"drained"`.
- `drain` also skips jobs that already failed, so an expired job keeps `"expired"` instead of being relabelled.

**Why this approach:**
- I fixed the producers, not the report. A failed job should always say why, so the report stays strict. A `None` guard in `report.py` would hide the gap.
- I didn't reuse `Job.fail`, because it rejects jobs that never started and `drain` has to fail queued jobs too.

**Checks:**
- The new `test_report_after_expire_and_drain` failed before the fix with `AttributeError: 'NoneType' object has no attribute 'strip'`.
- After the first commit it failed once more with `'a: failed: drained (attempt 1)' != 'a: failed: expired (attempt 1)'`. That showed `drain` overwriting the reason, which the second commit fixes.
- `python3 -m unittest` now gives `Ran 6 tests ... OK`.
- Not checked: no independent verifier has looked at it.

**Open question:** Jobs that `drain` fails before they ever started count as retryable through `can_retry`. That was already true and I left it alone.
