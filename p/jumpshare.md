# Jumpshare Basic

> jumpshare.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jumpshare/ | JSON https://fshy.ajam.dev/api/v1/entity/jumpshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jumpshare Basic

- `storage/jumpshare-basic` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.jumpshare.com/pricing
- free tier: Free plan is metered by upload count, not bytes: 25 uploads and 60 seconds of recording. No storage figure is published. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free within plan; bandwidth is a paid-plan upsell. | metered: no
- identity: email
- interface: s3, webdav, rclone
- limits note: pull-count/request-rate: 25 uploads total on Basic, 60 s recording; retention not stated.
- interface detail: web + desktop app; no S3/WebDAV
- tooling: official desktop app; no rclone backend
- composes with: 25 uploads x unlimited accounts. Count-metered rather than byte-metered, which is unusual, but 25 objects per identity is not a storage model.
- reliability: Basic is explicitly a trial-shaped experience ('For getting started'); the paid plan's selling point is 'Unlimited uploads'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free plan is metered by upload count, not bytes: 25 uploads and 60 seconds of recording. No storage figure is published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Basic (Free): '25 uploads limit', '5 minute recording time'; Plus: 'Unlimited uploads'
  - [2] 2026-10-21: 'The Jumpshare Basic plan is free to use and offers 60 seconds of video recording and 50 total uploads' (note: this page says 50, the pricing page says 25 — the number moved)
- sources:
  - [1] https://www.jumpshare.com/pricing
  - [2] https://support.jumpshare.com/article/125-which-jumpshare-plan-should-i-get
