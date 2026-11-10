# Kho Nhà Tôm ✨

> t0m.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t0m/ | JSON https://fshy.ajam.dev/api/v1/entity/t0m.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kho Nhà Tôm ✨

- `netdisk-pan/kho-t0m-top` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://kho.t0m.top/
- free tier: anonymous guest read of 4 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://kho.t0m.top/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 4 root entries, provider Local, AList v3.42.0, Cloudflare-fronted. A Vietnamese-language instance.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Local
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 16690055
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://kho.t0m.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'Kho Nhà Tôm ✨'
  - probe:https://kho.t0m.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 4 root entries; write:false, write_content_bypass:None, provider:Local
  - probe:https://kho.t0m.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://kho.t0m.top/
