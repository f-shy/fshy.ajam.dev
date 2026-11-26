# reddit as a file host

> postpone.app | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/postpone/ | JSON https://fshy.ajam.dev/api/v1/entity/postpone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## reddit as a file host

- `storage/reddit-as-a-file-host` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.551Z (live) | stale on 2026-12-04
- url https://help.postpone.app/platforms/reddit/media-limits
- free tier: None reachable: images and video only. There is no arbitrary-file attachment in the Reddit composer or API, so datasets cannot be stored at all regardless of the 20 MB figure. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Images and video only. There is no arbitrary-file attachment in the Reddit composer or API, so datasets cannot be stored at all regardless of the 20 MB figure.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: images and video only — there is no arbitrary-file attachment in the Reddit composer or API, so datasets cannot be stored at all regardless of the 20 MB figure
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: images and video only — there is no arbitrary-file attachment in the Reddit composer or API, so datasets cannot be stored at all regardless of the 20 MB figure
  - [1] 2026-11-19: Reddit uploads are limited to image/video media with a 20 MB image ceiling, so no arbitrary-file storage exists | capture: sha256:d857df23582f7eff0680474cf2ff22b5e4562e01332263220e8f157d45225ed4 | quote: Reddit accepts images up to 20 MB. Postpone automatically converts larger images, and .heic images, to a Reddit-compatible JPEG.
- sources:
  - [1] https://help.postpone.app/platforms/reddit/media-limits
