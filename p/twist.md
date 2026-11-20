# Twist

> twist.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/twist/ | JSON https://fshy.ajam.dev/api/v1/entity/twist.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Twist (Doist) Free plan

- `storage/twist-free-plan` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.931Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the Free plan of Twist still has a 5GB file storage limit | capture: sha256:7da6b49f9ae9eb3a6da0f82d081288610df6cab087ccef783d38785a847b9a09 | quote: When using the Free plan of Twist, the storage limit is 5GB. If your team is using the [Twist Unlimited](https://twistapp.com/pricing) plan, you’ll have unlimited file storage.
  - [1] 2026-11-19: attachments are capped at 100MB and forwarded-email attachments at 10MB | capture: sha256:7da6b49f9ae9eb3a6da0f82d081288610df6cab087ccef783d38785a847b9a09 | quote: Yes. There is a 100MB file size limit for attachments and a 10MB file size attachment limit when [forwarding emails to Twist](https://twist.com/help/articles/forward-emails-to-twist-pPt1bBUs).
  - [4] 2026-11-19: the first-party pricing page announces Twist shuts down on March 1, 2027 | capture: sha256:29bf159a5bb67d6adf91b1698f4f52a85423221ba7216afd7599c1ac588de81f | quote: Todoist Comms is replacing Twist. Workspace admins can choose when to move their team before Twist shuts down on March 1, 2027. [Learn how to move your team](https://twist.com/help/articles/move-your-team-from-twist-to-todoist-comms-cAhB9a6GO "Move your team from Twist to Todoist Comms").
- sources:
  - [1] https://get.twist.help/hc/en-us/articles/360004758880-Add-files-to-Twist
  - [2] https://twist.com/help/articles/what-is-twist-unlimited-mehD6bnu
  - [3] https://twist.com/pricing
  - [4] https://twist.com/help/articles/360004758880

## Twist (free plan)

- `storage/twist` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.931Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the Free plan of Twist still has a 5GB storage limit | capture: sha256:29bf159a5bb67d6adf91b1698f4f52a85423221ba7216afd7599c1ac588de81f | quote: When using the Free plan of Twist, the storage limit is 5GB. If your team is using the [Twist Unlimited](https://twistapp.com/pricing) plan, you’ll have unlimited file storage.
  - [2] 2026-11-19: Twist states no Free-plan data is ever deleted | capture: sha256:0dfeee1094380da6a3ef1b15a1c2de5de21c0c36ddf7628dfdcdc813b99dcd90 | quote: all your team’s data will still be safely stored on our servers – nothing will ever be deleted
  - [1] 2026-11-19: the first-party pricing page announces Twist shuts down on March 1, 2027 | capture: sha256:29bf159a5bb67d6adf91b1698f4f52a85423221ba7216afd7599c1ac588de81f | quote: Todoist Comms is replacing Twist. Workspace admins can choose when to move their team before Twist shuts down on March 1, 2027. [Learn how to move your team](https://twist.com/help/articles/move-your-team-from-twist-to-todoist-comms-cAhB9a6GO "Move your team from Twist to Todoist Comms").
- sources:
  - [1] https://twist.com/help/articles/360004758880
  - [2] https://twist.com/pricing
