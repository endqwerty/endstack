# Catalog size

## Why (2026-10-14)

homelab's `skill-usage` measurement (homelab `skill-usage.md`) found that
Codex listed every endstack skill's description in every request, about 2,060
tokens, while Claude Code listed only the six without
`disable-model-invocation`. The rule here said explicit-invocation skills cost
no catalog space; that held for Claude Code only. Since the routing table,
endstack skill text was 5.3% (Mac) and 8.3% (omarchy) of Codex input tokens,
the catalog a third of it.

## What changed

- Each of the 24 explicit-invocation skills has `agents/openai.yaml` with
  `policy: allow_implicit_invocation: false`. Codex's own skill documentation
  says such a skill "is not injected into the model context by default, but can
  still be invoked explicitly". The routing table already tells agents to read
  a skill that is not in their list from the skills directory, as Claude Code
  agents do today.
- Every description is at most 200 characters (6,879 characters in total
  before, 2,835 after). The six visible skills keep their trigger boundaries;
  the hidden ones are one line, since they are reached by name.
- `scripts/check-skills.py` enforces both: an explicit skill without the policy
  file, a visible skill with any `agents/openai.yaml`, and a description over
  200 characters are problems. The policy file must be byte for byte
  `policy:` / `  allow_implicit_invocation: false`: comparing text rather than
  reading YAML means no hand-written parser can disagree with Codex's (review
  rounds 2 and 3 found four ways one could). Tests in `scripts/test_check_skills.py`, written and seen failing
  before the checker changed.

| Catalog per request (endstack entries) | Before | After |
| --- | --- | --- |
| Codex | 30 entries, about 2,285 tokens | 6 entries, about 350 tokens |
| Claude Code | 6 entries, about 415 tokens | 6 entries, about 291 tokens |

Estimates at 4.0 (Codex) and 3.6 (Claude) characters a token, counting
Codex's `(file: ...)` suffix.

## Checks

- A probe in a throwaway repository with two project skills, one with a
  policy-only `agents/openai.yaml`: the Codex 0.162.1 rollout's skill list
  named the visible probe and not the hidden one. A live rollout on the Mac
  likewise lists `imagegen` and `skill-creator` but not `review-agent`, the one
  Codex system skill with the policy set to false.
- `python3 scripts/check-skills.py` and `check-routing.py`: 0 problems.
  `python3 -m unittest discover -s scripts`: 16 tests pass.
