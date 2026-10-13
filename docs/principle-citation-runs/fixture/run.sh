#!/bin/bash
# usage: run.sh <arm N|S> <task feature|bug> <sample>
set -u
S=/tmp/endstack-principles-dryrun; arm=$1; task=$2; n=$3; id=$arm-$task-$n
rm -rf $S/runs/$id; mkdir -p $S/runs; git clone -q $S/fixture $S/runs/$id; cd $S/runs/$id
cat >> AGENTS.md <<X

Your skills directory for this repository is $S/skills-$arm. Read a skill's
SKILL.md from there; skills installed anywhere else are out of date.
X
git -c user.name=dry -c user.email=dry@example.invalid commit -q -am "skills path"
case $task in
 feature) P="Add pause and resume to jobs. A running job can be paused and later resumed. A paused job cannot complete or fail, the queue must not hand it out, and the summary and the report should show it as paused.";;
 bug) P="The report crashes with AttributeError: 'NoneType' object has no attribute 'strip' after a job is expired. Fix it.";;
esac
PYTHONDONTWRITEBYTECODE=1 timeout 1200 claude -p "$P" --model claude-sonnet-5-5 --effort medium \
  --permission-mode bypassPermissions --tools 'Bash,Read,Edit,Write,Glob,Grep' \
  --no-session-persistence --output-format stream-json --verbose < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
echo "$id exit $?"
