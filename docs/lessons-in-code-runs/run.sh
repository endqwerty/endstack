#!/bin/bash
# usage: run.sh <arm N|S> <task rule|finding> <agent claude|codex> [sample]
# Setup: S=$(mktemp -d /tmp/endstack-lessons-XXXXXX); echo $S > /tmp/endstack-lessons-path;
# $S/fixture is a git repository of docs/principle-citation-runs/fixture (AGENTS.md, README.md,
# jobs.py, report.py, test_jobs.py); $S/skills-N and $S/ROUTING-N.md come from main,
# $S/skills-S and $S/ROUTING-S.md from the change.
set -u
S=$(cat /tmp/endstack-lessons-path); arm=$1; task=$2; agent=$3; id=$arm-$task-$agent${4:+-$4}
rm -rf $S/runs/$id; git clone -q $S/fixture $S/runs/$id; cd $S/runs/$id
{ printf '\nYour skills directory for this repository is %s. Read a skill'"'"'s\nSKILL.md from there; skills installed anywhere else are out of date. The\nrouting below replaces the skill routing in your global rules.\n\n' "$S/skills-$arm"; cat $S/ROUTING-$arm.md; } >> AGENTS.md
git -c user.name=dry -c user.email=dry@example.invalid commit -q -am "skills path"
case $task in
 rule) P="Add a rule to AGENTS.md: nothing outside the Job class sets a job's state fields (started, done, failed, error) directly; use its methods. Agents have done it twice and the report crashed both times.";;
 finding) P="A verifier reviewed this branch and reported: \`Queue.expire\` sets \`job.failed\` directly without an error, so \`render\` in report.py crashes on an expired job. The same fault was fixed by hand in \`Queue.drain\` once before and has come back. Address the finding.";;
esac
if [ $agent = claude ]; then
 PYTHONDONTWRITEBYTECODE=1 timeout 1500 claude -p "$P" --model claude-sonnet-5-5 --effort medium \
  --permission-mode bypassPermissions --tools 'Bash,Read,Edit,Write,Glob,Grep' \
  --no-session-persistence --output-format stream-json --verbose < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
else
 PYTHONDONTWRITEBYTECODE=1 timeout 1500 codex exec -m gpt-6.1-sol -c model_reasoning_effort=medium \
  --dangerously-bypass-approvals-and-sandbox --json -C $S/runs/$id "$P" < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
fi
echo "$id exit $?"
