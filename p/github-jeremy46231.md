# slack/discord-as-storage wrapper ecosystem

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jeremy46231/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jeremy46231.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## slack/discord-as-storage wrapper ecosystem (slackfs, slack-parrotbot, file-

- `storage/slack-discord-as-storage-wrapper-ecosystem-slackfs-slack` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:50.377Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-jeremy46231.md
- free tier: none reachable: These repos all solve the wrong problem: they archive, clean up or mount Slack - none of them removes the 5 GB cap or the 1-year deletion. slackfs is a FUSE view over channels (6 stars)… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not stated on https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack | note: not applicable
- retention: On the free subscription, you can choose to retain data for 90 days or one year; data older than one year is deleted on a rolling basis.
- egress: not stated on the first-party Slack free-workspace history page | metered: no
- identity: email
- interface: browser
- interface detail: Files are accessed through a Slack workspace, with a 90-day visible history window on the free plan.
- tooling: not documented
- composes with: Files shared via third-party apps stay in the originating service; deleting them from Slack does not touch the originals.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: These repos all solve the wrong problem: they archive, clean up or mount Slack - none of them removes the 5 GB cap or the 1-year deletion. slackfs is a FUSE view over channels (6 stars)…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: These repos all solve the wrong problem: they archive, clean up or mount Slack - none of them removes the 5 GB cap or the 1-year deletion. slackfs is a FUSE view over channels (6 stars)…
  - [1] 2026-11-19: slackfs is a FUSE view over Slack and adds no storage capacity | capture: sha256:10b090307586ed9aa7fd4f5ba2eef56a9ba56498415f57fd2d62802d2b84c668 | quote: This project provides a FUSE-based filesystem that exposes Slack channels and messages as directories and files, letting you interact with Slack using standard shell tools.
  - [2] 2026-11-19: Slack free workspaces expose the most recent 90 days of file history | capture: sha256:9d6b26f7413a7549051c462d265c29004932247bd0e9cc4bbde5db31a2c474fa | quote: you'll have full access to the past 90 days of message and file history
  - [3] 2026-11-19: Slack free workspaces delete files older than one year on a rolling basis | capture: sha256:6a552818b5491f2bfdc66c99cf3e48ef57f4532dc7448a563f07e0b8431a591c | quote: On the free subscription, you can choose to retain data for 90 days or one year. Data older than one year will be
  - [3] 2026-11-19: third-party shared files remain in the originating service, so a Slack wrapper does not hold those bytes | capture: sha256:6a552818b5491f2bfdc66c99cf3e48ef57f4532dc7448a563f07e0b8431a591c | quote: Files shared via third-party apps remain stored in the service they originate from. Deleting them from Slack won't impact the original files.
- sources:
  - [1] https://github.com/jeremy46231/slackfs
  - [2] https://slack.com/help/articles/29414264463635
  - [3] https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack
