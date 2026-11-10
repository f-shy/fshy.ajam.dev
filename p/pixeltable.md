# Pixeltable Cloud

> pixeltable.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixeltable/ | JSON https://fshy.ajam.dev/api/v1/entity/pixeltable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pixeltable Cloud

- `storage/pixeltable-cloud` | fails-quota | evidence reported | binding none | category mlops-artifacts
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.pixeltable.com
- free tier: 50 GB Media Store per organization on the free tier, explicitly a HARD limit ('50 GB Media Store per organization (hard limit)'), plus 10 GB database storage per database. Pro raises Media Store to 250 GB then $0.05/GB-mo, database storage 10 GB then $0.80/GB-mo. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not separately metered; storage is the billed dimension. Serving via Deploy endpoints is capped by compute (up to 1 vCPU / 2 GB on free). | metered: yes
- identity: email | detail: email.
- interface: s3, rest, webdav
- limits note: 50 GB hard per org, 10 GB per database, 1 vCPU / 2 GB per database/service on free. The word 'hard limit' means there is no overage path at all. Uploads fail rather than bill.
- interface detail: rest
- tooling: Python-native: `pxt.create_dir`, `pxt.create_table`, insert of images/video/audio/documents; the SDK is the client. Open-source core, so self-hosting is possible. No S3/WebDAV surface on the cloud tier.
- composes with: Per ORGANIZATION, so org multiplication is the only route, and the docs frame 50 GB as a hard cap designed to stop exactly that. 10 TiB would need 205 orgs.
- reliability: Small vendor; the product is really a declarative multimodal database rather than a blob store, so using it as bulk storage fights its data model (it wants typed columns, not opaque blobs).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB Media Store per organization on the free tier, explicitly a HARD limit ('50 GB Media Store per organization (hard limit)'), plus 10 GB database storage per database. Pro raises Media Store to 250 GB then $0.05/GB-mo, database storage 10 GB then $0.80/GB-mo.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: '50 GB Media Store per organization (hard limit)'; '10 GB database storage per database'; Pro '250 GB Media Store per organization, then $0.05 / GB-mo'
- sources:
  - [1] https://www.pixeltable.com/pricing
