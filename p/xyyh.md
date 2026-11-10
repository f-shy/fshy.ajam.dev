# 知网云盘

> xyyh.xyz | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xyyh/ | JSON https://fshy.ajam.dev/api/v1/entity/xyyh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 知网云盘

- `netdisk-pan/pan-xyyh-xyz` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.xyyh.xyz/
- free tier: anonymous guest read of 2 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through no identified front; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://pan.xyyh.xyz/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Answered as an AList API on one run and not on another, and listed 2 root entries once. Its zero-byte oracle returned neither of the two defined messages.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: not-tested
  - upstream_provider: unknown
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 9e6193c6
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.xyyh.xyz/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '知网云盘'
  - probe:https://pan.xyyh.xyz/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 2 root entries; write:false, write_content_bypass:None, provider:unknown
- sources:
  - [1] https://pan.xyyh.xyz/
