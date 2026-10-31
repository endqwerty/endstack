class Store:
    """In-memory stand-in for the release database."""

    def __init__(self, releases):
        self._rows = [dict(r) for r in releases]

    def count(self):
        return len(self._rows)

    def page(self, offset, limit):
        return self._rows[offset:offset + limit]

    def set_slug(self, release_id, slug):
        for row in self._rows:
            if row["id"] == release_id:
                row["slug"] = slug
