# sharefile storage

> sharefile.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sharefile/ | JSON https://fshy.ajam.dev/api/v1/entity/sharefile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sharefile (progress)

- `storage/sharefile` | paid-only | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:40.824Z (live) | stale on 2026-12-05
- url https://www.sharefile.com/pricing
- price USD 16.50 per TB per month at the lower Advanced price (1TB of account storage per license, minimum of 3 users). | parsed USD 16.5/TB-mo
- free tier: none: paid plans only. Advanced is $16.50 or $18.15 per user per month depending on the billing cycle, minimum of 3 users. A Try Free button is offered; the trial length is not stated on the page. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota: 3TB of account storage on plans (1TB per license aggregated); 3TB storage packs can be added [1]
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: the trial length is not stated on the pricing page, which offers a Try Free button next to Buy Now.
- notes: Paid plans only. Advanced is $16.50 or $18.15 per user per month depending on the billing cycle, minimum of 3 users.
- evidence note: documented from the vendor pricing page captured on 2026-11-03 (https://www.sharefile.com/pricing): the Advanced price per user per month, the minimum of 3 users, the 3TB of account storage with 1TB per license, and the Buy Now and Try Free buttons; the trial length is not stated on that page and stays unverified
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 14-day trial only. Paid plans start at $16.50/user/month with a 3-user minimum and 1 TB of account storage per license — enterprise-sized, not free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 14-day trial only. Paid plans start at $16.50/user/month with a 3-user minimum and 1 TB of account storage per license — enterprise-sized, not free.
  - [1] 2026-11-03: Advanced is priced per user per month with a minimum of 3 users | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: $18.15 $16.50 $18.15 Per user/month Minimum of 3 users
  - [1] 2026-11-03: plans start with 3TB of account storage, 1TB per license aggregated, with 3TB storage packs available | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: Plans start with 3TB of account storage (1TB of account storage per license aggregated). You can also add storage capacity with 3TB storage packs!
  - [1] 2026-11-03: Advanced is priced at $16.50 or $18.15 per user per month with a minimum of 3 users | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: $18.15 $16.50 $18.15 Per user/month Minimum of 3 users
  - [1] 2026-11-03: Advanced is priced per user per month with a minimum of 3 users, with no free plan shown | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: $18.15 $16.50 $18.15 Per user/month Minimum of 3 users
  - [1] 2026-11-03: Advanced is $16.50 or $18.15 per user per month (the page has a Pay Monthly / Pay Annually toggle) with a minimum of 3 users | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: $18.15 $16.50 $18.15 Per user/month Minimum of 3 users
  - [1] 2026-11-03: a Try Free button sits next to Buy Now; no trial length is stated | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: [Buy Now](https://www.sharefile.com/buy/advanced-plan/plan-details) Try Free
  - [1] 2026-11-03: plans start with 3TB of account storage, 1TB per license, with 3TB storage packs | capture: sha256:4da7d940cd61f47fdd8c25d992132002f0acc340af9d386dd624e6e661fd7637 | quote: Plans start with 3TB of account storage (1TB of account storage per license aggregated). You can also add storage capacity with 3TB storage packs!
- sources:
  - [1] https://www.sharefile.com/pricing

## sharefile storage model

- `storage/sharefile-storage-model` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.sharefile.com/pricing
- free tier: none reachable: Storage is sold as 3 TB account blocks plus $ per TB packs; there is no free byte anywhere in the product. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Storage is sold as 3 TB account blocks plus $ per TB packs; there is no free byte anywhere in the product.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Storage is sold as 3 TB account blocks plus $ per TB packs; there is no free byte anywhere in the product.
- sources:
  - [1] https://www.sharefile.com/pricing
