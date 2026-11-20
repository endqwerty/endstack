## 1. Pull request description

Title: Stream export rows in batches of 5,000

Body:

The export job in `jobs/export.py` loaded every order into memory. On the largest tenant, which has 2.1 million orders, the container killed it at 4 GB.

The job now reads rows through a server-side cursor and processes them in batches of 5,000. Start reading the diff at `jobs/export.py`.

Peak memory on the largest tenant dropped from 4.1 GB to 180 MB. Runtime dropped from 11 minutes to 9 minutes.

I considered raising the container memory limit and turned it down, because a bigger limit only delays the next kill as orders grow.

Tests: `pytest tests/jobs/test_export.py` reports 14 passed. One of them is new. It exports 12,000 rows and checks the CSV row count.

## 2. Chat reply

The export job no longer runs out of memory. It now streams rows in batches of 5,000 through a server-side cursor, so peak memory on the largest tenant fell from 4.1 GB to 180 MB and runtime fell from 11 to 9 minutes. I added a test that exports 12,000 rows and checks the CSV row count, and all 14 tests in `tests/jobs/test_export.py` pass. I did not raise the container memory limit, since that would hide the growth instead of fixing it. The batch size is set by the new `EXPORT_BATCH_SIZE` variable, which is documented in the README.

## 3. README section

## Export batch size for operators

The export job reads orders in batches. Set the `EXPORT_BATCH_SIZE` environment variable to change the number of rows in each batch. The default is 5000.

Lower the value if the export hits the database statement timeout. A smaller batch makes each query finish sooner.

Raise the value only if you have memory to spare. A larger batch uses more memory.
