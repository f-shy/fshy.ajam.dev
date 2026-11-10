# 591meta.com

> 591meta.com | Netdisk and pan; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/591meta/ | JSON https://fshy.ajam.dev/api/v1/entity/591meta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ppp.591meta.com

- `netdisk-pan/ppp-591meta-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://ppp.591meta.com/
- free tier: anonymous guest read of 26 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through no identified front; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: no write offered probe:https://ppp.591meta.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Additional hostname on the 591meta infrastructure. Responded to API calls and returned the same 26 package entries.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: not-tested
  - upstream_provider: unknown
  - advertised_write_flag: no
  - base_path: /
  - listing_sha256: 53eb1f51
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://ppp.591meta.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field
  - probe:https://ppp.591meta.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 26 root entries; write:false, write_content_bypass:None, provider:unknown
- sources:
  - [1] https://ppp.591meta.com/

## 小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源 (p 591meta com)

- `netdisk-pan/p-591meta-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://p.591meta.com/
- free tier: anonymous guest read of 26 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://p.591meta.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: One of five hostnames serving an identical 26-entry collection of iOS IPA packages. The file repository serves as an informational index for a commercial signing service.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 6fb4c929
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://p.591meta.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源'
  - probe:https://p.591meta.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 26 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://p.591meta.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://p.591meta.com/

## 小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源 (pp 591meta com)

- `netdisk-pan/pp-591meta-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pp.591meta.com/
- free tier: anonymous guest read of 26 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://pp.591meta.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Maintained under the same infrastructure as p.591meta.com. Directory listings vary by one dynamic entry across requests, reflecting a shared active package catalogue.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 6fb4c929
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pp.591meta.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源'
  - probe:https://pp.591meta.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 26 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pp.591meta.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
- sources:
  - [1] https://pp.591meta.com/
