# 小雅 xiaoya

> xiaoya.pro | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiaoya/ | JSON https://fshy.ajam.dev/api/v1/entity/xiaoya.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小雅 xiaoya, the most widely published public instance (alist.xiaoya.pro)

- `netdisk-pan/alist-xiaoya-pro` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:45.419Z (live) | stale on 2026-12-11
- url https://alist.xiaoya.pro/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; repurposed domain | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): the host stopped serving: repurposed domain probe:https://alist.xiaoya.pro/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Death mode: repurposed domain.
- notes: 小雅 xiaoya, the most widely published public instance. repurposed domain
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - death_mode: repurposed domain
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
  - first_seen: 2024-01-20
- evidence:
  - probe:https://alist.xiaoya.pro/api/public/settings 2026-10-22: GET /api/public/settings returned HTTP 302 to a consumer portal rather than JSON, so the domain has been repurposed or seized; no API and no mount list
  - probe:https://alist.xiaoya.pro/api/public/settings 2026-11-19: the API endpoint still 302-redirects to a consumer portal instead of returning AList JSON, so the domain remains repurposed | capture: sha256:f85751c254e517ded3af3923636e312c5e0f68504307aff4a90da6dcae22dcb2 | quote: "final_url": "https://bmh.163.com"
  - [1] 2026-11-19: the domain now serves a media-player product page rather than an AList mount list | capture: sha256:66e275f806f5864e5295e8a2c648ac907b0fe41302a024da6209414e6f3c04b3 | quote: 网易爆米花
- sources:
  - [1] https://alist.xiaoya.pro/
