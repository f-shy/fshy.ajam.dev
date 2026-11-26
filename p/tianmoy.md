# AList

> tianmoy.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tianmoy/ | JSON https://fshy.ajam.dev/api/v1/entity/tianmoy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AList

- `netdisk-pan/alist-tianmoy-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:08:33.683Z (live) | stale on 2026-12-17
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
  - listing_sha256: fcd1bca6
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T04:07:32.799Z
  - consecutive_failures: 0
- evidence:
  - probe:https://alist.tianmoy.cn/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'AList'
  - probe:https://alist.tianmoy.cn/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 3 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://alist.tianmoy.cn/ 2026-11-11:  | capture: sha256:54b1bf23cb5b3202dc1117ebb53f24c7e4c16cfd830a4ab2fe6fd3d04fcb7177
  - probe:https://alist.tianmoy.cn/ 2026-11-11:  | capture: sha256:54b1bf23cb5b3202dc1117ebb53f24c7e4c16cfd830a4ab2fe6fd3d04fcb7177 | quote: "checked_at": "2026-11-11T00:20:01.878Z"
  - probe:https://alist.tianmoy.cn/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:ad2083eb8a0ca854cecad0c45291ac01efa5ba3a5325e1efaa1e26e0bea3a17a | quote: "checked_at": "2026-11-19T03:31:20.741Z"
  - probe:https://alist.tianmoy.cn/ 2026-11-19: the host answered every request of this probe, so the failure count stayed at zero | capture: sha256:ad2083eb8a0ca854cecad0c45291ac01efa5ba3a5325e1efaa1e26e0bea3a17a
  - probe:https://alist.tianmoy.cn/api/public/settings 2026-11-25: a fresh anonymous probe of the AList public settings endpoint of alist.tianmoy.cn answered at this instant (HTTP 200, JSON, no challenge) | capture: sha256:9459e0e6e8ef666442186dc987f5a1cb51e1c23ddc0033b9bca6596d51a64da2 | quote: "probed_at": "2026-11-25T04:07:32.799Z"
  - probe:https://alist.tianmoy.cn/api/public/settings 2026-11-25: the settings endpoint of alist.tianmoy.cn answered HTTP 200 to an anonymous request | capture: sha256:9459e0e6e8ef666442186dc987f5a1cb51e1c23ddc0033b9bca6596d51a64da2 | quote: "status": 200
  - probe:https://alist.tianmoy.cn/ 2026-11-25: the fresh anonymous root listing hashed to the recorded value, so the listing is unchanged | capture: sha256:c50462e77d860586257a0e8c54e4b3b8c383e1c572eb1f048545abb292fd9eb5 | quote: "listing_sha256": "fcd1bca6"
  - probe:https://alist.tianmoy.cn/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:262e451150e183e3cba1bd68113e9b1eaffcef00b2afcbfa4fa796feb44f9875 | quote: "checked_at": "2026-11-25T01:38:28.684Z"
  - probe:https://alist.tianmoy.cn/ 2026-11-25: the anonymous session, settings and root listing all answered, so no consecutive failure | capture: sha256:262e451150e183e3cba1bd68113e9b1eaffcef00b2afcbfa4fa796feb44f9875 | quote: "alive": true
  - probe:https://alist.tianmoy.cn/ 2026-11-25: the anonymous root listing still hashes to fcd1bca6 with 3 entries | capture: sha256:262e451150e183e3cba1bd68113e9b1eaffcef00b2afcbfa4fa796feb44f9875 | quote: "guest": true, ... "root_entries": 3, ... "listing_sha256": "fcd1bca6"
- sources:
  - [1] https://alist.tianmoy.cn/
