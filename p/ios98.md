# 美辰云盘

> ios98.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ios98/ | JSON https://fshy.ajam.dev/api/v1/entity/ios98.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 美辰云盘

- `netdisk-pan/pan-ios98-com` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:08:34.600Z (live) | stale on 2026-12-17
- url https://pan.ios98.com/
- free tier: anonymous guest read of 11 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): write accepted but the read-back is signed probe:https://pan.ios98.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: The read-gated write. PUT returns code 200 with message success, and GET /p/ then returns 51 bytes of code 401 expire missing: the instance signs its raw path and a guest cannot mint the signature. Provider 139Yun. The bytes went in and cannot come out.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: read-gated
  - upstream_provider: 139Yun
  - fronting_cdn: nginx
  - advertised_write_flag: yes
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 9237b01d
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:33:30.444Z
  - consecutive_failures: 1
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - probe:https://pan.ios98.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '美辰云盘'
  - probe:https://pan.ios98.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 11 root entries; write:true, write_content_bypass:None, provider:139Yun
  - probe:https://pan.ios98.com/api/fs/put 2026-10-22: the zero-byte oracle returned code 403 with message 'file exists', so the write permission passed and nothing was written
  - probe:https://pan.ios98.com/p/ 2026-10-22: GET /p/<the written path> returned HTTP 200 with 51 bytes of code 401 'expire missing' instead of the 32 bytes written
  - probe:https://pan.ios98.com/ 2026-11-11:  | capture: sha256:e5bd635fe91525a9a6a4cd79616f10742c2c80b2ba0eeb6074e37243ba141d92 | quote: "checked_at": "2026-11-11T00:20:07.153Z"
  - probe:https://pan.ios98.com/ 2026-11-11: the anonymous root listing hashed to this value | capture: sha256:e5bd635fe91525a9a6a4cd79616f10742c2c80b2ba0eeb6074e37243ba141d92 | quote: "listing_sha256": "9237b01d"
  - probe:https://pan.ios98.com/ 2026-11-11:  | capture: sha256:e5bd635fe91525a9a6a4cd79616f10742c2c80b2ba0eeb6074e37243ba141d92
  - probe:https://pan.ios98.com/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:e5bd635fe91525a9a6a4cd79616f10742c2c80b2ba0eeb6074e37243ba141d92
  - probe:https://pan.ios98.com/ 2026-11-11: the anonymous guest session answered and its root listing returned entries, so the instance is reachable without an account | capture: sha256:e5bd635fe91525a9a6a4cd79616f10742c2c80b2ba0eeb6074e37243ba141d92 | quote: "alive": true
  - probe:https://pan.ios98.com/ 2026-11-19: the liveness and mount-list probe answered at this instant | capture: sha256:b8691d5bc16518ca359c33b7107dcf59d0fb47442907cb0214fcf638bdc3ed94 | quote: "checked_at": "2026-11-19T03:33:30.444Z"
  - probe:https://pan.ios98.com/ 2026-11-25: the fresh probe found no anonymous settings response and records this as the first consecutive liveness failure at pan.ios98.com | capture: sha256:7ae0a9aaf72b7a75db310b6e883967af50ac6e6b6105fddf602f827f9d80b923 | quote: "alive": false, "requests": { "settings": { "url": "https://pan.ios98.com/api/public/settings", "method": "GET", "status": null,
  - probe:https://pan.ios98.com/ 2026-11-25: the settings request of the probe received no HTTP status | capture: sha256:48c6e49fa274def1d9548703aa527871fed7adc859bdca7d350bd5b5bfb16e56 | quote: "status": 0
  - probe:https://pan.ios98.com/ 2026-11-25: the probe record was checked at this instant, when the host did not answer | capture: sha256:48c6e49fa274def1d9548703aa527871fed7adc859bdca7d350bd5b5bfb16e56 | quote: "checked_at": "2026-11-25T01:38:31.417Z"
- sources:
  - [1] https://pan.ios98.com/
