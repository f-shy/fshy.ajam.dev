# Mintfile

> mintfile.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mintfile/ | JSON https://fshy.ajam.dev/api/v1/entity/mintfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mintfile

- `storage/mintfile` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:25.164Z (live) | stale on 2026-11-25
- url https://mintfile.com
- free tier: Up to 300GB, sent as-is | unit: mixed | metered on: stored-bytes | read on: 2026-11-09 | source: [1] | note: Free, no sign-up, no monthly caps.
- per-object cap: source: [1] | note: not stated
- retention: Pick a retention window from 3 to 100 days. | days: 100 | source: [1] | note: the page's embedded plan data lists retention options by plan: anonymous [3,5,7,14,30]; free_registered and paid [3,5,7,14,30,60,100]
- egress: No monthly transfer caps stated: 'no sign-up, no monthly transfer caps'. No egress price. | metered: no
- identity: anonymous | detail: Free, no sign-up, no monthly caps.
- interface: rest, rclone
- limits:
  - retention-clamped (binding): retention selectable 3 to 100 days [1]
  - retention-clamped (binding): Retention max 100 days [1]
- limits note: 300 GB per transfer, 100 files per transfer, retention selectable 3 to 100 days then auto-delete. Every upload is security-scanned before publish, so flagged content never appears.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Web only; no documented API, no rclone backend.
- composes with: 300 GB x unlimited transfers, but retention is 3-100 days, so accumulation requires a re-upload loop. Useful as a transit leg, not a store.
- reliability: Retention max 100 days plus a mandatory malware scan on every file makes this a transfer service; a large binary dataset may be held for scanning before the link works.
- notes: Up to 300 GB per transfer, free, no sign-up, 100 files per transfer. There is no total-storage account at all. It is a per-transfer envelope.
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'up to 300GB ... up to 100 files per transfer, kept up to 100 days'; 'Pick a retention window from 3 to 100 days'
  - [1] 2026-11-09: the page states up to 300 GB per transfer | capture: sha256:fd14562e444cc183c191c8d57ca3faca6ef55e09045fc471bfcc00f66648ada2 | quote: Up to 300GB, sent as-is
  - [1] 2026-11-09: the page states the transfer is free with no sign-up and no monthly caps | capture: sha256:ffa56fa4055f43a95b8f2e1567d131d6fadbfc6a29c82bc94b3cc93a60cfe890 | quote: Free, no sign-up, no monthly caps.
  - [1] 2026-11-09: the page states up to 100 files per transfer kept up to 100 days | capture: sha256:fd14562e444cc183c191c8d57ca3faca6ef55e09045fc471bfcc00f66648ada2 | quote: up to 100 files per transfer, kept up to 100 days
  - [1] 2026-11-09: the page states a retention window from 3 to 100 days | capture: sha256:fd14562e444cc183c191c8d57ca3faca6ef55e09045fc471bfcc00f66648ada2 | quote: Pick a retention window from 3 to 100 days.
  - [1] 2026-11-09: the embedded plan data lists retention options by plan: anonymous 3-30 days, free_registered and paid 3-100 days | capture: sha256:ffa56fa4055f43a95b8f2e1567d131d6fadbfc6a29c82bc94b3cc93a60cfe890 | quote: retention:{byPlan:{anonymous:[3,5,7,14,30],free_registered:[3,5,7,14,30,60,100],paid:[3,5,7,14,30,60,100]}}
- sources:
  - [1] https://mintfile.com/
