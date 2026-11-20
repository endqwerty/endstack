---
name: pr-watch
description: Wait on any GitHub pull request, yours or someone else's, and act on each change (checks, reviews, comments, pushes, merge, close) without polling by hand. Read-only.
disable-model-invocation: true
---

# PR watch

Own one wait on one pull request and what you do when it changes. The
pull request may be yours or anyone's, in any repository the user's GitHub
login can read. Other skills call this one whenever they must wait on a
pull request's state: checks or reviews on your own change, an upstream
fix that must merge before you continue, someone else's pull request the
user wants news of.

## Choose the watcher

1. If the harness can watch a pull request for you and wake you on changes,
   use that and stop here; this skill is the fallback.
2. Otherwise run the bundled script, `scripts/watch_pr.py` in this skill's
   folder. It listens for the host's pull request events when the account
   has them and polls with backoff when it does not, so you never write a
   wait loop yourself. Never poll with sleep loops or repeated status reads.

The script takes a pull request URL, `owner/repo#N`, or a number in the
current repository. Run it with `--help` for every option.

## Choose what ends the wait

Name the outcome you are waiting for with `--until`; several may be given
and the first one met ends the wait.

| Waiting for | `--until` |
| --- | --- |
| A merge you depend on before continuing | `merged` |
| The pull request to leave the open state, merged or not | `closed` |
| All checks on the current head to finish, pass or fail | `checks-done` |
| A new review | `review` |
| A new head commit | `push` |
| Anything worth reading (the default) | `any-change` |

`merged`, `closed` and `checks-done` can already hold when the script
starts; it then reports and exits at once, so check its result rather than
assuming a wait happened. The rest need a change after it starts. With no
checks reported, `checks-done` keeps waiting.

Add `--timeout` (such as `30m`) whenever the wait has a sensible limit, so a
stalled pull request ends the wait instead of holding the task open. Use
`--follow` to stream every change, for "tell me when anything happens", and
`--json` when another program reads the lines.

## Run it in the background and act on each line

Start it as a background job if the harness has one, and keep working on
anything that does not depend on the result. The first line is a snapshot
of the current state; read it, since events before the start are not
replayed. Each later line is one change: a check that finished and how,
all checks passed or failed (with the failing names), a new review and its state, new comments, a new push with its
commit, a merge conflict or its resolution, draft or ready, merged, closed,
reopened.

Act on each line as it arrives, not only at exit: a failing check or a
change request on your own pull request is work to start now; on someone
else's, it is news to relay. When the script exits:

| Exit | Meaning | Next |
| --- | --- | --- |
| 0 | A condition held; the last line names it | Continue the task that was waiting |
| 3 | Closed without merging while waiting for a merge, or merged before the awaited change | Report it; do not continue as if it merged |
| 8 | Timeout | Report the state from the last lines; start a new wait only if the task still needs it |
| 2 | Bad input, no login, or no access | Fix the input or report the access gap; do not retry blindly |

A signal stops it cleanly. Keep one watcher per pull request and stop it
when the wait is over, the user says stop, or the task moves on.

## Never write from the watcher

The watcher only reads. It never comments, reviews, approves, pushes,
merges, closes or reruns checks, and neither does the step that waits on
it. Anything you do about a change goes through the skill that owns it:
[babysit](../babysit/SKILL.md) for readiness of your own pull request,
[ship](../ship/SKILL.md) for a merge the user asked for. On someone else's
pull request, report; do not act on it unless the user asks.
