# vpsFree.cz

> vpsfree.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsfree-2/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsfree-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vpsFree.cz

- `compute/vpsfree-cz` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://kb.vpsfree.org/information/membership_fees
- free tier: Not free. Quoted: "one VPS requires a membership fee of 300 CZK or 12 EUR", which buys 8 cores, 4 GB RAM, 120 GB SSD, one IPv4, an IPv6 /64, daily backups and 250 GB of network storage. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits note: The name is about software freedom, not price: the minimum membership fee is EUR 12 a month, and non-payment suspends the account within three weeks.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: EUR 12 a month for 8 cores and 4 GiB with a public IPv4 and daily backups is the strongest price per core found in among documented hosts, and it composes with nothing free because it is a paid floor.
- reliability: no reliability event recorded
- notes: vpsFree.cz is a member-supported non-profit association providing VPS hosting. Membership requires individual verification and monthly dues, offering trial access for new participants.
- extras:
  - facets.class: refutation-not-free
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 4
- evidence:
  - [1] 2026-10-22: "one VPS requires a membership fee of 300 CZK or 12 EUR" and 12 EUR is stated as the minimum possible fee, quoted
  - [2] 2026-10-22: member VPS parameters are 8 cores, 4 GB RAM, 120 GB SSD, 1 IPv4 and an IPv6 /64, with Prague at 1 Gbps
  - [3] 2026-10-22: the organisation describes itself as a non-profit association of members rather than a commercial provider, which is why the word free in the name is not a price
- sources:
  - [1] https://kb.vpsfree.org/information/membership_fees
  - [2] https://vpsfree.org/parameters/
  - [3] https://vpsfree.org/
