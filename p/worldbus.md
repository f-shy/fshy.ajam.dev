# WorldBus

> worldbus.ge | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/worldbus/ | JSON https://fshy.ajam.dev/api/v1/entity/worldbus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WorldBus

- `compute/worldbus` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-12-08
- url https://worldbus.ge/vps/turkey/
- price parsed USD 8.49/mo
- free tier: Turkey VPS SSD (A) (portal product TR - SSD VPS 01) at USD 8.49 per month, struck from a higher list price on the marketing page: 1 vCore at 2 GHz, 2 GB RAM, 30 GB SSD RAID10, 1 Gbps port, 2TB monthly traffic, 1 IPv4 and 4 IPv6, KVM with SolusVM, in Istanbul. Order page read 2026-11-07: monthly USD 8.49, quarterly USD 25.47, semi-annually USD 50.94, annually USD 101.88; renewal price not published; plan in stock (the order page renders every cycle with no out-of-stock marker). The Georgia equivalent and the B plan keep the prices quoted in the record's evidence rows. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month of traffic on a 1 Gbps port, stated on every plan card; no overage price published on the page read | metered: yes | free allowance: 2 TB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month on every Turkey and Georgia plan read, unchanged as cores and RAM rise. The allowance does not scale with the plan, so a bigger box does not buy more traffic. [1]
- limits note: 2 TB a month on every Turkey and Georgia plan read, unchanged as cores and RAM rise. The allowance does not scale with the plan, so a bigger box does not buy more traffic.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: SolusVM control panel named on the plan card; no API or client documented on the page read
- composes with: USD 8.49 in Istanbul is the only Turkey entry among documented hosts, and a 2 TB allowance at 1 Gbps makes it a regional egress point for traffic that must appear to originate there
- reliability: no reliability event recorded
- notes: The marketing page displays the discount as a strike-through (a higher list price struck beside the current monthly price, read 2026-11-07) and the portal store prices TR - SSD VPS 01 'Starting from' the same monthly figure; no page prints a renewal price, so the struck figure is the pre-promotion list price, not a stated renewal. The tracker's SPECIAL row (a cheaper plan with a far larger quota) still appears on no vendor page read on either date.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - price_on_page: USD 8.49/month for Turkey VPS SSD (A) (TR - SSD VPS 01)
  - renewal_usd: not published: the portal order page prints the four billing cycles (monthly, quarterly, semi-annually, annually) and no renewal figure
- evidence:
  - [1] 2026-10-22: 'Turkey VPS SSD (A) / 1 vCPU - 2Ghz Guranteed / 2 GB Guranteed RAM / 30GB SSD RAID10 / 1Gbps Network Port / 2TB Monthly Traffic / 1x IPv4 and 4x IPv6 / Istanbul, Turkey' with '<del>$16.99</del> $8.49 MONTHLY'
  - [2] 2026-10-22: 'Georgia VPS SSD (A)' with the same 1 vCPU / 2 GB / 30 GB SSD / 1 Gbps / 2 TB shape priced '$18.99 MONTHLY', and (B) at $24.99
  - [3] 2026-10-22: tracker lists a different, cheaper row the vendor's VPS pages do not show: '$8.00 / month 2 Intel Cores (shared) 2,048 MB RAM 30 GB SSD 51,200 GB/month bandwidth 1 Gbps port speed IPv4 + IPv6 Istanbul Turkey' as plan SPECIAL_VPS
  - [4] 2026-11-07: the order page prints four billing cycles for TR - SSD VPS 01, the annual term at USD 101.88 | capture: sha256:5dfe808796aca366575b2740fa4db8c17356ee603fb98e81e596c47afb8a8750 | quote: Monthly $8.49 USD Quarterly $25.47 USD Semi-Annually $50.94 USD Annually $101.88 USD
  - [5] 2026-11-07: the WHMCS portal store prices TR - SSD VPS 01 from USD 8.49 monthly, matching the marketing page | capture: sha256:1462283daad44c1d75596316edf93d9b27a86a4a7dd540031e518b7c5cc6b053 | quote: TR - SSD VPS 01 Starting from $8.49 USD Monthly
  - [1] 2026-11-07: the marketing page still displays the pre-promotion price struck through | capture: sha256:a3874089bf46beff74f8199c1f7d107fb1c5d142a96815ab480c81f125181169 | quote: ~~$16.99~~
  - [1] 2026-11-07: the marketing page prices Turkey VPS SSD (A) at USD 8.49 monthly | capture: sha256:a3874089bf46beff74f8199c1f7d107fb1c5d142a96815ab480c81f125181169 | quote: $8.49MONTHLY
  - [5] 2026-11-07: the portal store states the monthly bandwidth included on the Turkey plans | capture: sha256:1462283daad44c1d75596316edf93d9b27a86a4a7dd540031e518b7c5cc6b053 | quote: 2TB Monthly Included
  - [5] 2026-11-07: the portal price agrees with the marketing price, and no renewal price exists on either | capture: sha256:1462283daad44c1d75596316edf93d9b27a86a4a7dd540031e518b7c5cc6b053 | quote: TR - SSD VPS 01 Starting from $8.49 USD Monthly
  - [4] 2026-11-07: the entry plan price is unchanged on the order page | capture: sha256:5dfe808796aca366575b2740fa4db8c17356ee603fb98e81e596c47afb8a8750 | quote: Monthly $8.49 USD
  - [5] 2026-11-07: the WHMCS portal store prices TR - SSD VPS 01 from USD 8.49 monthly | capture: sha256:1462283daad44c1d75596316edf93d9b27a86a4a7dd540031e518b7c5cc6b053 | quote: TR - SSD VPS 01 Starting from $8.49 USD Monthly
  - [4] 2026-11-07: the portal order page prints the four billing cycles and no renewal figure | capture: sha256:5dfe808796aca366575b2740fa4db8c17356ee603fb98e81e596c47afb8a8750 | quote: Monthly $8.49 USD Quarterly $25.47 USD Semi-Annually $50.94 USD Annually $101.88 USD
  - [5] 2026-11-07: the portal store prices TR - SSD VPS 01 from USD 8.49 monthly | capture: sha256:1462283daad44c1d75596316edf93d9b27a86a4a7dd540031e518b7c5cc6b053 | quote: TR - SSD VPS 01 Starting from $8.49 USD Monthly
- sources:
  - [1] https://worldbus.ge/vps/turkey/
  - [2] https://worldbus.ge/vps/georgia/
  - [3] https://vpspricetracker.com/provider/WorldBus/vps
  - [4] https://portal.worldbus.ge/store/ssd-vps-in-turkey/ssd-vps-01
  - [5] https://portal.worldbus.ge/store/ssd-vps-in-turkey?currency=1
