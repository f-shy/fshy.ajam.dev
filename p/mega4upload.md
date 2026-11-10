# Mega4up

> mega4upload.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mega4upload/ | JSON https://fshy.ajam.dev/api/v1/entity/mega4upload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mega4up

- `storage/mega4up` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mega4upload.net
- free tier: Free registered: 183 GB storage, 3,000 Mb per file, download volume Unlimited; files deleted 150 days after last download | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 3,000 Mb per file | bytes: 3000000000 | source: [1] | note: not stated
- retention: Free registered: 183 GB storage, 3,000 Mb per file, download volume Unlimited; files deleted 150 days after last download | days: 150 | source: [1] | note: not stated
- egress: 'Download volume: Unlimited' on the free registered row; anonymous row unlimited too | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 3,000 Mb per file [1]
  - retention-clamped: deleted 150 days [1]
- limits note: 200 Mb anonymous, 3,000 Mb registered; 183 GB pool; 150-day retention after last download; unlimited download volume
- interface detail: rest
- tooling: XFileSharing Pro; /api/upload/server responds {"status":401,"msg":"Unauthorized"} without a key; PolyUploader lists Mega4up (200 MB anon / 15 days per its table)
- composes with: 183 GB per free registration, so each registration holds the same 183 GB; the host also runs a paid-per-download rewards program, which is why free storage is offered at all
- reliability: site is ad-monetised and pivots frequently; the 183 GB is per account, not per file, so reaching scale takes several accounts
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free registered: 183 GB storage, 3,000 Mb per file, download volume Unlimited; files deleted 150 days after last download
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free 200 Mb / '—' / Unlimited / 45 days; Registered 3000 Mb / 183 GB / Unlimited / 150 days; Premium Unlimited
  - [2] 2026-10-21: probe: GET -> 200 {"msg":"Unauthorized","status":401}
  - [3] 2026-10-21: 'Upload without an account, share without size limits'
- sources:
  - [1] https://mega4upload.net/premium.html
  - [2] https://mega4upload.net/api/upload/server?utype=anon
  - [3] https://mega4upload.net/
