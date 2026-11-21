import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "watch_pr.py")
spec = importlib.util.spec_from_file_location("watch_pr", SCRIPT)
wp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wp)

URL = "https://github.com/o/r/pull/7"
# A launcher variable can point sys.executable at a host binary that is not Python; use the interpreter.
PYTHON = getattr(sys, "_base_executable", None) or sys.executable
if not os.path.basename(PYTHON).startswith("python"):
    PYTHON = shutil.which("python3") or PYTHON


def check_run(name, status="COMPLETED", conclusion="SUCCESS"):
    return {"__typename": "CheckRun", "name": name, "status": status, "conclusion": conclusion}


def raw(**over):
    base = {
        "number": 7, "url": URL, "title": "t", "state": "OPEN", "isDraft": False,
        "headRefOid": "a" * 40, "mergeable": "MERGEABLE", "reviewDecision": "REVIEW_REQUIRED",
        "latestReviews": [], "comments": [], "statusCheckRollup": [check_run("test", "IN_PROGRESS", "")],
    }
    base.update(over)
    return base


def review(login, state, at):
    return {"author": {"login": login}, "state": state, "submittedAt": at}


def comment(login, cid=None):
    return {"id": cid or "IC_" + login, "author": {"login": login}, "body": "x"}


class Clock:
    def __init__(self):
        self.t = 0.0
        self.sleeps = []

    def now(self):
        return self.t

    def sleep(self, s):
        self.sleeps.append(s)
        self.t += s


class FakeGh:
    """Returns one queued pull request view per call; the last one repeats."""

    def __init__(self, views, clock, listener=None, errors=(), slow=None):
        self.views = list(views)
        self.clock = clock
        self.listener = listener
        self.errors = set(errors)
        self.slow = slow
        self.calls = 0
        self.listen_args = None
        self.timeouts = []

    def view(self, ref, timeout=None):
        i = self.calls
        self.calls += 1
        self.timeouts.append(timeout)
        if self.slow is not None:
            self.clock.t += min(self.slow, timeout if timeout is not None else self.slow)
            raise wp.GhError("gh pr view timed out")
        if i in self.errors:
            raise wp.GhError("boom")
        return self.views[min(i, len(self.views) - 1)]

    def listen(self, url, events):
        self.listen_args = (url, events)
        return self.listener if self.listener is not None else Unavailable()


class FakeListener:
    """Delivers an event at each listed call index, otherwise waits out the timeout."""

    def __init__(self, clock, events_at=()):
        self.clock = clock
        self.events_at = set(events_at)
        self.n = 0
        self.closed = False
        self.waits = []
        self.probe = None

    def start(self, probe):
        self.probe = probe

    def wait(self, timeout):
        self.waits.append(timeout)
        i = self.n
        self.n += 1
        if i in self.events_at:
            self.clock.t += 0.01
            return "event"
        self.clock.t += timeout
        return "timeout"

    def close(self):
        self.closed = True


class Unavailable(FakeListener):
    def __init__(self):
        super().__init__(None)

    def start(self, probe):
        raise wp.ListenUnavailable("unknown command \"event\" for \"gh\"")


def run(views, until=(), follow=False, timeout=None, as_json=False, listener=None, errors=(), interval=10,
        slow=None):
    clock = Clock()
    if listener is not None:
        listener.clock = clock
    gh = FakeGh(views, clock, listener, errors, slow)
    out, err = io.StringIO(), io.StringIO()
    w = wp.Watcher(gh, wp.parse_ref(URL), until=list(until), follow=follow, timeout=timeout,
                   interval=interval, as_json=as_json, out=out, err=err,
                   clock=clock.now, sleep=clock.sleep)
    code = w.run()
    return code, out.getvalue().splitlines(), err.getvalue(), clock, gh


class ParseRef(unittest.TestCase):
    def test_url(self):
        r = wp.parse_ref("https://github.com/cli/cli/pull/15117")
        self.assertEqual((r.repo, r.number, r.arg), ("cli/cli", 15117, "https://github.com/cli/cli/pull/15117"))

    def test_url_with_suffix(self):
        r = wp.parse_ref("https://github.com/cli/cli/pull/15117/files#diff")
        self.assertEqual((r.repo, r.number, r.arg), ("cli/cli", 15117, "https://github.com/cli/cli/pull/15117"))

    def test_owner_repo_number(self):
        r = wp.parse_ref("cli/cli#12")
        self.assertEqual((r.repo, r.number, r.arg), ("cli/cli", 12, "12"))
        self.assertEqual(r.gh_args(), ["12", "--repo", "cli/cli"])

    def test_number_in_current_repo(self):
        for s in ("12", "#12"):
            r = wp.parse_ref(s)
            self.assertEqual((r.repo, r.number), (None, 12))
            self.assertEqual(r.gh_args(), ["12"])

    def test_bad_input(self):
        for s in ("", "abc", "o/r", "https://github.com/o/r/issues/3", "o/r#x", "-3"):
            with self.assertRaises(ValueError, msg=s):
                wp.parse_ref(s)


class ParseDuration(unittest.TestCase):
    def test_forms(self):
        self.assertEqual(wp.parse_duration("30m"), 1800)
        self.assertEqual(wp.parse_duration("20s"), 20)
        self.assertEqual(wp.parse_duration("90"), 90)
        self.assertEqual(wp.parse_duration("1h30m"), 5400)
        self.assertEqual(wp.parse_duration("0.5"), 0.5)

    def test_bad(self):
        for s in ("", "abc", "10x", "-5"):
            with self.assertRaises(ValueError, msg=s):
                wp.parse_duration(s)


class Checks(unittest.TestCase):
    def test_states(self):
        self.assertEqual(wp.summarize_checks([])["state"], "none")
        self.assertEqual(wp.summarize_checks([check_run("a"), check_run("b", "QUEUED", "")])["state"], "pending")
        self.assertEqual(wp.summarize_checks([{"__typename": "StatusContext", "context": "ci", "state": "PENDING"}])["state"], "pending")
        self.assertEqual(wp.summarize_checks([check_run("a"), check_run("b", conclusion="SKIPPED")])["state"], "pass")
        s = wp.summarize_checks([check_run("a"), check_run("lint", conclusion="FAILURE"),
                                 {"__typename": "StatusContext", "context": "ext", "state": "ERROR"}])
        self.assertEqual((s["state"], s["failed"], s["total"], s["done"]), ("fail", ["ext", "lint"], 3, 3))


class Diff(unittest.TestCase):
    def kinds(self, old, new):
        a, b = wp.normalize(old), wp.normalize(new)
        return [(c["kind"], c["message"]) for c in wp.diff(a, wp.carry_unknown(a, b))]

    def test_no_change(self):
        self.assertEqual(self.kinds(raw(), raw()), [])

    def test_merged_closed_reopened(self):
        self.assertEqual(self.kinds(raw(), raw(state="MERGED")), [("merged", "merged")])
        self.assertEqual(self.kinds(raw(), raw(state="CLOSED")), [("closed", "closed without merging")])
        self.assertEqual(self.kinds(raw(state="CLOSED"), raw()), [("reopened", "reopened")])

    def test_draft_and_ready(self):
        self.assertEqual(self.kinds(raw(), raw(isDraft=True)), [("draft", "converted to draft")])
        self.assertEqual(self.kinds(raw(isDraft=True), raw()), [("ready", "ready for review")])

    def test_push(self):
        self.assertEqual(self.kinds(raw(), raw(headRefOid="b" * 40)),
                         [("push", "new push: head bbbbbbb (was aaaaaaa)"),
                          ("checks", "checks running (0/1 done)")])

    def test_mergeable(self):
        self.assertEqual(self.kinds(raw(), raw(mergeable="CONFLICTING")),
                         [("mergeable", "merge conflict (mergeable: CONFLICTING, was MERGEABLE)")])
        self.assertEqual(self.kinds(raw(mergeable="CONFLICTING"), raw()),
                         [("mergeable", "mergeable again (mergeable: MERGEABLE, was CONFLICTING)")])

    def test_unknown_mergeable_is_not_a_change(self):
        self.assertEqual(self.kinds(raw(), raw(mergeable="UNKNOWN")), [])
        a = wp.normalize(raw())
        b = wp.carry_unknown(a, wp.normalize(raw(mergeable="UNKNOWN")))
        self.assertEqual(wp.diff(b, wp.carry_unknown(b, wp.normalize(raw(mergeable="CONFLICTING"))))[0]["kind"], "mergeable")

    def test_checks_pass_fail_running(self):
        self.assertEqual(self.kinds(raw(), raw(statusCheckRollup=[check_run("test")])),
                         [("check", "check test passed"), ("checks", "checks passed (1/1)")])
        self.assertEqual(self.kinds(raw(), raw(statusCheckRollup=[check_run("test", conclusion="FAILURE")])),
                         [("check", "check test failed"), ("checks", "checks failed: test (1 of 1)")])
        self.assertEqual(self.kinds(raw(statusCheckRollup=[check_run("test")]), raw()),
                         [("checks", "checks running (0/1 done)")])

    def test_one_check_fails_while_another_runs(self):
        old = raw(statusCheckRollup=[check_run("a", "IN_PROGRESS", ""), check_run("b", "IN_PROGRESS", "")])
        new = raw(statusCheckRollup=[check_run("a", conclusion="FAILURE"), check_run("b", "IN_PROGRESS", "")])
        self.assertEqual(self.kinds(old, new), [("check", "check a failed")])
        status = raw(statusCheckRollup=[{"__typename": "StatusContext", "context": "ci", "state": "PENDING"},
                                        check_run("b", "IN_PROGRESS", "")])
        done = raw(statusCheckRollup=[{"__typename": "StatusContext", "context": "ci", "state": "SUCCESS"},
                                      check_run("b", "IN_PROGRESS", "")])
        self.assertEqual(self.kinds(status, done), [("check", "check ci passed")])

    def test_checks_on_a_new_head_are_new(self):
        old = raw(statusCheckRollup=[check_run("lint")])
        new = raw(headRefOid="b" * 40, statusCheckRollup=[check_run("lint"), check_run("test", "QUEUED", "")])
        self.assertEqual(self.kinds(old, new), [("push", "new push: head bbbbbbb (was aaaaaaa)"),
                                                ("check", "check lint passed"),
                                                ("checks", "checks running (1/2 done)")])
        done = raw(headRefOid="b" * 40, statusCheckRollup=[check_run("lint")])
        self.assertEqual(self.kinds(old, done), [("push", "new push: head bbbbbbb (was aaaaaaa)"),
                                                 ("check", "check lint passed"),
                                                 ("checks", "checks passed (1/1)")])

    def test_duplicate_check_names_are_told_apart(self):
        old = raw(statusCheckRollup=[check_run("label"), check_run("label", "QUEUED", ""), check_run("x", "QUEUED", "")])
        new = raw(statusCheckRollup=[check_run("label"), check_run("label"), check_run("x", "QUEUED", "")])
        self.assertEqual(self.kinds(old, new), [("check", "check label passed")])

    def test_review(self):
        old = raw(latestReviews=[review("al", "COMMENTED", "2026-01-01T00:00:00Z")])
        new = raw(latestReviews=[review("al", "APPROVED", "2026-01-02T00:00:00Z"),
                                 review("bo", "CHANGES_REQUESTED", "2026-01-02T00:00:00Z")])
        self.assertEqual(self.kinds(old, new), [("review", "review: al APPROVED"),
                                                ("review", "review: bo CHANGES_REQUESTED")])

    def test_review_decision(self):
        self.assertEqual(self.kinds(raw(), raw(reviewDecision="APPROVED")),
                         [("review_decision", "review decision: APPROVED (was REVIEW_REQUIRED)")])

    def test_replaced_comment_is_new(self):
        self.assertEqual(self.kinds(raw(comments=[comment("x", "IC_1")]), raw(comments=[comment("bo", "IC_2")])),
                         [("comment", "new comment by bo (1 total)")])
        self.assertEqual(self.kinds(raw(comments=[comment("x", "IC_1")]), raw(comments=[])), [])

    def test_same_author_new_review_same_state(self):
        old = raw(latestReviews=[review("al", "COMMENTED", "2026-01-01T00:00:00Z")])
        new = raw(latestReviews=[review("al", "COMMENTED", "2026-01-03T00:00:00Z")])
        self.assertEqual(self.kinds(old, new), [("review", "review: al COMMENTED")])

    def test_comment(self):
        self.assertEqual(self.kinds(raw(), raw(comments=[comment("bo")])),
                         [("comment", "new comment by bo (1 total)")])
        self.assertEqual(self.kinds(raw(comments=[comment("x")]), raw(comments=[comment("x"), comment("a"), comment("bo")])),
                         [("comment", "2 new comments, latest by bo (3 total)")])


class Until(unittest.TestCase):
    def test_already_merged_exits_at_once(self):
        code, out, _, clock, gh = run([raw(state="MERGED")], until=["merged"])
        self.assertEqual(code, 0)
        self.assertEqual(gh.calls, 1)
        self.assertEqual(clock.t, 0)
        self.assertIn("snapshot", out[0])
        self.assertIn("done: merged", out[-1])

    def test_waits_for_merge(self):
        code, out, err, _, gh = run([raw(), raw(), raw(state="MERGED")], until=["merged"])
        self.assertEqual(code, 0)
        self.assertEqual(gh.calls, 3)
        self.assertTrue(any(line == "o/r#7 merged" for line in out), out)
        self.assertIn("polling", err)

    def test_closed_unmerged_while_waiting_for_merge_exits_3(self):
        code, out, _, _, _ = run([raw(), raw(state="CLOSED")], until=["merged"])
        self.assertEqual(code, 3)
        self.assertIn("closed without merging", out[-1])

    def test_already_closed_waiting_for_merge_exits_3(self):
        code, _, _, _, gh = run([raw(state="CLOSED")], until=["merged"])
        self.assertEqual((code, gh.calls), (3, 1))

    def test_closed_satisfies_closed(self):
        self.assertEqual(run([raw(), raw(state="CLOSED")], until=["closed"])[0], 0)
        self.assertEqual(run([raw(), raw(state="MERGED")], until=["closed"])[0], 0)
        self.assertEqual(run([raw(), raw(state="CLOSED")], until=["merged", "closed"])[0], 0)

    def test_merged_while_waiting_for_push_exits_3(self):
        self.assertEqual(run([raw(), raw(state="MERGED")], until=["push"])[0], 3)

    def test_checks_done(self):
        code, out, _, _, _ = run([raw(), raw(), raw(statusCheckRollup=[check_run("test", conclusion="FAILURE")])],
                                 until=["checks-done"])
        self.assertEqual(code, 0)
        self.assertTrue(any("checks failed: test" in line for line in out))

    def test_checks_already_done(self):
        code, _, _, _, gh = run([raw(statusCheckRollup=[check_run("test")])], until=["checks-done"])
        self.assertEqual((code, gh.calls), (0, 1))

    def test_no_checks_is_not_done(self):
        code, _, _, _, _ = run([raw(statusCheckRollup=[])], until=["checks-done"], timeout=30)
        self.assertEqual(code, 8)

    def test_review_ignores_comment(self):
        code, out, _, _, gh = run([raw(), raw(comments=[comment("bo")]),
                                   raw(comments=[comment("bo")], latestReviews=[review("al", "APPROVED", "t")])],
                                  until=["review"])
        self.assertEqual((code, gh.calls), (0, 3))
        self.assertTrue(any("new comment by bo" in line for line in out))
        self.assertTrue(any("review: al APPROVED" in line for line in out))

    def test_push(self):
        self.assertEqual(run([raw(), raw(headRefOid="c" * 40)], until=["push"])[0], 0)

    def test_any_change_is_default(self):
        code, _, _, _, gh = run([raw(), raw(), raw(isDraft=True), raw(state="MERGED")])
        self.assertEqual((code, gh.calls), (0, 3))

    def test_several_until(self):
        code, _, _, _, gh = run([raw(), raw(latestReviews=[review("al", "APPROVED", "t")]), raw(state="MERGED")],
                                until=["merged", "review"])
        self.assertEqual((code, gh.calls), (0, 2))


class Timing(unittest.TestCase):
    def test_timeout_exits_8(self):
        code, out, _, clock, _ = run([raw()], until=["merged"], timeout=100)
        self.assertEqual(code, 8)
        self.assertAlmostEqual(clock.t, 100)
        self.assertIn("timeout after 100s", out[-1])

    def test_backoff_grows_and_resets_on_change(self):
        views = [raw()] * 4 + [raw(comments=[comment("a")])] + [raw(comments=[comment("a")])] * 10
        _, _, _, clock, _ = run(views, follow=True, timeout=400, interval=10)
        s = clock.sleeps
        self.assertEqual(s[:3], [10, 15, 22.5])
        self.assertEqual(s[4], 10)
        self.assertLessEqual(max(s), 300)

    def test_follow_streams_until_timeout(self):
        views = [raw(), raw(comments=[comment("a")]), raw(comments=[comment("a")], isDraft=True)]
        code, out, _, _, _ = run(views, follow=True, timeout=60)
        self.assertEqual(code, 8)
        self.assertTrue(any("new comment" in line for line in out))
        self.assertTrue(any("converted to draft" in line for line in out))

    def test_follow_with_until_still_stops(self):
        views = [raw(), raw(comments=[comment("a")]), raw(comments=[comment("a")], state="MERGED")]
        self.assertEqual(run(views, follow=True, until=["merged"], timeout=600)[0], 0)


class Limits(unittest.TestCase):
    def test_every_view_is_bounded_by_the_deadline(self):
        _, _, _, _, gh = run([raw()], until=["merged"], timeout=25, interval=10)
        self.assertEqual(gh.timeouts, [25, 15])

    def test_slow_view_past_deadline_is_a_timeout(self):
        code, out, _, clock, _ = run([raw()], until=["merged"], timeout=0.1, slow=120)
        self.assertEqual(code, 8)
        self.assertAlmostEqual(clock.t, 0.1)
        self.assertIn("timeout", out[-1])

    def test_interval_is_capped_at_five_minutes(self):
        _, _, _, clock, _ = run([raw()], until=["merged"], timeout=1000, interval=360)
        self.assertEqual(clock.sleeps[0], 300)

    def test_listener_probe_is_bounded_by_the_deadline(self):
        listener = FakeListener(None)
        run([raw()], until=["merged"], timeout=3, listener=listener)
        self.assertLessEqual(listener.probe, 3)

    def test_listener_is_closed_when_stopped_during_startup(self):
        class Interrupted(FakeListener):
            def start(self, probe):
                raise wp.Stopped(signal.SIGTERM)
        listener = Interrupted(None)
        with self.assertRaises(wp.Stopped):
            run([raw()], until=["merged"], listener=listener)
        self.assertTrue(listener.closed)


class Events(unittest.TestCase):
    def test_event_wakes_an_immediate_poll(self):
        listener = FakeListener(None, events_at={1})
        code, _, err, clock, gh = run([raw(), raw(), raw(state="MERGED")], until=["merged"], listener=listener,
                                      interval=30)
        self.assertEqual(code, 0)
        self.assertEqual(gh.listen_args[0], URL)
        self.assertIn("com.github.pull_request.state.changed.v1", gh.listen_args[1])
        self.assertEqual(listener.waits[0], 0)
        self.assertLess(clock.t, 1)
        self.assertTrue(listener.closed)
        self.assertIn("listening", err)

    def test_dead_listener_falls_back_to_polling(self):
        class Dead(FakeListener):
            def wait(self, timeout):
                return "dead"
        code, _, err, clock, _ = run([raw(), raw(), raw(state="MERGED")], until=["merged"], listener=Dead(None))
        self.assertEqual(code, 0)
        self.assertIn("polling", err)
        self.assertGreater(clock.t, 0)

    def test_unavailable_falls_back_to_polling(self):
        code, _, err, _, _ = run([raw(), raw(state="MERGED")], until=["merged"])
        self.assertEqual(code, 0)
        self.assertIn("event stream unavailable", err)


class Errors(unittest.TestCase):
    def test_initial_view_error_exits_2(self):
        code, _, err, _, _ = run([raw()], until=["merged"], errors={0})
        self.assertEqual(code, 2)
        self.assertIn("boom", err)

    def test_transient_poll_errors_are_retried(self):
        code, _, err, _, _ = run([raw(), raw(), raw(), raw(state="MERGED")], until=["merged"], errors={1, 2})
        self.assertEqual(code, 0)
        self.assertIn("boom", err)

    def test_persistent_poll_errors_exit_2(self):
        self.assertEqual(run([raw()], until=["merged"], errors=set(range(1, 50)))[0], 2)

    def test_gh_missing(self):
        gh = wp.GhClient(gh="/nonexistent/gh")
        with self.assertRaises(wp.GhError):
            gh.view(wp.parse_ref("1"))


class JsonOutput(unittest.TestCase):
    def test_every_line_is_json(self):
        code, out, _, _, _ = run([raw(), raw(isDraft=True), raw(isDraft=True, state="MERGED")],
                                 until=["merged"], as_json=True)
        self.assertEqual(code, 0)
        objs = [json.loads(line) for line in out]
        self.assertEqual([o["event"] for o in objs], ["snapshot", "change", "change", "done"])
        self.assertEqual(objs[0]["pr"], "o/r#7")
        self.assertEqual(objs[0]["snapshot"]["state"], "OPEN")
        self.assertEqual(objs[1]["kind"], "draft")
        self.assertEqual((objs[-1]["reason"], objs[-1]["exit"]), ("merged", 0))

    def test_timeout_json(self):
        _, out, _, _, _ = run([raw()], until=["merged"], timeout=5, as_json=True)
        self.assertEqual(json.loads(out[-1])["event"], "timeout")
        self.assertEqual(json.loads(out[-1])["exit"], 8)


FAKE_GH = r'''#!{python}
import json, os, sys, time
d = os.environ["FAKE_GH_DIR"]
args = sys.argv[1:]
if args[:2] == ["pr", "view"]:
    if os.environ.get("FAKE_GH_VIEW") == "slow":
        time.sleep(30)
    if os.environ.get("FAKE_GH_VIEW") == "noauth":
        sys.stderr.write("To get started with GitHub CLI, please run:  gh auth login\n")
        sys.exit(4)
    n_path = os.path.join(d, "n")
    n = int(open(n_path).read()) if os.path.exists(n_path) else 0
    open(n_path, "w").write(str(n + 1))
    views = sorted(f for f in os.listdir(d) if f.endswith(".json"))
    sys.stdout.write(open(os.path.join(d, views[min(n, len(views) - 1)])).read())
    sys.exit(0)
if args[:2] == ["event", "listen"]:
    mode = os.environ.get("FAKE_GH_EVENTS", "unsupported")
    if mode == "warn":
        sys.stderr.write("warning: event subscriptions are in preview\n")
        sys.stderr.flush()
        time.sleep(60)
        sys.exit(0)
    if mode == "hang":
        import subprocess
        child = subprocess.Popen(["sleep", "60"])
        open(os.path.join(d, "pids.tmp"), "w").write("%d %d" % (os.getpid(), child.pid))
        os.rename(os.path.join(d, "pids.tmp"), os.path.join(d, "pids"))
        time.sleep(60)
        sys.exit(0)
    if mode == "unsupported":
        sys.stderr.write('unknown command "event" for "gh"\n')
        sys.exit(1)
    sys.stderr.write("Listening for events\n")
    sys.stderr.flush()
    time.sleep(0.5)
    print(json.dumps({"type": "com.github.pull_request.state.changed.v1", "data": {}}))
    sys.stdout.flush()
    time.sleep(60)
    sys.exit(0)
sys.stderr.write("unexpected: %r\n" % args)
sys.exit(1)
'''


def _alive(pid):
    """Running and not a zombie; works with or without /proc."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        pass
    if os.path.isdir("/proc/self"):
        try:
            with open(f"/proc/{pid}/stat") as f:
                return f.read().split(")")[-1].split()[0] != "Z"
        except FileNotFoundError:
            return False
    p = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True)
    stat = p.stdout.strip()
    return bool(stat) and not stat.startswith("Z")


class EndToEnd(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.bin = os.path.join(self.dir.name, "bin")
        self.data = os.path.join(self.dir.name, "data")
        os.makedirs(self.bin)
        os.makedirs(self.data)
        gh = os.path.join(self.bin, "gh")
        with open(gh, "w") as f:
            f.write(FAKE_GH.replace("{python}", PYTHON))
        os.chmod(gh, 0o755)

    def tearDown(self):
        self.dir.cleanup()

    def views(self, *views):
        for i, v in enumerate(views):
            with open(os.path.join(self.data, "%03d.json" % i), "w") as f:
                json.dump(v, f)

    def env(self, **extra):
        env = dict(os.environ, PATH=self.bin + os.pathsep + os.environ.get("PATH", ""), FAKE_GH_DIR=self.data)
        env.pop("__PYVENV_LAUNCHER__", None)
        env.update(extra)
        return env

    def run_script(self, *args, **env):
        return subprocess.run([PYTHON, SCRIPT, *args], capture_output=True, text=True,
                              env=self.env(**env), timeout=60)

    def test_help(self):
        p = self.run_script("--help")
        self.assertEqual(p.returncode, 0)
        for word in ("--until", "--follow", "--timeout", "--json", "--interval"):
            self.assertIn(word, p.stdout)

    def test_bad_ref_exits_2(self):
        p = self.run_script("not a pr")
        self.assertEqual(p.returncode, 2)
        self.assertNotIn("Traceback", p.stderr)

    def test_not_logged_in_exits_2(self):
        self.views(raw())
        p = self.run_script(URL, FAKE_GH_VIEW="noauth")
        self.assertEqual(p.returncode, 2)
        self.assertIn("gh auth login", p.stderr)

    def test_polling_fallback_until_merged(self):
        self.views(raw(), raw(), raw(state="MERGED"))
        p = self.run_script(URL, "--until", "merged", "--interval", "0.05", "--timeout", "20s")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("event stream unavailable", p.stderr)
        self.assertIn("o/r#7 merged\n", p.stdout)

    def test_event_stream_wakes_poll(self):
        self.views(raw(), raw(), raw(state="MERGED"))
        start = time.monotonic()
        p = self.run_script(URL, "--until", "merged", "--interval", "30s", "--timeout", "40s", FAKE_GH_EVENTS="ok")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertLess(time.monotonic() - start, 15)
        self.assertIn("listening", p.stderr)

    def test_timeout_exits_8(self):
        self.views(raw())
        p = self.run_script("o/r#7", "--until", "merged", "--interval", "0.05", "--timeout", "0.3", "--json")
        self.assertEqual(p.returncode, 8, p.stderr)
        lines = [json.loads(line) for line in p.stdout.splitlines()]
        self.assertEqual((lines[0]["event"], lines[-1]["event"]), ("snapshot", "timeout"))

    def test_listener_startup_wait_stops_at_the_deadline(self):
        self.views(raw())
        start = time.monotonic()
        p = self.run_script(URL, "--until", "merged", "--timeout", "0.25", FAKE_GH_EVENTS="warn")
        self.assertEqual(p.returncode, 8, p.stderr)
        self.assertLess(time.monotonic() - start, 1.2)

    def test_alive_sees_a_running_and_an_ended_process(self):
        proc = subprocess.Popen(["sleep", "30"])
        try:
            self.assertTrue(_alive(proc.pid))
        finally:
            proc.kill()
            proc.wait()
        self.assertFalse(_alive(proc.pid))

    def test_slow_view_stops_at_the_deadline(self):
        self.views(raw())
        start = time.monotonic()
        p = self.run_script(URL, "--until", "merged", "--timeout", "0.3", FAKE_GH_VIEW="slow")
        self.assertEqual(p.returncode, 8, p.stderr)
        self.assertLess(time.monotonic() - start, 5)

    def test_sigterm_during_listener_startup_kills_its_process_group(self):
        self.views(raw())
        proc = subprocess.Popen([PYTHON, SCRIPT, URL, "--until", "merged"], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, env=self.env(FAKE_GH_EVENTS="hang"))
        pids_file = os.path.join(self.data, "pids")
        deadline = time.monotonic() + 10
        while not os.path.exists(pids_file) and time.monotonic() < deadline:
            time.sleep(0.05)
        pids = [int(x) for x in Path(pids_file).read_text().split()]
        proc.send_signal(signal.SIGTERM)
        _, err = proc.communicate(timeout=10)
        self.assertEqual(proc.returncode, 128 + signal.SIGTERM, err)
        deadline = time.monotonic() + 5
        alive = pids
        while alive and time.monotonic() < deadline:
            alive = [pid for pid in pids if _alive(pid)]
            time.sleep(0.05)
        self.assertEqual(alive, [], "listener or its child still running")

    def test_sigterm_exits_cleanly(self):
        self.views(raw())
        proc = subprocess.Popen([PYTHON, SCRIPT, URL, "--until", "merged", "--interval", "30"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=self.env())
        deadline = time.monotonic() + 10
        while not os.path.exists(os.path.join(self.data, "n")) and time.monotonic() < deadline:
            time.sleep(0.05)
        time.sleep(0.3)
        proc.send_signal(signal.SIGTERM)
        out, err = proc.communicate(timeout=10)
        self.assertEqual(proc.returncode, 128 + signal.SIGTERM, err)
        self.assertNotIn("Traceback", err)
        self.assertIn("stopped", out)


if __name__ == "__main__":
    unittest.main()
