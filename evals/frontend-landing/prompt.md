---
name: frontend-landing
tags:
- gemini-frontend-design
runs: 2
max_turns: 30
timeout_seconds: 900
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
---

Build a one-page website for Tidewater Cycles, a bicycle repair shop on the harbour front of a small fishing town. Facts: same-day tune-ups booked before 10am; wheel truing and rebuilds; e-bike motor and battery service; a loan bike while yours is in the shop; open Tuesday to Saturday, 8am to 6pm; 14 Quay Street; phone 01632 960 418. The owner, Mara Lind, has run it since 2009. The page should let a visitor book a repair and see prices: tune-up 45, full service 95, wheel true 20, e-bike diagnostic 30 (pounds).

Write it as a single `index.html` with inline CSS and any JavaScript inline. There is no server, no image files and no remote. Do not ask questions; finish and summarize.
