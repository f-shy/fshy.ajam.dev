# Filemail

> filemail.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filemail/ | JSON https://fshy.ajam.dev/api/v1/entity/filemail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filemail

- `storage/filemail` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.filemail.com
- free tier: 5 GB per transfer with no registration; 2 transfers per 24 hours; 7-day retention. Paid: Pro 250 GB/transfer, Business/Enterprise 'unlimited file size'. And only Business/Enterprise can pick 'Forever' retention. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: 5 GB per transfer with no registration; 2 transfers per 24 hours; 7-day retention | days: 1 | source: [1] | note: not stated
- egress: not metered on free; desktop apps recommended for speed. | metered: yes
- identity: institution
- interface: rest
- limits:
  - per-ip-shaping: Transfer, Business/Enterprise 'unlimited file size'. And only Business/Enterprise can pick 'Forever. [1]
  - retention-clamped: Retention: 7 days [1]
  - per-object-cap (binding): per-object-cap: 5 GB [1]
- limits note: per-object-cap: 5 GB free / 250 GB Pro / unlimited Business. Retention: 7 days free; 'Forever' requires Business or Enterprise. request-rate: API is 20 requests per 10 seconds plus a per-plan daily leaky-bucket quota (429 on exceed). pull-count: not capped on free.
- interface detail: rest
- tooling: Mature REST API 2.0 at api-public.filemail.com with x-api-key + x-api-version headers; real docs at docs.filemail.com. But 'only Personal, Pro, Business and Enterprise accounts have access to our API'. The free/no-account tier has NO API.
- composes with: 5 GB x 2 transfers/day x unlimited identities. But no programmatic path on the free tier, so every unit needs a human and an account. The one genuinely interesting hook is 'Store Files Forever', which is Business/Enterprise only and consumes the account's paid storage.
- reliability: Two independent caps stack on the free tier. 5 GB AND 2 transfers/24h. And the service is geo-restricted ('the free service is not available in certain regions'). The free tier is not a storage candidate at all.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 5 GB per transfer with no registration; 2 transfers per 24 hours; 7-day retention. Paid: Pro 250 GB/transfer, Business/Enterprise 'unlimited file size' — and only Business/Enterprise can pick 'Forever' retention.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '5 GB ... 2 transfers within a 24-hour period ... stored for a maximum 7 days'
  - [2] 2026-10-21: 'only Personal, Pro, Business and Enterprise accounts have access to our API'; '20 requests every 10 seconds'
  - [3] 2026-10-21: 'When you have a Filemail Business or Enterprise account you can keep your files available forever'
- sources:
  - [1] https://support.filemail.com/en/articles/4103694-free-file-sharing-service
  - [2] https://docs.filemail.com/filemail-api-2.0/getting-started
  - [3] https://support.filemail.com/en/articles/1668572-store-files-forever

## filemail 'store files forever'

- `storage/filemail-store-files-forever` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.filemail.com/en/articles/1668572-store-files-forever
- free tier: none reachable: The only genuine forever-retention product in this niche, but it is Business/Enterprise only and consumes paid account storage. Not reachable from the free tier. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: The only genuine forever-retention product in this niche, but it is Business/Enterprise only and consumes paid account storage. Not reachable from the free tier.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The only genuine forever-retention product in this niche, but it is Business/Enterprise only and consumes paid account storage. Not reachable from the free tier.
- sources:
  - [1] https://support.filemail.com/en/articles/1668572-store-files-forever

## Filemail Basic

- `storage/filemail-basic` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.filemail.com/plans/basic
- free tier: 5 GB of storage space and 5 GB max per transfer, on a free 1-user account. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: per-object-cap 5 GB; retention 7 days file availability; pull-count 10 downloads per transfer; 3 recipients per transfer; 5 GB total storage per account. | days: 7 | source: [1] | note: not stated
- egress: Free within the plan; download count is the real meter (10 downloads per transfer). | metered: no
- identity: anonymous
- interface: s3, webdav, sftp, rclone
- limits:
  - retention-clamped: retention 7 days [1]
  - per-object-cap (binding): per-object-cap 5 GB [1]
- limits note: per-object-cap 5 GB; retention 7 days file availability; pull-count 10 downloads per transfer; 3 recipients per transfer; 5 GB total storage per account.
- interface detail: web + desktop app; no S3/WebDAV/SFTP on the free tier
- tooling: Filemail desktop app; no rclone backend
- composes with: 5 GB storage x unlimited free 1-user accounts = trivially repeatable but each account is a 5 GB silo with 7-day file availability, so aggregate retention is worthless for archive. Would need 100+ accounts to reach 500 GB of expiring data.
- reliability: Files disappear after 7 days regardless of account; download cap of 10 makes it unusable for serving.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB of storage space and 5 GB max per transfer, on a free 1-user account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'We provide 5 GB of storage space and the ability to send and receive any file type, up to 5 GB in size', '7-Day File Availability', '10 Downloads Per Transfer', '3 Recipients Per Transfer'
- sources:
  - [1] https://www.filemail.com/plans/basic
