# Ikoula

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ikoula/ | JSON https://fshy.ajam.dev/api/v1/entity/ikoula.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ikoula

- `compute/ikoula` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.serverhunter.com/offer/ikoula-micro-server/
- free tier: EUR 3.99/month for the Micro Server in Reims, France: 1x Raspberry Pi 4 ARM v8 at 4 cores and 1.5 GHz, 4 GB DDR4, 16 GB of storage, 1,000 Mbit uplink, traffic listed as 'Unlimited' with 'Unmetered Inbound, Unmetered Outbound', monthly billing, no setup fee, listed in stock. The product type on the row is 'Dedicated' and the virtualization type is 'None'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: traffic listed as 'Unlimited', unmetered in both directions, with a 1,000 Mbit uplink. The vendor VPS page states 'unlimited traffic and guaranteed 100 Mbps bandwidth' instead | metered: no | free allowance: unlimited, per the tracker row; no byte allowance is stated | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): The row sells no monthly byte allowance: traffic reads 'Unlimited' with both directions unmetered, so the only stated cap is the 1,000 Mbit port. The vendor's own VPS page disagrees, saying 'guaranteed 100 Mbps bandwidth', so the port figure is the one number in this record where two sources conflict and the tracker is the higher claim. [1]
- limits note: The row sells no monthly byte allowance: traffic reads 'Unlimited' with both directions unmetered, so the only stated cap is the 1,000 Mbit port. The vendor's own VPS page disagrees, saying 'guaranteed 100 Mbps bandwidth', so the port figure is the one number in this record where two sources conflict and the tracker is the higher claim.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the pages read: no API, control panel or image list appears in either extract
- composes with: An ARM v8 machine with 4 GB for EUR 3.99 a month is the cheapest always-on CPU among evaluated providers after the free tiers, and the architecture is the whole caveat: x86 binaries and most prebuilt CUDA tooling will not run on it, so it is a scheduler, a proxy, a queue consumer or an ARM-native build host rather than a general worker.
- reliability: no reliability event recorded
- notes: Found via serverhunter. Two Ikoula rows were read: the Micro Server at EUR 3.99 and the Agile S at EUR 20.99, and the second is flagged by the tracker itself as invisible and possibly outdated, so the lower row is the one recorded. verification criteria: the vendor's order page for the Micro Server, since the vendor page read carries no price at all.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 16
- evidence:
  - [1] 2026-10-22: row quoted: 'Monthly price EUR 3.99', 'Product type Dedicated', 'Virtualization type None', 'Stock In stock', 'Processor cores 4 cores', 'Processor speed 1.5 GHz', 'Processor 1x Raspberry Pi 4 ARM v8', 'Memory amount 4 GB', 'Memory type DDR4', 'Total HDD Capacity 16 GB', 'Uplink 1,000 Mbit', 'Traffic Unlimited', 'Unmetered Unmetered Inbound, Unmetered Outbound', 'Location Reims, France'
  - [2] 2026-10-22: the vendor page states 'Deploy a powerful and flexible Linux VPS with unlimited traffic and guaranteed 100 Mbps bandwidth. Hosted in France', and renders no plan table: the 880-word extract is marketing copy and tab labels, with no price string in it
  - [3] 2026-10-22: a second Ikoula row (Agile S) carries these cells: Monthly price EUR 20.99, 4 cores, 8 GB, Total HDD Capacity 1 TB, processor 1x Intel Xeon E3 1220v5 (the page prints registered-trade-mark signs on the two Xeon words); its page also prints 'This offer is invisible. It can only be reached by this direct link. The offer below might be outdated or no longer available.'
- sources:
  - [1] https://www.serverhunter.com/offer/ikoula-micro-server/
  - [2] https://www.ikoula.com/en/vps
  - [3] https://www.serverhunter.com/offer/ikoula-agile-s-10/
