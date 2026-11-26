# Rapidgator

> rapidgator.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rapidgator/ | JSON https://fshy.ajam.dev/api/v1/entity/rapidgator.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rapidgator

- `storage/rapidgator` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.037Z (live) | stale on 2026-12-04
- url https://rapidgator.net
- free tier: Free: 5 GB upload per file, no storage allowance published; files kept 30 days from last download. Premium sells storage explicitly as a metered block: 6 TB / 12 TB / 24 TB with matching bandwidth. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: max file overall ('the maximum file size is up to 80GB | bytes: 80000000000 | source: [1] | note: not stated
- retention: Free: 5 GB upload per file, no storage allowance published; files kept 30 days from last download | days: 30 | source: [1] | note: not stated
- egress: Free downloads are one-stream-at-a-time with no download accelerator and waiting; premium is metered against the purchased bandwidth block. No free egress path. | metered: no
- identity: anonymous
- interface: rest, ftp, rclone
- limits:
  - retention-clamped: Retention 30 days [1]
  - per-object-cap (binding): max file overall ('the maximum file size is up to 80GB [1]
- limits note: 80 GB max file overall ('the maximum file size is up to 80GB'), but free users are told 'you can upload files up to 5 GB and download files up to 5 GB'. Retention 30 days from last download (60 days on unlimited-storage premium). Free = one simultaneous download, IP-counted.
- interface detail: rest
- tooling: FTP upload, JDownloader/pyLoad and rclone-adjacent download managers; no first-party REST API documented for uploads.
- composes with: No free storage allowance to chain. Storage is a purchased block, so the multiplier is billing, not accounts.
- reliability: Documentation states 5 GB maximum file size on free tiers versus 80 GB on paid premium tiers. Free accounts are limited to single simultaneous downloads and throttled speeds.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free: 5 GB upload per file, no storage allowance published; files kept 30 days from last download. Premium sells storage explicitly as a metered block: 6 TB / 12 TB / 24 TB with matching bandwidth.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'As free user, you can upload files up to 5 GB and download files up to 5 GB!'
  - [1] 2026-10-21: 'the maximum file size is up to 80GB'; '30 days since its last download for regular accounts'
  - [3] 2026-10-21: '6 TB / 12 TB / 24 TB' storage blocks priced at 49.99 USD per 180 days
  - [1] 2026-11-19: Rapidgator's first-party FAQ still states an 80 GB maximum file size | capture: sha256:6bf9d261c883c32d72a7139b12be48e311f1495a41ac3d414e6cc59df03303cd | quote: You can upload any files (EXE, MP3, MPEG, AVI, RAR, ZIP, JPG, etc.), the maximum file size is up to 80GB!
  - [1] 2026-11-19: regular accounts keep files 30 days from the last download | capture: sha256:6bf9d261c883c32d72a7139b12be48e311f1495a41ac3d414e6cc59df03303cd | quote: 30 days since its last download for regular accounts and unlimited for the owners of premium accounts with limited storage space.
  - [2] 2026-11-19: Rapidgator free users can upload and download files up to 5 GB | capture: sha256:ad9fdd73701c7221302d12b877ee2c9c442c56001544ee0c3f9e886feed8b38e | quote: As free user, you can upload files up to 5 GB and download files up to 5 GB!
- sources:
  - [1] https://rapidgator.net/article/faq/id/3
  - [2] https://rapidgator.net/article/faq/id/1
  - [3] https://rapidgator.net/article/premium
