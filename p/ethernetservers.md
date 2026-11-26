# EthernetServers

> ethernetservers.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ethernetservers/ | JSON https://fshy.ajam.dev/api/v1/entity/ethernetservers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EthernetServers

- `compute/ethernetservers` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.321Z (live) | stale on 2026-12-08
- url https://www.ethernetservers.com/vps-hosting
- price parsed USD 3/mo
- free tier: 1 GB KVM VPS from the vendor's own plan table: 1 CPU core, 1 GB RAM, 55 GB SSD, 3 TB outbound with inbound stated as unmetered, 10 Gbps port, 1 IPv4 plus a /64 IPv6. USD 3.00 per month; the page advertises term discounts of 15 percent for 1 year, 20 percent for 2 years and 25 percent for 3 years, and a coupon SAVETEN for 10 percent off the first billing cycle. Locations listed: Miami, Los Angeles and New Jersey (US), Frankfurt (DE), London (UK). The tracker lists the same plan at USD 3.00 with 3,072 GB a month on a 10 Gbps port. Re-read 2026-11-07: the plan table still shows the 1 GB plan at $3.00 USD monthly with the cycle tabs 'Monthly Save 0 %', '1-Year Save 15 %', '2-Years Save 20 %', '3-Years Save 25 %' and the coupon code SAVETEN for 10 percent off the first billing cycle. The cart configurator for pid 322 renders all six cycle prices server-side in descending term order: $3.00, $2.85, $2.70, $2.55, $2.40 and $2.25, plus an unlabelled $1.00; the page's discount line pins $2.55 on the 1-year term, $2.40 on 2 years and $2.25 on 3 years, which leaves $2.85 and $2.70 for the quarterly and semiannual terms by elimination. The add resolves with status 200 and no out-of-stock marker, so the plan is in stock. No page read prints a renewal price; the checkout step renders its totals client-side. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB outbound a month, inbound stated as unmetered; no overage rate is published on the page read | metered: yes | free allowance: 3 TB outbound a month | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): 3 TB outbound a month with inbound unmetered is the first wall a daytime crawler meets; 55 GB of SSD is the second, and no block-storage add-on is priced on this page [1]
- limits note: 3 TB outbound a month with inbound unmetered is the first wall a daytime crawler meets; 55 GB of SSD is the second, and no block-storage add-on is priced on this page
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full root, VirtFusion control panel with ISO mount and rDNS; SSH and the panel, no vendor API documented on the page read
- composes with: 55 GB of SSD and 3 TB a month on a 10 Gbps port at USD 3.00 is the cheapest per-gigabyte front end among evaluated providers; it is a good crawler edge or a build node that pushes bulk bytes to a storage host.
- reliability: no reliability event observed; the vendor advertises 5 Gbps of network-level DDoS protection included.
- notes: The 60-day money-back guarantee is a refund of money already paid, not a free tier, so free_tier_kind stays none and the verdict stays paid-only; the vendor's own phrasing calls it 'effectively' a free trial, which is why it is recorded here rather than dropped. verification criteria: a probe of the order form for setup fees, and the knowledge base for what the 3 TB counts.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 55
  - price_on_page: USD 3.00/month: the 1 GB KVM VPS
  - renewal_note: not published: no page read prints a renewal price; the checkout step renders its totals client-side
- evidence:
  - [1] 2026-10-22: the 1 GB plan card lists '55 GB SSD Space', '1 GB RAM', '1 CPU Core', 'Unmetered Inbound Bandwidth', '3 TB Outbound Bandwidth', '10 Gbps Port', '1 IPv4 Address', '/64 IPv6 Space' at '$3.00 USD' per month
  - [1] 2026-10-22: 'Deploy Your SSD Virtual Private Server Anywhere -- Miami, Los Angeles, New Jersey (US) | Frankfurt (DE) | London (UK)', quoted from the location line above the plan table
  - [1] 2026-10-22: FAQ answer: 'We provide a 60-day money-back guarantee with no questions asked, effectively giving you a comprehensive virtual server hosting free trial to evaluate our SSD VPS provider services'
  - probe:https://www.ethernetservers.com/cart.php?a=add&pid=322&billingcycle=monthly 2026-11-07: the cart configurator for pid 322 renders six cycle prices server-side: $3.00, $2.85, $2.70, $2.55, $2.40, $2.25, plus an unlabelled $1.00 | capture: sha256:e5f726eda0bfc92247c36dbfcad6b20a765053f417da6621d166f2205f7369cc | quote: "$3.00", "$2.85", "$2.70", "$2.55", "$2.40", "$2.25", "$1.00"
  - [1] 2026-11-07: the 1 GB plan card's price attribute holds six term prices in the cycle order the same template's data-plan-link array fixes (triennial, biennial, annual, semiannual, quarterly, monthly): $2.25, $2.40, $2.55, $2.70, $2.85, $3.00 - the page's discount line (15/20/25 percent for 1/2/3 years) agrees with $2.55, $2.40, $2.25 | capture: sha256:bbadd8d802ac7260aa91158e51d25bf0d1c66b31a489a6b8dae1a51e7d6c454c | quote: ["$2.25 <sub> USD</sub>","$2.40 <sub> USD</sub>","$2.55 <sub> USD</sub>","$2.70 <sub> USD</sub>","$2.85 <sub> USD</sub>","$3.00 <sub> USD</sub>"]
  - [1] 2026-11-07: the 1 GB plan card prices USD 3.00 a month | capture: sha256:bbadd8d802ac7260aa91158e51d25bf0d1c66b31a489a6b8dae1a51e7d6c454c | quote: ["$2.25 <sub> USD</sub>","$2.40 <sub> USD</sub>","$2.55 <sub> USD</sub>","$2.70 <sub> USD</sub>","$2.85 <sub> USD</sub>","$3.00 <sub> USD</sub>"]
- sources:
  - [1] https://www.ethernetservers.com/vps-hosting
