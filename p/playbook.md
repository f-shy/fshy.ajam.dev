# Playbook

> playbook.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/playbook/ | JSON https://fshy.ajam.dev/api/v1/entity/playbook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Playbook — 100 GB free (300-asset cap)

- `storage/playbook-100-gb-free` | fails-quota | evidence reported | binding write-gated | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.playbook.com
- free tier: Free: '100GB included' OR 300 total assets, whichever comes first. API 1K calls/month. Paid Pro $10/mo/member = 2 TB + 1 TB per added member up to 10 TB. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: CDN links are a paid-tier feature ('CDN links' listed under Pro). Free tier egress not metered but also not CDN-served. | metered: yes
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - write-gated (binding): review), not bulk objects [1]
- limits note: 300 assets OR 100 GB, whichever first. This is an asset-count cap disguised as a storage cap, the same failure mode as TeraBox's 500-file cap. API 1K calls/month is request-rate bound.
- interface detail: rest
- tooling: Documented developer API (dev.playbook.com), 1,000 calls/month on free. No rclone backend.
- composes with: 100 GB per account, and a second account carries a second allowance, but the 300-asset cap binds first for bulk data. 300 objects at 100 GB means ~333 MB average object.
- reliability: Designed for creative asset management and video preview rather than bulk binary storage. Free tier includes 100 GB storage without documented egress transit terms.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: '100GB included' OR 300 total assets, whichever comes first. API 1K calls/month. Paid Pro $10/mo/member = 2 TB + 1 TB per added member up to 10 TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free: The Free plan includes 300 total assets or 100GB of storage, whichever comes first', 'API 1K calls / month', fetched 2026-10-21
- sources:
  - [1] https://www.playbook.com/pricing/
