# Distribution acceptance checks

Written before implementation, 2026-10-10. Scope: install the six reviewed
endstack skills through homelab sync, verify actual discovery in Codex and
Claude, and document usable invocation examples. Repository merge policies
and global instructions are not migrated in this step.

## Installer checks

1. Source of truth remains endstack. Homelab declares an immutable reviewed
   revision and an explicit six-name allowlist; no upstream skill is installed.
2. A first sync obtains that revision and installs byte-matching copies of the
   six skills to both agents. Sibling references resolve in the installed tree.
3. A second sync performs no writes; check and dry-run are read-only. An
   installed source can be checked offline.
4. Source acquisition failure, invalid pin/names, dirty cached source, missing
   skill, duplicate name or unmanaged destination conflict fails before any
   managed destination is modified or removed.
5. Existing homelab skills and vendor/unmanaged skills remain intact. Removed
   declared skills are cleaned up only where homelab owns them. Tests run on
   disposable homes and local repositories without network or credentials.

## Discovery and command checks

6. Fresh sessions on this machine discover all six skills from their actual
   installed locations, without a supplied catalog or repository-local copies.
7. Explicit invocation and ordinary matching prompts select the expected
   workflow. Status/help requests stop at information; stack/babysit/build
   preserve human landing; ship/full require their own authorization and gates.
8. Record startup/catalog and selection evidence separately from simulated
   decisions. These checks do not prove live merge/watch enforcement or another
   machine's installation. Preserve failures and successful baselines honestly.
9. The cookbook lists verified syntax for each agent, copyable prompts and
   stopping points, plus installation/update steps and limitations. Exercise a
   small real artifact where useful, preserving review-first delivery.

## Delivery

10. Independently review the homelab CLI change with a different provider, run
    its regression suite, publish only main to its existing private remote,
    install the CLI, run sync and confirm check passes. Endstack documentation
    goes through its own review-first PR. Keep durable evidence in each repo.

## Installer evidence

Homelab owns the implementation and its detailed `skill-distribution-checks.md`.
The source pin is `bb6bcee884644fb5db4d8cc9e57a301f56cace45` (merged PR #3).
The initial allowlist regression failed because old sync ignored the manifest.
The first implementation passed 132 tests, but independent Claude Opus 5.5
review reproduced three failures: inherited Git environment redirected source
acquisition into the caller's repository; index flags hid cached edits; checkout
conversion changed pinned bytes. That revision was held from installation.

Follow-up `6213168` isolates repository-local Git environment and compares
selected path sets and raw bytes with pinned objects. Transformed bytes fail
closed; manifest names reject case-fold collisions. The regression set against
the original implementation reported `FAILED (failures=16)`; the fixed full
suite reported `Ran 141 tests` / `OK`, also rerun by the parent. Claude Opus 5.5
independently passed `6213168` with no unresolved blockers. Its one further
finding (the test fixture's Git helper inherited repository environment) was
fixed in `6cd724b`, a test-and-docs-only commit: Claude re-ran the suite
(`Ran 142 tests` / `OK`) and confirmed that diff touches no installed code.
Homelab `main` and its private remote are both at `6cd724b`.

The parent reran real private GitHub acquisition on `6213168` in a disposable
home: `private_remote_acquisition: pass`, `pinned_blob_matches: 12`,
`first_writes: 19`, `second_writes: 0`, `status: all ok`. Exactly the six names
plus existing builtin skills were installed there. The temporary home was
removed; this was not a real-home installation.

## Discovery checkpoint

Before installation, a fresh Codex 0.162.1 app-server in a temporary non-repo
workspace returned `found: [], count: 0` for the six names through `skills/list`
with `forceReload: true`. This was actual runtime discovery, without a supplied
catalog.

## Installed state (2026-10-10, this machine only)

- `homelab sync --check` reports `ok` for all six skills in both
  `~/.codex/skills` and `~/.claude/skills`.
- The same Codex `skills/list` query from a non-repo workspace now returns all
  six names (`autopilot-full`, `autopilot-stack`, `babysit`, `build`, `ship`,
  `verify`; 15 skills in total). A Claude Code session started afterwards lists
  the same six in its skill catalog.

## Not checked

- Automatic (unnamed) selection by an ordinary matching prompt: the run that
  would test it ended when Codex hit its usage limit (resets 2026-10-13).
- Remote merge/watch enforcement, another machine's installation, macOS.
- Verification of this documentation by a different provider: docs are exempt
  under [verify](../skills/verify/SKILL.md), and Codex was unavailable anyway.
