# vpsFree.cz

> vpsfree.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsfree-2/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsfree-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vpsFree.cz

- `compute/vpsfree-cz` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:37.952Z (live) | stale on 2026-12-26
- url https://kb.vpsfree.org/information/membership_fees
- free tier: Not free. one VPS requires a membership fee of 300 CZK or 12 EUR | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: Member VPS parameters: 8 cores, 4 GB RAM, 120 GB SSD, 1× IPv4, IPv6 /64 or upon request, Prague 1 Gbps and Brno 300 Mbps connectivity, remote console and daily backups.
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
  - [1] 2026-11-25: one VPS requires a paid membership of 300 CZK or 12 EUR | capture: sha256:1a4aa7643fe713a13da820d732765519482c3ab63ccf027e40f0d2f865b63263 | quote: - one VPS requires a membership fee of 300 CZK or 12 EUR
  - [1] 2026-11-25: 300 CZK or 12 EUR is the minimum possible membership fee | capture: sha256:1a4aa7643fe713a13da820d732765519482c3ab63ccf027e40f0d2f865b63263 | quote: - 300 CZK or 12 EUR is the minimum possible membership fee
  - [2] 2026-11-25: the member VPS has 8 cores, 4 GB RAM, 120 GB SSD, one IPv4 and daily backups | capture: sha256:a3a5ae679aa77627b52dafa00da3ba7f0b4b0b90c6a3c4c92291bbe538a0ba20 | quote: | CPU: | 8 cores | | --- | --- | | RAM: | 4 GB | | SSD: | 120 GB | | IPv4: | 1× | | IPv6: | /64 or upon request | | Connectivity: | Prague 1 Gbps, Brno 300 Mbps | | Remote console | | | Daily backups | |
- sources:
  - [1] https://kb.vpsfree.org/information/membership_fees
  - [2] https://vpsfree.org/parameters/
  - [3] https://vpsfree.org/
