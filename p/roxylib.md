# 洛琪希图书馆

> roxylib.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roxylib/ | JSON https://fshy.ajam.dev/api/v1/entity/roxylib.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 洛琪希图书馆 - 借书柜台

- `netdisk-pan/pan-roxylib-com` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.roxylib.com/
- free tier: anonymous guest read of 1 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.roxylib.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 1 root entry on OpenList v4.2.3. The smallest listing in the population, and it still advertises write:true and denies the oracle.
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
  - base_path: /
  - listing_sha256: d60da3f8
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.roxylib.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '洛琪希图书馆 - 借书柜台'
  - probe:https://pan.roxylib.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 1 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.roxylib.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.roxylib.com/
