# rsync.net

> rsync.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rsync/ | JSON https://fshy.ajam.dev/api/v1/entity/rsync.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rsync.net — Standard (ZFS, SSH-only filesystem)

- `storage/rsync-net-standard` | qualifies-with-caveat | evidence reported | binding none | category storage-only (bare UNIX filesystem on ZFS)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T19:55:19.659Z (live) | stale on 2026-12-10
- url https://www.rsync.net/pricing.html
- price 0-9TB: $15.00/TB/mo. 10-99TB: $12.50/TB. 100TB+: $7.50/TB. restic accounts: $10.00/TB (200 GB min). openSUSE-developer Standard Single Region: $8.00/TB. openSUSE 500 GB tier is free-forever | parsed USD 7.5/TB-mo
- free tier: 800 GB Minimum Order | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: ZFS limits individual files to ~18000 Petabytes (16 exbibytes). | source: [1] | note: It is unlikely that you will encounter this limit.
- retention: All accounts have seven daily snapshots free of charge. | source: [1] | note: You do not need to set up or maintain these snapshots - they are automatically created and rotated.
- egress: No Egress Charges | metered: no
- identity: card | detail: card
- interface: sftp, scp, rsync, ssh, git, rclone
- limits note: 800 GB minimum; price falls in bands only at 10 TB and 100 TB
- interface detail: Any SSH tool: rsync, sftp, scp, borg, rclone, restic, git-annex; zfs send/recv on request
- tooling: The canonical rclone/restic/borg/rsync target. Every backend works because it is a real filesystem.
- composes with: SSHFS mount -> AList -> Cloudflare. No HTTP object API, so a wrapper is mandatory for serving
- reliability: Operating since 2001, 7 daily + 4 weekly snapshots on 10 TB+ accounts, physical media shipment. The expensive-but-unbreakable end of the market.
- notes: 800 GB minimum order; 0-9 TB, 10-99 TB, 100+ TB bands
- evidence note: the pricing page states an 800 GB minimum order
- extras:
  - price_verbatim: 0-9TB: $15.00/TB/mo. 10-99TB: $12.50/TB. 100TB+: $7.50/TB. restic accounts: $10.00/TB (200 GB min). openSUSE-developer Standard Single Region: $8.00/TB. openSUSE 500 GB tier is free-forever
- evidence:
  - [1] 2026-10-21: verbatim: 0-9 TB '1.5 Cents Per GB Per Month' (800 GB min), 10-99 TB '1.25 Cents Per GB', 100+ TB '0.75 Cents Per GB'; header states 'No Egress Charges'
  - [2] 2026-10-21: (search snippet) — restic accounts '$0.01 per GB, per month - 200 GB Minimum'
  - [3] 2026-10-21: 'Standard Single Region: $0.008 per GB per month' + 500 GB free-forever for openSUSE addresses
  - [1] 2026-11-09: the pricing page states an 800 GB minimum order | capture: sha256:ca5db9035b16a9efda238a1046754b2c1a48bfe620aef13e39b175c7ebdca1b5 | quote: 800 GB Minimum Order
  - [1] 2026-11-09: the pricing page header states no egress charges | capture: sha256:38100aff45a6fa53048f87a9a55cf19e6a3cb5a50958aa743f55ff6a4982af37 | quote: No Egress Charges
  - [4] 2026-11-25: the FAQ states the ZFS per-file limit | capture: sha256:e3af2c7d8d17c241b7d74ea401dc3edfcee4939bb0bfadf9977739f52d611995 | quote: ZFS limits individual files to ~18000 Petabytes (16 exbibytes).
  - [4] 2026-11-25: the FAQ qualifies the per-file limit as far above normal use | capture: sha256:e3af2c7d8d17c241b7d74ea401dc3edfcee4939bb0bfadf9977739f52d611995 | quote: It is unlikely that you will encounter this limit.
  - [5] 2026-11-25: all accounts receive seven daily snapshots | capture: sha256:69a539c8189bd85421fa35d24a7dfd64f2f4971fcaff6a11605ee29341c8b217 | quote: All accounts have seven daily snapshots free of charge.
  - [5] 2026-11-25: snapshot creation and rotation are automatic | capture: sha256:69a539c8189bd85421fa35d24a7dfd64f2f4971fcaff6a11605ee29341c8b217 | quote: You do not need to set up or maintain these snapshots - they are automatically created and rotated.
  - [1] 2026-11-25: the pricing page states there are no egress charges | capture: sha256:e00641865d2dc78fd26ef66ed8a3c00af25cb3f5e2dc418dd4f15434894bbf7e | quote: No Egress Charges
  - [1] 2026-11-25: the pricing page states an 800 GB minimum order | capture: sha256:ca5db9035b16a9efda238a1046754b2c1a48bfe620aef13e39b175c7ebdca1b5 | quote: 800 GB Minimum Order
- sources:
  - [1] https://www.rsync.net/pricing.html
  - [2] https://rsync.net/products/restic.html
  - [3] https://news.opensuse.org/2024/11/12/rsync-net-becomes-gold-sponsor/
  - [4] https://www.rsync.net/resources/faq.html
  - [5] https://rsync.net/resources/howto/snapshots.html

## rsync.net as the 20 tb solution

- `storage/rsync-net-as-the-20-tb-solution` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.047Z (live) | stale on 2026-12-04
- url https://www.rsync.net/pricing.html
- free tier: none reachable: Priced at $15/TB monthly with unmetered egress. Total cost for 20 TB is $300 per month compared to lower-cost providers. A free 500 GB allowance is available for openSUSE contributors. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the rsync.net pricing page states an 800 GB minimum order but no per-object size cap | source: [1] | note: not applicable
- retention: 7 daily snapshots on the 0-9 TB plan; 7 days + 4 weeks snapshots on the 10+ TB plans | source: [1]
- egress: stated-absent: the rsync.net pricing page states per-GB monthly storage prices but no egress charge or allowance | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the rsync.net pricing page states capacity tiers and per-GB prices but names no client interface
- tooling: not documented
- composes with: stated-absent: the rsync.net pricing page states no way to chain the offer with other storage services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Only worth it for the 500 GB free openSUSE
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Only worth it for the 500 GB free openSUSE
  - [1] 2026-11-19: the 0-9 TB tier is priced at 1.5 cents per GB per month | capture: sha256:ca5db9035b16a9efda238a1046754b2c1a48bfe620aef13e39b175c7ebdca1b5 | quote: 1.5 Cents Per GB Per Month
  - [1] 2026-11-19: the first-party pricing page lists storage tiers priced per GB per month | capture: sha256:ca5db9035b16a9efda238a1046754b2c1a48bfe620aef13e39b175c7ebdca1b5 | quote: ### 0 - 9 Terabytes
  - [1] 2026-11-19: the 0-9 TB plan includes 7 daily snapshots, a stated retention of snapshots | capture: sha256:ca5db9035b16a9efda238a1046754b2c1a48bfe620aef13e39b175c7ebdca1b5 | quote: - 7 daily snapshots [[info]](https://rsync.net/resources/howto/snapshots.html)
- sources:
  - [1] https://www.rsync.net/pricing.html
