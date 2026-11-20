# myminifactory

> myminifactory.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/myminifactory/ | JSON https://fshy.ajam.dev/api/v1/entity/myminifactory.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## myminifactory

- `storage/myminifactory` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:13.422Z (live) | stale on 2026-12-04
- url https://creator.myminifactory.com/whats-the-max-file-size
- free tier: none reachable: 100 MB/file for a plain Designer, 500 MB with a Store subscription; the 5 GB 'Archive Mode' is staff-granted (write-gated) and capped at 25 archives = 125 GB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 100 MB/file for a plain Designer, 500 MB with a Store subscription; the 5 GB 'Archive Mode' is staff-granted (write-gated) and capped at 25 archives = 125 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 100 MB/file for a plain Designer, 500 MB with a Store subscription; the 5 GB 'Archive Mode' is staff-granted (write-gated) and capped at 25 archives = 125 GB.
  - [2] 2026-10-21: cited as the basis of the rejection: 100 MB/file for a plain Designer, 500 MB with a Store subscription; the 5 GB 'Archive Mode' is staff-granted (write-gated) and capped at 25 archives = 125 GB.
  - [1] 2026-11-19: plain Designer file cap is 100MB, confirming the fails-quota rejection | capture: sha256:60c7a3019948de0fbdac7edceca7c7640a0a9315ab08d3d3a4b2b300a5720e14 | quote: If you are a Designer without Store Subscription, you can upload 100MB for each file.
  - [2] 2026-11-19: Archive Mode gives at most 5GB per archive across 25 archives, and is staff-granted | capture: sha256:2c06381a8a50a1688e3d1eb75b87170f0975742604d471a5c51f8049d1bc42b6 | quote: Currently, we allow 5GB per archive (25 archives in total).
- sources:
  - [1] https://creator.myminifactory.com/whats-the-max-file-size
  - [2] https://creator.myminifactory.com/using-archive-mode-to-upload-files
