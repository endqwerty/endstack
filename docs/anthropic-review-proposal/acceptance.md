# Acceptance checks recorded before drafting

- Every attributed recommendation has an opened primary source; unsupported
  claims remain labelled unsupported, not disproven.
- The proposal preserves the current provider requirement, review trigger,
  carry-forward, merge authority and two-round rethink pending Daniel's choices.
- Existing mechanical checks pass. A temporary application of the proposed
  patch also passes check-skills.py and check-routing.py.
- Fresh, isolated baseline and candidate reviewers see the same spec, code,
  diff and smoke-test command, without author reasoning or the answer key.
- Observable acceptance: both injected contract defects are found with a
  reproducer; stylistic and future-only suggestions do not become required
  fixes; unavailable runtime evidence stays not checked; a clean result is
  allowed. Equal baseline/candidate outcomes mean no demonstrated improvement.
- A separate cross-provider reviewer checks the final report, proposed patch,
  dry-run evidence and limits. No production policy is installed by this PR.
- Deliver committed research and exact proposal in an unmerged PR.
