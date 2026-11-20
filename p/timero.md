# ximu's alist

> timero.xyz | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/timero/ | JSON https://fshy.ajam.dev/api/v1/entity/timero.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ximu's alist

- `netdisk-pan/pan-timero-xyz` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:07.761Z (live) | stale on 2026-12-11
- url https://pan.timero.xyz/
- free tier: anonymous guest read of 1724 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://pan.timero.xyz/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. allow_indexed true means /api/public/search can enumerate the whole tree without walking it, which is the useful mechanism to take from this host
- reliability: The root listing hash changed from the recorded value and both fresh probes agreed on the new hash; this probe requests at most 200 root entries, so the comparison uses a truncated listing.
- notes: anonymous POST /api/fs/list on / returned code 200 with 1724 root entries (listing sha256 780159e3)
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Onedrive
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /onedrive/adv_lib_001
  - listing_sha256: 4e972413
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:36:59.774Z
  - consecutive_failures: 0
  - aliases: pan.timero.xyz (ximu's alist) — public AList, 1,724-entry visual-novel library
  - allow_indexed: yes
- evidence:
  - probe:https://pan.timero.xyz/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title "ximu's alist"
  - probe:https://pan.timero.xyz/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 1724 root entries; write:false, write_content_bypass:None, provider:Onedrive
  - probe:https://pan.timero.xyz/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://pan.timero.xyz/ 2026-11-11: the fs/list response carries this error text | capture: sha256:cef2cdfc5ec0ae894616ad02973b5c4071bf66181a6b58ba4d0d4af518f61e7c | quote: "list_failure": "failed get objs: failed get dir: failed get parent list: failed get dir: object not found"
  - probe:https://pan.timero.xyz/ 2026-11-11: this run's probe found no listing, so the count is one | capture: sha256:cef2cdfc5ec0ae894616ad02973b5c4071bf66181a6b58ba4d0d4af518f61e7c | quote: "consecutive_failures": 1
  - probe:https://pan.timero.xyz/ 2026-11-11: the settings endpoint answered HTTP 200 while the listing did not | capture: sha256:cef2cdfc5ec0ae894616ad02973b5c4071bf66181a6b58ba4d0d4af518f61e7c | quote: "status": 200
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f | quote: "checked_at": "2026-11-11T01:56:23.248Z"
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f | quote: "listing_sha256": "4e972413"
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f | quote: "alive": true
  - probe:https://pan.timero.xyz/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 200 root entries (listing sha256 4e972413)"
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:c1836f3f9c6090eb85a22b4be8a1a0c2e7ec418c0be3b0a00959c78176751c8f
  - probe:https://pan.timero.xyz/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:bb4f25a338604f30d43ddcd769f3bfbb6e8e3d612eff8c06db1a149ff019f019 | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 1724 root entries (listing sha256 780159e3)"
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:bb4f25a338604f30d43ddcd769f3bfbb6e8e3d612eff8c06db1a149ff019f019 | quote: "checked_at": "2026-11-11T02:29:43.242Z"
  - probe:https://pan.timero.xyz/ 2026-11-11:  | capture: sha256:bb4f25a338604f30d43ddcd769f3bfbb6e8e3d612eff8c06db1a149ff019f019 | quote: "listing_sha256": "780159e3"
  - probe:https://pan.timero.xyz 2026-11-19: the probe's checked_at instant is the fresh last-alive verification time | capture: sha256:080a892146a9273d101aa285e089949c97f377900770f52b4d2a3edcb27c849b | quote: "checked_at": "2026-11-19T03:36:59.774Z"
  - probe:https://pan.timero.xyz 2026-11-19: the anonymous guest session answered and the root listing returned entries | capture: sha256:080a892146a9273d101aa285e089949c97f377900770f52b4d2a3edcb27c849b | quote: "alive": true
  - probe:https://pan.timero.xyz 2026-11-19: the /api/public/settings request answered HTTP 200 | capture: sha256:080a892146a9273d101aa285e089949c97f377900770f52b4d2a3edcb27c849b | quote: "status": 200
  - probe:https://pan.timero.xyz 2026-11-19: a fresh anonymous root listing produced this hash | capture: sha256:080a892146a9273d101aa285e089949c97f377900770f52b4d2a3edcb27c849b | quote: "listing_sha256": "4e972413"
  - probe:https://pan.timero.xyz 2026-11-19: the fresh root listing hash supports the changed-hash or flapping note | capture: sha256:080a892146a9273d101aa285e089949c97f377900770f52b4d2a3edcb27c849b | quote: "listing_sha256": "4e972413"
  - probe:https://pan.timero.xyz 2026-11-19: the second fresh probe reproduced the new hash | capture: sha256:db08ae17c6b5a2cab27b24b828386c4bfd17cc63caa98b6f5403276056288405 | quote: "listing_sha256": "4e972413"
- sources:
  - [1] https://pan.timero.xyz/
