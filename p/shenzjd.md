# 神族九帝云盘,转存网盘资源请去网盘搜索

> shenzjd.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shenzjd/ | JSON https://fshy.ajam.dev/api/v1/entity/shenzjd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 神族九帝云盘，转存网盘资源请去网盘搜索

- `netdisk-pan/alist-shenzjd-com` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T14:53:24.752Z (live) | stale on 2026-12-17
- url https://alist.shenzjd.com/
- free tier: anonymous guest read of 3 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through openresty; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://alist.shenzjd.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 3 root entries on AList v4.2.6; advertises write:true on one mount and denies the oracle.
- notes: 3 root entries on AList v4.2.6; advertises write:true on one mount and denies the oracle. Re-probed 2026-11-20: the home page answered 200 with 69,408 bytes of text/html, but the AList API still returned no listing, so the host stays dead and last_verified_alive stays at the last live observation (2026-11-11).
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: openresty
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 773158e3
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-11T00:20:01.882Z
  - last_verified_dead: 2026-11-25T01:38:28.683Z
  - consecutive_failures: 4
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - probe:https://alist.shenzjd.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '神族九帝云盘，转存网盘资源请去网盘搜索'
  - probe:https://alist.shenzjd.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 3 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://alist.shenzjd.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://alist.shenzjd.com/ 2026-11-11:  | capture: sha256:4955e230d93a1af81d14f00de819f335157f6a0cdfb8eb730869dee3f8e26479
  - probe:https://alist.shenzjd.com/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:4955e230d93a1af81d14f00de819f335157f6a0cdfb8eb730869dee3f8e26479
  - probe:https://alist.shenzjd.com/ 2026-11-11: the anonymous guest session answered and its root listing returned entries, so the instance is reachable without an account | capture: sha256:4955e230d93a1af81d14f00de819f335157f6a0cdfb8eb730869dee3f8e26479 | quote: "alive": true
  - probe:https://alist.shenzjd.com/ 2026-11-11:  | capture: sha256:4955e230d93a1af81d14f00de819f335157f6a0cdfb8eb730869dee3f8e26479 | quote: "checked_at": "2026-11-11T00:20:01.882Z"
  - probe:https://alist.shenzjd.com/ 2026-11-11: the anonymous root listing hashed to this value | capture: sha256:4955e230d93a1af81d14f00de819f335157f6a0cdfb8eb730869dee3f8e26479 | quote: "listing_sha256": "773158e3"
  - probe:https://alist.shenzjd.com/ 2026-11-19: three liveness probes minutes apart found no AList API or mount list at this host | capture: sha256:8c6dfce441df6db2bed3db672b1b477f748d615aa356d237c4120a03d563f8d4 | quote: "consecutive_failures": 3
  - probe:https://alist.shenzjd.com/ 2026-11-19: the third consecutive failed liveness probe was taken at this instant | capture: sha256:8c6dfce441df6db2bed3db672b1b477f748d615aa356d237c4120a03d563f8d4 | quote: "checked_at": "2026-11-19T03:32:53.747Z"
  - probe:https://alist.shenzjd.com/ 2026-11-19: every API path returned an unrelated text/html page, so the host was recorded dead at this re-check | capture: sha256:8c6dfce441df6db2bed3db672b1b477f748d615aa356d237c4120a03d563f8d4 | quote: "content_type": "text/html;charset=utf-8"
  - [1] 2026-11-20: a 2026-11-20 probe of the home page answered 200 with 69,408 bytes of text/html; no AList API listing was returned | capture: sha256:039bd613b9468c1a74d042fddd578781f67fa57939c8a9f565a7f6574afc9873 | quote: "status": 200,
  - probe:https://alist.shenzjd.com/api/public/settings 2026-11-25: a fresh anonymous probe of the AList public settings endpoint of alist.shenzjd.com answered at this instant (HTTP 200, JSON, no challenge) | capture: sha256:5ff5d73af331e64f67ade5ed0c1b0b3bdad46050aa43e3d04b22b61a0e851a41 | quote: "probed_at": "2026-11-25T04:07:31.090Z"
  - probe:https://alist.shenzjd.com/ 2026-11-25: a fourth consecutive anonymous liveness probe found no AList API or mount list at this host | capture: sha256:d54bd4b883ce016a5fb8c1365a9e38fb68ac2b62c534f56b60b905e895bb7945 | quote: "consecutive_failures": 4
  - probe:https://alist.shenzjd.com/ 2026-11-25: the fresh probe found no anonymous settings, session or mount list, so the host stays dead | capture: sha256:d54bd4b883ce016a5fb8c1365a9e38fb68ac2b62c534f56b60b905e895bb7945 | quote: "alive": false
  - probe:https://alist.shenzjd.com/api/public/settings 2026-11-25: the API path of the dead host now redirects to an unrelated panhub page rather than serving an AList API | capture: sha256:5ff5d73af331e64f67ade5ed0c1b0b3bdad46050aa43e3d04b22b61a0e851a41 | quote: "final_url": "https://panhub.shenzjd.com/"
  - probe:https://alist.shenzjd.com/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:7a7b8dfb80b81be21948c29108a2700df15a5a9fb7b93d37e75685a98018cb9a | quote: "checked_at": "2026-11-25T01:38:28.683Z"
- sources:
  - [1] https://alist.shenzjd.com/
