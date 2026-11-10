# AList

> tianmoy.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tianmoy/ | JSON https://fshy.ajam.dev/api/v1/entity/tianmoy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AList

- `netdisk-pan/alist-tianmoy-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://alist.tianmoy.cn/
- free tier: anonymous guest read of 3 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through no identified front; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://alist.tianmoy.cn/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 3 root entries on AList v4.2.6. It flaps between answering as an AList API and answering 200 with no API at all, and between listing and not listing, across runs minutes apart.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: not-tested
  - upstream_provider: unknown
  - advertised_write_flag: yes
  - write_content_bypass: no
  - base_path: /
  - listing_sha256: 78ea8a65
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://alist.tianmoy.cn/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'AList'
  - probe:https://alist.tianmoy.cn/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 3 root entries; write:true, write_content_bypass:False, provider:unknown
- sources:
  - [1] https://alist.tianmoy.cn/
