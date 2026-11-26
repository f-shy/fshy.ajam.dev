# neon

> neonscience.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neonscience/ | JSON https://fshy.ajam.dev/api/v1/entity/neonscience.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## neon

- `storage/neon-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:48.162Z (live) | stale on 2026-12-04
- url https://data.neonscience.org/api/v0/sites
- free tier: none reachable: Read-only observatory API (verified live) serving instrument data from fixed sites. No ingest endpoint for outside data. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Read-only observatory API (verified live) serving instrument data from fixed sites. No ingest endpoint for outside data.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Read-only observatory API (verified live) serving instrument data from fixed sites. No ingest endpoint for outside data.
  - [1] 2026-11-19: the NEON sites endpoint is a live read-only listing of fixed observatory sites | capture: sha256:6fedf9b18a0090da6e70e074e7031295d7e49495b78895a708ccafb96a92e35a | quote: "siteCode":"ABBY","siteName":"Abby Road NEON","siteType":"GRADIENT"
- sources:
  - [1] https://data.neonscience.org/api/v0/sites
