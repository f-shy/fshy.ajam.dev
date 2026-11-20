# applep12.vip

> applep12.vip | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/applep12/ | JSON https://fshy.ajam.dev/api/v1/entity/applep12.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源

- `netdisk-pan/pan-applep12-vip` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:07.393Z (live) | stale on 2026-12-11
- url https://pan.applep12.vip/
- free tier: anonymous guest read of 26 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://pan.applep12.vip/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Same 26-entry IPA corpus as p.591meta.com, identical listing bytes.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: e715d3d0
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:33:08.812Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.applep12.vip/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小鹿乐玩iOS网盘IPA资源｜路灯网盘-iOS砸壳分享网-IPA分享网-巨魔商店IPA软件资源-后厂村路灯的网盘资源'
  - probe:https://pan.applep12.vip/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 26 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.applep12.vip/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.applep12.vip/ 2026-11-11:  | capture: sha256:5d0e69d9e8562aa551fb205fa16bfa11d805b292b0d56fc0bae60a77dae057ab | quote: "checked_at": "2026-11-11T00:20:06.149Z"
  - probe:https://pan.applep12.vip/ 2026-11-11:  | capture: sha256:5d0e69d9e8562aa551fb205fa16bfa11d805b292b0d56fc0bae60a77dae057ab | quote: "listing_sha256": "e715d3d0"
  - probe:https://pan.applep12.vip/ 2026-11-11:  | capture: sha256:5d0e69d9e8562aa551fb205fa16bfa11d805b292b0d56fc0bae60a77dae057ab
  - probe:https://pan.applep12.vip/ 2026-11-11:  | capture: sha256:5d0e69d9e8562aa551fb205fa16bfa11d805b292b0d56fc0bae60a77dae057ab
  - probe:https://pan.applep12.vip/ 2026-11-11:  | capture: sha256:5d0e69d9e8562aa551fb205fa16bfa11d805b292b0d56fc0bae60a77dae057ab | quote: "alive": true
  - probe:https://pan.applep12.vip/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:6583aabb80aecc145068eadc6511c16e1709485313f119dcac4832c177f167e5 | quote: "checked_at": "2026-11-19T03:33:08.812Z"
- sources:
  - [1] https://pan.applep12.vip/
