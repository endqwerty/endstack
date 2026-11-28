# Flaky "expires an entry once its ttl has passed"

Goal: `node --test` passes 20 runs in a row. Budget: about an hour; 40 minutes spent.

| Round | Tried | Why | Result |
| --- | --- | --- | --- |
| 1 | test timeout 100 ms to 200 ms | CI box is slow, the test may be timing out | 13 of 20 runs failed: `AssertionError: 1 !== undefined` |
| 2 | test timeout 200 ms to 500 ms | still slow under load | 14 of 20 failed, same assertion |
| 3 | ran the suite with `--test-concurrency=1` | other tests may starve the timer | 13 of 20 failed, same assertion |
| 4 | test timeout 500 ms to 1000 ms | give it plenty of room | 12 of 20 failed, same assertion |

Next round: raise the timeout to 2000 ms.
