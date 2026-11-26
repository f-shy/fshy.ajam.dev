# ReliableSite

> reliablesite.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reliablesite/ | JSON https://fshy.ajam.dev/api/v1/entity/reliablesite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ReliableSite

- `compute/reliablesite` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.reliablesite.net/
- free tier: no price was readable among documented hosts. The vendor announces bare metal in New York, Miami, Los Angeles, Dallas, Amsterdam and Queretaro, with AMD Ryzen 9950X and AMD EPYC 4545P builds in the two new sites, unmetered bandwidth with no fair-use policy or tiers, no setup fees, no long-term contracts, Rapid Deploy provisioning, on-site technicians and BYOIP and ASN announcements. The offer post is an expansion announcement and states no plan, no RAM, no disk and no rate, and the vendor page returned 403 before any price block. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unmetered per the announcement, with no fair-use policy or tiers stated; no port speed and no overage term were readable | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): unverified, and named only so the field is not blank: the vendor states unmetered bandwidth with no fair-use policy or tiers, which would make the port the wall, but no port speed, no byte allowance and no overage term appear on either page read. Nothing about this provider's limits is established. [1]
- limits note: unverified, and named only so the field is not blank: the vendor states unmetered bandwidth with no fair-use policy or tiers, which would make the port the wall, but no port speed, no byte allowance and no overage term appear on either page read. Nothing about this provider's limits is established.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor page advertises a 'Metal+' tier with 10 Gbps, a second IPv4, ADMN and Blesta; no API or CLI is documented on the pages read
- composes with: the reason to keep this record is the location list rather than the price: it is one of the few providers in documented records offering bare metal in Latin America from a company trading since 2006, and unmetered bandwidth on a dedicated box is the shape the archive job wants. Without a rate it cannot be compared to anything.
- reliability: no reliability event recorded
- notes: This is the weakest record in this category and it is kept because a missing provider is the finding and a missing price is a gap in it, not a reason to drop it. No number is asserted: shape, RAM, disk, port and rate are all null or absent, and the binding field carries the word unverified. Unverified: the Amsterdam and Queretaro plan pages and their rates, which need a fetch path that does not return 403; the one attempt this category was allowed was spent, so the wall is recorded rather than retried.
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [2] 2026-10-22: third-party offer post, published 2026-09-10: 'Unmetered Bandwidth: Standard servers include unmetered bandwidth with no fair usage policies or complex tiers'; 'All dedicated servers come with no setup fees or long-term contracts'; 'AMD Ryzen 9950X and AMD EPYC 4545P series'; the two new locations are 'Amsterdam, Netherlands' and 'Queretaro, Mexico'. The post carries no plan, no RAM, no disk and no price
  - [1] 2026-10-22: the vendor page returned upstream_status 403; the snapshot returned with the refusal reads 'Bare Metal Servers Delivered Instantly', 'Dedicated Hosting Since 2006', 'Data centers in New York, Miami, Los Angeles, Dallas, Amsterdam, and Queretaro, Mexico' and no price block
- sources:
  - [1] https://www.reliablesite.net/
  - [2] https://lowendbox.com/blog/reliablesite-expands-internationally-to-europe-and-latin-america-as-the-company-approaches-20th-anniversary/
