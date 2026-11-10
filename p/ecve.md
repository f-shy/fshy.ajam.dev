# LZENX

> ecve.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ecve/ | JSON https://fshy.ajam.dev/api/v1/entity/ecve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LZENX｜资源小站

- `netdisk-pan/pan-ecve-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.ecve.cn/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.ecve.cn/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 6 root entries on OpenList v4.2.2 with base_path /游客分区, write:true advertised and denied.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 2
  - base_path: /游客分区
  - listing_sha256: 80259305
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.ecve.cn/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'LZENX｜资源小站'
  - probe:https://pan.ecve.cn/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 6 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.ecve.cn/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.ecve.cn/
