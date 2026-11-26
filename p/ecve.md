# LZENX

> ecve.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ecve/ | JSON https://fshy.ajam.dev/api/v1/entity/ecve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LZENX｜资源小站

- `netdisk-pan/pan-ecve-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:34.327Z (live) | stale on 2026-12-17
- url https://pan.ecve.cn/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.ecve.cn/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 6 root entries on OpenList v4.2.2 with base_path /游客分区, write:true advertised and denied.
- notes: anonymous POST /api/fs/list on / returned code 200 with 6 root entries (listing sha256 5509f4a9)
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 2
  - base_path: /游客分区
  - listing_sha256: 5509f4a9
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T02:34:36.265Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.ecve.cn/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'LZENX｜资源小站'
  - probe:https://pan.ecve.cn/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 6 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://pan.ecve.cn/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.ecve.cn/ 2026-11-11: the fs/list response carries this error text | capture: sha256:b031f00958c522262eec154de9837cafe37b64b70b534a124d8cc258c4e46293 | quote: "list_failure": "failed get objs: failed get dir: failed to get obj: object not found"
  - probe:https://pan.ecve.cn/ 2026-11-11: this run's probe found no listing, so the count is one | capture: sha256:b031f00958c522262eec154de9837cafe37b64b70b534a124d8cc258c4e46293 | quote: "consecutive_failures": 1
  - probe:https://pan.ecve.cn/ 2026-11-11: the settings endpoint answered HTTP 200 while the listing did not | capture: sha256:b031f00958c522262eec154de9837cafe37b64b70b534a124d8cc258c4e46293 | quote: "status": 200
  - probe:https://pan.ecve.cn/ 2026-11-11:  | capture: sha256:5a9dd53b205e58230c477318be658a5c91e57099c49b6759555bdf4d7957e998 | quote: "checked_at": "2026-11-11T01:56:23.247Z"
  - probe:https://pan.ecve.cn/ 2026-11-11:  | capture: sha256:5a9dd53b205e58230c477318be658a5c91e57099c49b6759555bdf4d7957e998
  - probe:https://pan.ecve.cn/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:5a9dd53b205e58230c477318be658a5c91e57099c49b6759555bdf4d7957e998 | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 6 root entries (listing sha256 5509f4a9)"
  - probe:https://pan.ecve.cn/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:5a9dd53b205e58230c477318be658a5c91e57099c49b6759555bdf4d7957e998
  - probe:https://pan.ecve.cn/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:ff95d3535d15e9f40b4f9865db4769d6067e8cd2f2f04f7cba625752fedaa1e8 | quote: "checked_at": "2026-11-19T03:33:23.057Z"
  - probe:https://pan.ecve.cn/ 2026-11-25: a fresh anonymous probe of pan.ecve.cn answered the settings, session and mount-list requests at this timestamp | capture: sha256:3d8e068eff0610d165e6126adba4703d6e4678056b5511c82a3fac393d6f4a29 | quote: "probed_at": "2026-11-25T02:34:36.265Z"
  - probe:https://pan.ecve.cn/ 2026-11-25: the fresh probe completed the anonymous settings, session and mount-list requests at pan.ecve.cn | capture: sha256:3d8e068eff0610d165e6126adba4703d6e4678056b5511c82a3fac393d6f4a29 | quote: "alive": true
  - probe:https://pan.ecve.cn/ 2026-11-25: the fresh anonymous root listing of pan.ecve.cn hashed to the recorded value, so the listing is unchanged | capture: sha256:3d8e068eff0610d165e6126adba4703d6e4678056b5511c82a3fac393d6f4a29 | quote: "listing_sha256": "5509f4a9"
  - probe:https://pan.ecve.cn/ 2026-11-25: the probe was checked at this instant | capture: sha256:4d183b5701e3a8a6bf4e5b52bb9acd65697d017a96e4d7a972576e597790c2df | quote: "checked_at": "2026-11-25T01:38:31.390Z"
  - probe:https://pan.ecve.cn/ 2026-11-25: the instance reports this version string | capture: sha256:4d183b5701e3a8a6bf4e5b52bb9acd65697d017a96e4d7a972576e597790c2df | quote: "version": "v4.2.2 (Commit: b28208bd) - Frontend: v4.2.2 - Build at: 2026-05-25 15:25:29 +0000"
  - probe:https://pan.ecve.cn/ 2026-11-25: the guest session uses this base path | capture: sha256:4d183b5701e3a8a6bf4e5b52bb9acd65697d017a96e4d7a972576e597790c2df | quote: "base_path": "/游客分区"
- sources:
  - [1] https://pan.ecve.cn/
