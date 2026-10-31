Every prompt is a single piece of work, so I'd skip `swarm` for all five. Each reply is prose, so `unslop` applies throughout. The explicit-only helpers (`bro`, `ketchup`, `recall`, `reflect`, `sharpen`) stay closed because you named none.

1. **`archify`**: the PM only needs a picture of the order states. Nobody asked for a checked model or a bug path, so `statechart` is more than this needs.

2. **`statechart`**: you want a bug shown as a path through states, checked against a model, which is exactly its second use. If no model of the sync exists yet, `create-formal-verification-skill` could build one first.

3. **`archify`**: this is an architecture picture, not a state diagram. If I don't yet know the payment service's code, I'd open `how` first to learn the runtime flow.

4. **`tdd`**: it's a bug fix with a regression test, and the race is cheap to reproduce locally. `principles` also applies because this is stateful, branchy logic. `build` covers the implementation. `verify` runs before I call it done, since behaviour changes. `ship` stays closed unless you ask to merge.

5. **`create-formal-verification-skill`**: you asked me to prove a property that tests rarely reach (mutual exclusion in the lease protocol). `maintain-formal-verification-skill` doesn't apply unless a formal check already exists and the code changed since its recorded sync commit.
