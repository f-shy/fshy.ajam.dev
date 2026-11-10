# rsync.net

> rsync.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rsync/ | JSON https://fshy.ajam.dev/api/v1/entity/rsync.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rsync.net — Standard (ZFS, SSH-only filesystem)

- `storage/rsync-net-standard` | qualifies-with-caveat | evidence reported | binding none | category storage-only (bare UNIX filesystem on ZFS)
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.rsync.net/pricing.html
- price 0-9TB: $15.00/TB/mo. 10-99TB: $12.50/TB. 100TB+: $7.50/TB. restic accounts: $10.00/TB (200 GB min). openSUSE-developer Standard Single Region: $8.00/TB. openSUSE 500 GB tier is free-forever | parsed USD 7.5/TB-mo
- free tier: 800 GB minimum order; 0-9 TB, 10-99 TB, 100+ TB bands | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "No Egress Charges" / "NO Charges for ingress/egress". Unmetered both ways, no per-request fees. | metered: no
- identity: card | detail: card
- interface: sftp, scp, rsync, ssh, git, rclone
- limits note: 800 GB minimum; price falls in bands only at 10 TB and 100 TB
- interface detail: Any SSH tool: rsync, sftp, scp, borg, rclone, restic, git-annex; zfs send/recv on request
- tooling: The canonical rclone/restic/borg/rsync target. Every backend works because it is a real filesystem.
- composes with: SSHFS mount -> AList -> Cloudflare. No HTTP object API, so a wrapper is mandatory for serving
- reliability: Operating since 2001, 7 daily + 4 weekly snapshots on 10 TB+ accounts, physical media shipment. The expensive-but-unbreakable end of the market.
- notes: the same as the free tier
- extras:
  - price_verbatim: 0-9TB: $15.00/TB/mo. 10-99TB: $12.50/TB. 100TB+: $7.50/TB. restic accounts: $10.00/TB (200 GB min). openSUSE-developer Standard Single Region: $8.00/TB. openSUSE 500 GB tier is free-forever
- evidence:
  - [1] 2026-10-21: verbatim: 0-9 TB '1.5 Cents Per GB Per Month' (800 GB min), 10-99 TB '1.25 Cents Per GB', 100+ TB '0.75 Cents Per GB'; header states 'No Egress Charges'
  - [2] 2026-10-21: (search snippet) — restic accounts '$0.01 per GB, per month - 200 GB Minimum'
  - [3] 2026-10-21: 'Standard Single Region: $0.008 per GB per month' + 500 GB free-forever for openSUSE addresses
- sources:
  - [1] https://www.rsync.net/pricing.html
  - [2] https://rsync.net/products/restic.html
  - [3] https://news.opensuse.org/2024/11/12/rsync-net-becomes-gold-sponsor/

## rsync.net as the 20 tb solution

- `storage/rsync-net-as-the-20-tb-solution` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.rsync.net/pricing.html
- free tier: none reachable: Priced at $15/TB monthly with unmetered egress. Total cost for 20 TB is $300 per month compared to lower-cost providers. A free 500 GB allowance is available for openSUSE contributors. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Only worth it for the 500 GB free openSUSE
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Only worth it for the 500 GB free openSUSE
- sources:
  - [1] https://www.rsync.net/pricing.html
