# Bilibili video upload

> bilibili.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bilibili/ | JSON https://fshy.ajam.dev/api/v1/entity/bilibili.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bilibili video upload

- `storage/bilibili-video-upload` | fails-egress | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://bilibili.com
- free tier: 8 GB per video reported for most accounts; some accounts higher (third-party guide, not vendor docs) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 8 GB/file | bytes: 8000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free playback CDN, but segment/m3u8 delivery with Referer and anti-leech checks. Not a plain file GET. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 8 GB/file [1]
  - write-gated: review gate [1]
  - write-gated: review rejects arbitrary data, so it is a video host, not storage [1]
- limits note: 8 GB/file; mandatory transcode (never byte-exact); content review gate; account must be phone-verified; playback URLs are signed and expire
- interface detail: rest
- tooling: open upload API documented in Chinese (POST /arcopen/fn/archive/video/init, chunked upload above 100 MB); bilibili-API-collect and multiple uploader CLIs exist
- composes with: 8 GB x unlimited videos x N verified accounts; 20 TiB = 2,560 uploads. Realistically the biggest single-file social quota found, but each video must pass transcode + review
- reliability: transcoding destroys the bytes and review rejects arbitrary data, so it is a video host, not storage; CDN URLs are time-signed
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 8 GB per video reported for most accounts; some accounts higher (third-party guide, not vendor docs)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Maximum file size is reported to be 8GB for most accounts; some accounts may have higher limits' (third-party, hedged)
  - [2] 2026-10-21: /arcopen/fn/archive/video/init, '文件不超过100M时...超过100M时，须通过分片上传流程' (chunked upload above 100 MB)
- sources:
  - [1] https://bilibilihelp.com/creator/bilibili-video-upload-guide/
  - [2] https://bilibili.apifox.cn/api-23693239
