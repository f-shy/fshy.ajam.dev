# podomatic

> podomatic.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/podomatic/ | JSON https://fshy.ajam.dev/api/v1/entity/podomatic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## podomatic

- `storage/podomatic` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:35:00.811Z (live) | stale on 2026-12-04
- url https://www.podomatic.com/plans
- free tier: free Basic plan: 500MB of storage and 15GB of bandwidth per month; the $49.99 per month Broadcaster plan lists Unlimited storage and bandwidth | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Bandwidth is capped per month: 15GB on the free Basic plan, 200GB on Pro Plus ($9.99/month), 500GB on Pro Platinum ($24.99/month); the Broadcaster plan ($49.99/month) lists Unlimited bandwidth and Unlimited storage. No fair-use cap on it is stated on the plans page, the storage and bandwidth help article or the terms page. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free Basic plan: 500MB of storage and 15GB of bandwidth per month. Paid route: Broadcaster at $49.99 per month lists Unlimited storage and bandwidth; Pro Plus has 200GB and Pro Platinum 500GB of bandwidth per month.
- notes: the same as reliability
- evidence note: vendor pages captured 2026-11-03: https://www.podomatic.com/plans, https://www.podomatic.com/help-center/articles/what-is-storage-and-bandwidth; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 500 MB total storage and 15 GB/month bandwidth on the free Basic plan — smaller than Podbean and with no unlimited-drafts trick. 'Unlimited Storage and Bandwidth' is the $49.99/mo…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 500 MB total storage and 15 GB/month bandwidth on the free Basic plan — smaller than Podbean and with no unlimited-drafts trick. 'Unlimited Storage and Bandwidth' is the $49.99/mo…
  - [2] 2026-10-21: cited as the basis of the rejection: 500 MB total storage and 15 GB/month bandwidth on the free Basic plan — smaller than Podbean and with no unlimited-drafts trick. 'Unlimited Storage and Bandwidth' is the $49.99/mo Broadcaste
  - [1] 2026-11-03: the Broadcaster plan lists Unlimited storage and Unlimited bandwidth | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: - - Storage Unlimited - Bandwidth Unlimited
  - [1] 2026-11-03: free Basic plan includes 15GB of bandwidth per month | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: Bandwidth 15GB
  - [1] 2026-11-03: Broadcaster costs $49.99 per month | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: $49.99 per month $499.90 per year $149.90 per quarterly
  - [2] 2026-11-03: bandwidth is a fixed monthly amount per plan | capture: sha256:0f53bc85bdf2fc683dba3e96130ee1d562bee0c52ec31d21e821df77bd0932b9 | quote: Each account level has a fixed amount of Bandwidth each month.
  - [2] 2026-11-03: unlimited storage and bandwidth belongs to Broadcaster | capture: sha256:0f53bc85bdf2fc683dba3e96130ee1d562bee0c52ec31d21e821df77bd0932b9 | quote: To have Unlimited Storage and Bandwidth Every Month, be a [Broadcaster]
  - [1] 2026-11-03: the free Basic plan holds 500MB of storage | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: - - Storage 500MB
  - [1] 2026-11-03: the Basic plan is free with no expiry, so the offer is not paid-only | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: Free Forever
  - [1] 2026-11-03: the free Basic plan includes 15GB of bandwidth per month | capture: sha256:001ad621fcda4ec09c9a447fcb22ed0d62057a07a4000f91aaf4ad1208f2200b | quote: Bandwidth 15GB
- sources:
  - [1] https://www.podomatic.com/plans
  - [2] https://www.podomatic.com/help-center/articles/what-is-storage-and-bandwidth
