## 1. Pull request description

Title: Stream order export in batches to fix out-of-memory kill

Why: The export job in `jobs/export.py` loaded every order into memory. On the largest tenant (2.1 million orders) the operating system killed it at 4 GB.

What changes: The job now reads rows with a server-side cursor in batches of 5,000 and writes each batch to the CSV before fetching the next. Start reading at `jobs/export.py`.

Result on the largest tenant:
- Peak memory dropped from 4.1 GB to 180 MB.
- Runtime dropped from 11 minutes to 9 minutes.

Tests: `pytest tests/jobs/test_export.py` reports 14 passed. One of them is new. It exports 12,000 rows and checks the CSV row count.

Turned down: Raising the container memory limit. Memory use would keep growing with order count, so the job would be killed again on a larger tenant.

## 2. Final chat reply

The export job no longer runs out of memory. It now reads orders in batches of 5,000 through a server-side cursor instead of loading all 2.1 million into memory. On the largest tenant, peak memory fell from 4.1 GB to 180 MB and runtime fell from 11 minutes to 9 minutes. All 14 tests in `tests/jobs/test_export.py` pass, including a new one that exports 12,000 rows and checks the CSV row count. I did not raise the container memory limit, because memory use would keep growing with order count.

## 3. README section

## For operators: export batch size

The export job reads orders in batches. Set the batch size with the `EXPORT_BATCH_SIZE` environment variable. The default is 5000.

Lower the value if the export hits the database statement timeout. Each batch then takes less time to fetch.

A higher value uses more memory, because the job holds one full batch in memory at a time.
