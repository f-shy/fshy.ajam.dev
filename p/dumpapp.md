# DumpApp

> dumpapp.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dumpapp/ | JSON https://fshy.ajam.dev/api/v1/entity/dumpapp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DumpApp

- `netdisk-pan/pan-dumpapp-com` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:07.393Z (live) | stale on 2026-12-11
- url https://pan.dumpapp.com/
- free tier: anonymous guest read of 4 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://pan.dumpapp.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 4 root entries on AList v3.57.0, providers unknown and 189CloudPC, write:false.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: nginx
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 3e8593df
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:33:14.099Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.dumpapp.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'DumpApp'
  - probe:https://pan.dumpapp.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 4 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.dumpapp.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2 | quote: "checked_at": "2026-11-11T00:20:06.416Z"
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2 | quote: "listing_sha256": "3e8593df"
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2 | quote: "alive": true
  - probe:https://pan.dumpapp.com/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:aca055ff48c2677046a222c71bb5b20f242584478a69402a53b74cd01a981d77 | quote: "checked_at": "2026-11-19T03:33:14.099Z"
- sources:
  - [1] https://pan.dumpapp.com/
