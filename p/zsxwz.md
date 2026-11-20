# 姿势网盘

> zsxwz.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zsxwz/ | JSON https://fshy.ajam.dev/api/v1/entity/zsxwz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 姿势网盘

- `netdisk-pan/cloud-zsxwz-com` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:06.659Z (live) | stale on 2026-12-11
- url https://cloud.zsxwz.com/
- free tier: anonymous guest read of 2 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx/1.22.1; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://cloud.zsxwz.com/api/fs/put
- interface detail: rest
- composes with: Read-only retrieval source with negligible volume, suitable for caching or mirroring rather than write storage. Documented to track public instance availability.
- reliability: 2 root entries on AList v4.1.7, built 2025-11. Small, alive, read-only.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx/1.22.1
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: cae07434
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:31:49.279Z
  - consecutive_failures: 0
  - aliases: 姿势网盘 (cloud.zsxwz.com) — public AList, OneDrive-backed
- evidence:
  - probe:https://cloud.zsxwz.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '姿势网盘'
  - probe:https://cloud.zsxwz.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 2 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://cloud.zsxwz.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://cloud.zsxwz.com/ 2026-11-11:  | capture: sha256:88a33b10c685a8913869d2ffc112cf9fba5044145c7472458a71a4f8f57317e1
  - probe:https://cloud.zsxwz.com/ 2026-11-11:  | capture: sha256:88a33b10c685a8913869d2ffc112cf9fba5044145c7472458a71a4f8f57317e1
  - probe:https://cloud.zsxwz.com/ 2026-11-11:  | capture: sha256:88a33b10c685a8913869d2ffc112cf9fba5044145c7472458a71a4f8f57317e1 | quote: "alive": true
  - probe:https://cloud.zsxwz.com/ 2026-11-11:  | capture: sha256:88a33b10c685a8913869d2ffc112cf9fba5044145c7472458a71a4f8f57317e1 | quote: "checked_at": "2026-11-11T00:20:01.880Z"
  - probe:https://cloud.zsxwz.com/ 2026-11-11:  | capture: sha256:88a33b10c685a8913869d2ffc112cf9fba5044145c7472458a71a4f8f57317e1 | quote: "listing_sha256": "cae07434"
  - probe:https://cloud.zsxwz.com/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:e8fc1a8e260340809ea36acfc9f0e73a49d5be042e2b5bfe8b4ba6906d8dbd40 | quote: "checked_at": "2026-11-19T03:31:49.279Z"
  - probe:https://cloud.zsxwz.com/ 2026-11-19: the anonymous session, settings and mount list all answered, so the fresh alive timestamp stands | capture: sha256:e8fc1a8e260340809ea36acfc9f0e73a49d5be042e2b5bfe8b4ba6906d8dbd40 | quote: "alive": true
  - probe:https://cloud.zsxwz.com/ 2026-11-19: the anonymous root listing hashed to cae07434, equal to the recorded value; no hash change | capture: sha256:e8fc1a8e260340809ea36acfc9f0e73a49d5be042e2b5bfe8b4ba6906d8dbd40 | quote: "listing_sha256": "cae07434"
  - probe:https://cloud.zsxwz.com/ 2026-11-19: the host answered every request of this probe, so the failure count stayed at zero | capture: sha256:e8fc1a8e260340809ea36acfc9f0e73a49d5be042e2b5bfe8b4ba6906d8dbd40
- sources:
  - [1] https://cloud.zsxwz.com/
