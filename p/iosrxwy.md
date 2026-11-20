# 七喵的宝藏

> iosrxwy.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iosrxwy/ | JSON https://fshy.ajam.dev/api/v1/entity/iosrxwy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 七喵的宝藏

- `netdisk-pan/pan-iosrxwy-com` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:45.420Z (live) | stale on 2026-12-11
- url https://pan.iosrxwy.com/
- free tier: anonymous guest read of 0 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through nginx; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://pan.iosrxwy.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Anonymous JSON listing of 2 root directories returned by the AList API on a fresh probe; guest session with permission 0; the instance still flaps between API and non-API answers.
- notes: Answered as an AList API in one run and as a non-API in another, and never returned a listing. Unclassifiable at this sample size.
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - fronting_cdn: nginx
  - advertised_write_flag: no
  - write_content_bypass: absent
  - base_path: /
  - first_seen: 2024-01-20
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
- evidence:
  - probe:https://pan.iosrxwy.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '七喵的宝藏'
  - probe:https://pan.iosrxwy.com/api/fs/list 2026-11-19: an anonymous GET /api/fs/list returns a success JSON body with two root directory entries | capture: sha256:068c0a361f70e48ae82030b590187da12975ae8cdbc10e16275507c18123e210 | quote: "total":2
  - probe:https://pan.iosrxwy.com/api/fs/list 2026-11-19: the read path now returns an anonymous listing of two root directories | capture: sha256:068c0a361f70e48ae82030b590187da12975ae8cdbc10e16275507c18123e210 | quote: "total":2
  - probe:https://pan.iosrxwy.com/api/me 2026-11-19: the session is anonymous: /api/me returns a guest user with permission 0 and no account requirement | capture: sha256:92b5f17df4530587fe3412ec271b5970bf2cf3764f1adab0b418c9d9a10368fe | quote: "username":"guest"
  - probe:https://pan.iosrxwy.com/api/public/settings 2026-11-19: the host answers the AList settings API with title 七喵的宝藏 | capture: sha256:5aa80b49531272b3f77f952c1944a76495d95d16c9a7651095ac9d8dd5cef94e | quote: "site_title":"七喵的宝藏"
- sources:
  - [1] https://pan.iosrxwy.com/
