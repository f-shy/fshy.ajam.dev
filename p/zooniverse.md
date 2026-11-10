# galaxy zoo

> zooniverse.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zooniverse/ | JSON https://fshy.ajam.dev/api/v1/entity/zooniverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## galaxy zoo / foldit / seti@home

- `storage/galaxy-zoo-foldit-seti-home` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://static.zooniverse.org/www.citizensciencealliance.org/downloads/zooniverse_guide.pdf
- free tier: none reachable: Pure volunteer-compute. Galaxy Zoo runs inside Zooniverse (so the same 10,000-subject / review gate applies) and Foldit distributes protein-puzzle clients; neither exposes any… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: Pure volunteer-compute. Galaxy Zoo runs inside Zooniverse (so the same 10,000-subject / review gate applies) and Foldit distributes protein-puzzle clients; neither exposes any…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Pure volunteer-compute. Galaxy Zoo runs inside Zooniverse (so the same 10,000-subject / review gate applies) and Foldit distributes protein-puzzle clients; neither exposes any…
  - [2] 2026-10-21: cited as the basis of the rejection: Pure volunteer-compute. Galaxy Zoo runs inside Zooniverse (so the same 10,000-subject / review gate applies) and Foldit distributes protein-puzzle clients; neither exposes any user-addressab
- sources:
  - [1] https://static.zooniverse.org/www.citizensciencealliance.org/downloads/zooniverse_guide.pdf
  - [2] https://help.zooniverse.org/getting-started/lab-policies/

## Zooniverse (Panoptes)

- `storage/zooniverse` | fails-quota | evidence reported | binding write-gated | category citizen-science classification platform
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zooniverse.org
- free tier: Stores contributor classifications, not contributor uploads. And the upload side is capped at 10,000 subjects per user. Zooniverse Help, Lab Policies, verbatim: 'there is a limit of 10,000 subject uploads per user. Please contact us if you'd like to upload more.'. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free read, but only per-subject image URLs. No bulk export endpoint without project-owner credentials. | metered: no
- identity: email | detail: Email for a volunteer account ('Only your name and email are captured'), but publishing a project is `write-gated`. Internal review + beta test + launch scheduling, typically weeks.
- interface: cli
- limits:
  - write-gated (binding): review and a one-week beta before launch [1]
- limits note: 10,000 subjects/user; every project passes a two-stage review and a one-week beta before launch; media must be licensed and rights-clear
- interface detail: Panoptes API (api.zooniverse.org); project builder; subject sets
- tooling: panoptes-client (Ruby/JS); subject uploader UI; no bulk CLI
- composes with: None. Each project's subjects live in a project-scoped S3 bucket; the data exports are CSV manifests, not a filesystem.
- reliability: Dead as a storage target. It is a volunteer-compute platform: the storage is incidental to the classification task and cannot be addressed as a bucket.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Stores contributor classifications, not contributor uploads — and the upload side is capped at 10,000 subjects per user. Zooniverse Help, Lab Policies, verbatim: 'there is a limit of 10,000 subject uploads per user. Please contact us if you'd like to upload more.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'there is a limit of 10,000 subject uploads per user'; two-stage review before launch
  - [2] 2026-10-21: 'Only your name and email are captured'
  - [3] 2026-10-21: external subjects count against 'the upload limit for that [project]' (host DNS now dead: 530/dns-failure)
  - [4] 2026-10-21: 'Your classifications are stored in the Zooniverse's secure online database'
- sources:
  - [1] https://help.zooniverse.org/getting-started/lab-policies/
  - [2] https://zooniverse.freshdesk.com/support/solutions/articles/44001770575
  - [3] https://developer.zooniverse.org/en/latest/science/subject_uploads.html
  - [4] https://www.zooniverse.org/about/faq
