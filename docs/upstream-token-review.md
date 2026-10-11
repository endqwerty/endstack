# Upstream prompt reduction — 2026-10-10

Reviewed [pstack PR #538](https://github.com/cursor/plugins/pull/538), merged as
`00b14f1df36b32a8dd1529324a3a459f6563b127` on October 10. It reports 169,348 to
153,004 bytes (-9.7%) and 26,177 to 23,829 words (-9.0%) across 35 Markdown
files. Those are source-size measurements, not measured end-to-end token or
cost reductions. Model defaults and reviewer panel composition did not change.

## Already present

Our retained source snapshot is the later `978ca6e`. Comparing each of the 35
changed Markdown files with the upstream commit's blob IDs found **35 byte-exact
matches**. No upstream refresh is needed to obtain this revision.

The six endstack skills total 11,452 bytes, individually 1,746–2,087 bytes.
They are separate workflows; the retained 19,341-byte poteto-mode is excluded
from installation. These sizes describe different artifacts, not a measured
percentage saving for equivalent tasks.

## What changed upstream

- Removed repeated introductions and recaps when the steps already said the
  same thing; condensed phrasing while retaining operational requirements.
- Stated principle and playbook filename conventions once in each index,
  replacing repeated names and paths. Leaves are opened for the applicable task.
- Consolidated output requirements rather than repeating them in every step
  and again at the end. The PR brief carries conclusions; linked artifacts
  carry lengthy evidence.
- Corrected an interface mismatch: architect now asks for the architectural
  explanation that how actually produces.

## Recommended endstack follow-up

1. **Audit repetition before adding policy.** Keep one authoritative statement
   of a gate and short references from callers. Start with verify's repeated
   evidence/current-revision wording. Preserve the explicit independent-provider,
   current-revision, blocker and merge-authority requirements. A byte target is
   not grounds to remove a rule.
2. **Finish distribution before shrinking global instructions.** The global
   homelab agent file is 6,910 bytes and repeats verification/delivery material.
   Only replace that material with pointers after fresh installed discovery and
   pointer-only dry runs prove both agents load the required policy. That is a
   separate migration, already gated in DISTILL.md.
3. **Keep detailed teaching outside runtime skills.** Cookbook examples, pstack
   comparisons and regression evidence belong in docs. A skill needs the trigger,
   decisions, deliverable and stopping point. Our six-workflow split already
   follows this direction; a new routing skill is not justified.
4. **Reduce repeated orchestration context.** Pass the task, exact revision,
   checks and relevant artifact paths. Return findings and deciding output.
   Avoid retransmitting whole tool catalogs, diffs and prior transcripts when a
   focused read suffices. This is an application of upstream's consolidation
   approach, not a new feature claimed by #538.
5. **Measure a candidate before adoption.** Compare original and shortened
   text against the same trigger and authority cases, record actual input/output
   usage where available, and reject versions that miss a gate. Bytes and words
   are useful screening metrics, but do not establish runtime savings.

The immediate recommendation is a controlled prose pass on the existing six
skills after distribution. Keep mandatory checks and current-revision review.
No model-routing change, new skill, skill-text rewrite, or global-policy
migration is made by this research note.
