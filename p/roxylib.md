# 洛琪希图书馆

> roxylib.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roxylib/ | JSON https://fshy.ajam.dev/api/v1/entity/roxylib.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 洛琪希图书馆 - 借书柜台

- `netdisk-pan/pan-roxylib-com` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T21:46:10.685Z (live) | stale on 2026-12-17
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
  - listing_sha256: 4e4fd534
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T02:34:39.845Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.roxylib.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '洛琪希图书馆 - 借书柜台'
  - probe:https://pan.roxylib.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 1 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.roxylib.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.roxylib.com/ 2026-11-11:  | capture: sha256:bc2ce086c89af49f9c53c6990e9731a729beba4c9db7434da5606c84ca6997d8 | quote: "checked_at": "2026-11-11T00:20:09.449Z"
  - probe:https://pan.roxylib.com/ 2026-11-11: the anonymous root listing hashed to this value | capture: sha256:bc2ce086c89af49f9c53c6990e9731a729beba4c9db7434da5606c84ca6997d8 | quote: "listing_sha256": "4e4fd534"
  - probe:https://pan.roxylib.com/ 2026-11-11:  | capture: sha256:bc2ce086c89af49f9c53c6990e9731a729beba4c9db7434da5606c84ca6997d8
  - probe:https://pan.roxylib.com/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:bc2ce086c89af49f9c53c6990e9731a729beba4c9db7434da5606c84ca6997d8
  - probe:https://pan.roxylib.com 2026-11-19: the probe's checked_at instant is the fresh last-alive verification time | capture: sha256:4f47c8e14773d85f229178223de93aadc2cbb763911ba3c9543a79e8f0ac459b | quote: "checked_at": "2026-11-19T03:36:57.285Z"
  - probe:https://pan.roxylib.com 2026-11-19: the anonymous guest session answered and the root listing returned entries | capture: sha256:4f47c8e14773d85f229178223de93aadc2cbb763911ba3c9543a79e8f0ac459b | quote: "alive": true
  - probe:https://pan.roxylib.com 2026-11-19: the /api/public/settings request answered HTTP 200 | capture: sha256:4f47c8e14773d85f229178223de93aadc2cbb763911ba3c9543a79e8f0ac459b | quote: "status": 200
  - probe:https://pan.roxylib.com/ 2026-11-25: the anonymous settings and mount-list requests answered at this instant | capture: sha256:070268791b6e27b899e4ab9025b987e4f5c4135aa1e606c4b9bd1544fbc32075 | quote: "alive": true
  - probe:https://pan.roxylib.com/ 2026-11-25: the probe checked this host at this instant | capture: sha256:3777ef9da951cc8eced4d9bac0c896d3d994b3dd174f88242cd988df4d52b8ee | quote: "checked_at": "2026-11-25T01:38:33.938Z"
  - probe:https://pan.roxylib.com/ 2026-11-25: the anonymous guest session answered and the settings request returned 200, so the host is alive | capture: sha256:3777ef9da951cc8eced4d9bac0c896d3d994b3dd174f88242cd988df4d52b8ee | quote: "alive": true, ... "status": 200,
  - probe:https://pan.roxylib.com/ 2026-11-25: the anonymous root listing has this entry count and hash | capture: sha256:3777ef9da951cc8eced4d9bac0c896d3d994b3dd174f88242cd988df4d52b8ee | quote: "listing_sha256": "4e4fd534", ... "root_entries": 1,
  - probe:https://pan.roxylib.com/ 2026-11-25: the session is an anonymous guest user | capture: sha256:3777ef9da951cc8eced4d9bac0c896d3d994b3dd174f88242cd988df4d52b8ee | quote: "guest": true, ... "username": "guest",
  - probe:https://pan.roxylib.com/ 2026-11-25: the guest role has this permission bitmask, base path and advertised write flags | capture: sha256:3777ef9da951cc8eced4d9bac0c896d3d994b3dd174f88242cd988df4d52b8ee | quote: "permission": 0, ... "base_path": "/", ... "write_advertised": true, ... "write_content_bypass": false,
- sources:
  - [1] https://pan.roxylib.com/
