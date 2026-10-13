# jobkit

A tiny in-memory job queue. A job is queued, then running, then done or failed.
A failed job can be retried until it has used `max_attempts`.

Run the tests with `python3 -B -m unittest`.
