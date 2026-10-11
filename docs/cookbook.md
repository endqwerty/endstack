# endstack command cookbook

## What can I call?

These six skill files exist in this checkout. They are **not yet installed**
in either agent's global catalog. Do not assume a slash command exists just
because you see its name here. For now, explicitly ask the agent to read the
linked file in this checkout; the prompts below work that way.

| Skill | Use it for | Deliverable / stop |
| --- | --- | --- |
| [build](../skills/build/SKILL.md) | A feature or bug fix | Checked, independently verified non-draft PR; no watcher or merge |
| [babysit](../skills/babysit/SKILL.md) | Existing PR feedback and failed checks | Merge-ready PR; no merge. Status questions are read-only |
| [ship](../skills/ship/SKILL.md) | Explicitly landing identified work | Confirmed revision in its destination, or a named blocker |
| [autopilot-stack](../skills/autopilot-stack/SKILL.md) | A bounded dependent queue, with human landing | Verified bottom-up PR chain; you land it |
| [autopilot-full](../skills/autopilot-full/SKILL.md) | A bounded queue with explicit merge authority | Verified, landed items; held items remain held |
| [verify](../skills/verify/SKILL.md) | Independent evidence on an exact revision | Read-only pass / issues / not checked verdict; no merge authority |

Future installation must expose this same allowlist in both harnesses and test
actual discovery. No distribution mechanism is claimed here. Upstream's other
skills and its playbooks are reference material, **not extra endstack commands**.

## Copyable examples

Replace the bracketed details with your actual work. On another checkout,
provide the absolute path to this repository's skill file.

**Build:**
> Read `skills/build/SKILL.md`. Fix [bug]; completion means [observable result].
> Prepare the PR for my review. Do not watch or merge it.

**Babysit:**
> Read `skills/babysit/SKILL.md`. Babysit [PR URL] until it is merge-ready.
> Handle real review findings and failed checks. Leave merging to me.

**One status check:**
> Read `skills/babysit/SKILL.md`. Is [PR URL] green? One read-only pass;
> do not change anything or start a watcher.

**Ship:**
> Read `skills/ship/SKILL.md`. Merge [PR URL] into [destination] only if its
> required checks and independent current-revision verdict already pass.
> Otherwise report the blockers; do not watch or arm automatic merging.

That grants landing authority for that work, not deployment authority. “Ship
this PR” also grants it when the PR and destination are clear. Missing checks,
stale verdicts and operator holds still block. Merely asking how ship works
does not execute it. Automatic merge-when-ready needs its own explicit request
and safeguards for the verified revision; green checks alone do not grant it.

**Autopilot stack:**
> Read `skills/autopilot-stack/SKILL.md`. Implement [A, then B, then C] as a
> reviewable PR chain. Verify every layer and leave all merges to me.

**Full autopilot (the special case):**
> Read `skills/autopilot-full/SKILL.md`. Implement and merge only [A, B, C],
> in dependency order, after verification. I authorize those merges into
> [destination]. Hold [operator decision] for me. Do not deploy.

**Verify:**
> Read `skills/verify/SKILL.md`. Independently review [base..head] against
> [task and observable checks]. Change nothing; report evidence and limits.

**Help, not execution:**
> Explain which endstack skill fits [task] and draft a prompt. Do not start.

## Normal flow

Build → you review → optionally babysit → you merge, or explicitly ask ship.
Choose autopilot-stack for a larger dependent queue with the same human merge
boundary. Choose autopilot-full only when you deliberately delegate landing.
“Keep going”, unused allowance and ownership do not silently switch modes.
This repository now uses review-first delivery; other repositories retain their
own rules until deliberately migrated. Nothing here changes global rules.

## What pstack actually separates

pstack uses a mode plus named playbooks, not one slash command per playbook.
Its [help](../skills/poteto-help/SKILL.md) supplies example prompts without
starting work. We keep that discoverability in this guide, not a new router.

- [Opening a PR](../skills/poteto-mode/playbooks/opening-a-pr.md) is separate
  from [babysitting](../skills/poteto-mode/playbooks/babysit.md), which starts
  when requested and stops at merge-ready.
- [Shipping](../skills/poteto-mode/playbooks/shipping.md) is the landing stage.
  The babysit playbook explicitly routes merge/land/ship requests there.
- [Autopilot-stack](../skills/poteto-mode/playbooks/autopilot-stack.md) says
  “You own the stack, never the landing”; the operator lands it.
- [Autopilot-full](../skills/poteto-mode/playbooks/autopilot-full.md) owns the
  delivery loop, while retaining operator gates.

endstack preserves these decisions, not the upstream polling machinery, named
tools, model choices or decision-trail system. It deliberately requires a new
verdict after any revision change rather than reusing upstream patch-equivalence
exceptions. [Acceptance checks and limitations](delivery-checks.md) describe
what has actually been exercised.
