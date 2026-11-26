# Gumlet

> gumlet.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gumlet/ | JSON https://fshy.ajam.dev/api/v1/entity/gumlet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gumlet

- `storage/gumlet-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:43.469Z (inherited) | stale on 2026-12-04
- url https://www.gumlet.com/pricing/
- free tier: None reachable: Free plan is 60 storage minutes of video (not GB) with 100 GB bandwidth/month. A transcode-and-deliver product, not storage; API access starts on the $6/mo Creator tier. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Free plan is 60 storage minutes of video (not GB) with 100 GB bandwidth/month — a transcode-and-deliver product, not storage; API access starts on the $6/mo Creator tier
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is 60 storage minutes of video (not GB) with 100 GB bandwidth/month — a transcode-and-deliver product, not storage; API access starts on the $6/mo Creator tier
  - probe:https://www.gumlet.com/pricing/ 2026-11-19: the free plan meters storage in minutes, not GB, with 100 GB bandwidth, so it is a video platform and not byte storage | capture: sha256:a0b049506942ce1bd69de577ca696d5f0f74e33d2b4fad1cff3373c2d6d45f13 | quote: Gumlet's Free Plan includes 60 storage minutes, 100 GB bandwidth
  - probe:https://www.gumlet.com/pricing/ 2026-11-19: API access is gated on paid tiers, not the free plan | capture: sha256:a0b049506942ce1bd69de577ca696d5f0f74e33d2b4fad1cff3373c2d6d45f13 | quote: API Access\",\"tiers
- sources:
  - [1] https://www.gumlet.com/pricing/

## Gumlet (free plan)

- `storage/gumlet` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:42.833Z (live) | stale on 2026-12-04
- url https://www.gumlet.com
- free tier: Free Forever video plan: 60 storage minutes, 100 GB bandwidth/mo, 60 mins live streaming/mo, 1 seat. Storage minutes are minutes of uploaded video, not bytes; original images are not stored. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 100 GB/month bandwidth on free (generous), then metered. | metered: yes | free allowance: 100 GB per month
- identity: email
- interface: s3, rest
- limits note: 60 storage mins, 100 GB/mo bandwidth, 60 mins live streaming. All assets transcoded to adaptive bitrate.
- interface detail: rest
- tooling: REST upload plus URL transformations, S3 source pull.
- composes with: Unlimited free accounts x 60 storage minutes. A video-minute is a terrible unit for binary storage: 60 min at 1080p is ~1-4 GB and everything is transcoded, never stored as original bytes.
- reliability: Transcodes by design; originals are not the delivered artifact. Unusable for byte-exact storage.
- notes: 60 storage minutes of video, not bytes. No meaningful free image allowance. This is a video-first CDN.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 60 storage minutes of video, not bytes. No meaningful free image allowance — this is a video-first CDN.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: '60 storage mins', '100 GB bandwidth/mo', 'Free Forever'
  - [1] 2026-11-19: the first-party pricing page states the Free plan's 60 storage minutes, 100 GB bandwidth and 60 live-streaming minutes | capture: sha256:6b541a820b550fc091125ded728425c46a82bc1172da716635fb2c549eb48e3d | quote: Gumlet's Free Plan includes 60 storage minutes, 100 GB bandwidth, 60 minutes of live streaming
  - [1] 2026-11-19: the video Free plan is labelled Free Forever | capture: sha256:6b541a820b550fc091125ded728425c46a82bc1172da716635fb2c549eb48e3d | quote: Free Forever
  - [2] 2026-11-19: uploaded videos are transcoded into multiple formats, so originals are not the delivered bytes | capture: sha256:e0bae767724c5cd51d58bc9e287923fa6919634be363223045dd8d5af5b088c7 | quote: When you upload a video, Gumlet transcodes it into multiple resolutions and formats (for example, HLS, DASH, MP4) to support adaptive playback.
- sources:
  - [1] https://www.gumlet.com/pricing/
  - [2] https://docs.gumlet.com/video/getting-started/faqs
