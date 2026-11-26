# 七十二时.的资源站

> qsesvick.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qsesvick/ | JSON https://fshy.ajam.dev/api/v1/entity/qsesvick.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 七十二时.的资源站

- `netdisk-pan/alist-qsesvick-top` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:08:33.683Z (live) | stale on 2026-12-17
- url https://alist.qsesvick.top/
- free tier: anonymous guest read of 6 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through openresty; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://alist.qsesvick.top/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: One of three hostnames on the 20237737 operator's corpus, and the one the community index publishes as its WebDAV endpoint. 5 root entries; the WebDAV endpoint answers PROPFIND with 207 to the published guest credential.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: openresty
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 1280
  - base_path: /
  - listing_sha256: 7a909707
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T04:07:28.035Z
  - consecutive_failures: 0
- evidence:
  - probe:https://alist.qsesvick.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '七十二时.的资源站'
  - probe:https://alist.qsesvick.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 5 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://alist.qsesvick.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://alist.qsesvick.top/ 2026-11-11:  | capture: sha256:8843ab27a9e81b12ae7d93cd30c679a2c7056ae913e61134585508df346d43c3
  - probe:https://alist.qsesvick.top/ 2026-11-11:  | capture: sha256:8843ab27a9e81b12ae7d93cd30c679a2c7056ae913e61134585508df346d43c3 | quote: "checked_at": "2026-11-11T00:20:01.877Z"
  - probe:https://alist.qsesvick.top/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:accc248bab6c79ba7701345bb6328cae00eabd06249cfc7d03bf96fde7c3eb2d | quote: "checked_at": "2026-11-19T03:31:03.163Z"
  - probe:https://alist.qsesvick.top/ 2026-11-19: the anonymous root listing hashed to ec8bc9ba, equal to the recorded value; no hash change | capture: sha256:accc248bab6c79ba7701345bb6328cae00eabd06249cfc7d03bf96fde7c3eb2d | quote: "listing_sha256": "ec8bc9ba"
  - probe:https://alist.qsesvick.top/ 2026-11-19: the host answered every request of this probe, so the failure count stayed at zero | capture: sha256:accc248bab6c79ba7701345bb6328cae00eabd06249cfc7d03bf96fde7c3eb2d
  - probe:https://alist.qsesvick.top/api/public/settings 2026-11-25: a fresh anonymous probe of the AList public settings endpoint of alist.qsesvick.top answered at this instant (HTTP 200, JSON, no challenge) | capture: sha256:f6c0f5eee0f1161e2ad2221de83c6c34e8d740ed74876132d1b9489305c85555 | quote: "probed_at": "2026-11-25T04:07:28.035Z"
  - probe:https://alist.qsesvick.top/api/public/settings 2026-11-25: the settings endpoint of alist.qsesvick.top answered HTTP 200 to an anonymous request | capture: sha256:f6c0f5eee0f1161e2ad2221de83c6c34e8d740ed74876132d1b9489305c85555 | quote: "status": 200
  - probe:https://alist.qsesvick.top/ 2026-11-25: the anonymous root listing of this host hashed to 7a909707 in the fresh probe, not the previously recorded ec8bc9ba | capture: sha256:f6c75fb7dafecb65ee7fb4ed8f4418e1ba681460bba3a55abdd957c39a1aa789 | quote: "listing_sha256": "7a909707"
  - probe:https://alist.qsesvick.top/ 2026-11-25: the fresh anonymous root listing returned six entries, one more than the five previously recorded | capture: sha256:f6c75fb7dafecb65ee7fb4ed8f4418e1ba681460bba3a55abdd957c39a1aa789 | quote: "entry_count": 6
  - probe:https://alist.qsesvick.top/ 2026-11-25: the fresh probe answered the anonymous session, settings and mount list, so the fresh listing hash stands | capture: sha256:f6c75fb7dafecb65ee7fb4ed8f4418e1ba681460bba3a55abdd957c39a1aa789 | quote: "alive": true
  - probe:https://alist.qsesvick.top/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:b00050c87e6a68ed7155e717ba45c413fad2e95152d2f7a3d8dedb4bbf3d3cf5 | quote: "checked_at": "2026-11-25T01:38:28.682Z"
  - probe:https://alist.qsesvick.top/ 2026-11-25: the anonymous root listing now returns 6 entries, not 5 | capture: sha256:b00050c87e6a68ed7155e717ba45c413fad2e95152d2f7a3d8dedb4bbf3d3cf5 | quote: "root_entries": 6
  - probe:https://alist.qsesvick.top/ 2026-11-25: the re-probe answered as an anonymous guest, so registration is not needed | capture: sha256:b00050c87e6a68ed7155e717ba45c413fad2e95152d2f7a3d8dedb4bbf3d3cf5 | quote: "guest": true
- sources:
  - [1] https://alist.qsesvick.top/
