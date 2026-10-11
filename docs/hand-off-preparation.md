# Hand-off preparation

**Superseded (2026-10-10).** Historical research only, not current policy or an
installed skill. Daniel explicitly requested separate build, babysit, ship,
autopilot-stack and autopilot-full workflows. Read [the cookbook](cookbook.md)
and [DISTILL.md](../DISTILL.md) for the replacement. The recurrence objection
below was too broad for explicitly authorized core distillation. The proposed
automatic watcher and refusal to treat an explicit ship request as authority
were not adopted. The rest is retained as a record of the rejected design.

## Evidence before adding a skill

AGENTS.md requires the same failure to have appeared twice before adding a
skill. The reviewed sources do not yet establish that for `hand-off`:

- Homelab's CHANGELOG entry “2026-10-09 — careful-work removed” records
  crosspoint-reader #28: a very long description and log, and merging unchanged
  because the project rules already allowed it. Its workstation reference is
  the same incident, not another one.
- Endstack #1 merged without a current passing verdict. That is evidence for
  fixing `verify`, not a second instance of violating a no-merge boundary.
- Homelab's `delivery-policy.md` states the intended casebook boundary but
  does not identify a second violating pull request.

Do not invent recurrence or count one incident twice. Before promoting this
candidate to `skills/hand-off`, establish the second relevant failure or get
an explicit exception to the new-skill rule. The planned order is not itself
evidence that the recurrence condition has been met.

## Intended contract

- Own a checked, independently verified, non-draft pull request with a
  standalone description and a short verdict comment tied to its revision.
- Stop before merge, auto-merge, delivery-branch pushes or closing the pull
  request. “Ship it”, “autopilot” and “go on” do not override hand-off. Explicit
  current-task merge permission invokes the project's landing workflow;
  “don't merge” and “I'll review” select hand-off even in a land project.
- Use `verify` for review rules and exemptions rather than copying them.
  Missing checks or a current verdict remain unverified, not merge-ready.
- Keep the work branch and pull request; release only the project's prescribed
  artifacts. Use one harness watcher when available, without adding a polling
  loop. Check review comments against the artifact and batch proven fixes.
- Keep the skill around 2 KB and free of tool/model/provider names. Check the
  frontmatter as actual YAML, including quoting description values containing
  a colon followed by a space.

## Checks to run before promotion

These checks are planned, not run. Use paired with/without-skill tasks in both
harnesses with the same global rules, repository policy and `verify` revision.
Use a disposable surface that records attempted operations and resulting state.

1. Normal hand-off and vague “ship it” prompts: current checks/verdict,
   non-draft open pull request, standalone brief, branch retained, delivery
   branch unchanged; no merge, auto-merge, close or delivery-branch push attempt.
2. Missing reviewer, failing required check, or stale verdict: no merge-ready
   claim; an actual nonbehavioral exemption is recorded accurately.
3. Watch/release: reuse an existing watcher or start exactly one; release only
   required artifacts before yielding, without losing the work branch or PR.
4. Explicit override: quote current-task merge permission and follow the
   landing gates. A later task reverts to repository policy. A no-merge request
   in a land project still selects hand-off.
5. Negative triggers: research, a plan, or status-only inspection must not
   create a PR, start delivery or run cleanup. Explicit landing must not become
   an unconditional hand-off stop.

Retain deciding outputs and any successful baseline. Fixture decisions prove
neither installed discovery nor live delivery nor instruction enforcement.

## Upstream retention

Keep the upstream sources verbatim while callers remain, as AGENTS.md allows:
`skills/poteto-mode/playbooks/babysit.md`, `opening-a-pr.md`, `shipping.md`,
and `skills/show-me-your-work/` with its helper and references. They are linked
from the mode, sibling playbooks, help, and original guide. Shipping is also
input to `land`; hand-off does not replace the decision-trail contract.

Upstream's acceptance of “ship” as merge permission and its broad autonomy
wording conflict with the proposed narrow override. Preserve them as reference
material, but do not load them alongside a distilled delivery policy or install
the whole upstream collection. Distribution and global-rule migration remain
separate, untested work.
