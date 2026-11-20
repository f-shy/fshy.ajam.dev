# rclone

> github.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-rclone/ | JSON https://fshy.ajam.dev/api/v1/entity/github-rclone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rclone as a github client

- `storage/rclone-as-a-github-client` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.637Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-rclone.md
- free tier: None reachable: No GitHub/Gist/Releases backend exists. Verified by listing rclone's backend directory (alias, archive, azureblob, b2, .. s3, sftp, webdav, yandex, zoho; nothing for github). Any GitHub-ba. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party page states no a per-object cap; rclone is a client and a chunker backend splits large files | note: not applicable
- retention: stated-absent: the first-party page states no a retention period; rclone is a client and does not host bytes
- egress: stated-absent: the first-party page states no egress terms; rclone is a client and sets none of its own | metered: no
- identity: email
- interface: cli
- interface detail: Command-line program driven by subcommands such as copy, sync and mount over configured remotes
- tooling: not documented
- composes with: Wraps remotes with alias, chunker, crypt, compress and union; the documented backend list has no GitHub backend.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No GitHub/Gist/Releases backend exists — verified by listing rclone's backend directory (alias, archive, azureblob, b2, ... s3, sftp, webdav, yandex, zoho; nothing for github). Any…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: No GitHub/Gist/Releases backend exists — verified by listing rclone's backend directory (alias, archive, azureblob, b2, ... s3, sftp, webdav, yandex, zoho; nothing for github). Any…
  - [1] 2026-11-19: rclone's live backend directory lists no github, gist or releases backend, confirming the rejection | capture: sha256:b6217b28fec7f10e99431c1198022a8bc1f009b8e56ee0d06912133c58989481 | quote: | [gofile](https://github.com/rclone/rclone/tree/master/backend/gofile) | [gofile](https://github.com/rclone/rclone/tree/master/backend/gofile) | | | | [googlecloudstorage](https://github.com/rclone/rclone/tree/master/backend/googlecloudstorage) | [googlecloudstorage](https://github.com/rclone/rclone/tree/master/backend/googlecloudstorage) | | |
  - [2] 2026-11-19: the rclone first-party documentation describes a command-line interface | capture: sha256:6aef1b42f0d6bc764e287733162455d2c34afc6ce119bb2b4dfa1ecef5a1348f | quote: Rclone is a command line program to manage files on cloud storage.
  - [2] 2026-11-19: the rclone first-party documentation lists a chunker backend for chaining remotes | capture: sha256:6aef1b42f0d6bc764e287733162455d2c34afc6ce119bb2b4dfa1ecef5a1348f | quote: - [Chunker](https://rclone.org/chunker/) - transparently splits large files for other remotes
- sources:
  - [1] https://github.com/rclone/rclone/tree/master/backend
  - [2] https://rclone.org/docs/

## stock rclone telegram backend

- `storage/stock-rclone-telegram-backend` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.948Z (live) | stale on 2026-12-04
- url https://github.com/rclone/rclone/issues/6975
- free tier: none reachable: Does not exist. rclone's own tracker has the request closed unimplemented (issue #6975, 'Telegram Backend'; issue #5829 '[backend] add Telegram'). The only working rclone path is the… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Does not exist. rclone's own tracker has the request closed unimplemented (issue #6975, 'Telegram Backend'; issue #5829 '[backend] add Telegram'). The only working rclone path is the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Does not exist. rclone's own tracker has the request closed unimplemented (issue #6975, 'Telegram Backend'; issue #5829 '[backend] add Telegram'). The only working rclone path is the…
  - [2] 2026-10-21: cited as the basis of the rejection: Does not exist. rclone's own tracker has the request closed unimplemented (issue #6975, 'Telegram Backend'; issue #5829 '[backend] add Telegram'). The only working rclone path is the Teldriv
  - [3] 2026-11-19: the upstream feature request for a Telegram backend is still open and a maintainer states it is unlikely to be approved | capture: sha256:a5ab146d81d116a7604bbae9a779bb7c3eeaeecee968fe2f9da5dffcdcf3175a | quote: Telegram is not a storage service but a messaging platform. I don't think ncw will approve it.
  - [1] 2026-11-19: the duplicate request for a Telegram backend was closed as a duplicate of the still-open #5829 | capture: sha256:36e233677d7b89339c8960bbaeb67d7a0fcbfea213dce8f172a84617ca2125d0 | quote: Duplicate of
- sources:
  - [1] https://github.com/rclone/rclone/issues/6975
  - [2] https://tgdrive.github.io/teldrive/rclone/setup
  - [3] https://github.com/rclone/rclone/issues/5829
