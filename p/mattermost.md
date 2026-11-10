# mattermost cloud

> mattermost.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mattermost/ | JSON https://fshy.ajam.dev/api/v1/entity/mattermost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mattermost cloud free

- `storage/mattermost-cloud-free` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://forum.mattermost.com/t/cloud-free-deprecation/15802
- free tier: none reachable: The free cloud tier is deprecated - Mattermost now steers free users to self-hosted Entry. Self-hosted 'unlimited storage' just means you buy the disk, which is not free storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The free cloud tier is deprecated - Mattermost now steers free users to self-hosted Entry. Self-hosted 'unlimited storage' just means you buy the disk, which is not free storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The free cloud tier is deprecated - Mattermost now steers free users to self-hosted Entry. Self-hosted 'unlimited storage' just means you buy the disk, which is not free storage.
  - [2] 2026-10-21: cited as the basis of the rejection: The free cloud tier is deprecated - Mattermost now steers free users to self-hosted Entry. Self-hosted 'unlimited storage' just means you buy the disk, which is not free storage.
- sources:
  - [1] https://forum.mattermost.com/t/cloud-free-deprecation/15802
  - [2] https://docs.mattermost.com/product-overview/editions-and-offerings

## Mattermost Team Edition / Entry (self-hosted)

- `storage/mattermost-team-edition-entry` | self-hosted, last resort | verdict fails-egress | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.mattermost.com/product-overview/editions-and-offerings
- free tier: No storage quota at all in self-hosted Mattermost, free or paid. Only the per-file ceiling is configurable: default 100 MB (`MaxFileSize = 104857600` bytes), settable to anything. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-file ceiling is configurable: default 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Your server. Free of platform metering; you pay the host. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-file ceiling is configurable: default 100 MB [1]
- limits note: 100 MB per attachment default (configurable), 10 attachments per post, 16,383-char messages. Entry caps message history at 10,000 channel messages across all channels and 1,000 Board cards.
- interface detail: rest
- tooling: Mattermost REST API v4 `POST /api/v4/files` (multipart, up to 10 files per post) returning file IDs. Team Edition is MIT-licensed; Entry is the free mode of Enterprise Edition.
- composes with: N self-hosted deployments; 10,000 teams per deployment; users per team 'no enforced limit'. Storage is whatever disk you mount. Including an S3/MinIO backend via FileSettings.
- reliability: Zero platform risk. Nothing can delete your files. The failure mode is operational: attachments live on the app server's local disk unless you configure S3, and the docs warn that raising MaxFileSize risks server crashes on large uploads.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota at all in self-hosted Mattermost, free or paid. Only the per-file ceiling is configurable: default 100 MB (`MaxFileSize = 104857600` bytes), settable to anything.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Attachment file size | 100 MB | Configurable'; 'Attachments per message ... 10'; 'Teams per deployment 10,000'; 'Users per team No enforced limit'
  - [1] 2026-10-21: 'The maximum file size for message attachments and plugin uploads... The default is 104857600 bytes (100 mebibytes)'
  - [3] 2026-10-21: 'Team Edition is a free-to-use, open source, self-hosted collaboration platform... MIT'
- sources:
  - [1] https://docs.mattermost.com/configure/environment-configuration-settings.html
  - [2] https://docs.mattermost.com/administration-guide/manage/product-limits
  - [3] https://docs.mattermost.com/product-overview/editions-and-offerings
