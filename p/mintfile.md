# Mintfile

> mintfile.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mintfile/ | JSON https://fshy.ajam.dev/api/v1/entity/mintfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mintfile

- `storage/mintfile` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mintfile.com
- free tier: Up to 300 GB per transfer, free, no sign-up, 100 files per transfer. There is no total-storage account at all. It is a per-transfer envelope. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 300 GB per transfer, 100 files per transfer, retention selectable 3 to 100 days then auto-delete | days: 100 | source: [1] | note: not stated
- egress: No monthly transfer caps stated: 'no sign-up, no monthly transfer caps'. No egress price. | metered: no
- identity: anonymous
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
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'up to 300GB ... up to 100 files per transfer, kept up to 100 days'; 'Pick a retention window from 3 to 100 days'
- sources:
  - [1] https://mintfile.com/
