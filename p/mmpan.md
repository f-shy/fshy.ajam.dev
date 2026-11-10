# mmpan.net

> mmpan.net | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mmpan/ | JSON https://fshy.ajam.dev/api/v1/entity/mmpan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mmpan.net

- `netdisk-pan/mmpan-net` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://mmpan.net/
- free tier: anonymous guest read of 0 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://mmpan.net/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Answers the AList API and returns HTTP 200 on /api/fs/list with no usable body, so there is nothing to read.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - write_content_bypass: absent
  - base_path: /
  - first_seen: 2024-01-20
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
- evidence:
  - probe:https://mmpan.net/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '?'
- sources:
  - [1] https://mmpan.net/
