# 趣盘

> mediy.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mediy/ | JSON https://fshy.ajam.dev/api/v1/entity/mediy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 趣盘 - 存兴趣，享乐趣

- `netdisk-pan/pan-mediy-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.mediy.cn/
- free tier: anonymous guest read of 7 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.mediy.cn/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. A book and software corpus, and the index notes that parts of it are already dead
- reliability: Contains 7 root entries. Advertised write permissions are denied on execution. Responded as an active API endpoint on 2026-10-22 and intermittently failed to respond on separate test queries.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 29b5335a
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: 趣盘 (pan.mediy.cn) — public OpenList, mixed media/book corpus
- evidence:
  - probe:https://pan.mediy.cn/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '趣盘 - 存兴趣，享乐趣'
  - probe:https://pan.mediy.cn/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 7 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.mediy.cn/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.mediy.cn/
