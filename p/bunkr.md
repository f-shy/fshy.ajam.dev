# Bunkr

> bunkr.cr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bunkr/ | JSON https://fshy.ajam.dev/api/v1/entity/bunkr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bunkr

- `storage/bunkr` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bunkr.cr
- free tier: No total quota published; 2 GB maximum per file. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2 GB maximum per file | bytes: 2000000000 | source: [1] | note: not stated
- retention: Inactive files deleted 30 days after last visit | days: 30 | source: [1] | note: not stated
- egress: No stated cap. | metered: no
- identity: anonymous
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file [1]
  - retention-clamped: deleted 30 days [1]
- limits note: 2 GB per file (hard, on the landing page). Requires login to upload ('Running in private mode. Login to upload'). Inactive files deleted 30 days after last visit. Explicitly bans movies/TV shows.
- interface detail: wrapper-only
- tooling: No official API. Web upload requires login; community tools (bunkr-downloader / gallery-dl extractors) exist but are third-party and fragile.
- composes with: Unlimited accounts x unlimited files at 2 GB each. 2 GB/file x N files is enough for bulk media; retention needs activity every 30 days.
- reliability: Small per-file cap and login-gated uploads make it poor for datasets; the 30-day activity rule plus a ban list that covers most large media means files disappear for reasons outside your control. Domain rotates (.cr/.ru/.su).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No total quota published; 2 GB maximum per file.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Login to upload ... Maximum upload size per file is 2 GB'
  - [2] 2026-10-21: 'Inactive files will get deleted 30 days after the last visit'
  - [1] 2026-10-21: probe: GET -> 200
- sources:
  - [1] https://bunkr.cr/
  - [2] https://bunkr.cr/faq
