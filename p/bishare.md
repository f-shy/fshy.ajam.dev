# BIShare

> bishare.app | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bishare/ | JSON https://fshy.ajam.dev/api/v1/entity/bishare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BIShare

- `storage/bishare` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bishare.app
- free tier: 100 GB per transfer by link, no account on either side; unlimited size device-to-device on the same LAN (nothing uploaded). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 100 GB | bytes: 100000000000 | source: [1] | note: not stated
- retention: Retention: 6, 12 or 24 hours, or after first download | days: 1 | source: [1] | note: not stated
- egress: free; delivery is via their link service or direct LAN. | metered: no
- identity: anonymous
- interface: unknown
- limits:
  - retention-clamped: Retention: 6, 12 or 24 hours [1]
  - per-object-cap (binding): per-object-cap: 100 GB [1]
- limits note: per-object-cap: 100 GB by link. Retention: 6, 12 or 24 hours, or after first download. That is the shortest retention of any 100 GB-class service found.
- interface detail: none
- tooling: Apps for iOS/Android/Windows plus a browser page. No documented API; the LAN path is a local protocol, not a storage interface.
- composes with: 100 GB x unlimited transfers, but every link self-destructs in 6/12/24 hours. The LAN mode is a file-transfer convenience, not storage.
- reliability: Open source and E2E encrypted, but retention is measured in hours. Useful as a staging/burner channel, never as storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 GB per transfer by link, no account on either side; unlimited size device-to-device on the same LAN (nothing uploaded).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Up to 100 GB, free', 'link expires in 6, 12 or 24 hours'
  - [1] 2026-10-21: retention and 100 GB per-transfer table, checked 2026-10
- sources:
  - [1] https://bishare.app/send-large-files
  - [2] https://bishare.app/transfer
