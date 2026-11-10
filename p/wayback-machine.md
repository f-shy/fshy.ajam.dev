# Wayback Machine

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wayback-machine/ | JSON https://fshy.ajam.dev/api/v1/entity/wayback-machine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wayback Machine — Save Page Now 2 (capture API)

- `storage/wayback-machine-save-page-now-2` | fails-quota | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://web.archive.org/save
- free tier: No storage quota; Retention is effectively permanent. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object at 2GB | bytes: 2000000000 | source: [1] | note: not stated
- retention: No storage quota; Retention is effectively permanent | source: [1] | note: not stated
- egress: Free, via web.archive.org replay with Range support | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): per-object at 2GB [1]
- limits note: 2GB max resource; 10s connect timeout; 50s capture / 2m total; 12 concurrent captures (authenticated), 6 anonymous; 10 captures per URL per day; redirects max 3; robots-blocked URLs rejected; delay_wb_availability=1 defers visibility ~12h.
- interface detail: rest
- tooling: SPN2 REST API (POST https://web.archive.org/save, job_id polling); wrappers palewire/savepagenow, akamhy/waybackpy, overcast07/wayback-machine-spn-scripts
- composes with: In practice bounded by concurrency (12 concurrent authenticated).
- reliability: Live probe now returns 401 'You need to be logged in to use Save Page Now' for anonymous POST, so the 4k/day anonymous allowance in the 2022 spec is stale; the plain GET /save/<url> path returned 429 on first try.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No storage quota; Retention is effectively permanent.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Max resource size = 2GB', 'Max captures per day for authenticated users = 100k', 'Max concurrent captures = 12'
  - [2] 2026-10-21: probe: POST (anonymous, Accept: application/json) -> HTTP 401 {"message":"You need to be logged in to use Save Page Now."}
  - [3] 2026-10-21: probe: GET -> HTTP 429 TOO MANY REQUESTS
  - [4] 2026-10-21: (snapshot 2023-11-06) — 'no more than 15 per minute ... we will block Save Page Now requests from your IP number for one day'
- sources:
  - [1] https://gist.github.com/regstuff/82e690db2f1d91ba59f6681c1abad6cf
  - [2] https://web.archive.org/save
  - [3] https://web.archive.org/save/https://example.com/
  - [4] https://archive.org/post/1103865
