# 平凡

> iosi.vip | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iosi/ | JSON https://fshy.ajam.dev/api/v1/entity/iosi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 平凡

- `netdisk-pan/pan-iosi-vip` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.iosi.vip/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.iosi.vip/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 6 root entries on AList v3.45.0, write:false, read-only by configuration.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 352f2d5d
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.iosi.vip/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '平凡'
  - probe:https://pan.iosi.vip/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 6 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.iosi.vip/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.iosi.vip/
