# AvenaCloud

> avenacloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/avenacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/avenacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AvenaCloud

- `compute/avenacloud` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:02.760Z (live) | stale on 2026-12-08
- url https://avenacloud.com/vps/
- price parsed USD 6.2/mo
- free tier: KVM VPS/VDS 10 at EUR 5.50 per month, or EUR 58.93 a year: 1 vCPU dedicated, 1 GB DDR4 dedicated RAM, 10 GB SSD, 100 Mbps port, Moldova. The page's plan ladder continues above it; the homepage separately advertises VPS 'starting at 11.50 EUR / year or monthly at 2.50 EUR', which is lower than any plan the VPS page itemises. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: marketed unlimited: 'unlimited bandwidth' on the plan page and no overage price; the tracker records 31,641 GB/month | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): the plan carries a 100 Mbps port and the page states 'unlimited bandwidth' with no monthly counter, so the port is the limit; at 100 Mbps a full month is about 32 TB, which is the same order as the 31,641 GB/month the tracker records for this plan. [1]
- limits note: the plan carries a 100 Mbps port and the page states 'unlimited bandwidth' with no monthly counter, so the port is the limit; at 100 Mbps a full month is about 32 TB, which is the same order as the 31,641 GB/month the tracker records for this plan.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor runs KVM with a looking glass at lg.avenacloud.com and documents no API on the pages read
- composes with: a 100 Mbps port with 10 GB of SSD is a mail relay, a DNS secondary or a monitoring node rather than a transfer or storage host; the annual rate of EUR 58.93 is the only term the page prices
- reliability: no reliability event recorded
- notes: The cart read fixes the entry price: no addable product carries the homepage's entry figures - the cart's store index prices the VPS/VDS category 'From €5.50', its itemised ladder starts at VDS 10 at €5.50 monthly / €58.93 annually, and its cheapest addable row is the promo product PROMO VDS 10 at €5.00 monthly (all four cycles priced €5.00). Open: whether the 100 Mbps port is upgradeable - no page read states an upgrade path; no renewal price is printed; no stock counter is printed on the plan rows.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - monthly_eur: 5.5
  - annual_eur: 58.93
  - renewal_eur: not published: neither the VPS page nor the cart prints a renewal price; read at https://secure.avenacloud.com/cart/vps-vds-hosting/?id=1
  - term: monthly, quarterly, semi-annually and annually: EUR 5.50 / 16.02 / 31.13 / 58.93 on VDS 10
  - in_stock: no stock counter is printed on the VPS page or the cart; the cart resolves the VPS/VDS group with all cycles priced, so the plan is orderable
  - cart_url: https://secure.avenacloud.com/cart/vps-vds-hosting/?id=1
  - price_on_page: EUR 5.50/month for KVM VPS/VDS 10
- evidence:
  - [1] 2026-10-22: plan quoted: 'KVM VPS/VDS 10', 'Dedicated-CPU', '5.50 EUR / month', 'Or annually at 58.93 EUR / year', '1 CPU vCore', '1 GB DDR4 Dedicated RAM', '10 GB SSD Storage', '100 Mbps', 'Moldova'
  - [1] 2026-10-22: page text: 'Each plan includes essential benefits such as SSD storage, unlimited bandwidth, and 24/7 support'; meta description claims 'starting at just 3.50 EUR/mo'
  - [2] 2026-10-22: homepage VPS/VDS block: 'Starting at: 11.50 EUR / year' and 'Or monthly at 2.50 EUR', with 'Unlimited Bandwidth' among the listed features
  - [3] 2026-10-22: tracker's cheapest row: 'AvenaCloud - 5.50 / month', 'cpu 1 Intel Cores (shared)', 'ram 1,024 MB RAM', 'disk 10 GB HDD', 'bandwidth 31,641 GB/month bandwidth', 'rj45 0.1 Gbps port speed', city Moldova
  - [4] 2026-11-07: the vendor's own cart lists the VDS 10 ladder with all four billing cycles | capture: sha256:9bcd25eb51a0fb102ca905b22bfbe7c04d9d4e9c384197c9fd7652b59df2951a | quote: KVM VPS/VDS 10 €5.50 EUR €16.02 EUR €31.13 EUR €58.93 EUR / Monthly Quarterly Semi-Annually Annually
  - [5] 2026-11-07: the cart's VDS 10 ladder prices the four cycles; the first is the monthly cycle per the cycle line beside it | capture: sha256:b1fc8fa70a7f68b90f3d7521f517e6cb1541cadba569b97009d98937118010ef | quote: €5.50 EUR €16.02 EUR €31.13 EUR €58.93 EUR
  - [5] 2026-11-07: the cart's VDS 10 ladder prices the annual cycle last | capture: sha256:b1fc8fa70a7f68b90f3d7521f517e6cb1541cadba569b97009d98937118010ef | quote: €5.50 EUR €16.02 EUR €31.13 EUR €58.93 EUR
  - [5] 2026-11-07: the cart prints the four cycle prices and no renewal figure | capture: sha256:b1fc8fa70a7f68b90f3d7521f517e6cb1541cadba569b97009d98937118010ef | quote: €5.50 EUR €16.02 EUR €31.13 EUR €58.93 EUR
  - [5] 2026-11-07: the cart's cycle line names the four cycles in the ladder's order | capture: sha256:b1fc8fa70a7f68b90f3d7521f517e6cb1541cadba569b97009d98937118010ef | quote: Monthly Quarterly Semi-Annually Annually
  - probe:https://secure.avenacloud.com/?cmd=module&module=27&cid=240 2026-11-07: the cart resolves and prices the VPS/VDS group | capture: sha256:cfc2199ae854b7910953608b9ddfacf913ab65ff4e74cc5df76f96082a12b8c6 | quote: "verdict": "priced"
  - probe:https://secure.avenacloud.com/?cmd=module&module=27&cid=240 2026-11-07: the VPS page's order link lands on the cart's VPS/VDS group page | capture: sha256:cfc2199ae854b7910953608b9ddfacf913ab65ff4e74cc5df76f96082a12b8c6 | quote: "final_url": "https://secure.avenacloud.com/cart/vps-vds-hosting/?id=1"
  - [1] 2026-11-07: the VPS page still prices KVM VPS/VDS 10 at 5.50 EUR monthly and 58.93 EUR a year | capture: sha256:d28169731a003674abfa375370f411dc085f5d6ad7e9679ef1ecefeb84485c04 | quote: 5.50 €/ month
  - [5] 2026-11-07: the vendor's own cart lists the VDS 10 ladder with all four billing cycles, the first the monthly one at €5.50 | capture: sha256:9bcd25eb51a0fb102ca905b22bfbe7c04d9d4e9c384197c9fd7652b59df2951a | quote: KVM VPS/VDS 10 €5.50 EUR €16.02 EUR €31.13 EUR €58.93 EUR / Monthly Quarterly Semi-Annually Annually
- sources:
  - [1] https://avenacloud.com/vps/
  - [2] https://avenacloud.com/
  - [3] https://vpspricetracker.com/provider/AvenaCloud/vps
  - [4] https://secure.avenacloud.com/cart/
  - [5] https://secure.avenacloud.com/cart/vps-vds-hosting/?id=1
