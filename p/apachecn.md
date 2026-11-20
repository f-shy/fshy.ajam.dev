# 组织云盘合集

> apachecn.org | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apachecn/ | JSON https://fshy.ajam.dev/api/v1/entity/apachecn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 组织云盘合集

- `netdisk-pan/w2-apachecn-org` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:08.144Z (live) | stale on 2026-12-11
- url https://w2.apachecn.org/
- free tier: anonymous guest read of 18 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://w2.apachecn.org/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. The ApacheCN corpus is the largest publicly listable AList library found, so a reader who needs a specific dataset should search here before paying anyone
- reliability: An 18-entry public corpus on AList v3.35 with base_path /公共. Read-only by design and stable since at least 2024-01.
- notes: anonymous POST /api/fs/list on / returned code 200 with 18 root entries (listing sha256 0d46fd71)
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /公共
  - listing_sha256: 0d46fd71
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:42:55.824Z
  - consecutive_failures: 0
  - aliases: 组织云盘合集 (w2.apachecn.org) — public AList, largest visible corpus, 252 TB claimed
- evidence:
  - probe:https://w2.apachecn.org/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '组织云盘合集 '
  - probe:https://w2.apachecn.org/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 18 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://w2.apachecn.org/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://w2.apachecn.org/ 2026-11-11: the fs/list response carries this error text | capture: sha256:3c140e4000a7d1c704df10d8c6259020a8b9acb9b03cf6cb17a7589aa1d4d382 | quote: "list_failure": "failed get storage: storage not found; rawPath: /公共/公共"
  - probe:https://w2.apachecn.org/ 2026-11-11: this run's probe found no listing, so the count is one | capture: sha256:3c140e4000a7d1c704df10d8c6259020a8b9acb9b03cf6cb17a7589aa1d4d382 | quote: "consecutive_failures": 1
  - probe:https://w2.apachecn.org/ 2026-11-11: the settings endpoint answered HTTP 200 while the listing did not | capture: sha256:3c140e4000a7d1c704df10d8c6259020a8b9acb9b03cf6cb17a7589aa1d4d382 | quote: "status": 200
  - probe:https://w2.apachecn.org/ 2026-11-11:  | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17 | quote: "checked_at": "2026-11-11T01:56:23.253Z"
  - probe:https://w2.apachecn.org/ 2026-11-11:  | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17 | quote: "listing_sha256": "0d46fd71"
  - probe:https://w2.apachecn.org/ 2026-11-11:  | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17
  - probe:https://w2.apachecn.org/ 2026-11-11:  | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17 | quote: "alive": true
  - probe:https://w2.apachecn.org/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17 | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 18 root entries (listing sha256 0d46fd71)"
  - probe:https://w2.apachecn.org/ 2026-11-11:  | capture: sha256:74a256a63363e33534f8499658525261e1fa6a72a7d02b69d009540ec0ba2e17
  - probe:https://w2.apachecn.org/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:4ce083ec4a966fa8db29b6ead18c4ed112c378e0ccce17755b3bd1a02b403ed5 | quote: "checked_at": "2026-11-19T03:42:55.824Z"
  - probe:https://w2.apachecn.org/ 2026-11-19: the anonymous session, settings and mount list all answered, so the fresh alive timestamp stands | capture: sha256:4ce083ec4a966fa8db29b6ead18c4ed112c378e0ccce17755b3bd1a02b403ed5 | quote: "alive": true
  - probe:https://w2.apachecn.org/ 2026-11-19: the root listing hashed to the recorded 0d46fd71 on both runs and the host answered every request | capture: sha256:4ce083ec4a966fa8db29b6ead18c4ed112c378e0ccce17755b3bd1a02b403ed5 | quote: "listing_sha256": "0d46fd71"..."consecutive_failures": 0
- sources:
  - [1] https://w2.apachecn.org/
