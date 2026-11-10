# Shade

> shade.inc | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shade/ | JSON https://fshy.ajam.dev/api/v1/entity/shade.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shade

- `storage/shade` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://shade.inc
- free tier: 20 GB free account (stated in rclone's own backend docs) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: not documented; marketed as a media-workflow NAS with collaboration, no published free transfer allowance | metered: yes
- identity: email
- interface: rest, rclone
- limits note: 20 GB free; product is sold as enterprise media storage (LucidLink/Frame.io replacement), so the free tier is a trial-shaped loss-leader
- interface detail: rest
- tooling: rclone backend 'shade' (Tier 1, added v1.73)
- composes with: Free tier provides 20 GB per account across independently registered accounts.
- reliability: very new backend (v1.73) on an enterprise-oriented vendor; free tier may be repriced or withdrawn as the product matures
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB free account (stated in rclone's own backend docs)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'you can start with a free account and get 20GB of storage for free', backend added v1.73
  - [2] 2026-10-21: product positioning as media NAS / LucidLink-Frame.io-Iconik replacement, no public free-tier pricing table
- sources:
  - [1] https://rclone.org/shade/
  - [2] https://shade.inc/

## shade (shade.inc)

- `storage/shade-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.shade.inc/pricing
- free tier: None reachable: Enterprise 'AI cloud NAS' at $29.75-35 per seat/month for 500 GB active storage per seat. Has both a native rclone backend and an S3 API at s3.shade.inc, so technically excellent. But per-s. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Enterprise 'AI cloud NAS' at $29.75-35 per seat/month for 500 GB active storage per seat. Has both a native rclone backend and an S3 API at s3.shade.inc, so technically excellent — but…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Enterprise 'AI cloud NAS' at $29.75-35 per seat/month for 500 GB active storage per seat. Has both a native rclone backend and an S3 API at s3.shade.inc, so technically excellent — but…
  - [2] 2026-10-21: cited as the basis of the rejection: Enterprise 'AI cloud NAS' at $29.75-35 per seat/month for 500 GB active storage per seat. Has both a native rclone backend and an S3 API at s3.shade.inc, so technically excellent — but per-s
  - [3] 2026-10-21: cited as the basis of the rejection: Enterprise 'AI cloud NAS' at $29.75-35 per seat/month for 500 GB active storage per seat. Has both a native rclone backend and an S3 API at s3.shade.inc, so technically excellent — but per-s
- sources:
  - [1] https://www.shade.inc/pricing
  - [2] https://rclone.org/shade/
  - [3] https://academy.shade.inc/developers/guides/uploading-to-shade
