Write three pieces of text, applying the skill you were given. Use only these facts.

1. A pull request description (title plus body). Facts: the export job in `jobs/export.py` loaded every order into memory and was killed at 4 GB on the largest tenant (2.1 million orders). The change streams rows in batches of 5,000 with a server-side cursor. Peak memory on the largest tenant dropped from 4.1 GB to 180 MB; runtime went from 11 min to 9 min. Tests: `pytest tests/jobs/test_export.py` 14 passed, including a new test that exports 12,000 rows and checks the CSV row count. Turned down: raising the container memory limit (hides the growth).
2. A final chat reply to the user after finishing that work (3 to 6 sentences).
3. A README section titled for operators, explaining the new `EXPORT_BATCH_SIZE` environment variable (default 5000; lower it if the database statement timeout is hit; higher values use more memory).
