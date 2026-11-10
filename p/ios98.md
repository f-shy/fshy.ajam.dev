# 美辰云盘

> ios98.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ios98/ | JSON https://fshy.ajam.dev/api/v1/entity/ios98.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 美辰云盘

- `netdisk-pan/pan-ios98-com` | fails-egress | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.ios98.com/
- free tier: anonymous guest read of 11 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): write accepted but the read-back is signed probe:https://pan.ios98.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: The read-gated write. PUT returns code 200 with message success, and GET /p/ then returns 51 bytes of code 401 expire missing: the instance signs its raw path and a guest cannot mint the signature. Provider 139Yun. The bytes went in and cannot come out.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: read-gated
  - upstream_provider: 139Yun
  - fronting_cdn: nginx
  - advertised_write_flag: yes
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 8f0623bf
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.ios98.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '美辰云盘'
  - probe:https://pan.ios98.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 11 root entries; write:true, write_content_bypass:None, provider:139Yun
  - probe:https://pan.ios98.com/api/fs/put 2026-10-22: the zero-byte oracle returned code 403 with message 'file exists', so the write permission passed and nothing was written
  - probe:https://pan.ios98.com/p/ 2026-10-22: GET /p/<the written path> returned HTTP 200 with 51 bytes of code 401 'expire missing' instead of the 32 bytes written
- sources:
  - [1] https://pan.ios98.com/
