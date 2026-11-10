# 萤火虫资源站

> yhcres.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yhcres/ | JSON https://fshy.ajam.dev/api/v1/entity/yhcres.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 萤火虫资源站

- `netdisk-pan/www-yhcres-top` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://www.yhcres.top/
- free tier: anonymous guest read of 13 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://www.yhcres.top/api/fs/put
- interface detail: rest
- composes with: Read-only retrieval target for specialized router firmware downloads. Functions as an external read repository rather than writable application storage.
- reliability: 13 root entries on OpenList v4.2.7, base_path /public, write:true advertised and denied. An Android-flashing resource site.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 0
  - base_path: /public
  - listing_sha256: 8b6933f4
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: 萤火虫资源站 (www.yhcres.top) — public AList, Android flashing/repair corpus
  - allow_indexed: yes
- evidence:
  - probe:https://www.yhcres.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '萤火虫资源站'
  - probe:https://www.yhcres.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 13 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://www.yhcres.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://www.yhcres.top/
