# gopher

> gemcities.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gemcities/ | JSON https://fshy.ajam.dev/api/v1/entity/gemcities.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gopher / gemini capsule hosting (gemcities, tilde.team, sdf)

- `storage/gopher-gemini-capsule-hosting` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:42.831Z (live) | stale on 2026-12-04
- url https://gemcities.com/
- free tier: none reachable: Quotas are in megabytes: gemcities gives 50 MB per capsule and exists only for gemtext; tilde.team enforces 1 GB soft / 3 GB hard per user; SDF sells extra disks in 20 GB increments for… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Quotas are in megabytes: gemcities gives 50 MB per capsule and exists only for gemtext; tilde.team enforces 1 GB soft / 3 GB hard per user; SDF sells extra disks in 20 GB increments for…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Quotas are in megabytes: gemcities gives 50 MB per capsule and exists only for gemtext; tilde.team enforces 1 GB soft / 3 GB hard per user; SDF sells extra disks in 20 GB increments for…
  - [2] 2026-10-21: cited as the basis of the rejection: Quotas are in megabytes: gemcities gives 50 MB per capsule and exists only for gemtext; tilde.team enforces 1 GB soft / 3 GB hard per user; SDF sells extra disks in 20 GB increments for $3/m
  - [3] 2026-10-21: cited as the basis of the rejection: Quotas are in megabytes: gemcities gives 50 MB per capsule and exists only for gemtext; tilde.team enforces 1 GB soft / 3 GB hard per user; SDF sells extra disks in 20 GB increments for $3/m
  - [1] 2026-11-19: the first-party Gemcities homepage still gives each capsule 50 MB, a megabyte-scale quota | capture: sha256:ea17a63626ef9b54ce10fb72f9a0613e4d8343e7704ed1b40cd7bb02351bb6c0 | quote: Every capsule gets 50 MB of storage, which is generous for gemtext files.
  - [2] 2026-11-19: tilde.team still documents per-user disk quotas of 1 GB soft and 3 GB hard | capture: sha256:edf7b7fa8ecd6f446ba91d97c024caf5247c03c96c4ab80f8221e1337ee1e7a0 | quote: the limits will be 1gb as a soft limit then 3gb as the hard limit.
  - [3] 2026-11-19: SDF's join page still prices extra disk in 20 GB increments at $3 per month | capture: sha256:816fd48f02286ccf1b4578b6657253549dc33f1a9e896498ef33b25d571f4a4f | quote: Additional disks available in 20GB increments for an additional $3/mo
- sources:
  - [1] https://gemcities.com/
  - [2] https://tilde.team/news/032_disk_quotas
  - [3] https://sdf.org/?join
