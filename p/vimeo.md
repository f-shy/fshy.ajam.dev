# vimeo weekly-quota

> vimeo.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vimeo/ | JSON https://fshy.ajam.dev/api/v1/entity/vimeo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vimeo (Free plan)

- `storage/vimeo` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:22.710Z (live) | stale on 2026-12-04
- url https://vimeo.com
- free tier: Unlimited storage for public, non-embeddable videos; 3 GB total for embeddable and non-public videos. This is a 2024-onwards rewrite of the old '500 MB/week' rule. The weekly quota now applies only to legacy paid Plus/Pro accounts, not Free. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 200 GB per file | bytes: 200000000000 | source: [1] | note: not stated
- retention: The killer is not quota, it is that Vimeo deletes exactly the thing you want to store: 'your source file will be permanently deleted if you are a Free or Basic member' | source: [1] | note: not stated
- egress: Unlimited bandwidth for public non-embeddable videos; 1 TB/month for embeddable and non-public. No per-GB charge on Free. | metered: no | free allowance: 1 TB per month
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 200 GB per file [1]
  - per-object-cap (binding): 200 GB/file [1]
- limits note: ~200 GB per file advised for a successful upload, and no video longer than 24 hours. That 200 GB/file is genuinely large.
- interface detail: rest
- tooling: The yt-dlp tool includes a Vimeo extractor that requires authentication cookies for protected content. Vimeo API v3 exposes `/me/videos`, but direct binary download links require paid subscriptions.
- composes with: Unlimited public videos x unlimited free accounts. In principle unbounded capacity at zero cost. The only thing stopping it is the original-file problem below.
- reliability: The killer is not quota, it is that Vimeo deletes exactly the thing you want to store: 'your source file will be permanently deleted if you are a Free or Basic member'. Free accounts also cannot enable downloads at all, so there is no supported retrieval path.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'unlimited public videos ... Embeddable and non-public videos are limited to 3 GB'; '1 TB of bandwidth per month'
  - [2] 2026-10-21: 'your source file will be permanently deleted if you are a Free or Basic member'
  - [3] 2026-10-21: 'Plan type: Free and Basic members cannot enable video downloads. They also cannot download videos from their own account.'
  - [4] 2026-10-21: 'files are kept within 200 GB ... no videos longer than 24 hours'
  - [1] 2026-11-19: Free plan: unlimited public videos; 3 GB Managed storage for embeddable and non-public videos; free forever | capture: sha256:08c9ff2fede6cec71f5ce408cfd24c144cf571b7617f558d32d1bcde4dfe9313 | quote: Vimeo is free, with unlimited public videos and no ads. Embeddable and non-public videos are limited to 3 GB of Managed storage, and the plan stays free forever for active accounts.
  - [5] 2026-11-19: 200 GB per-file advice and a 24-hour video length limit remain on the upload page | capture: sha256:c0b107ec0394103449c4237d4feaa8acfadbf0a98ef7504de81afccac0a49535 | quote: We advise that files are kept within 200 GB for a successful upload. We also do not support uploads of videos longer than 24 hours.
  - [2] 2026-11-19: Free members' source files are permanently deleted by default | capture: sha256:b2b86675503a22a7f28305aceb802a01cae91f8f89ae01b06cd6c157a6554067 | quote: By default, your source file will be permanently deleted if you are a Free member or if you are a paid member but haven't enabled source file storage in your account settings as described above.
- sources:
  - [1] https://help.vimeo.com/hc/en-us/articles/12425432518801-About-the-Vimeo-Free-plan
  - [2] https://help.vimeo.com/hc/en-us/articles/46427284891537-Store-your-source-files-on-Vimeo
  - [3] https://help.vimeo.com/hc/en-us/articles/29641627072017
  - [4] https://help.vimeo.com/hc/en-us/articles/18774922216721
  - [5] https://help.vimeo.com/hc/en-us/articles/18774922216721-How-to-upload-a-video-to-Vimeo

## vimeo weekly-quota premise (500 mb/week)

- `storage/vimeo-weekly-quota-premise` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:35.531Z (live) | stale on 2026-12-04
- url https://help.vimeo.com/hc/en-us/articles/26238558836881
- free tier: none reachable: Dead premise worth correcting: the widely-repeated '500 MB/week free' figure describes the pre-June-2024 Free plan and legacy paid Plus/Pro weekly quotas. Current Free is unlimited public… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Dead premise worth correcting: the widely-repeated '500 MB/week free' figure describes the pre-June-2024 Free plan and legacy paid Plus/Pro weekly quotas. Current Free is unlimited public…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Dead premise worth correcting: the widely-repeated '500 MB/week free' figure describes the pre-June-2024 Free plan and legacy paid Plus/Pro weekly quotas. Current Free is unlimited public…
  - [1] 2026-11-19: the first-party Vimeo help page states the current Free plan has no weekly 500 MB quota but unlimited public storage and 3 GB embeddable/non-public | capture: sha256:2b09ea9d0c2624f743f0d46c3c92df5917a37df0b8fe2e702f7cab77d434dd48 | quote: Free plan: unlimited storage for public, non-embeddable videos, and up to 3 GB for embeddable and non-public videos.
- sources:
  - [1] https://help.vimeo.com/hc/en-us/articles/26238558836881
