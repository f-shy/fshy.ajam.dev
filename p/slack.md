# Slack

> slack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/slack/ | JSON https://fshy.ajam.dev/api/v1/entity/slack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Slack (free plan)

- `storage/slack` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://slack.com
- free tier: 5 GB per free workspace (hard cap), 1 GB max per file, plus a 90-day visibility window and permanent deletion of anything over one year old | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB max per file | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; files served from files.slack.com -> files-origin.slack.com behind CloudFront | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per file [1]
- limits note: 5 GB workspace total; 1 GB per file; 10 apps max; content older than 90 days is hidden, content older than 1 year is permanently deleted (rolling, since 2024-08-26); high-volume upload throttling is explicitly mentioned in the free-plan limits
- interface detail: rest
- tooling: Slack Web API (files.getUploadURLExternal + files.completeUploadExternal), 1 GB per file; jeremy46231/slackfs (FUSE mount, 6 stars) exists but only mounts, does not add capacity
- composes with: 5 GB x N free workspaces, but the one-year deletion makes it useless as an archive and the 90-day hide makes it useless as storage. Only viable as a transient relay.
- reliability: Data loss on deletion is by design, not accidental: Slack states it 'will not be possible to restore messages and files once deletion occurs'. Also explicitly throttles 'use for storage and spam'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB per free workspace (hard cap), 1 GB max per file, plus a 90-day visibility window and permanent deletion of anything over one year old
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: error table: 'storage_limit_reached - File storage limit has been reached. This occurs when free teams have uploaded 5GB of files.'
  - [2] 2026-10-21: 'You can view and search messages and files from the last 90 days... Messages and files more than one year old will be permanently deleted'
  - [3] 2026-10-21: 'Members and guests can add files up to 1GB in size.'
  - [4] 2026-10-21: probe: POST -> HTTP 200 {"ok":false,"error":"not_authed"} (API live)
- sources:
  - [1] https://docs.slack.dev/reference/methods/files.getUploadURLExternal/
  - [2] https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces
  - [3] https://slack.com/help/articles/201330736-Add-files-to-Slack
  - [4] https://slack.com/api/files.getUploadURLExternal
