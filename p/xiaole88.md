# 小乐的网盘

> xiaole88.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiaole88/ | JSON https://fshy.ajam.dev/api/v1/entity/xiaole88.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小乐的网盘

- `netdisk-pan/share-xiaole88-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://share.xiaole88.com/
- free tier: anonymous guest read of 15 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through Tengine; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://share.xiaole88.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. Useful as an Android TV software mirror and not as capacity
- reliability: 15 root entries, provider Onedrive, on AList v3.40 behind Tengine. A pooled-tenant export like al.chirmyram.com but without Cloudflare in front, so no edge cache.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Onedrive
  - fronting_cdn: tengine
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 410d4236
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: 小乐的网盘 (share.xiaole88.com) — public AList, Android TV software
- evidence:
  - probe:https://share.xiaole88.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小乐的网盘'
  - probe:https://share.xiaole88.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 15 root entries; write:false, write_content_bypass:None, provider:Onedrive
  - probe:https://share.xiaole88.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://share.xiaole88.com/
