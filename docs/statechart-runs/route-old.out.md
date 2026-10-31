Each prompt gets the swarm check first, and I'd run `unslop` on this reply and on every reply. `bro`, `ketchup`, `recall`, `reflect` and `sharpen` run only when named, and none is named here.

1. **Checkout order states for the PM:** `how`, because the states come from the runtime flow in the code. No `swarm`, since it's one question with one answer. `unslop` applies because the PM reads the labels.

2. **"Synced" shown for an unsaved edit, checked against a model:** `create-formal-verification-skill`, because the request is to model-check a path through states. `how` first, to learn the real sync flow before modeling it. `maintain-formal-verification-skill` replaces the create skill if a formal check already covers this code and the code changed since its recorded sync commit. No `swarm`.

3. **Payment service architecture diagram:** `how`, for the flow and where each piece belongs. `architect` is for designing non-trivial changes, so it doesn't apply to describing what exists. I'd use `swarm` only if the service has several independent components worth reading in parallel.

4. **Fix the double-pickup race and add a regression test:**
   - `tdd`: it's a bug fix with a cheap local test, and a regression test was asked for. The test should fail first.
   - `build`: it's a change request.
   - `principles`: the job-claiming logic is stateful and branchy.
   - `verify`: it changes behavior, so a fresh read-only reviewer must pass it before I call it done.
   - `typescript-best-practices`: only if the files are `.ts` or `.tsx`.
   - `architect`: only if the fix grows past one function boundary.
   - Not `ship` or `autopilot-full`, since no merge was requested. No `swarm`.

5. **Prove the lease protocol never allows two writers:** `create-formal-verification-skill`, since this is a property to prove or model-check. `maintain-formal-verification-skill` replaces it if an existing check already covers the protocol and the code has changed since. `how` first to read the protocol. No `swarm`.
