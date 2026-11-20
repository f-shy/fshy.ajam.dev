# cpan

> mail-archive.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mail-archive/ | JSON https://fshy.ajam.dev/api/v1/entity/mail-archive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cpan / pause

- `storage/cpan-pause-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:10.067Z (live) | stale on 2026-12-04
- url https://www.mail-archive.com/modules@perl.org/msg53837.html
- free tier: none reachable: No published quota, but the whole of CPAN was only 29.0 GB in 2021 and PAUSE has publicly run out of disk. A 2 MB distribution was rejected with 413 'Request Entity Too Large' in a public… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: No published quota, but the whole of CPAN was only 29.0 GB in 2021 and PAUSE has publicly run out of disk. A 2 MB distribution was rejected with 413 'Request Entity Too Large' in a public…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No published quota, but the whole of CPAN was only 29.0 GB in 2021 and PAUSE has publicly run out of disk. A 2 MB distribution was rejected with 413 'Request Entity Too Large' in a public…
  - [2] 2026-10-21: cited as the basis of the rejection: No published quota, but the whole of CPAN was only 29.0 GB in 2021 and PAUSE has publicly run out of disk. A 2 MB distribution was rejected with 413 'Request Entity Too Large' in a public ma
  - [3] 2026-10-21: cited as the basis of the rejection: No published quota, but the whole of CPAN was only 29.0 GB in 2021 and PAUSE has publicly run out of disk. A 2 MB distribution was rejected with 413 'Request Entity Too Large' in a public ma
  - [1] 2026-11-19: a roughly 2 Mb distribution upload failed with HTTP 413 Request Entity Too Large | capture: sha256:19fef6cf6903e32e3ab0d0eccc8a7f1c879d02401b6c30a07bc53646b47e8013 | quote: Upload failed (request failed with error code 413
  - [4] 2026-11-19: the same distribution uploaded successfully shortly after, so the 413 was transient | capture: sha256:be2ccaf26653b3f56c8dab15fa8b54d3ebf7df3d01746d9542fff2a5c5332c80 | quote: I'm now able to upload the distribution, so that issue seems to have been temporary in nature.
- sources:
  - [1] https://www.mail-archive.com/modules@perl.org/msg53837.html
  - [2] https://www.cpan.org/modules/04pause.html
  - [3] https://perlancar.wordpress.com/2021/05/16/disk-space-usage-of-cpan-authors-may-16-2021-edition/
  - [4] https://www.mail-archive.com/modules@perl.org/msg53838.html
