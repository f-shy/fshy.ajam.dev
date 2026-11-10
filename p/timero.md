# ximu's alist

> timero.xyz | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/timero/ | JSON https://fshy.ajam.dev/api/v1/entity/timero.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ximu's alist

- `netdisk-pan/pan-timero-xyz` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.timero.xyz/
- free tier: anonymous guest read of 1724 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://pan.timero.xyz/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. allow_indexed true means /api/public/search can enumerate the whole tree without walking it, which is the useful mechanism to take from this host
- reliability: 1,724 root entries on an AList v3.43 build, base_path /onedrive/adv_lib_001, provider Onedrive. The largest listing in the population and the clearest example of a pooled tenant re-exported.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Onedrive
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /onedrive/adv_lib_001
  - listing_sha256: 6e818fb6
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
  - aliases: pan.timero.xyz (ximu's alist) — public AList, 1,724-entry visual-novel library
  - allow_indexed: yes
- evidence:
  - probe:https://pan.timero.xyz/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title "ximu's alist"
  - probe:https://pan.timero.xyz/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 1724 root entries; write:false, write_content_bypass:None, provider:Onedrive
  - probe:https://pan.timero.xyz/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pan.timero.xyz/
