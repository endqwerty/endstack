#!/bin/bash
# usage: run.sh <arm N|S> <agent claude|codex> <sample>
set -u
R=~/.cache/endstack-tdd-dryrun; arm=$1; agent=$2; n=$3; id=$arm-$agent-$n
rm -rf $R/runs/$id; mkdir -p $R/runs; git clone -q $R/fixture $R/runs/$id; cd $R/runs/$id
git config user.name dry; git config user.email dry@example.invalid
cat >> AGENTS.md <<X

Your skills directory for this repository is $R/skills-$arm. Read a skill's
SKILL.md from there; skills installed anywhere else are out of date.
X
git commit -q -am "skills path"
P="Users report that \`gatekeep show feat\` sometimes prints a passing verdict above results that contain failures. It happens when CI pushes a new head while the command is running. Fix it."
if [ $agent = claude ]; then
 timeout 1500 claude -p "$P" --model claude-sonnet-5-5 --effort medium \
  --permission-mode bypassPermissions --tools 'Bash,Read,Edit,Write,Glob,Grep' \
  --no-session-persistence --output-format stream-json --verbose < /dev/null > $R/runs/$id.jsonl 2> $R/runs/$id.err
else
 timeout 1500 codex exec -m gpt-6.1-sol -c model_reasoning_effort=medium \
  --dangerously-bypass-approvals-and-sandbox --json -C $R/runs/$id "$P" < /dev/null > $R/runs/$id.jsonl 2> $R/runs/$id.err
fi
echo "$id exit $?"
