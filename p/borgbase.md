# BorgBase

> borgbase.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/borgbase/ | JSON https://fshy.ajam.dev/api/v1/entity/borgbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BorgBase — Medium / Large

- `storage/borgbase-medium-large` | fails-quota | evidence reported | binding none | category storage-only (Borg/restic repository host)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.borgbase.com/
- price 2TB: $165/yr -> $6.88/TB/mo. 1TB: $90/yr -> $7.50/TB/mo. Marginal beyond plan: $6.00/TB/mo | parsed USD 6/TB-mo
- free tier: 10 GB free forever; Small 250 GB, Medium 1 TB, Large 2 TB; flexible quota up to 3x plan | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
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
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB free forever; Small 250 GB, Medium 1 TB, Large 2 TB; flexible quota up to 3x plan
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: 2TB: $165/yr -> $6.88/TB/mo. 1TB: $90/yr -> $7.50/TB/mo. Marginal beyond plan: $6.00/TB/mo
- evidence:
  - [1] 2026-10-21: verbatim 'We don't charge upload, download or API calls', 3x flexible quota, custom plans by email
  - [2] 2026-10-21: homepage meta: 10 GB free, $2.50/mo floor; 'No API- or data transfer charges'
  - [3] 2026-10-21: + https://saaspartout.com/marketplace/borgbase/ — Medium 1TB $90/yr ($7.50/TB), Large 2TB $165/yr, additional usage $6/TB
- sources:
  - [1] https://docs.borgbase.com/pricing
  - [2] https://www.borgbase.com/
  - [3] https://freetier.co/directory/products/borgbase
