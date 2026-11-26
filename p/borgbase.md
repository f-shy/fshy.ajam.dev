# BorgBase

> borgbase.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/borgbase/ | JSON https://fshy.ajam.dev/api/v1/entity/borgbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BorgBase — Medium / Large

- `storage/borgbase-medium-large` | fails-quota | evidence reported | binding none | category storage-only (Borg/restic repository host)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:06.015Z (live) | stale on 2026-12-04
- url https://www.borgbase.com/
- price USD 110/year for 1 TB = USD 9.17/TB-month; USD 210/year for 2 TB = USD 8.75/TB-month; marginal beyond plan: USD 12/TB-month on Medium, USD 10/TB-month on Large | parsed USD 8.75/TB-mo
- free tier: 10 GB free forever; Small 250 GB, Medium 1 TB, Large 2 TB; flexible quota up to 3x plan. On the current pricing page: Medium USD 110/year with 12 USD/TB/month extra, Large USD 210/year with 10 USD/TB/month extra | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 10 GB free forever; Small 250 GB, Medium 1 TB, Large 2 TB; flexible quota up to 3x plan | Plan size + 3x flexible quota; append-only mode; no S3 | source: [1] | note: not stated
- egress: Verbatim from docs: "We don't charge upload, download or API calls." Unmetered, fair-use policed by a human. | metered: no
- identity: email | detail: email
- interface: rest, sftp, ssh, rclone
- limits note: Plan size + 3x flexible quota; append-only mode; no S3
- interface detail: SSH (borg/restic), web UI, REST API
- tooling: borg, borgmatic, restic, Vorta; rclone only via SFTP
- composes with: Append-only repository. A backup tier, not a mountable serving tier.
- reliability: EU or US region choice; 30-day refund on annual. Small operator. The 2 TB ceiling means 20 TB would need a custom plan.
- notes: part of the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB free forever; Small 250 GB, Medium 1 TB, Large 2 TB; flexible quota up to 3x plan
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: 2TB: $165/yr -> $6.88/TB/mo. 1TB: $90/yr -> $7.50/TB/mo. Marginal beyond plan: $6.00/TB/mo
- evidence:
  - [1] 2026-10-21: verbatim 'We don't charge upload, download or API calls', 3x flexible quota, custom plans by email
  - [2] 2026-10-21: homepage meta: 10 GB free, $2.50/mo floor; 'No API- or data transfer charges'
  - [3] 2026-10-21: + https://saaspartout.com/marketplace/borgbase/ — Medium 1TB $90/yr ($7.50/TB), Large 2TB $165/yr, additional usage $6/TB
  - [2] 2026-11-19: the first-party pricing page now lists Medium at USD 110/year for 1 TB with USD 12/TB/month extra | capture: sha256:ab79075e40db80e3bdbf7cf7f57968e6bb52f94964f0cdb8930d461d5609bc4a | quote: Medium$110/year Billed annually For power users with multiple workstations or a home server. 1 TB included Additional space $12/TB/month
  - [2] 2026-11-19: the first-party pricing page now lists Large at USD 210/year for 2 TB with USD 10/TB/month extra | capture: sha256:ab79075e40db80e3bdbf7cf7f57968e6bb52f94964f0cdb8930d461d5609bc4a | quote: Large$210/year Billed annually or $20/month Perfect for backing up larger servers or a company NAS. 2 TB included Additional space $10/TB/month
  - [2] 2026-11-19: the free tier and the no-transfer-charge terms on the current homepage are unchanged | capture: sha256:ab79075e40db80e3bdbf7cf7f57968e6bb52f94964f0cdb8930d461d5609bc4a | quote: 10 GB and 2 repos free forever. No API- or data transfer charges.
  - [1] 2026-11-19: the first-party pricing docs still state no charge for upload, download or API calls | capture: sha256:24f37422f330054cfe68ac3f52002eff24552f28f16ce3fb3afdbed4ecdf6fb6 | quote: We don’t charge upload, download or API calls.
- sources:
  - [1] https://docs.borgbase.com/pricing
  - [2] https://www.borgbase.com/
  - [3] https://freetier.co/directory/products/borgbase
