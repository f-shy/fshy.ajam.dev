# boinc projects as storage

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-boinc/ | JSON https://fshy.ajam.dev/api/v1/entity/github-boinc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boinc projects as storage

- `storage/boinc-projects-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/BOINC/boinc/wiki/User-file-sandbox
- free tier: none reachable: BOINC allocates client disk to projects, not server storage to users. The user-facing server facility is a 'file sandbox' for job inputs, and job submitters have explicit server disk… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: BOINC allocates client disk to projects, not server storage to users. The user-facing server facility is a 'file sandbox' for job inputs, and job submitters have explicit server disk…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: BOINC allocates client disk to projects, not server storage to users. The user-facing server facility is a 'file sandbox' for job inputs, and job submitters have explicit server disk quota
  - [2] 2026-10-21: cited as the basis of the rejection: BOINC allocates client disk to projects, not server storage to users. The user-facing server facility is a 'file sandbox' for job inputs, and job submitters have explicit server disk quota
  - [3] 2026-10-21: cited as the basis of the rejection: BOINC allocates client disk to projects, not server storage to users. The user-facing server facility is a 'file sandbox' for job inputs, and job submitters have explicit server disk quota
- sources:
  - [1] https://github.com/BOINC/boinc/wiki/User-file-sandbox
  - [2] https://github.com/BOINC/boinc/issues/6578
  - [3] https://github.com/BOINC/boinc/wiki/VolunteerStorage
