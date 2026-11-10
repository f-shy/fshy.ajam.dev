# 槿南盘

> jinnan.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jinnan/ | JSON https://fshy.ajam.dev/api/v1/entity/jinnan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 槿南盘

- `netdisk-pan/pan-jinnan-top` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.jinnan.top/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.jinnan.top/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only despite the directory name. The guest-upload folder is the single clearest example of the gap between an instance's intent and what it actually permits
- reliability: The cleanest illustration of the write-flag lie: its root listing contains a directory named 05 游客上传, every mount advertises write:true, and every PUT returns permission denied inside an HTTP 200. The operator intended guest upload and the permission never reached the guest role.
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
  - listing_sha256: dd9a52fe
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: 槿南盘 (pan.jinnan.top) — public OpenList with a literal '05 游客上传' guest-upload directory
- evidence:
  - probe:https://pan.jinnan.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '槿南盘'
  - probe:https://pan.jinnan.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 6 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.jinnan.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.jinnan.top/
