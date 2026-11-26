# rclone imap

> github.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-repos/ | JSON https://fshy.ajam.dev/api/v1/entity/github-repos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iroh-dns-server (as a hosted third-party service)

- `storage/iroh-dns-server` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.854Z (live) | stale on 2026-12-04
- url https://api.github.com/repos/n0-computer/iroh-dns-server
- free tier: none reachable: The n0-computer/iroh-dns-server GitHub repo is archived (last push 2024-04-24) and carries no description. The functionality moved into the main iroh repo, and the maintained artefact is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The n0-computer/iroh-dns-server GitHub repo is archived (last push 2024-04-24) and carries no description. The functionality moved into the main iroh repo, and the maintained artefact is…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The n0-computer/iroh-dns-server GitHub repo is archived (last push 2024-04-24) and carries no description. The functionality moved into the main iroh repo, and the maintained artefact is…
  - [2] 2026-10-21: cited as the basis of the rejection: The n0-computer/iroh-dns-server GitHub repo is archived (last push 2024-04-24) and carries no description. The functionality moved into the main iroh repo, and the maintained artefact is the
  - [3] 2026-11-19: the iroh-dns-server repository was archived on 2024-04-26 and is read-only | capture: sha256:97f732254ff43e21380307ab5b6d378e7650f674003c7fbe3d9a94f567169438 | quote: This repository was archived by the owner on Apr 26, 2024. It is now read-only.
  - [3] 2026-11-19: the iroh-dns-server code moved into the main iroh repository | capture: sha256:97f732254ff43e21380307ab5b6d378e7650f674003c7fbe3d9a94f567169438
- sources:
  - [1] https://api.github.com/repos/n0-computer/iroh-dns-server
  - [2] https://crates.io/crates/iroh-dns-server
  - [3] https://github.com/n0-computer/iroh-dns-server

## rclone imap backend (the missing tooling)

- `storage/rclone-imap-backend` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:50.377Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-repos.md
- free tier: none reachable: The wrapper that would make this whole niche rclone-addressable does not exist yet. PR #9071 (2025-12-30) was closed unmerged; PR #9208 (2026-02-23) is still open, merged=false; issue… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not stated on the first-party rclone IMAP pull request | note: not applicable
- retention: not stated on the first-party rclone IMAP pull request
- egress: not stated on the first-party rclone IMAP pull request | metered: no
- identity: email
- interface: rclone
- interface detail: IMAP backend proposed for rclone; IMAP holds valid mail messages, not general-purpose files.
- tooling: not documented
- composes with: An IMAP backend copies mail to or from any other rclone storage backend, writing Maildir-named files on the non-IMAP side.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The wrapper that would make this whole niche rclone-addressable does not exist yet. PR #9071 (2025-12-30) was closed unmerged; PR #9208 (2026-02-23) is still open, merged=false; issue…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The wrapper that would make this whole niche rclone-addressable does not exist yet. PR #9071 (2025-12-30) was closed unmerged; PR #9208 (2026-02-23) is still open, merged=false; issue #8
  - [1] 2026-11-19: the IMAP backend PR 9208 is still open and unmerged, so the missing backend holds | capture: sha256:494d05019affe2cd9cd4830ea2dd268f3b482b4382888238d28beb55410e1357 | quote: "state": "open",
  - [2] 2026-11-19: the earlier IMAP backend PR 9071 is closed, matching the record's note that it was closed unmerged | capture: sha256:a0fc17bc6ebc22315d326987cdf1e09d0a1bc1c3677ec92d6f1251fcbc060d76 | quote: "state": "closed",
  - [3] 2026-11-19: the proposed IMAP backend composes with any rclone storage backend using Maildir naming | capture: sha256:dffe6f26f089769e600275a9ec7e5c95a4d9c3207fc21e6f84166ec833bdf0c7 | quote: You can copy from imap server to any type of storage, if it's not an imap server it will create files using the Maildir naming format.
  - [3] 2026-11-19: the maintainer states IMAP cannot store general-purpose files or directories | capture: sha256:dffe6f26f089769e600275a9ec7e5c95a4d9c3207fc21e6f84166ec833bdf0c7 | quote: I don't think IMAP can store general purpose files/directories so I don't think the backend should attempt to do that
  - [3] 2026-11-19: the pull request describes backend operations and states no retention period | capture: sha256:dffe6f26f089769e600275a9ec7e5c95a4d9c3207fc21e6f84166ec833bdf0c7 | quote: I tested ls/cat/mkdir/rmdir/copy/sync/delete.
  - [3] 2026-11-19: the pull request states full messages are read into memory, with no per-object size cap | capture: sha256:dffe6f26f089769e600275a9ec7e5c95a4d9c3207fc21e6f84166ec833bdf0c7 | quote: the way the imap library works I have to read the full message to memory
- sources:
  - [1] https://api.github.com/repos/rclone/rclone/pulls/9208
  - [2] https://api.github.com/repos/rclone/rclone/pulls/9071
  - [3] https://github.com/rclone/rclone/pull/9208
