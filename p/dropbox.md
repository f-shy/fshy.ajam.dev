# dropbox basic

> dropbox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dropbox/ | JSON https://fshy.ajam.dev/api/v1/entity/dropbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dropbox basic

- `storage/dropbox-basic` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.673Z (live) | stale on 2026-12-04
- url https://www.dropbox.com/plans
- free tier: none reachable: 2 GB free at signup; referral bonuses are capped and the account is capped well under 500 GB. rclone backend exists (Tier 1) but the quota is fatal. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 2 GB free at signup; referral bonuses are capped and the account is capped well under 500 GB. rclone backend exists (Tier 1) but the quota is fatal.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 2 GB free at signup; referral bonuses are capped and the account is capped well under 500 GB. rclone backend exists (Tier 1) but the quota is fatal.
  - [1] 2026-11-19: the free Basic plan provides 2 GB | capture: sha256:63b23d14995203a24ccc762d5a4759aa9f872a66bba055a29bf32dd5f63467b5 | quote: BasicFree 2 GB to store and share your files
- sources:
  - [1] https://www.dropbox.com/plans
