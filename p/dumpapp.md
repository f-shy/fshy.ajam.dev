# DumpApp

> dumpapp.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dumpapp/ | JSON https://fshy.ajam.dev/api/v1/entity/dumpapp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DumpApp

- `netdisk-pan/pan-dumpapp-com` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:34.327Z (live) | stale on 2026-12-17
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
  - last_verified_alive: 2026-11-25T02:34:36.231Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.dumpapp.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'DumpApp'
  - probe:https://pan.dumpapp.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 4 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.dumpapp.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2 | quote: "checked_at": "2026-11-11T00:20:06.416Z"
  - probe:https://pan.dumpapp.com/ 2026-11-11:  | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2
  - probe:https://pan.dumpapp.com/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:b2ea9a5ae7a183584b36d8577ac05b9ee65a2b15eb4177f628c5323f6bf9ccf2
  - probe:https://pan.dumpapp.com/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:aca055ff48c2677046a222c71bb5b20f242584478a69402a53b74cd01a981d77 | quote: "checked_at": "2026-11-19T03:33:14.099Z"
  - probe:https://pan.dumpapp.com/ 2026-11-25: a fresh anonymous probe of pan.dumpapp.com answered the settings, session and mount-list requests at this timestamp | capture: sha256:1e88b349d45d126811ac9d7d4f2b328590ab7beb615ce106fb2059c82765b52b | quote: "probed_at": "2026-11-25T02:34:36.231Z"
  - probe:https://pan.dumpapp.com/ 2026-11-25: the fresh probe completed the anonymous settings, session and mount-list requests at pan.dumpapp.com | capture: sha256:1e88b349d45d126811ac9d7d4f2b328590ab7beb615ce106fb2059c82765b52b | quote: "alive": true
  - probe:https://pan.dumpapp.com/ 2026-11-25: the fresh anonymous root listing of pan.dumpapp.com hashed to the recorded value, so the listing is unchanged | capture: sha256:1e88b349d45d126811ac9d7d4f2b328590ab7beb615ce106fb2059c82765b52b | quote: "listing_sha256": "3e8593df"
  - probe:https://pan.dumpapp.com/ 2026-11-25: the probe was checked at this instant | capture: sha256:01bbca15d9e66e1a349b954c980a600a3a453af4d0511c30cd00ee2055b1cadf | quote: "checked_at": "2026-11-25T01:38:31.256Z"
  - probe:https://pan.dumpapp.com/ 2026-11-25: the anonymous root listing returned 4 entries | capture: sha256:01bbca15d9e66e1a349b954c980a600a3a453af4d0511c30cd00ee2055b1cadf | quote: "root_entries": 4
- sources:
  - [1] https://pan.dumpapp.com/
