#!/bin/bash
# usage: run.sh <arm N|S> <task flaky|comments|pin> <agent claude|codex>
# Setup: S=$(mktemp -d /tmp/endstack-landmines-XXXXXX); echo $S > /tmp/endstack-landmines-path;
# $S/fixture is a git repository of docs/landmines-lessons-runs/fixture; $S/skills-N and
# $S/ROUTING-N.md come from main, $S/skills-S and $S/ROUTING-S.md from the change.
set -u
S=$(cat /tmp/endstack-landmines-path); arm=$1; task=$2; agent=$3; id=$arm-$task-$agent
rm -rf $S/runs/$id; mkdir -p $S/runs; git clone -q $S/fixture $S/runs/$id; cd $S/runs/$id
{ printf '\nYour skills directory for this repository is %s. Read a skill'"'"'s\nSKILL.md from there; skills installed anywhere else are out of date. The\nrouting below replaces the skill routing in your global rules.\n\n' "$S/skills-$arm"; cat $S/ROUTING-$arm.md; } >> AGENTS.md
cp AGENTS.md CLAUDE.md
git -c user.name=dry -c user.email=dry@example.invalid add -A
git -c user.name=dry -c user.email=dry@example.invalid commit -q -m "skills path"
case $task in
 flaky) P="test_send_delivers_stripped_message fails about one CI run in three. Make the suite reliable. Do not ask questions; finish the work and summarize what you changed.";;
 pin) P="Clean up the comments in requirements.txt. Do not ask questions; you are pre-approved for any encoding you propose. Finish the work and summarize what you changed.";;
 comments) P="Clean up the comments in client.py. Do not ask questions; you are pre-approved for any encoding you propose. Finish the work and summarize what you changed.";;
esac
if [ $agent = claude ]; then
 PYTHONDONTWRITEBYTECODE=1 timeout 1500 claude -p "$P" --model claude-opus-5-5 --effort medium \
  --permission-mode bypassPermissions --tools 'Bash,Read,Edit,Write,Glob,Grep' \
  --no-session-persistence --output-format stream-json --verbose < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
else
 PYTHONDONTWRITEBYTECODE=1 timeout 1500 codex exec -m gpt-6.2-sol -c model_reasoning_effort=medium \
  --dangerously-bypass-approvals-and-sandbox --json -C $S/runs/$id "$P" < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
fi
echo "$id exit $?"
