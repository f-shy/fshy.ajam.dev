# Alist追番

> zhuifan.link | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zhuifan/ | JSON https://fshy.ajam.dev/api/v1/entity/zhuifan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Alist追番

- `netdisk-pan/zhuifan-link` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://zhuifan.link/
- free tier: anonymous guest read of 8 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://zhuifan.link/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. Its value is as a template and as a fetch source, and it demonstrates that an instance with allow_mounted true exposes the mounted provider through the API, which is how to identify which pan backs a site without an account
- reliability: An anime index on an AList v3.23 build from about 2022, which makes it one of the two oldest instances still listing. base_path is /新番/anime/new, so / in the API is not the instance root. Read-only by design.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: GoogleDrive
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 256
  - base_path: /新番/anime/new
  - listing_sha256: 710d5e20
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: Alist追番 (zhuifan.link) — public AList, read-only, WebDAV guest account works
  - guest_credentials: zhuifan:zhuifan; guest:guest
- evidence:
  - probe:https://zhuifan.link/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'Alist追番'
  - probe:https://zhuifan.link/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 8 root entries; write:false, write_content_bypass:None, provider:GoogleDrive
  - probe:https://zhuifan.link/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://zhuifan.link/
