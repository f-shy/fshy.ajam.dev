# myQNAPcloud Storage

> qnap.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qnap/ | JSON https://fshy.ajam.dev/api/v1/entity/qnap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## myQNAPcloud Storage

- `storage/myqnapcloud-storage` | fails-quota | evidence reported | binding none | category NAS vendor cloud backup
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.qnap.com/en-us/software/myqnapcloud-storage/pricing
- price $4.99/TB/mo with free egress (beta pricing for 1 TB) | parsed USD 4.99/TB-mo
- free tier: 16 GB free with any QNAP ID, no trial period, no file-size minimum. Paid starts $0.99/month; 1 TB was $4.99/month during beta. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No data transmission costs. 'Data transmission is completely free', stated repeatedly and used as the explicit differentiator against S3/Azure/GCP. | metered: no
- identity: email | detail: email
- interface: s3, rest, webdav, rclone
- limits note: Per-unit: 16 GB free; one plan per region per QNAP ID. Deliberately unshardable.
- interface detail: rest
- tooling: QNAP-only API and Hybrid Backup Sync / HybridMount. No rclone backend, no public S3 or WebDAV endpoint. Programmatic access is effectively gated behind QNAP firmware. One subscription plan per QNAP ID per region, which forecloses stacking on a single account.
- composes with: Proprietary cloud storage service requires QNAP NAS hardware for access without public REST API endpoints.
- reliability: Requires QNAP hardware or at least the QNAP account ecosystem for write access; the API is not a general object store.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 16 GB free with any QNAP ID, no trial period, no file-size minimum. Paid starts $0.99/month; 1 TB was $4.99/month during beta.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $4.99/TB/mo with free egress (beta pricing for 1 TB)
- evidence:
  - [1] 2026-10-21: 'myQNAPcloud Storage, a QNAP-hosted cloud storage starts at USD 0.99/month... Free / No Trial Period / 16 GB / USD 0'
  - [2] 2026-10-21: '16GB Free Storage: Everyone with a QNAP Account is entitled to 16GB free storage space as standard'
  - [3] 2026-10-21: '1TB/year is priced at $4.99/month during the beta period... does not charge for egress'
  - [4] 2026-10-21: 'QNAP ID can only have a single subscription plan in each region'
- sources:
  - [1] https://www.qnap.com/en-us/software/myqnapcloud-storage/pricing
  - [2] https://www.qnap.com/en/news/2025/qnap-officially-launches-myqnapcloud-storage-a-perfect-cloud-for-file-drives-and-backup-destinations
  - [3] https://www.qnap.com/en-us/how-to/faq/article/is-myqnapcloud-storage-more-affordable-than-aws-s3-microsoft-azure-and-google-cloud
  - [4] https://software.qnap.com/myqnapcloud-storage.html
