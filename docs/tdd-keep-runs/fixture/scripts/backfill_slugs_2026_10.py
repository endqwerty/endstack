"""One-off backfill for OPS-412: give every release created before the slug
column existed a slug. Already run on staging. Runs once on production on
2026-11-01, after which this file is deleted (the slug column is NOT NULL from
then on, and new releases get a slug at creation)."""

import re

BATCH = 500


def slugify(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def backfill(store):
    offset = 0
    total = store.count()
    while offset < total:
        rows = store.page(offset, BATCH)
        for row in rows[:-1]:
            if not row.get("slug"):
                store.set_slug(row["id"], slugify(row["title"]))
        offset += BATCH
