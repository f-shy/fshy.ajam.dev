# 'email as filesystem' projects

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-waweber/ | JSON https://fshy.ajam.dev/api/v1/entity/github-waweber.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 'email as filesystem' projects (imapfs, imapfs, gmailfs, gitmail)

- `storage/email-as-filesystem-projects` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.062Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-waweber.md
- free tier: none reachable: All real, all abandoned or trivial, none production-grade. waweber/imapfs (7 stars, last push 2024-03) documents the fatal economics itself: base64 means "a 33% overhead (only 75% of server | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the imapfs first-party page states no per-object size cap | note: not applicable
- retention: stated-absent: the imapfs first-party page states no retention period for stored files
- egress: stated-absent: the imapfs first-party page states no egress terms for stored files | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: imapfs is a FUSE filesystem over IMAP provided as software the user installs and runs; no hosted storage interface is stated
- tooling: not documented
- composes with: stated-absent: imapfs is self-installed software that stores files in an IMAP inbox and states no chaining into a hosted byte-storage service
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: All real, all abandoned or trivial, none production-grade. waweber/imapfs (7 stars, last push 2024-03) documents the fatal economics itself: base64 means "a 33% overhead (only 75% of server
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All real, all abandoned or trivial, none production-grade. waweber/imapfs (7 stars, last push 2024-03) documents the fatal economics itself: base64 means "a 33% overhead only 75% of server
  - [1] 2026-11-19: imapfs documents a base64 overhead of 33 percent on 2026-11-19 | capture: sha256:fbabe8817fb85abe520b4724c29fb4f0410a4692db0511e2169f3134eef62771 | quote: This results in a 33% overhead (only 75% of server storage space is available).
  - [1] 2026-11-19: imapfs is a FUSE filesystem backed by an IMAP mail server, not a hosted byte-store interface | capture: sha256:fbabe8817fb85abe520b4724c29fb4f0410a4692db0511e2169f3134eef62771 | quote: This program provides a FUSE filesystem that stores files as email messages on the
  - [1] 2026-11-19: the project turns an IMAP inbox into storage via software the user runs | capture: sha256:fbabe8817fb85abe520b4724c29fb4f0410a4692db0511e2169f3134eef62771 | quote: IMAPFS turns an inbox on your IMAP-enabled mail server into cloud storage.
  - [1] 2026-11-19: the page documents encoding overhead but states no per-object cap | capture: sha256:fbabe8817fb85abe520b4724c29fb4f0410a4692db0511e2169f3134eef62771 | quote: This results in a 33% overhead (only 75% of server storage space
  - [1] 2026-11-19: the project is a single-client self-run filesystem, not a hosted chaining endpoint | capture: sha256:fbabe8817fb85abe520b4724c29fb4f0410a4692db0511e2169f3134eef62771 | quote: This filesystem must only be mounted by one client at a time.
- sources:
  - [1] https://github.com/waweber/imapfs
