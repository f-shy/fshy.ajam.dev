# ThunderNews

> thundernews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thundernews/ | JSON https://fshy.ajam.dev/api/v1/entity/thundernews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ThunderNews

- `debrid/thundernews` | paid-only | evidence documented | binding none | category Usenet provider (United States) - no free trial | tier Unlimited Access
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.thundernews.com/
- free tier: None on the page read: "$6.00/month Unlimited Access" and "$3.50 / 25GB Block Account" are the two entries. No trial, free account or free allowance is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The page is a sales page with two price links; nothing else is offered.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "Up To 5,800+ Days Retention", "50 SSL Encrypted Connections". | days: 5800 | source: [1]
- egress: Unlimited bandwidth on the subscription; the block is 25 GB prepaid. No overage price is published. | metered: no | free allowance: none | source: [1]
- identity: card | detail: Both links go to members.thundernews.com billing pages; there is no free path. The instrument at checkout was not read.
- interface: unknown
- limits:
  - volume-quota: unlimited on subscription; 25 GB on the block [1]
  - request-rate: 50 SSL connections [1]
  - retention-clamped: 5,800+ days [1]
- binding note: The unlimited plan has no byte counter and 50 connections; at 1 TiB/month nothing in the vocabulary fails and the constraint is the $6 price.
- interface detail: NNTP over 256-bit SSL, 50 connections. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: A 25 GB block at $3.50 is the cheapest single purchase among debrid providers's usenet set, so it is the fallback when a free step has already been spent and one specific missing article blocks a job.
- reliability: Page metadata dates from 2020-05-28, with legible price options on an aging page.
- notes: Repeatability: not applicable. Abandonment: the page is old enough that a price change would not have shown up in its own markup; re-read before acting on the $6.
- evidence note: The two prices and the retention line are quoted from the vendor page as rendered on 2026-10-23. The page's own published date is 2020, so a stale price is possible and a checkout confirms the threshold.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
- evidence:
  - [1] 2026-10-23: "$6.00/month Unlimited Access", "$3.50 / 25GB Block Account", "Up To 5,800+ Days Retention 50 SSL Encrypted Connections", "$8.00/month Billed at $24 every 3 months" for Unlimited+VPN
- sources:
  - [1] https://www.thundernews.com/
