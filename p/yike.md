# 一刻相册

> yike.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yike/ | JSON https://fshy.ajam.dev/api/v1/entity/yike.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 一刻相册 (Baidu One Moment photo cloud)

- `netdisk-pan/yike-album` | fails-quota | evidence reported | binding per-object-cap | category photo cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T14:57:25.809Z (inherited) | stale on 2026-12-10
- url https://www.yike.com
- free tier: unverified: the service page advertises unlimited album space but publishes no free capacity figure, price or tier | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published, media only | source: [2]
- retention: Not published | source: [2]
- egress: Free viewing and download, with no byte meter mentioned | metered: no | source: [1]
- identity: country-phone | detail: a Baidu account | country: 86
- interface: rest
- limits:
  - per-object-cap (binding): unverified: the service page publishes no original-byte return test or re-encoding behaviour [1]
- binding note: The quota is unlimited and the gate is that only photographs and video are accepted, with re-encoding at ingest, so the number that binds is the per-object type restriction and not a byte count. An unlimited store that returns different bytes is not capacity.
- tooling: mobile and web clients only, with no WebDAV, S3 or rclone. Any automation would need an unofficial scraper that does not exist
- composes with: Unlimited per account by design, and Baidu uses it as a photo-loss-leader. If a wrapper existed it would be the only genuinely unlimited free tier on the forum, and no wrapper exists
- reliability: Baidu-backed, so it is unlikely to close. It is a photo album and not storage: the original-bytes-return test is unproven here, and ingest re-encoding is the documented behaviour of the album path
- notes: The lowest-confidence record in the batch: one forum sentence and no vendor page. Kept because an unlimited free photo tier from Baidu is worth a later check, and because the re-encode question is the one that decides whether it is storage.
- extras:
  - access_mode: registration-gated
  - media_only: yes
  - reencodes_at_ingest: unverified
- evidence:
  - [1] 2026-10-21: '图片存储可以用一刻相册，无限容量'
  - [3] 2026-10-21: '自己存色图都用谷歌无限相册', an adjacent forum thread on the same unlimited-photo-album pattern
  - probe:https://yike.baidu.com 2026-11-03: the page on yike.baidu.com answers 200 with the unlimited album space title; the record's own URL www.yike.com did not answer | capture: sha256:ec6cf66b3bf7f6e667a3de215cb7d4cc95691d892e19c73023b42354306e3a90 | quote: <title>领取无限相册空间</title>
  - probe:https://www.yike.com 2026-11-03: the URL this record names, www.yike.com, did not answer the probe, which timed out | capture: sha256:aed554ad07ed9d9437dde20b0b301193de6ad76509f8468359306d89791fc6e8 | quote: "error": "timeout"
  - [4] 2026-11-25: the service page title advertises unlimited album space | capture: sha256:a08b6a8eca3017dce2fa5d3d01a6af0b56df44c3f5cda3e2aac1795138a63172 | quote: <title>领取无限相册空间</title>
  - [5] 2026-11-25: the Baidu app listing states unlimited storage space with unlimited original-quality photo and video backup | capture: sha256:9baf247822f806ba9c1168ef92271b235625010f59c09a4a89cfc7fe3d566dff | quote: 1、无限存储空间：无限量原画质备份照片视频，任意手机设备都能访问。
- sources:
  - [1] https://linux.do/t/topic/802517
  - [2] https://www.yike.com
  - [3] https://linux.do/t/topic/1037046
  - [4] https://yike.baidu.com
  - [5] https://mobile.baidu.com/appitemp/3869444
