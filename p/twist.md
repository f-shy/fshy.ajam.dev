# Twist

> twist.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/twist/ | JSON https://fshy.ajam.dev/api/v1/entity/twist.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Twist (Doist) Free plan

- `storage/twist-free-plan` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://twist.com/pricing
- free tier: 5 GB of file storage per team on Free; unlimited on Twist Unlimited. 100 MB per attachment. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, unmetered. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB cap [1]
- limits note: 5 GB/team; 100 MB/attachment; 10 MB for emailed attachments; free-plan thread history older than one month is not viewable (though Twist explicitly retains it server-side and never deletes).
- interface detail: rest
- tooling: Twist REST API (api.twist.com/api/v3) with attachment upload by `file_id`; OAuth2 app registration. Weaker client ecosystem than Slack.
- composes with: Unlimited free teams per account ('create a separate, free team'), so N teams x 5 GB is trivially repeatable. But each team needs its own members/invites.
- reliability: No deletion stated ('nothing will ever be deleted'), which is unusual and good. The 5 GB cap is the wall.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB of file storage per team on Free; unlimited on Twist Unlimited. 100 MB per attachment.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Unlimited file storage' (Unlimited plan)
  - [1] 2026-10-21: 'There is a 100MB file size limit for attachments'; 'When using the Free plan of Twist, the storage limit is 5GB.'
  - [3] 2026-10-21: 'all your team's data will still be safely stored on our servers – nothing will ever be deleted'
- sources:
  - [1] https://get.twist.help/hc/en-us/articles/360004758880-Add-files-to-Twist
  - [2] https://twist.com/help/articles/what-is-twist-unlimited-mehD6bnu
  - [3] https://twist.com/pricing

## Twist (free plan)

- `storage/twist` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://twist.com
- free tier: 5 GB storage on Free (unlimited on Twist Unlimited); 100 MB per attachment | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; files served from Twist's own storage | metered: no
- identity: email
- interface: rest, rclone
- limits note: 5 GB per team; 100 MB per attachment; 10 MB for emailed attachments; thread history older than one month is not viewable on Free (data retained server-side, not deleted)
- interface detail: rest
- tooling: Twist has an API but no documented bulk file-upload surface and no rclone backend; wrapper-only
- composes with: 5 GB x N free teams. Twist free teams are unlimited in number from one account ('create a separate, free team'), so it chains - but 5 GB/team means ~100 teams for 500 GB.
- reliability: Distinctive upside: Twist explicitly never deletes data on the Free plan - the one-month limit is visibility only. That makes it a rare non-hostile free tier, just a small one.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB storage on Free (unlimited on Twist Unlimited); 100 MB per attachment
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'There is a 100MB file size limit for attachments'; 'When using the Free plan of Twist, the storage limit is 5GB'
  - [2] 2026-10-21: 'all your team's data will still be safely stored on our servers - nothing will ever be deleted'
- sources:
  - [1] https://twist.com/help/articles/360004758880
  - [2] https://twist.com/pricing
