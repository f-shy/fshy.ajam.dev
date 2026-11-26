# boinc projects as storage

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-boinc/ | JSON https://fshy.ajam.dev/api/v1/entity/github-boinc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boinc projects as storage

- `storage/boinc-projects-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.015Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the first-party wiki still describes a per-user server file sandbox for job inputs, not general user storage | capture: sha256:118a90c07dab12062f53784b0de241caace1ab6a9f5aee8af6eee564db3520f6 | quote: users can maintain a set of files on the project server; this is called the user's "file sandbox".
  - [3] 2026-11-19: the first-party wiki describes volunteer storage as using volunteer client hosts, not server storage given to users | capture: sha256:d34d020b10d24d2737cd62579c8e04104f9001deb550be66f00efad0e27673f0 | quote: volunteer hosts are used to store data that originates from the server
- sources:
  - [1] https://github.com/BOINC/boinc/wiki/User-file-sandbox
  - [2] https://github.com/BOINC/boinc/issues/6578
  - [3] https://github.com/BOINC/boinc/wiki/VolunteerStorage
