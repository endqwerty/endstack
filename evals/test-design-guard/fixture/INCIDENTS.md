# Incidents

- 2026-11-03: `POST /admin/refunds` shipped with no permission; a support account issued refunds. Fixed by hand, then it regressed in a refactor.
- 2026-11-19: `PUT /admin/flags` shipped with no permission; anyone signed in could flip feature flags.

Every route under /admin must require a permission. New admin routes are added most weeks.
