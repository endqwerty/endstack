# endstack command cookbook

## What can I call?

Every skill in `skills/` is distributed through `homelab sync` from a pinned,
reviewed revision of endstack. The table lists the ones you call by name. A fresh agent session discovers them in its user
skill directory. Use a named command when you want a particular workflow; an
ordinary matching request can also select it automatically.

| Skill | Codex | Claude Code |
| --- | --- | --- |
| build | `$build` | `/build` |
| babysit | `$babysit` | `/babysit` |
| ship | `$ship` | `/ship` |
| ketchup-video | `$ketchup-video` | `/ketchup-video` |
| orchestrate | `$orchestrate` | `/orchestrate` |
| autopilot-full | `$autopilot-full` | `/autopilot-full` |
| verify | `$verify` | `/verify` |

These are prompts typed into the agent, not shell commands. In Codex, `/skills`
also opens skill selection. If a newly installed skill does not appear, start
a fresh session. In a wrapper that does not expand command syntax, ask to use
the named skill and check that the agent loads its installed `SKILL.md`.

| Skill | Use it for | Deliverable / stop |
| --- | --- | --- |
| [build](../skills/build/SKILL.md) | A feature or bug fix | Checked, independently verified non-draft PR; no watcher or merge |
| [babysit](../skills/babysit/SKILL.md) | Existing PR feedback and failed checks | Merge-ready PR; no merge. Status questions are read-only |
| [ship](../skills/ship/SKILL.md) | Explicitly landing identified work | Confirmed revision in its destination, or a named blocker |
| [ketchup-video](../skills/ketchup-video/SKILL.md) | Named video catch-up since your last message | Silent subtitled video, followed by all user decisions in text |
| [orchestrate](../skills/orchestrate/SKILL.md) | Named multi-day program under one coordinator thread | Owners build, verify and land each PR; explicit no-merge stops at merge-ready |
| [autopilot-full](../skills/autopilot-full/SKILL.md) | A bounded queue with explicit merge authority | Verified, landed items; held items remain held |
| [verify](../skills/verify/SKILL.md) | Independent evidence on an exact revision | Read-only pass / issues / not checked verdict; no merge authority |

The role skills (architect, swarm, tdd and the rest) install alongside them;
ROUTING.md says when each applies. Upstream's playbooks remain reference only.

## Install and update

Install the current homelab CLI from its checkout with `scripts/homelab install`
before the first sync; older CLI copies do not understand external sources.
Then run `homelab sync`, followed by `homelab sync --check`.
Homelab's `skill-sources.json` pins a reviewed endstack commit; it obtains that
source and installs copies into `~/.codex/skills` and `~/.claude/skills`.
The first fetch needs access to the private source repository. Cached checks
work offline; check and dry-run do not fetch or change files. Existing unmanaged
names are reported as conflicts rather than overwritten.

A missing private source blocks the whole sync until access is available.
Symlinked home, skill or cache ancestors are rejected. Each machine needs its
own install and discovery check. See [distribution evidence](distribution-checks.md)
for the tested machines and current limits.

For an update, change and review endstack first, then advance its exact commit
in the homelab manifest and sync again. Do not edit installed copies. One source
of truth remains here; installing from remote main without updating the reviewed
pin is intentionally not an automatic update mechanism.

## Copyable examples

Replace the bracketed details with your actual work. Examples use Codex's `$`
prefix; in Claude Code use `/` instead. Without installation, the fallback is
“Read [absolute path to endstack]/skills/[name]/SKILL.md” followed by the request.

**Build:**
> $build Fix [bug]; completion means [observable result].
> Prepare the PR for my review. Do not watch or merge it.

**Babysit:**
> $babysit Babysit [PR URL] until it is merge-ready.
> Handle real review findings and failed checks. Leave merging to me.

**One status check:**
> $babysit Is [PR URL] green? One read-only pass;
> do not change anything or start a watcher.

**Ship:**
> $ship [PR URL]

Invoking ship is the go-ahead: it lands the named work (or, with none named,
what the conversation built or the current branch's pull request) without
asking whether to. “Ship this PR” or “merge it” does the same. It grants
landing, not deployment. Missing checks, a stale or missing independent
verdict and operator holds still stop it, and it reports them rather than
asking. Merely asking how ship works does not execute it. Automatic
merge-when-ready needs its own explicit request and safeguards for the
verified revision; green checks alone do not grant it.

**Standing coordinator:**
> $orchestrate Own [program] through [checkable completion goal].
> Do not deploy or expand the program.

Invoking orchestrate grants landing authority for the program. It asks the
questions that could later hold a merge together before the first unit, with
defaults, then never asks whether to merge. The coordinator never edits code
or merges; each PR owner lands after an independent verdict on the current
head and required checks, and failed gates go back to owners. "Don't merge,
I'll land it" reserves landing. Deployment and destructive actions stay
excluded.

**Video catch-up:**
> $ketchup-video Catch me up since my last message.

**Full autopilot (the special case):**
> $autopilot-full Implement and merge only [A, B, C],
> in dependency order, after verification. I authorize those merges into
> [destination]. Hold [operator decision] for me. Do not deploy.

**Verify:**
> $verify Independently review [base..head] against
> [task and observable checks]. Change nothing; report evidence and limits.

**Help, not execution:**
> Explain which endstack skill fits [task] and draft a prompt. Do not start.

**Interview before a feature:**
> $interview I want [feature]. Question me before designing it, then propose
> the first design yourself and write the design doc.

**Goldfish a document:**
> $goldfish Test [path to design doc or AGENTS.md] on fresh readers with
> these tasks: [two to four tasks as I would ask them].

## Normal flow

Build → you review → optionally babysit → you merge, or explicitly ask ship.
For a dependent queue you land yourself, build each item on its parent's
branch. Choose autopilot-full only when you deliberately delegate landing.
(autopilot-stack, which built such a chain, was dropped on 2026-10-23 as unused.)
“Keep going”, unused allowance and ownership do not silently switch modes.
This repository now uses review-first delivery; other repositories retain their
own rules until deliberately migrated. Nothing here changes global rules.

## Where the split came from

pstack uses a mode plus named playbooks, not one slash command per playbook. The
playbooks live on as reference in [candidates/poteto-mode](../candidates/poteto-mode/SKILL.md):
opening a PR, babysitting (starts when requested, stops at merge-ready),
shipping (the landing stage), autopilot-stack ("You own the stack, never the
landing") and autopilot-full (owns the delivery loop, retains operator gates).

endstack preserves these decisions, not the upstream polling machinery, named
tools, model choices or decision-trail system. It deliberately requires a new
verdict after any revision change rather than reusing upstream patch-equivalence
exceptions. [Acceptance checks and limitations](delivery-checks.md) describe
what has actually been exercised.
