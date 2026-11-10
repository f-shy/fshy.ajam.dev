# rapidseedbox

> rapidseedbox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rapidseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/rapidseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rapidseedbox

- `storage/rapidseedbox` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T11:28:41.304Z (inherited) | stale on 2026-11-18
- url https://www.rapidseedbox.com/pricing
- free tier: No free tier. Cheapest plan: Basic (Lean range) at $5/month for 500 GB with unlimited traffic and a ratio limit of 3. The Premium range starts at Fast, $19/month for 1.2 TB. 14-day money-back guarantee. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Unlimited traffic on every plan; network bandwidth is subject to the plan's fair use policy. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Cheapest plan is Basic at $5/month for 500 GB ($10 per TB per month); Premium plans start at Fast, $19/month for 1.2 TB. Traffic is unlimited, subject to a fair use policy.
- notes: Cheapest plan $19/mo for 1.2 TB = ~$15.83/TB/mo, 5x the floor. Unlimited traffic but priced as a premium managed service.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cheapest plan $19/mo for 1.2 TB = ~$15.83/TB/mo, 5x the floor. Unlimited traffic but priced as a premium managed service.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cheapest plan $19/mo for 1.2 TB = ~$15.83/TB/mo, 5x the floor. Unlimited traffic but priced as a premium managed service.
  - [1] 2026-11-03: the page's stated starting price is $5/month (the Lean range's Basic plan, 500 GB) | capture: sha256:f647336e4c2c521ed2592575e6a70fe63c7df685b9881a8ad5691ae97f8f9dd4 | quote: Private and Secure Seedbox starting at $5/month. Up to 5TB storage and 10Gbps network.
  - [1] 2026-11-03: Premium plan storage: Fast 1.2 TB (the $19/month plan) | capture: sha256:6451c87f2a7e67eb25d0ce0aa575c87633c0729e1f7df5edf0a38967399c50cd | quote: | Storage | 5.6 TB | 2.8 TB | 2.2 TB | 1.2 TB |
  - [1] 2026-11-03: traffic is unlimited on each Premium plan | capture: sha256:6451c87f2a7e67eb25d0ce0aa575c87633c0729e1f7df5edf0a38967399c50cd | quote: | Traffic Amount of data you can send/receive. | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: network bandwidth is subject to a fair use policy | capture: sha256:6451c87f2a7e67eb25d0ce0aa575c87633c0729e1f7df5edf0a38967399c50cd | quote: | Network Bandwidth is subject to the appropriate usage of the plan, following our fair use policy. | 10 Gbps | 10 Gbps | 10 Gbps | 1 Gbps |
- sources:
  - [1] https://www.rapidseedbox.com/pricing
