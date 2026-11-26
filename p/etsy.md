# etsy

> etsy.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/etsy/ | JSON https://fshy.ajam.dev/api/v1/entity/etsy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## etsy (digital downloads)

- `storage/etsy` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:35.942Z (live) | stale on 2026-12-04
- url https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings
- free tier: None. A digital listing accepts at most five files of 20 MB each; this is a paid listing channel for selling digital downloads, not a storage allocation. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: 5 files per listing at 20 MB each = 100 MB per listing ceiling, plus a $0.20 listing fee per shard, so sharding costs more than the storage is worth. No programmatic way to attach files.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 files per listing at 20 MB each = 100 MB per listing ceiling, plus a $0.20 listing fee per shard, so sharding costs more than the storage is worth. No programmatic way to attach files.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 files per listing at 20 MB each = 100 MB per listing ceiling, plus a $0.20 listing fee per shard, so sharding costs more than the storage is worth. No programmatic way to attach files.
  - [1] 2026-11-19: a digital listing accepts at most five files of 20 MB each | capture: sha256:bb1b1b515a403c672be155eef228caf1e108295d0504f938c81a8552622e4129 | quote: When listing a digital item that is an instant download, you’ll need to upload the files that the buyer is purchasing when you create the listing. You can upload up to five digital files. The maximum size for each file is 20MB.
- sources:
  - [1] https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings
