# 知网云盘

> xyyh.xyz | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xyyh/ | JSON https://fshy.ajam.dev/api/v1/entity/xyyh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 知网云盘

- `netdisk-pan/pan-xyyh-xyz` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-20T04:19:05.278Z (live) | stale on 2026-12-12
- url https://pan.xyyh.xyz/
- free tier: anonymous guest read of 2 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through no identified front; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://pan.xyyh.xyz/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: On 2026-11-19 the WebDAV endpoint answered HTTP 401 with Basic realm=alist, so only the REST read path is anonymous.
- notes: Answered as an AList API on one run and not on another, and listed 2 root entries once. Its zero-byte oracle returned neither of the two defined messages.
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: not-tested
  - upstream_provider: unknown
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 9e6193c6
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-20T04:00:34.104Z
  - consecutive_failures: 0
- evidence:
  - probe:https://pan.xyyh.xyz/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '知网云盘'
  - probe:https://pan.xyyh.xyz/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 2 root entries; write:false, write_content_bypass:None, provider:unknown
  - probe:https://pan.xyyh.xyz/api/fs/list 2026-11-19: the guest API read succeeded on 2026-11-19 and returned 2 root entries with write:false, so the service is alive | capture: sha256:5f8dfd280cd8a3fd93d80f6f86c5136fc86e39a2d3a63f36215297934461a999 | quote: "total":2,"readme":"","header":"","write":false,"provider":"unknown"
  - probe:https://pan.xyyh.xyz/dav 2026-11-19: the WebDAV endpoint on 2026-11-19 answered 401 with Basic realm=alist | capture: sha256:2d68a90cd50e458fe176e9916a28b7ef9bace1081455f8864758746ab50d8298 | quote: "status": 401,
  - probe:https://pan.xyyh.xyz/api/fs/list 2026-11-19: the anonymous 2026-11-19 listing returned 2 root entries with write:false and provider:unknown | capture: sha256:5f8dfd280cd8a3fd93d80f6f86c5136fc86e39a2d3a63f36215297934461a999 | quote: "total":2,"readme":"","header":"","write":false,"provider":"unknown"
  - probe:https://pan.xyyh.xyz/api/me 2026-11-19: the 2026-11-19 session is an anonymous guest with an empty password and permission 2, so no account is needed | capture: sha256:9cee0342201241f36f6c62be3b4e1292b11efe5ee46cdcfd2dcaee0391d552b3 | quote: "id":2,"username":"guest","password":"","base_path":"/","role":1,"disabled":false,"permission":2
  - probe:https://pan.xyyh.xyz/api/public/settings 2026-11-19: the 2026-11-19 settings read identifies the AList instance 知网云盘 and publishes no per-object cap | capture: sha256:73017d6d8813b3aac0f62ecbfe840f102ae827df9893765ba5fea063d2d38d4c | quote: "site_title":"知网云盘","sso_compatibility_mode":"false"
  - probe:https://pan.xyyh.xyz/dav 2026-11-19: the WebDAV endpoint on 2026-11-19 answered 401 with Basic realm=alist, so the WebDAV interface exists but is gated | capture: sha256:2d68a90cd50e458fe176e9916a28b7ef9bace1081455f8864758746ab50d8298 | quote: "status": 401,
  - probe:https://pan.xyyh.xyz/api/fs/list 2026-11-20: a live 2026-11-20 probe of the anonymous AList listing endpoint answered HTTP 200 with 546 bytes | capture: sha256:483a76bd860f32b6e89c77b5b6995a7e466cf125bac2b1eb57ace21e5ace51c4 | quote: "probed_at": "2026-11-20T04:00:34.104Z"
- sources:
  - [1] https://pan.xyyh.xyz/
