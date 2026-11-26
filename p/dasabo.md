# Dasabo

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dasabo/ | JSON https://fshy.ajam.dev/api/v1/entity/dasabo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dasabo

- `compute/dasabo` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.076Z (live) | stale on 2026-12-08
- url https://vpspricetracker.com/provider/Dasabo/vps
- free tier: SRP-1 at EUR 3.99/month: 1 GB RAM, 1 vCore, 20 GB storage, 5 TB bandwidth, printed by the vendor's own store group (Cloud VPS - Shared Regular Performance) with order links per billing cycle. This matches the tracker row's shape and price; the tracker row already in evidence remains the only source for the port speed, the location and custom ISO support. The next vendor tiers are SRP-2 EUR 9.99 (2 GB, 40 GB, 10 TB), SRP-3 EUR 19.99 (4 GB, 80 GB, 10 TB), SRP-4 EUR 39.99 (8 GB, 160 GB, 20 TB), SRP-5 EUR 79.99 (16 GB, 240 GB, 20 TB) and SRP-6 EUR 149.99 (32 GB, 480 GB, 20 TB). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB of bandwidth on SRP-1 per the vendor's store card; the tracker quotes a larger monthly figure on a 0.49 Gbps port, which the vendor page does not print | metered: yes | free allowance: 5 TB on SRP-1 (vendor store card) | source: [2]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 5 TB of bandwidth on SRP-1 per the vendor's store card; the tracker quotes a larger monthly figure on a 0.49 Gbps port, which the vendor page does not print [2]
- limits note: 5 TB of bandwidth on SRP-1 per the vendor's store card; the tracker quotes a larger monthly figure on a 0.49 Gbps port, which the vendor page does not print
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: order path is a WHMCS store at my.dasabo.com; the tracker records custom ISO support, which matters for installing a non-standard image
- composes with: 1 GB and 20 GB in Frankfurt for EUR 3.99 with 5 TB of transfer is a workable EU relay or crawler host; the 0.49 Gbps port halves the throughput this slice's other EUR 4 hosts give, so it is the second choice behind Bullethost for the same money
- reliability: no reliability event recorded
- notes: The vendor's store now prints the plan: SRP-1 at EUR 3.99/month with 1 GB RAM, 1 vCore, 20 GB storage and 5 TB bandwidth, matching the tracker row's shape and price, and the cart prices SRP-1 at EUR 3.99 with no out-of-stock phrase. The four tier names the store page showed on 2026-10-22 (Essential EUR 2.99 to Premium EUR 19.99) are the Web Hosting Shared tiers, not VPS tiers. The tracker remains the only source for the port speed (0.49 Gbps), the Frankfurt location and custom ISO support. dasabo.com's own /vps/ and /hosting/ pages print no VPS price table.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - monthly_eur: 3.99
  - annual_eur: not published: the VPS cards print a Monthly price only
  - renewal_eur: not published: no page read prints a renewal figure
  - billing_term: monthly
  - in_stock: yes
- evidence:
  - [1] 2026-10-22: card row quoted: 'Dasabo - EUR3.99 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '20 GB HDD', '5,120 GB/month bandwidth', '0.49 Gbps port speed', 'IPv4 + IPv6', 'Frankfurt Germany'
  - [3] 2026-10-22: 
  - [2] 2026-11-07: the vendor's own VPS group prints SRP-1 at EUR 3.99 a month | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's own store prints the plan shape and price | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's store card prints the transfer allowance for SRP-1 | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: 1GB RAM 1 VCORE 20GB STORAGE 5TB BANDWIDTH
  - [2] 2026-11-07: the vendor's store group page is where the transfer allowance is printed | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's store group page is where the plan and its transfer allowance are printed | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's store prints SRP-1 at EUR 3.99 a month | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's store card for SRP-1 prints a Monthly price only | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - [2] 2026-11-07: the vendor's store card for SRP-1 prints a Monthly price | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
  - probe:https://my.dasabo.com/store/vps-shared-regular-performance/srp-1?billingcycle=monthly 2026-11-07: the cart read resolves SRP-1 to the product configurator, prices it EUR 3.99 and carries no out-of-stock phrase | capture: sha256:692ba072a78a3e5c13ed35ad49cda52c664d5e695c0d918e617f5959cbf6db79 | quote: priced
  - [2] 2026-11-07: the store page exposes a direct order URL for SRP-1 with the monthly billing cycle | capture: sha256:2c305aee6d283109ebc6e2b2aa0a56685c35fad7eea75849d07b47beca921411 | quote: href="/store/vps-shared-regular-performance/srp-1?billingcycle=monthly"
  - probe:https://my.dasabo.com/store/vps-shared-regular-performance/srp-1?billingcycle=monthly 2026-11-07: the cart read prices SRP-1 at EUR 3.99 and carries no out-of-stock phrase | capture: sha256:692ba072a78a3e5c13ed35ad49cda52c664d5e695c0d918e617f5959cbf6db79 | quote: 3.99
  - [2] 2026-11-07: the vendor's own store prints the plan shape and monthly price | capture: sha256:df1253a35fed64b8b5d46dfeca15d4a2808e681e72808ad675a284eb4fced69a | quote: ### SRP-1 €3.99 EUR Monthly
- sources:
  - [1] https://vpspricetracker.com/provider/Dasabo/vps
  - [2] https://my.dasabo.com/store/vps-shared-regular-performance
  - [3] https://vpspricetracker.com/info/1876601/Dasabo/
