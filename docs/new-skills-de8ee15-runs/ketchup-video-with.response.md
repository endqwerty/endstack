**Test artifact — slide plan (planning only)**

Scope: everything since “Fix the checkout total and let me choose how receipts look.” The earlier catch-up does not reset that window. This is one connected catch-up; no delegation is needed.

Takeaway: The checkout fix is ready for a merge decision, and detailed receipts are the recommended choice.

Use two slides on a persistent checkout-and-receipt canvas. All captures below are fixture references; nothing is rendered or inspected in this dry run.

1. **Checkout correction.** Place `before.png` and `after.png` side by side, highlighting only the total changing from $99 to $100 for the same cart. Use an arrow between the totals; do not imply other visible changes. Subtitle: “The same cart now totals correctly at the exact-$100 boundary.” Planned hold: eight seconds.
2. **Receipt choice.** Keep the corrected checkout visible as an anchor and expand its receipt area into the existing `compact.png` and `detailed.png` captures. Label them **Compact** and **Detailed**. Under Compact: “Less space; hides line-item tax.” Under Detailed: “More space; shows line-item tax.” Subtitle: “Choose the receipt layout; detailed makes the tax easier to see.” Planned hold: twelve seconds.

These are proposed holds, not measured playback. A real render would require checking frames, readability, subtitle placement, and added-word counts before embedding. The subtitle strip would stay below the pictures at a consistent height. No video exists in this test.

**Proposed reply shape**

You have two decisions: choose a receipt layout and decide whether to merge the checkout fix.

**[Video placeholder — not rendered; no video artifact exists.]**

I can check the second receipt preview job later; it is still running, and its result is unknown.

- **Choose receipts: Compact or Detailed.** Compact saves vertical space but hides line-item tax. Detailed takes more space and shows line-item tax; I recommend **Detailed** for clarity. The existing captures show both choices, but the currently selected layout is unknown. If you do not choose, checkout is not blocked; which receipt layout remains in effect is unknown.
- **Merge the [checkout fix PR](https://example.invalid/pr/1).** It corrects the exact-$100 boundary. The deterministic test passes, and an independent review passed on current head `abc123`; the PR is merge-ready. I recommend merging. The captures show the same cart changing from $99 to $100, with no other visible changes. Remaining risk beyond that evidence is unknown. Merge awaits your decision; without it, the PR stays unmerged.