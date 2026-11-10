# MediaFire Pro

> mediafire.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mediafire/ | JSON https://fshy.ajam.dev/api/v1/entity/mediafire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MediaFire

- `storage/mediafire` | fails-quota | evidence reported | binding per-object-cap | category consumer file host / drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mediafire.com/
- price $8.33/TB/mo (Pro, 1 TB) | parsed USD 8.33/TB-mo
- free tier: 10 GB free, up to 50 GB with bonuses. 4 GB per file free. Pro 1 TB, 30% off. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file | bytes: 4000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Direct-link egress is metered and ad-gated on free; Pro removes ads and gives 1 TB with standard transfer speeds. | metered: yes
- identity: email | detail: email
- interface: rest, webdav, rclone, webdav-proxy
- limits:
  - per-object-cap (binding): 4 GB per file [1]
  - per-object-cap (binding): 4 GB/file [1]
- limits note: per-object: 4 GB/file free. Bonus scheme caps at 50 GB.
- interface detail: rest
- tooling: No rclone backend (AList has a MediaFire driver). No WebDAV. REST API exists but is oriented at upload/share, not bulk sync.
- composes with: 10-50 GB units with no rclone backend means the shard count for 20 TB is 400+ accounts against an unaudited REST API. Economically absurd.
- reliability: 100M users, stable, but tuned for sharing rather than storage; free tier is ad-supported.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB free, up to 50 GB with bonuses. 4 GB per file free. Pro 1 TB, 30% off.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $8.33/TB/mo (Pro, 1 TB)
- evidence:
  - [1] 2026-10-21: '10GB for free. Up to 50GB free with bonuses'; '10GB Free/Up to 4GB per file'; '1 TB of storage' on Pro
  - [2] 2026-10-21: 'Pro 30% Off... 1 TB of long-term storage, standard transfer speeds, no ads... $8.33/month'
- sources:
  - [1] https://www.mediafire.com/
  - [2] https://www.mediafire.com/upgrade/

## MediaFire Pro 1 TB

- `storage/mediafire-pro-1-tb` | fails-quota | evidence documented | binding volume-quota | category File host with paid storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T01:24:31.179Z (live) | stale on 2026-12-05
- url https://www.mediafire.com/upgrade/
- price $5.83/TB-month on the 1 TB Pro plan billed annually ($8.33/month original price). Pro is the largest fixed plan listed; the Business plan has a space slider starting at 2TB whose price did not render in the page read: unverified. | parsed USD 5.83/TB-mo
- free tier: Pro 1 TB; Ultra 100 GB (tier naming is inverted on the page) | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB per file on Pro and Ultra; 5 GB per file on the free Basic plan | bytes: 50000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Pro includes '1 TB of ad-free standard transfers'; Ultra '50 GB of ad-free CDN fast transfers'; the free Basic plan has ad-supported standard transfers. The page does not say per which period the allowance runs or what happens past it: unverified. | metered: no
- identity: card | detail: card
- interface: rest, webdav
- limits:
  - volume-quota (binding): Pro: 1 TB of long-term storage and 1 TB of ad-free standard transfers [1]
  - per-object-cap: 50 GB per file [1]
- limits note: Constraint type: per-ip-shaping (speed tiering). 1 TB ceiling per plan.
- binding note: the Pro plan's 1 TB storage and 1 TB ad-free transfer allowance bound the total, well below the 10 TiB stored and 1 TiB a day served need
- interface detail: REST API (legacy), no WebDAV
- tooling: weak; API is dated
- composes with: poor
- reliability: Long-lived (100M users claimed) but no enterprise durability posture. Not suitable as a primary archive.
- notes: the same as the free tier
- evidence note: documented: the Pro 1 TB storage, 1 TB ad-free standard transfer allowance, 50 GB per-file limit and $5.83/month annual price were read on 2026-11-03 at https://www.mediafire.com/upgrade/. The card identity cost and the period of the transfer allowance are not stated on that page: unverified.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Pro 1 TB; Ultra 100 GB (tier naming is inverted on the page)
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $5.83/TB at 1 TB annual; cannot reach 5 TB or 20 TB on one plan — $29.15/TB/mo if you stacked five Pro plans, which the provider does not obviously permit
- evidence:
  - [1] 2026-10-21: 'Pro ... 1 TB of long-term storage, standard transfer speeds, no ads ... $8.33/month ... $5.83/month billed annually'
  - [1] 2026-11-03: the Pro plan is $5.83/month billed annually | capture: sha256:827fd36da8e16f0c2021116b013f71900b9c725be3574d3f4b9b803b6b8b7f93 | quote: $5.83/month billed annually
  - [1] 2026-11-03: the Pro plan has 1 TB of storage, 1 TB of ad-free standard transfers and 50 GB per file | capture: sha256:827fd36da8e16f0c2021116b013f71900b9c725be3574d3f4b9b803b6b8b7f93 | quote: 1 TB of long-term storage - 1 TB of ad-free standard transfers - 50 GB per file
  - [1] 2026-11-03: the Pro plan lists a 50 GB per-file limit, with no byte count | capture: sha256:035467608351730731472f4228619941fc1dc30bc3b5d7535bf09c17b74ff731 | quote: 50 GB per file
  - [1] 2026-11-03: the page's only unit statement, printed under the Business plan space slider, relates TB to GB by 1024; it gives no byte count for the 50 GB per-file limit | capture: sha256:035467608351730731472f4228619941fc1dc30bc3b5d7535bf09c17b74ff731 | quote: 1 TB = 1024 GB
  - [1] 2026-11-04: the Pro plan lists 1 TB of long-term storage | capture: sha256:827fd36da8e16f0c2021116b013f71900b9c725be3574d3f4b9b803b6b8b7f93 | quote: - 1 TB of long-term storage
- sources:
  - [1] https://www.mediafire.com/upgrade/
