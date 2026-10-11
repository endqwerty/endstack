## Audit the log against the transcript

At the end of the run, before handing back, check the log told the truth. Read this run's transcript from the active workspace-scoped location provided by the harness. Never search unrelated workspaces or private chats. If the transcript is unavailable, disclose that this audit could not be completed. Walk this run's rows against what actually happened. Each stretch of them begins at one of this run's `start` rows, or at the first row if this run created the log, and ends at the next `start` row of another run:

- Check that every row maps to a real decision or action.
- Check that each row's evidence resolves and shows what the row claims.
- A fork, pivot, or abandoned approach that shaped the work but isn't logged is a gap. Add it.

Correct the log, not the story. The audit never edits or removes a row, even an invented one. When a row records neither a real decision nor a real action, or its claim or evidence is wrong, add a row that supersedes it with what actually happened and a pointer that resolves. This audit does not check rows outside this run's stretches. If this run's own work shows one of them is wrong, supersede it like any wrong call.

## Cross-model review of the trail

Before handing back, give the trail to a separate reviewer on a different model family from yours, if available; otherwise say the review is not independent. Self-review is not a substitute. The reviewer reads the audit trail and the run's transcript, then flags what the user should pay attention to. Not a redo of the work, a scan for what's suboptimal or risky.

- Decisions logged with weak or absent evidence.
- Verification steps skipped or claimed without proof in the transcript.
- Choices that look risky in hindsight (premature, scope-creeping, papering over a symptom).
- Gaps the user would otherwise miss on a casual skim.

Every reply for a run that produced a trail ends with an "Attention" section. Lead with the reviewer identity and independence limits on their own line, then list each flag pointing to specific rows or moments. "No flags" is a valid value. An unnamed or falsely independent reviewer is not.

## Reviewing the trail

Read top to bottom, follow the evidence pointers, spot-check. Use a tabular viewer for the TSV; committed copies can be reviewed alongside the change.

## Composing this skill

Other skills route their audit trail here instead of inventing one. Reference it by name and let it own the format. Don't restate the columns.
