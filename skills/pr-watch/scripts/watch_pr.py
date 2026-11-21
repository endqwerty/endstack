#!/usr/bin/env python3
"""Wait on a GitHub pull request and print one line per meaningful change.

Read-only: it only reads the pull request through the GitHub CLI (`gh pr view`,
and `gh event listen` when event subscriptions work for the account), so it can
watch anyone's pull request in any repository the login can read.
"""
import argparse
import datetime
import json
import os
import queue
import re
import signal
import subprocess
import sys
import threading
import time

FIELDS = ("number,url,title,state,isDraft,headRefOid,mergeable,reviewDecision,"
          "latestReviews,comments,statusCheckRollup")
EVENTS = [
    "com.github.pull_request.state.changed.v1",
    "com.github.pull_request.review.submitted.v1",
    "com.github.pull_request.head.changed.v1",
    "com.github.pull_request.merge_conflict.v1",
    "com.github.pull_request.check_suite.status.changed.v1",
]
CONDITIONS = ["merged", "closed", "checks-done", "review", "push", "any-change"]
FAILED = {"FAILURE", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED", "STARTUP_FAILURE", "ERROR"}
PENDING_STATES = {"PENDING", "EXPECTED"}
BACKOFF = 1.5
MAX_POLL = 300.0
MAX_ERRORS = 5
VIEW_TIMEOUT = 120.0
PROBE = 8.0
EXIT_OK, EXIT_ERROR, EXIT_ENDED, EXIT_TIMEOUT = 0, 2, 3, 8


class GhError(Exception):
    pass


class ListenUnavailable(Exception):
    pass


class Stopped(Exception):
    def __init__(self, signum):
        super().__init__(signum)
        self.signum = signum


class Ref:
    def __init__(self, arg, repo=None, number=None):
        self.arg, self.repo, self.number = arg, repo, number

    def gh_args(self):
        if self.repo and not self.arg.startswith("http"):
            return [self.arg, "--repo", self.repo]
        return [self.arg]


def parse_ref(text):
    """A pull request URL, owner/repo#N, or a number in the current repository."""
    s = (text or "").strip()
    m = re.match(r"^(https?://[^/\s]+)/([^/\s]+)/([^/\s]+)/pull/(\d+)(?:[/?#].*)?$", s)
    if m:
        host, owner, repo, n = m.groups()
        return Ref(f"{host}/{owner}/{repo}/pull/{n}", f"{owner}/{repo}", int(n))
    m = re.match(r"^([\w.-]+/[\w.-]+)#(\d+)$", s)
    if m:
        return Ref(m.group(2), m.group(1), int(m.group(2)))
    m = re.match(r"^#?(\d+)$", s)
    if m:
        return Ref(m.group(1), None, int(m.group(1)))
    raise ValueError(f"not a pull request: {text!r}; give a URL, owner/repo#N or a number")


def parse_duration(text):
    """Seconds from 90, 0.5, 20s, 30m, 1h30m."""
    s = (text or "").strip().lower()
    if re.fullmatch(r"\d+(?:\.\d+)?", s):
        return float(s) if "." in s else int(s)
    parts = re.findall(r"(\d+(?:\.\d+)?)([hms])", s)
    if not parts or "".join(n + u for n, u in parts) != s:
        raise ValueError(f"not a duration: {text!r}; use e.g. 90, 20s, 30m or 1h30m")
    total = sum(float(n) * {"h": 3600, "m": 60, "s": 1}[u] for n, u in parts)
    return int(total) if total == int(total) else total


def check_runs(rollup):
    """[(key, name, pending|pass|fail)]; a repeated name gets #2, #3 in rollup order."""
    runs, seen = [], {}
    for c in rollup or []:
        if c.get("__typename") == "StatusContext" or "context" in c:
            name = c.get("context") or "?"
            raw = (c.get("state") or "").upper()
            state = "pending" if raw in PENDING_STATES else ("fail" if raw in FAILED else "pass")
        else:
            name = c.get("name") or "?"
            if (c.get("status") or "").upper() != "COMPLETED":
                state = "pending"
            else:
                state = "fail" if (c.get("conclusion") or "").upper() in FAILED else "pass"
        base = f"{c.get('workflowName')}/{name}" if c.get("workflowName") else name
        seen[base] = seen.get(base, 0) + 1
        runs.append((base if seen[base] == 1 else f"{base}#{seen[base]}", name, state))
    return runs


def summarize_checks(rollup):
    runs = check_runs(rollup)
    total = len(runs)
    done = sum(1 for _, _, st in runs if st != "pending")
    failed = [name for _, name, st in runs if st == "fail"]
    if total == 0:
        state = "none"
    elif done < total:
        state = "pending"
    else:
        state = "fail" if failed else "pass"
    return {"state": state, "total": total, "done": done, "failed": sorted(set(failed)),
            "runs": {key: [name, st] for key, name, st in runs}}


def normalize(raw):
    comments = raw.get("comments") or []
    reviews = [{"author": (r.get("author") or {}).get("login") or "?", "state": r.get("state") or "",
                "submitted_at": r.get("submittedAt") or ""} for r in raw.get("latestReviews") or []]
    return {
        "url": raw.get("url") or "",
        "number": raw.get("number"),
        "title": raw.get("title") or "",
        "state": raw.get("state") or "",
        "merged": raw.get("state") == "MERGED",
        "draft": bool(raw.get("isDraft")),
        "head": raw.get("headRefOid") or "",
        "mergeable": raw.get("mergeable") or "UNKNOWN",
        "review_decision": raw.get("reviewDecision") or "",
        "reviews": sorted(reviews, key=lambda r: (r["author"], r["submitted_at"])),
        "comments": len(comments),
        "comment_ids": [_comment_id(c) for c in comments],
        "comment_authors": [(c.get("author") or {}).get("login") or "?" for c in comments],
        "checks": summarize_checks(raw.get("statusCheckRollup")),
    }


def _comment_id(c):
    return c.get("id") or f"{(c.get('author') or {}).get('login')}@{c.get('createdAt')}"


def carry_unknown(old, new):
    """GitHub reports UNKNOWN while it recomputes mergeability; keep the last known value."""
    if new["mergeable"] == "UNKNOWN" and old["mergeable"] != "UNKNOWN":
        new = dict(new, mergeable=old["mergeable"])
    return new


def _checks_line(c):
    if c["state"] == "pass":
        return f"checks passed ({c['done']}/{c['total']})"
    if c["state"] == "fail":
        return f"checks failed: {', '.join(c['failed'])} ({len(c['failed'])} of {c['total']})"
    if c["state"] == "pending":
        return f"checks running ({c['done']}/{c['total']} done)"
    return "no checks reported"


def diff(old, new):
    changes = []

    def add(kind, message):
        changes.append({"kind": kind, "message": message})

    if old["state"] != new["state"]:
        if new["state"] == "MERGED":
            add("merged", "merged")
        elif new["state"] == "CLOSED":
            add("closed", "closed without merging")
        elif new["state"] == "OPEN":
            add("reopened", "reopened")
    if old["draft"] != new["draft"]:
        add("draft", "converted to draft") if new["draft"] else add("ready", "ready for review")
    if old["head"] != new["head"] and new["head"]:
        add("push", f"new push: head {new['head'][:7]} (was {old['head'][:7]})")
    if old["mergeable"] != new["mergeable"] and new["mergeable"] != "UNKNOWN":
        what = "merge conflict" if new["mergeable"] == "CONFLICTING" else (
            "mergeable again" if old["mergeable"] == "CONFLICTING" else "mergeability changed")
        add("mergeable", f"{what} (mergeable: {new['mergeable']}, was {old['mergeable']})")
    oc, nc = old["checks"], new["checks"]
    if old["head"] != new["head"]:
        oc = {"state": "none", "failed": [], "runs": {}}
    for key, (name, st) in nc["runs"].items():
        before = oc["runs"].get(key, [name, "pending"])[1]
        if st != "pending" and st != before:
            add("check", f"check {name} {'passed' if st == 'pass' else 'failed'}")
    if (oc["state"], oc["failed"]) != (nc["state"], nc["failed"]) and nc["state"] != "none":
        if nc["state"] != "pending" or oc["state"] != "pending":
            add("checks", _checks_line(nc))
    seen = {(r["author"], r["submitted_at"]) for r in old["reviews"]}
    for r in new["reviews"]:
        if (r["author"], r["submitted_at"]) not in seen:
            add("review", f"review: {r['author']} {r['state']}")
    if old["review_decision"] != new["review_decision"] and new["review_decision"]:
        add("review_decision", f"review decision: {new['review_decision']} (was {old['review_decision'] or 'none'})")
    known = set(old["comment_ids"])
    fresh = [a for cid, a in zip(new["comment_ids"], new["comment_authors"]) if cid not in known]
    if len(fresh) == 1:
        add("comment", f"new comment by {fresh[-1]} ({new['comments']} total)")
    elif fresh:
        add("comment", f"{len(fresh)} new comments, latest by {fresh[-1]} ({new['comments']} total)")
    return changes


def describe(s):
    state = s["state"].lower() + (", draft" if s["draft"] else "")
    return (f"{state}, head {s['head'][:7]}, mergeable {s['mergeable']}, "
            f"review decision {s['review_decision'] or 'none'}, {len(s['reviews'])} reviews, "
            f"{s['comments']} comments, {_checks_line(s['checks'])}")


class EventListener:
    """Runs `gh event listen --follow` and turns its stdout lines into wake-ups."""

    def __init__(self, gh, url, events):
        self.cmd = [gh, "event", "listen", "--resource", url, "--event", ",".join(events), "--follow"]
        self.proc = None
        self.q = queue.Queue()
        self.stderr = []

    def start(self, probe=8.0):
        """Spawn in its own process group and wait up to probe seconds to see that it attached."""
        try:
            self.proc = subprocess.Popen(self.cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE, text=True, start_new_session=True)
        except OSError as e:
            raise ListenUnavailable(str(e))
        threading.Thread(target=self._read, args=(self.proc.stdout, "event"), daemon=True).start()
        threading.Thread(target=self._read, args=(self.proc.stderr, "status"), daemon=True).start()
        deadline = time.monotonic() + probe
        while time.monotonic() < deadline:
            try:
                kind, _ = self.q.get(timeout=0.1)
            except queue.Empty:
                if self.proc.poll() is not None:
                    break
                continue
            if kind == "status":
                try:
                    self.proc.wait(timeout=max(0.0, min(1.5, deadline - time.monotonic())))
                except subprocess.TimeoutExpired:
                    return
                break
            if kind == "event":
                self.q.put(("event", ""))
                return
        if self.proc.poll() is not None:
            self.close()
            msg = " ".join(self.stderr).strip() or f"exit {self.proc.returncode}"
            raise ListenUnavailable(msg)

    def _read(self, stream, kind):
        for line in stream:
            if kind == "status":
                self.stderr.append(line.strip())
            self.q.put((kind, line))
        if kind == "event":
            self.q.put(("eof", ""))

    def wait(self, timeout):
        deadline = time.monotonic() + timeout
        while True:
            left = deadline - time.monotonic()
            if left <= 0:
                return "timeout"
            try:
                kind, _ = self.q.get(timeout=left)
            except queue.Empty:
                return "timeout"
            if kind == "event":
                while True:
                    try:
                        if self.q.get_nowait()[0] == "eof":
                            self.q.put(("eof", ""))
                            break
                    except queue.Empty:
                        break
                return "event"
            if kind == "eof":
                return "dead"

    def close(self):
        """Stop the listener and anything it started (its whole process group)."""
        if self.proc is None:
            return
        for sig, grace in ((signal.SIGTERM, 5), (signal.SIGKILL, 5)):
            try:
                os.killpg(self.proc.pid, sig)
            except (ProcessLookupError, PermissionError):
                break
            try:
                self.proc.wait(timeout=grace)
                os.killpg(self.proc.pid, 0)
            except subprocess.TimeoutExpired:
                continue
            except (ProcessLookupError, PermissionError):
                break


class GhClient:
    def __init__(self, gh="gh"):
        self.gh = gh

    def view(self, ref, timeout=None):
        limit = VIEW_TIMEOUT if timeout is None else max(0.01, min(timeout, VIEW_TIMEOUT))
        try:
            p = subprocess.run([self.gh, "pr", "view", *ref.gh_args(), "--json", FIELDS],
                               stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=limit)
        except FileNotFoundError:
            raise GhError("the GitHub CLI (gh) is not installed or not on PATH")
        except (OSError, subprocess.TimeoutExpired) as e:
            raise GhError(f"gh pr view failed: {e}")
        if p.returncode != 0:
            lines = [l for l in p.stderr.splitlines() if l.strip() and not l.startswith(("hint:", "  "))]
            raise GhError("gh pr view failed: " + (" ".join(lines) or f"exit {p.returncode}"))
        try:
            return json.loads(p.stdout)
        except ValueError:
            raise GhError("gh pr view returned no JSON")

    def listen(self, url, events):
        return EventListener(self.gh, url, events)


class Watcher:
    def __init__(self, gh, ref, until=(), follow=False, timeout=None, interval=30, as_json=False,
                 out=sys.stdout, err=sys.stderr, clock=time.monotonic, sleep=time.sleep):
        conds = [c for u in until for c in u.split(",") if c]
        self.explicit = bool(conds)
        self.conds = conds or ([] if follow else ["any-change"])
        self.gh, self.ref, self.follow, self.timeout = gh, ref, follow, timeout
        self.interval, self.as_json = min(interval, MAX_POLL), as_json
        self.out, self.err, self.clock, self.sleep = out, err, clock, sleep
        self.label = f"{ref.repo}#{ref.number}" if ref.repo else f"#{ref.number}"
        self.listener = None
        self.deadline = None

    def _now(self):
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def emit(self, event, text, **fields):
        if self.as_json:
            line = json.dumps({"event": event, "pr": self.label, "time": self._now(), **fields})
        else:
            line = f"{self.label} {text}"
        print(line, file=self.out, flush=True)

    def note(self, text):
        print(f"pr-watch: {text}", file=self.err, flush=True)

    def verdict(self, snap, changes):
        """(exit code, reason) once the wait is over, else None."""
        kinds = {c["kind"] for c in changes}
        for c in self.conds:
            if (c == "merged" and snap["merged"]) or (c == "closed" and snap["state"] != "OPEN") \
                    or (c == "checks-done" and snap["checks"]["state"] in ("pass", "fail")) \
                    or (c == "review" and "review" in kinds) or (c == "push" and "push" in kinds) \
                    or (c == "any-change" and changes):
                return EXIT_OK, c
        if "merged" in self.conds and snap["state"] == "CLOSED":
            return EXIT_ENDED, "closed without merging"
        if self.conds and snap["merged"]:
            return EXIT_ENDED, "merged before " + " or ".join(self.conds)
        return None

    def finish(self, verdict):
        code, reason = verdict
        if code == EXIT_OK:
            self.emit("done", f"done: {reason}", reason=reason, exit=code)
        else:
            self.emit("ended", f"ended: {reason} (exit {code})", reason=reason, exit=code)
        return code

    def run(self):
        try:
            return self._run()
        finally:
            if self.listener is not None:
                self.listener.close()

    def left(self):
        return None if self.deadline is None else self.deadline - self.clock()

    def timed_out(self):
        self.emit("timeout", f"timeout after {self.timeout}s (exit {EXIT_TIMEOUT})", exit=EXIT_TIMEOUT)
        return EXIT_TIMEOUT

    def _run(self):
        self.deadline = None if self.timeout is None else self.clock() + self.timeout
        try:
            snap = normalize(self.gh.view(self.ref, timeout=self.left()))
        except GhError as e:
            if self.deadline is not None and self.left() <= 0:
                return self.timed_out()
            self.note(str(e))
            if self.as_json:
                self.emit("error", "", message=str(e), exit=EXIT_ERROR)
            return EXIT_ERROR
        if snap["number"] is not None and not self.ref.repo:
            m = re.match(r"^https?://[^/]+/([^/]+/[^/]+)/pull/", snap["url"])
            if m:
                self.label = f"{m.group(1)}#{snap['number']}"
        self.emit("snapshot", "snapshot: " + describe(snap), snapshot=snap)
        changes = []
        v = self.verdict(snap, changes)
        if v:
            return self.finish(v)
        self.listener = self.gh.listen(snap["url"], EVENTS)
        try:
            left = self.left()
            self.listener.start(PROBE if left is None else max(0.0, min(PROBE, left)))
            self.note("listening for pull request events, with a poll as backstop")
            wait = 0
        except ListenUnavailable as e:
            self.listener.close()
            self.listener = None
            self.note(f"event stream unavailable ({e}); polling from every {self.interval}s")
            wait = self.interval
        step, errors = self.interval, 0
        while True:
            left = self.left()
            if left is not None:
                if left <= 0:
                    return self.timed_out()
                wait = min(wait, left)
            woke = False
            if self.listener is not None:
                r = self.listener.wait(wait)
                if r == "dead":
                    self.listener.close()
                    self.listener = None
                    self.note(f"event stream ended; polling from every {self.interval}s")
                woke = r == "event"
            else:
                self.sleep(wait)
            left = self.left()
            if left is not None and left <= 0:
                return self.timed_out()
            try:
                new = carry_unknown(snap, normalize(self.gh.view(self.ref, timeout=left)))
                errors = 0
            except GhError as e:
                if left is not None and self.left() <= 0:
                    return self.timed_out()
                errors += 1
                self.note(f"{e} (attempt {errors} of {MAX_ERRORS})")
                if errors >= MAX_ERRORS:
                    if self.as_json:
                        self.emit("error", "", message=str(e), exit=EXIT_ERROR)
                    return EXIT_ERROR
                wait = step = min(step * BACKOFF, MAX_POLL)
                continue
            found = diff(snap, new)
            snap = new
            for c in found:
                self.emit("change", c["message"], **c)
            changes.extend(found)
            step = self.interval if (found or woke) else min(step * BACKOFF, MAX_POLL)
            wait = step
            v = self.verdict(snap, changes)
            if v:
                return self.finish(v)


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="watch_pr.py",
        description="Wait on a GitHub pull request, anyone's, and print one line per meaningful change. "
                    "Never writes to the pull request.",
        epilog="Exit status: 0 an --until condition was met; 2 bad input, gh missing, not logged in or no "
               "access; 3 the pull request closed unmerged while waiting for merged, or merged before the "
               "awaited condition; 8 timeout; 128+N on signal N. Conditions: merged; closed (no longer open, "
               "merged included); checks-done (every reported check finished; none reported keeps waiting); "
               "review (a new review); push (a new head commit); any-change (default, any change listed). "
               "merged, closed and checks-done can be met at once; the others need a change after start.")
    p.add_argument("pr", help="pull request URL, owner/repo#N, or a number in the current repository")
    p.add_argument("--until", action="append", default=[], metavar="COND",
                   help="stop when this holds: " + ", ".join(CONDITIONS) + "; repeat or comma-separate for any of several")
    p.add_argument("--follow", action="store_true",
                   help="keep printing changes until --timeout or a signal; with --until, still stop when it holds")
    p.add_argument("--timeout", metavar="DURATION", help="give up after this long (90, 20s, 30m, 1h30m); exit 8")
    p.add_argument("--interval", metavar="DURATION", default="30s",
                   help="first poll interval (default 30s, above 5m capped at 5m); grows by half when "
                        "nothing changes, to at most 5m")
    p.add_argument("--json", action="store_true", help="print one JSON object per line")
    a = p.parse_args(argv)
    try:
        ref = parse_ref(a.pr)
        timeout = parse_duration(a.timeout) if a.timeout else None
        interval = parse_duration(a.interval)
        if interval <= 0:
            raise ValueError("--interval must be above zero")
        for u in a.until:
            for c in u.split(","):
                if c not in CONDITIONS:
                    raise ValueError(f"unknown --until {c!r}; choose from {', '.join(CONDITIONS)}")
    except ValueError as e:
        p.print_usage(sys.stderr)
        print(f"watch_pr.py: error: {e}", file=sys.stderr)
        return EXIT_ERROR

    def stop(signum, _frame):
        raise Stopped(signum)

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    w = Watcher(GhClient(), ref, until=a.until, follow=a.follow,
                timeout=timeout, interval=interval, as_json=a.json)
    try:
        return w.run()
    except Stopped as s:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        w.emit("stopped", f"stopped by signal {s.signum}", signal=s.signum, exit=128 + s.signum)
        return 128 + s.signum


if __name__ == "__main__":
    sys.exit(main())
