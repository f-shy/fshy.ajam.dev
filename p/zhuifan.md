# Alist追番

> zhuifan.link | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zhuifan/ | JSON https://fshy.ajam.dev/api/v1/entity/zhuifan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Alist追番

- `netdisk-pan/zhuifan-link` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:35.337Z (live) | stale on 2026-12-17
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
- notes: anonymous POST /api/fs/list on / returned code 200 with 8 root entries (listing sha256 4d9849d5) Re-probed 2026-11-20: the host answered HTTP 502, so it is still dead and last_verified_alive stays at the last live observation (2026-11-11).
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: GoogleDrive
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 256
  - base_path: /新番/anime/new
  - listing_sha256: 4d9849d5
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-11T01:56:23.247Z
  - last_verified_dead: 2026-11-25T02:34:44.320Z
  - consecutive_failures: 4
  - aliases: Alist追番 (zhuifan.link) — public AList, read-only, WebDAV guest account works
  - guest_credentials: zhuifan:zhuifan; guest:guest
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - probe:https://zhuifan.link/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'Alist追番'
  - probe:https://zhuifan.link/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 8 root entries; write:false, write_content_bypass:None, provider:GoogleDrive
  - probe:https://zhuifan.link/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://zhuifan.link/ 2026-11-11: the fs/list response carries this error text | capture: sha256:cce20089b80e5fbb36bb85a0946b12b470058fb5bc35101d1766616d99043293 | quote: "list_failure": "failed get objs: failed get dir: failed get parent list: failed get dir: failed get parent list: failed get dir: object not found"
  - probe:https://zhuifan.link/ 2026-11-11: this run's probe found no listing, so the count is one | capture: sha256:cce20089b80e5fbb36bb85a0946b12b470058fb5bc35101d1766616d99043293 | quote: "consecutive_failures": 1
  - probe:https://zhuifan.link/ 2026-11-11: the settings endpoint answered HTTP 200 while the listing did not | capture: sha256:cce20089b80e5fbb36bb85a0946b12b470058fb5bc35101d1766616d99043293 | quote: "status": 200
  - probe:https://zhuifan.link/ 2026-11-11:  | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c | quote: "checked_at": "2026-11-11T01:56:23.247Z"
  - probe:https://zhuifan.link/ 2026-11-11: the anonymous root listing hashed to this value | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c | quote: "listing_sha256": "4d9849d5"
  - probe:https://zhuifan.link/ 2026-11-11:  | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c
  - probe:https://zhuifan.link/ 2026-11-11: the anonymous guest session answered and its root listing returned entries, so the instance is reachable without an account | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c | quote: "alive": true
  - probe:https://zhuifan.link/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 8 root entries (listing sha256 4d9849d5)"
  - probe:https://zhuifan.link/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:938704625041850b0c2d8ea8bb83bd99a38160e8845b2ba09c5f890a86df6b0c
  - probe:https://zhuifan.link/ 2026-11-19: three liveness probes minutes apart found no AList API or mount list at this host | capture: sha256:b9c452d427140e15b09e46b3597c3fde6b7d8d90bbc114768b4dfcd3e6afbf1a | quote: "consecutive_failures": 3
  - probe:https://zhuifan.link/ 2026-11-19: the third consecutive failed liveness probe was taken at this instant | capture: sha256:b9c452d427140e15b09e46b3597c3fde6b7d8d90bbc114768b4dfcd3e6afbf1a | quote: "checked_at": "2026-11-19T03:45:17.450Z"
  - [1] 2026-11-20: a 2026-11-20 probe of the host answered HTTP 502, so it is still down | capture: sha256:a7186d06d4614f6c4e360d51063497323eac457517808a6eca0d599cfb878d2e | quote: "status": 502,
  - probe:https://zhuifan.link/ 2026-11-25: a fourth consecutive probe found no AList API or mount list at this host | capture: sha256:4003be0f3bb88a1f3736e362c97fcf69782e7f91e191b4427322851e852a520c | quote: "consecutive_failures": 4
  - probe:https://zhuifan.link/ 2026-11-25: the fourth consecutive failed probe was checked at this instant | capture: sha256:4003be0f3bb88a1f3736e362c97fcf69782e7f91e191b4427322851e852a520c | quote: "checked_at": "2026-11-25T02:34:44.320Z"
  - probe:https://zhuifan.link/ 2026-11-25: the fresh probe found no anonymous settings, guest session or mount list, so the host is still dead | capture: sha256:4003be0f3bb88a1f3736e362c97fcf69782e7f91e191b4427322851e852a520c | quote: "alive": false
  - probe:https://zhuifan.link/ 2026-11-25: the settings, guest-session and mount-list paths of the fresh probe all answered HTTP 502 | capture: sha256:4003be0f3bb88a1f3736e362c97fcf69782e7f91e191b4427322851e852a520c | quote: "status": 502
  - probe:https://zhuifan.link/ 2026-11-25: the dead host returned no listing hash | capture: sha256:0ae1eddb5516f938b65645b617a27702549a3e54211c9473c596db42641b571f | quote: "listing_sha256": null
  - probe:https://zhuifan.link/ 2026-11-25: the probe record states the dead verdict for this host | capture: sha256:48c6012071c7ff67bdffea2e686c6cd15bb932a5e1707ff21e86e044b07ebb50 | quote: "verdict": "dead"
- sources:
  - [1] https://zhuifan.link/
