# Jumpshare Basic

> jumpshare.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jumpshare/ | JSON https://fshy.ajam.dev/api/v1/entity/jumpshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jumpshare Basic

- `storage/jumpshare-basic` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:06.407Z (live) | stale on 2026-12-04
- url https://www.jumpshare.com/pricing
- free tier: Free plan is metered by upload count, not bytes: 25 uploads and 60 seconds of recording. No storage figure is published. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Basic: 250 MB maximum file size per upload (pricing comparison table). | source: [1] | note: not stated
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
  - [1] 2026-11-19: the Basic plan still lists 25 uploads on the pricing page | capture: sha256:b80970567fdbde185fc2de2733d39cea69a28f0ae9b8ffeb922c859b9d441618 | quote: 25 uploads limit
  - [1] 2026-11-19: the Basic plan caps a single upload at 250 MB | capture: sha256:b80970567fdbde185fc2de2733d39cea69a28f0ae9b8ffeb922c859b9d441618 | quote: Maximum file size per upload 250 MB 10 GB 20 GB Unlimited
  - [2] 2026-11-19: the support page still states 60 seconds of recording and 50 total uploads, differing from the pricing page's 25 | capture: sha256:878a36b1a241a200b484efc1ec548c932f5d3c77206c52b4d548f10c741f831b | quote: The Jumpshare Basic plan is free to use and offers 60 seconds of video recording and 50 total uploads
- sources:
  - [1] https://www.jumpshare.com/pricing
  - [2] https://support.jumpshare.com/article/125-which-jumpshare-plan-should-i-get
