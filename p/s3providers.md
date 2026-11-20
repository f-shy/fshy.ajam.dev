# contabo object storage as a *new* signup

> s3providers.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/s3providers/ | JSON https://fshy.ajam.dev/api/v1/entity/s3providers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## contabo object storage as a *new* signup

- `storage/contabo-object-storage-as-a-new-signup` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:09.482Z (live) | stale on 2026-12-04
- url https://s3providers.com/providers/contabo-object-storage
- free tier: None: a live first-party object-storage page documents paid S3-compatible storage with documented per-object, bucket and object-count limits and free unlimited data transfer; a third-party catalog lists a paid entry plan priced per 250 GB. No public free tier found. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: First-party object-storage page is live and documents paid S3-compatible storage with free unlimited transfer; the dedicated pricing URL no longer returns a page and a third-party catalog lists EUR 2.49 per 250 GB per month. No free tier is published.
- notes: Product appears delisted from public pricing. Contabo.com/en/object-storage/ now 301s to /storage-vps/ (a VM product) and contabo.com/en/pricing/ lists no Object Storage. Orderable only fro.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Product appears delisted from public pricing — contabo.com/en/object-storage/ now 301s to /storage-vps/ (a VM product) and contabo.com/en/pricing/ lists no Object Storage. Orderable only…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Product appears delisted from public pricing — contabo.com/en/object-storage/ now 301s to /storage-vps/ (a VM product) and contabo.com/en/pricing/ lists no Object Storage. Orderable only…
  - [2] 2026-10-21: cited as the basis of the rejection: Product appears delisted from public pricing — contabo.com/en/object-storage/ now 301s to /storage-vps/ (a VM product) and contabo.com/en/pricing/ lists no Object Storage. Orderable only fro
  - [3] 2026-11-19: the object storage service is live and priced on storage used with free unlimited transfer | capture: sha256:b9c21baa6040814736b259183d61519e8469b7edfe3fcba5028a11c5b8568cf4 | quote: Data transfer is free and unlimited. You only pay for the storage space you use - there are no hidden traffic or download fees.
  - [3] 2026-11-19: the product is live with documented paid-plan specs, not delisted | capture: sha256:b9c21baa6040814736b259183d61519e8469b7edfe3fcba5028a11c5b8568cf4 | quote: up to 100 buckets per customer, up to 3 million objects per customer (increasable on request), 250 API requests per second, and a default bandwidth of 10 MB/s.
  - [1] 2026-11-19: a third-party catalog lists a paid entry plan at EUR 2.49 per 250 GB per month with no free tier | capture: sha256:f5a3dd6fd0730e9ae0033e1be4793fc6f6e40d304cc7f8fb35548b1eb323f169 | quote: €2.49/month · 250 GB storage included
  - [1] 2026-11-19: the offer is a paid EUR 2.49 per 250 GB plan | capture: sha256:f5a3dd6fd0730e9ae0033e1be4793fc6f6e40d304cc7f8fb35548b1eb323f169 | quote: €2.49/month · 250 GB storage included
- sources:
  - [1] https://s3providers.com/providers/contabo-object-storage
  - [2] https://contabo.com/en/object-storage/pricing/
  - [3] https://contabo.com/en/object-storage/
