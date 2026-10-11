# Create a note

Create note lets a user save a titled note from the browser or CLI, cancel an unfinished draft, and confirm the saved note from a second user-facing view.

## Sub-features

- `create-open` opens a blank editor from each browser entry point.
- `create-save` persists a title and body.
- `create-cancel` discards an unfinished browser draft.
- `create-cli` creates the same note shape from the terminal.

## How to get to it (user POV)

- Choose the `New note` button in the browser toolbar.
- Press `n` in the browser while focus is outside an editable field.
- Invoke the app's note-creation command with a title and body in a terminal.

## Driving it with the repository interaction recipe

Preconditions:

- Notes is healthy at `http://127.0.0.1:4173`.
- No note is titled `Release checklist`.
- The read-only instance health check reports the expected URL and disposable data directory.

- **Open editor.** Choose the button named `New note`. A form named `Note editor` appears with focus in the `Title` textbox.
- **Enter content.** Fill the `Title` textbox with `Release checklist` and the `Body` textbox with `Tag and publish`. The `Save note` button becomes enabled.
- **Save note.** Choose the `Save note` button. A status named `Note saved` appears and the heading reads `Release checklist`.
- **Confirm persistence.** Choose the `All notes` link, then the `Release checklist` link. The editor shows both saved values.
- **Cancel draft.** Choose `New note`, enter `Discard me` in `Title`, and choose `Cancel`. The note list returns and has no `Discard me` link.
- **CLI entry.** Create a second note through the terminal interface with title `CLI note`, body `Created from terminal`, and JSON output. Exit code `0` and stdout contain the new note ID and title.
- **Proof.** Reopen both saved notes from `All notes`. Capture an ARIA snapshot at `artifacts/create-note/list.aria.txt` and a screenshot at `artifacts/create-note/list.png`. The artifacts show `Release checklist` and `CLI note`.

## Gotchas

- Pressing `n` while a textbox has focus types the character instead of opening a new editor.
- Titles are trimmed on save. Assert the rendered title, not the draft input value.
- A save status alone is insufficient proof. Reopen the note from the list.
- Remove `Release checklist` and `CLI note` during fixture cleanup, but retain their proof artifacts.
