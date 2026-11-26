# Linkbox

> linkbox.to | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linkbox/ | JSON https://fshy.ajam.dev/api/v1/entity/linkbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linkbox / TeleBox

- `storage/linkbox-telebox` | qualifies-with-caveat | evidence inferred | binding per-ip-shaping | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:24.410Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.linkbox.to
- free tier: 5 GB on plain signup; 10 TB for free after upgrading the account | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Upload: 15-17Mb/s; Download: 700Kb/s | metered: no
- identity: email | detail: the account's email and password
- interface: rest, rclone
- limits:
  - per-ip-shaping (binding): 700 Kb/s [1]
- limits note: free downloads throttled to under 1 MB/s; the site is a JS SPA (www.linkbox.to now serves a 'TeleBox' bundle) so quotas are not readable without executing JS; rclone backend is Tier 5, i.e. least-tested
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: rclone backend 'linkbox' (Tier 5, since v1.65; since v1.74 needs API token and email/password because listing/downloading moved to account auth)
- composes with: If the edu/gov verification path still works, one verified identity yields 10 TB. That is 2000x the base tier, i.e. the largest single-account multiplier in this niche; otherwise 5 GB x unlimited accounts.
- reliability: origin times out repeatedly under a headless reader (504 deadline on /, /pricing, /admin/account), indicative of an unstable front end behind an automated-traffic filter; Tier 5 backend means frequent breakage
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: backend exists, Tier 5, changed auth model in v1.74
  - [1] 2026-10-21: 'Each registered user will receive 5Gb of free storage... I will guide you to upgrade your account to 10TB' via edu/gov email; measured upload 15-17 MB/s, download 700 KB/s
  - [3] 2026-10-21: origin returns a 'TeleBox' SPA shell only
  - [1] 2026-11-09: the walkthrough states 5 GB on signup and a free upgrade to 10TB | capture: sha256:4de66e37600598948afb3a255dafcf8f9dc8f871d10d5aad13e80e92a8ebdee4 | quote: Each registered user will receive 5Gb of free storage, but in this article I will guide you to upgrade your account to 10TB for free to store data.
  - [1] 2026-11-09: the walkthrough measured a 700 Kb/s download rate | capture: sha256:4de66e37600598948afb3a255dafcf8f9dc8f871d10d5aad13e80e92a8ebdee4 | quote: Download: 700Kb/s
  - [1] 2026-11-09: the walkthrough measured upload and download rates | capture: sha256:4de66e37600598948afb3a255dafcf8f9dc8f871d10d5aad13e80e92a8ebdee4 | quote: Upload: 15-17Mb/s Download: 700Kb/s
  - [2] 2026-11-09: the rclone backend page names the account email and password as credentials | capture: sha256:53962d6d7dfd625ec3bfe76c748f17bcfa90b41d1824a65cfa6bb6518fdb79b3 | quote: The email and password for your Linkbox account
- sources:
  - [1] https://en.anonyviet.com/instructions-for-getting-10tb-of-storage-on-linkbox-to/
  - [2] https://rclone.org/linkbox/
  - [3] https://www.linkbox.to/pricing
