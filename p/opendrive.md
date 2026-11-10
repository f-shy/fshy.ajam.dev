# OpenDrive

> opendrive.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opendrive/ | JSON https://fshy.ajam.dev/api/v1/entity/opendrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenDrive

- `storage/opendrive` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.opendrive.com/
- free tier: 5 GB free (100 MB max file size, 1 GB/day bandwidth); 'Unlimited' storage/bandwidth/file-size starts at $12.95/month | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free plan is capped at 1 GB/day bandwidth. A hard daily meter, not a throttle. Paid Personal Unlimited claims 'Unlimited Storage, Bandwidth, File Size'. | metered: no
- identity: card
- interface: rest, webdav, rclone
- limits:
  - per-ip-shaping: 1 GB/day [1]
  - per-ip-shaping: 200 KB/s [1]
  - per-object-cap (binding): 100 MB per file [1]
- limits note: 100 MB per file, 1 GB/day download, 200 KB/s on free. Hotlinking is offered as a feature but only meaningful with paid bandwidth.
- interface detail: webdav
- tooling: Native rclone backend 'opendrive' (Tier 1); WebDAV at webdav.opendrive.com; documented REST API at opendrive.com/api.
- composes with: 5 GB x unlimited accounts, but 1 GB/day egress per account means serving 1 TiB/day needs ~1000 accounts. Shard the serving layer, not just storage.
- reliability: Existing since 2011 and still alive; free tier is deliberately vestigial (100 MB files cannot hold useful datasets).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 5 GB free (100 MB max file size, 1 GB/day bandwidth); 'Unlimited' storage/bandwidth/file-size starts at $12.95/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: (raw HTML) — 'Personal Free Get Started 5GB Online Storage 5 GB Storage, 100 MB Max File Size, 1 GB/Day Bandwidth, 200 KB/s Speed'
  - [1] 2026-10-21: 'Personal ... Unlimited Online Storage / Unlimited Storage, Bandwidth, File Size' at $129/year
  - [2] 2026-10-21: probe: OPTIONS -> 401 Unauthorized, WWW-Authenticate: Basic realm="OpenDrive", serverid: s1 — WebDAV endpoint live
  - [3] 2026-10-21: Opendrive listed Tier 1, R/W, hash md5
- sources:
  - [1] https://www.opendrive.com/pricing
  - [2] https://webdav.opendrive.com/
  - [3] https://rclone.org/overview/
