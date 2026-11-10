# Calameo

> calameo.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/calameo/ | JSON https://fshy.ajam.dev/api/v1/entity/calameo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Calameo

- `storage/calameo` | fails-quota | evidence reported | binding none | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.calameo.com
- free tier: BASIC (free) account: 1 GB storage, 100 MB / 500 pages max per document, unlimited number of publications, 5 private publications. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Flipbook viewing is free and unmetered for readers, but there is no direct-download of the original on the free tier; the service reserves the right to requote at "2,500 publications or 1,000,000 reads per month" (its own industrial-scale threshold). | metered: no
- identity: email
- interface: webdav, sftp, rclone
- limits note: 1 GB total storage; 100 MB / 500 pages per document; 5 private publications; 1 administrator; 1 folder; 2,500-publication / 1M-read threshold triggers a commercial requote.
- interface detail: wrapper-only
- tooling: No public upload API on BASIC; conversion is browser-driven. No rclone/WebDAV/SFTP.
- composes with: 1 GB/account x unlimited accounts = technically repeatable but 1 GB units with a 100 MB/file cap make 10 TiB == 10,240 accounts. Not viable.
- reliability: Free tier storage is 1 GB. Document processing errors may occur on large PDF uploads.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: BASIC (free) account: 1 GB storage, 100 MB / 500 pages max per document, unlimited number of publications, 5 private publications.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The User of a BASIC Account enjoys the following advantages: - Storage: 1 GB - Maximum document size: 100MB and 500 pages - Private Publications: 5'
  - [1] 2026-10-21: 'For any intensive use that exceeds 2,500 publications or 1,000,000 reads per month, the Company reserves the right to propose a personalized quote'
- sources:
  - [1] https://www.calameo.com/en/terms
