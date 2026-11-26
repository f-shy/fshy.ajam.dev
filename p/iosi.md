# 平凡

> iosi.vip | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iosi/ | JSON https://fshy.ajam.dev/api/v1/entity/iosi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 平凡

- `netdisk-pan/pan-iosi-vip` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:34.328Z (live) | stale on 2026-12-17
- url https://pan.iosi.vip/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.iosi.vip/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 6 root entries on AList v3.45.0, write:false, read-only by configuration.
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
  - listing_sha256: d4817232
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T02:34:36.629Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.iosi.vip/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '平凡'
  - probe:https://pan.iosi.vip/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 6 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.iosi.vip/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.iosi.vip/ 2026-11-11:  | capture: sha256:bdcbc557424e4037fd44a80557d4b8aaec78374ab3afc5ba597e056c938cb533 | quote: "checked_at": "2026-11-11T00:20:07.663Z"
  - probe:https://pan.iosi.vip/ 2026-11-11:  | capture: sha256:bdcbc557424e4037fd44a80557d4b8aaec78374ab3afc5ba597e056c938cb533
  - probe:https://pan.iosi.vip/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:bdcbc557424e4037fd44a80557d4b8aaec78374ab3afc5ba597e056c938cb533
  - probe:https://pan.iosi.vip/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:33cb773ab19bb4a1ceb64d9d5bb61f8b06c0dcf100c622bc9184bcf66e125b4d | quote: "checked_at": "2026-11-19T03:33:37.140Z"
  - probe:https://pan.iosi.vip/ 2026-11-25: a fresh anonymous probe of pan.iosi.vip answered the settings, session and mount-list requests at this timestamp | capture: sha256:cf61ec7004f0976debb990836b6f32af4a0e2662844086ca8aae50ce7c05b71f | quote: "probed_at": "2026-11-25T02:34:36.629Z"
  - probe:https://pan.iosi.vip/ 2026-11-25: the fresh probe completed the anonymous settings, session and mount-list requests at pan.iosi.vip | capture: sha256:cf61ec7004f0976debb990836b6f32af4a0e2662844086ca8aae50ce7c05b71f | quote: "alive": true
  - probe:https://pan.iosi.vip/ 2026-11-25: the fresh anonymous root listing of pan.iosi.vip hashed to the recorded value, so the listing is unchanged | capture: sha256:cf61ec7004f0976debb990836b6f32af4a0e2662844086ca8aae50ce7c05b71f | quote: "listing_sha256": "d4817232"
  - probe:https://pan.iosi.vip/ 2026-11-25: the probe was checked at this instant | capture: sha256:cf3137cb0cb17df16818307268ebb9e5228e64a484d5dfdce5a6fe93a2f46c5f | quote: "checked_at": "2026-11-25T01:38:31.564Z"
  - probe:https://pan.iosi.vip/ 2026-11-25: the anonymous root listing returned 6 entries | capture: sha256:cf3137cb0cb17df16818307268ebb9e5228e64a484d5dfdce5a6fe93a2f46c5f | quote: "root_entries": 6
- sources:
  - [1] https://pan.iosi.vip/
