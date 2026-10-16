#!/bin/bash
# usage: run.sh <arm N|S> <task port|shape|brief> <agent claude|codex> <sample>
set -u
S=~/.cache/endstack-design-dryrun; arm=$1; task=$2; agent=$3; n=$4; id=$arm-$task-$agent-$n${TAG:-}
rm -rf $S/runs/$id; mkdir -p $S/runs; git clone -q $S/fixture $S/runs/$id; cd $S/runs/$id
git config user.name dry; git config user.email dry@example.invalid
cat >> AGENTS.md <<X

Your skills directory for this repository is $S/skills-$arm. Read a skill's
SKILL.md from there; skills installed anywhere else are out of date.
X
git commit -q -am "skills path"
case $task in
 port) P="Users report that \`gatekeep show feat\` sometimes prints a passing verdict above results that contain failures. It happens when CI pushes a new head while the command is running. Fix it.";;
 shape) P="Add cancelling a tracker request: an operator can cancel a request that is still queued, giving a reason. A cancelled request is never sent, and describe() shows who cancelled it and why.";;
 full) P="Full autopilot this queue; you may merge each item once it is done. This repository has no remote, so a commit on main counts as landed. Queue: (1) an operator can quarantine a test with a reason; a quarantined test's failures no longer fail the gate, and both the web page and the command line mark quarantined tests. (2) a tracker request can be cancelled while queued, with a reason; describe() shows who cancelled it and why.";;
 build) P="You are the builder for this change. Your coordinator's brief follows.

$(cat $S/brief-$arm.md)";;
 auto) P="I'll run this queue on full autopilot later, and you may merge it then. For now write the brief you would hand the builder for the first item to BRIEF.md and commit it. Do not implement. Queue: (1) an operator can quarantine a test with a reason; a quarantined test's failures no longer fail the gate, and both the web page and the command line mark quarantined tests. (2) a tracker request can be cancelled while queued.";;
 brief) P="Plan this feature for another agent to build; you coordinate and will review its work. Feature: an operator can quarantine a test with a reason; a quarantined test's failures no longer fail the gate, and both the web page and the command line mark quarantined tests. Write the brief you would hand the builder to BRIEF.md and commit it. Do not implement the feature.";;
esac
if [ $agent = claude ]; then
 timeout 1500 claude -p "$P" --model claude-sonnet-5-5 --effort medium \
  --permission-mode bypassPermissions --tools 'Bash,Read,Edit,Write,Glob,Grep' \
  --no-session-persistence --output-format stream-json --verbose < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
else
 timeout 1500 codex exec -m gpt-6.1-sol -c model_reasoning_effort=medium \
  --dangerously-bypass-approvals-and-sandbox --json -C $S/runs/$id "$P" < /dev/null > $S/runs/$id.jsonl 2> $S/runs/$id.err
fi
echo "$id exit $?"
