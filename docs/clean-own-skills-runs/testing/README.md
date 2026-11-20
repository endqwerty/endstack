# Dry run: tdd merged into test-design

The question was whether the merged `test-design` still finds every consumer
with the same fault and writes the failing test first, as `tdd` did.

## Fixture

[mkfixture.sh](mkfixture.sh) `<empty dir>` builds the fixture. It is a small
Node shop. `orderTotalCents` in `src/lib/orders.js` counts refunded lines.
Two consumers share it: the CLI receipt (`src/cli/receipt.js`) and the mail
summary (`src/integrations/mail/summary.js`). The web invoice
(`src/web/invoice.js`) sums the lines in its own loop, with the same fault
and a different call spelling. The receipt also caps the total at
`chargedCents`, a downstream guard that the fix makes redundant.

Old arm: `tdd` and `test-design` from 05cad93, with the principles. New arm:
the merged `test-design` and the principles. Each arm ran on one fresh
agent, same model, one sample.

## Task (same for both arms)

> Follow the skill at `<arm>/skills/<tdd|test-design>/SKILL.md`. Bug report
> from a user: "The command-line receipt shows the wrong total when an order
> has a refunded line. Refunded lines should not count toward the total."
> Fix it. Commit as you go if the skill asks. Put what you would put in a
> pull request in your final reply, and list every test or commit command in
> order with its outcome.

## Results

| | Old (`tdd`) | New (`test-design`) |
| --- | --- | --- |
| Consumers found | receipt, mail (shared), invoice (own loop) | receipt, mail (shared), invoice (own loop) |
| Fixed the cause in the shared function | yes | yes |
| Invoice fixed | yes, now calls the shared function | yes, now calls the shared function |
| Redundant `chargedCents` cap deleted | yes | yes |
| Failing tests committed before the fix | yes, 5 tests | yes, 2 tests |
| Tests per shared implementation | one per consumer, 3 dropped later | one on the shared function, one on the invoice |
| Report lists consumers, kept and dropped tests | yes | yes |

Commit histories: [old-history.txt](old-history.txt) and
[new-history.txt](new-history.txt).

Both arms found both consumers of the shared fault and the separate
reimplementation. Both committed the failing tests before the fix. The new
arm wrote one regression test for the shared implementation and one for the
invoice. The old arm wrote one test per consumer and dropped three of them
in a fourth commit, so its history has one more commit and three throwaway
tests. One sample per arm is enough to show the merge kept the behaviour.
It cannot show that the smaller test count is a reliable improvement.
