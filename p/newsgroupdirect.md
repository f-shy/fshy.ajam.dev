# NewsgroupDirect

> newsgroupdirect.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsgroupdirect/ | JSON https://fshy.ajam.dev/api/v1/entity/newsgroupdirect.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NewsgroupDirect

- `debrid/newsgroupdirect` | paid-only | evidence documented | binding none | category Usenet provider (United States, three backbones) - no free trial | tier Monthly Unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.newsgroupdirect.com/
- free tier: None on the page read. The home page is a plan and block table and carries no trial, no free allowance and no free account: "Monthly Unlimited $9", "Triple Play Monthly $13", "Unlimited Yearly $75", blocks 50 GB/$6 to 2000 GB/$75. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The claim is about this page, not about the company: a trial could exist behind a path not linked from the home page. No such path is linked.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "Up to 5,915+ Days Binary Retention" on every plan row. | days: 5915 | source: [1]
- egress: Unlimited usage on the subscription plans; blocks are prepaid by volume and "never expire and do not renew automatically". No overage price is published. | metered: no | free allowance: none | source: [1]
- identity: card | detail: Every route on the page is a checkout link into /member/billing; there is no free path to register. The instrument at checkout was not read.
- interface: unknown
- limits:
  - volume-quota: unlimited on subscriptions; blocks 50 GB to 2000 GB, non-expiring [1]
  - request-rate: 100 connections [1]
  - retention-clamped: 5,915+ days binary [1]
- binding note: The monthly unlimited plan has no byte counter and 100 connections; at 1 TiB/month nothing in the vocabulary fails. The entry cost is the constraint, and it is money rather than identity.
- interface detail: NNTP, 100 connections, SSL. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: Its value here is the bundled access: every plan advertises "Supernews Access, ViperNews Access, Usenet.Farm Access", so one $9 month reaches three backbones that each want their own account elsewhere.
- reliability: No suspension or throttle report was read. Block accounts are advertised as non-expiring and non-renewing.
- notes: Repeatability: not applicable. Abandonment: if a trial link appears on the home page, this record needs a trial tier.
- evidence note: Prices, retention and the absence of a trial are quoted from the vendor home page read. Nothing was purchased.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
- evidence:
  - [1] 2026-10-23: "Monthly Unlimited $9", "Triple Play Monthly $13", "Unlimited Yearly $75", block prices from 50 GB/$6 to 2000 GB/$75, "Up to 5,915+ Days Binary Retention", "Supernews Access, ViperNews Access, Usenet.Farm Access"
- sources:
  - [1] https://www.newsgroupdirect.com/
