# Code Archaeology (history + in-repo)

## What this source contains

- Commit history (messages, dates, authors, diffs)
- PR descriptions, review comments, and discussion threads
- Inline code comments, TODOs, FIXMEs, deprecation notes
- ADRs (architectural decision records) if the repo keeps them
- Tests, whose names and assertions often encode the edge cases that motivated a change
- Related files modified in the same commits (co-change signal)
- CHANGELOG entries and release notes in the repo
- Issue/ticket IDs in commit messages and PR bodies

The most trustworthy source, tied directly to the code, and the most complete. Everything that went through the repo should be here.

## How to search it

Expand the seed commit list:

- Trace full history through file renames.
- Find commits that added or removed an exact string, or changed a matching pattern.
- Identify who last changed each relevant line and when.
- Read a substantive commit's full diff.
- Compare patches between two points affecting the target file.

For each substantive commit, pull the PR context:

Read complete commit messages to recover PR numbers. Read each PR's body, author, dates, labels, linked issues, review comments, discussion and changed files. Reviews and comments often hold the real rationale.

Look for out-of-band docs:

Search for architectural decision records in documentation, nearby TODOs and workaround comments with surrounding context, and tests referencing the target's symbols.

## What good evidence looks like here

- A PR description that explains the problem, not just the change ("This fixes the pagination bug that caused X")
- A long review thread where alternatives were debated
- An inline comment near the target line that explains a non-obvious constraint
- A test named `test_handles_edge_case_when_X` that reveals a motivating edge case
- A commit message that references a ticket or incident ID
- A CHANGELOG entry that summarizes the user-visible rationale

## Common pitfalls

- **Squash-merge flatlands.** Squashed PRs lose their branch commits. Fall back to the PR body and comments.
- **Misleading commit messages.** "Small refactor" sometimes hides an intentional behavior change. Look at the diff, not the message.
- **Cargo-culted patterns.** The author may have copied a pattern without understanding why. Check whether it originated earlier in the codebase, and investigate *that* commit.
- **Bot commits and auto-merges.** Dependabot, Renovate, and automated backports usually carry no motivation. Skip them when looking for intent.
- **Treating code as evidence of intent.** The code isn't evidence for why it exists. Evidence comes from commit messages, PRs, comments, tests, and docs. Don't cite "the function is named X" as evidence of intent.

## What to return

Every commit/PR/comment that bears on the question, with:
- The exact text (quoted)
- The hash / PR number / file:line
- Author and date
- Whether it's direct (explicitly addresses the question) or circumstantial
