# Seedbox.io

> seedbox.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedbox-3/ | JSON https://fshy.ajam.dev/api/v1/entity/seedbox-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedbox.io

- `debrid/seedbox-io` | dead | evidence documented | binding none | category seedbox host (brand retired into Hosting by Design) | tier n/a
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:56:20.000Z (live) | stale on 2026-11-23
- url https://seedbox.io/
- free tier: None. The seedbox.io domain no longer serves a seedbox product: every request lands on hostingby.design, whose cheapest entry is 'App hosting €6.59 Starting price'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: seedbox.io and www.seedbox.io both resolve to hostingby.design with a wp-json Link header naming that host
- per-object cap: not applicable: no seedbox product is offered at this domain any more | source: [1]
- retention: not applicable: no storage product is sold under this name | source: [1]
- egress: The successor publishes its own allowances: application hosting at EUR 10.95 includes '4TB' capacity and '10TB' outgoing data; the EUR 6.59 entry does not state an allowance on the page read. | metered: no | free allowance: not applicable at seedbox.io | source: [1]
- identity: card | detail: the successor requires an account and a card for hosting; there is no free tier.
- interface: ssh
- limits note: no limits apply because no seedbox is sold here; the successor's app-hosting tiers state 4 TB capacity and 10 TB outgoing on the EUR 10.95 plan.
- binding note: A dead brand has no constraint to fail: nothing is sold at this domain, so the record carries no binding limit by design rather than by omission.
- interface detail: the successor sells 'Application hosting' with 'SSH Access Included'; no torrent panel is described.
- tooling: not applicable: the seedbox product and its panel are gone from this brand
- composes with: do not plan around this name. The successor's app-hosting product is a generic VPS-shaped service and would have to be evaluated as compute, not as a seedbox.
- reliability: a brand that was widely recommended as a cheap seedbox now redirects to a hosting consolidator ('Hostingby.design is a new consolidation of multiple brands under the HNielsen Technologies umbrella'), which is why any older guide naming seedbox.io is stale.
- notes: The record is kept so a later search for seedbox.io's plans finds the answer here. The distinction that matters for debrid: what survives is a rented app-hosting box, not a torrent-to-cloud service and not a seedbox panel.
- evidence note: the redirect was observed twice today (apex and www) with the successor's own page returned as final_url. A historical price for seedbox.io itself was not recoverable and is not recorded.
- extras:
  - successor: Hosting by Design (HNielsen Technologies)
  - observed_redirect: seedbox.io -> hostingby.design
- evidence:
  - [2] 2026-10-23: final_url is https://hostingby.design/ and the response Link header names hostingby.design/wp-json
  - [1] 2026-10-23: 'App hosting €6.59 Starting price', 'VPS Hosting €5.00', the EUR 10.95 application plan with 'Capacity 4TB' and 'Outgoing data 10TB', and the consolidation notice
- sources:
  - [1] https://hostingby.design/
  - [2] https://seedbox.io/
