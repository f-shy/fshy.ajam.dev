# Terabix

> terabix.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/terabix/ | JSON https://fshy.ajam.dev/api/v1/entity/terabix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Terabix

- `compute/terabix` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T11:15:41.617Z (live) | stale on 2026-12-08
- url https://terabix.net/cloud-vm
- price parsed USD 6/mo
- free tier: CVM-4GB-M at USD 6/month: 2 vCPU (AMD EPYC Milan), 4 GB DDR4, 30 GB NVMe Gen4, 1 TB premium bandwidth, in Johor Bahru, Malaysia (Equinix JH1). The cart for CVM-4GB-Milan priced monthly USD 6.00, quarterly USD 18.00, semi-annually USD 36.00 and annually USD 72.00 with USD 0.00 setup on 2026-11-07, prints no renewal price and shows no out-of-stock notice. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month of premium bandwidth per plan, with no overage price and no throttle stated on the page read | metered: yes | free allowance: 1 TB per month | source: [1]
- identity: email | detail: the cart requires an account: the cart page carries Login and Register links; the registration form's fields were not read
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month of 'Premium Bandwidth' is stated per plan; the page publishes no overage rate, so the allowance is the wall and the port speed is not stated on the page read [1]
- limits note: 1 TB a month of 'Premium Bandwidth' is stated per plan; the page publishes no overage rate, so the allowance is the wall and the port speed is not stated on the page read
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the page names a self-service 'Cloud Panel' and a client portal at clients.terabix.net, plus a looking glass at lg.terabix.net; no API is documented on the page read
- composes with: 2 vCPU and 4 GB for USD 6 with a Singapore-adjacent location makes this the only South-East Asian host among documented hosts at that shape, so it fits an APAC crawl edge or a regional DNS probe; it is not the cheapest 4 GB here, because TNAHosting sells 4 GB for USD 5
- reliability: no reliability event recorded
- notes: The tracker's 1,024 GB and the vendor's 1 TB are the same figure in different units, so the two agree. The vendor states a 3-day money-back guarantee and accepts card, PayPal, Alipay and cryptocurrency, quoted on the page; that is a payment fact, not a trial. Unverified: the port speed, which neither page states plainly, and whether the 1 TB is calculated on outbound only. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 30
  - price_on_page: USD 6.00/month for CVM-4GB-Milan
- evidence:
  - [2] 2026-10-22: cheapest row: 'Terabix - USD 6.00 / month', '2 Epyc Cores (shared)', '4,096 MB RAM', '30 GB NVMe', '1,024 GB/month bandwidth', '1 Gbps port speed', 'Malaysia'
  - [1] 2026-10-22: Standard table row, quoted: 'CVM-4GB-M', '2 vCPU', '4 GB', '30 GB', '1 TB', 'USD 6/mo'; column heads read 'Plan', 'CPU', 'DDR4 Memory', 'NVMe Gen4', 'Premium Bandwidth', 'Price'
  - [1] 2026-10-22: Premium table starts at 'CVM-4GB', '2 vCPU', '4 GB', '30 GB', '1 TB', 'USD 7/mo', under 'DDR5 Memory'; the ladder runs to 'CVM-96GB' at 'USD 144/mo'
  - [3] 2026-10-22: home page: 'Starting from USD 6/month', 'AMD Genoa/Milan CPU Options', 'RAID-10 NVMe Gen4', 'IPv4 + IPv6 /64'; and 'Located in Equinix JH1' with '~1ms' to Singapore
  - [4] 2026-11-07: the cart configuration page prices all four cycles for CVM-4GB-Milan and the order summary shows USD 0.00 setup | capture: sha256:c4697e099273ec77c0967b4426ab724d29bb885804bdf3ad415ca90d236744f1 | quote: Choose Billing Cycle $6.00 USD Monthly $18.00 USD Quarterly $36.00 USD Semi-Annually $72.00 USD Annually
  - [4] 2026-11-07: the cart configuration page prices all four cycles for CVM-4GB-Milan | capture: sha256:c4697e099273ec77c0967b4426ab724d29bb885804bdf3ad415ca90d236744f1 | quote: Choose Billing Cycle $6.00 USD Monthly $18.00 USD Quarterly $36.00 USD Semi-Annually $72.00 USD Annually
  - [4] 2026-11-07: the cart page carries Login and Register links | capture: sha256:c4697e099273ec77c0967b4426ab724d29bb885804bdf3ad415ca90d236744f1 | quote: [Register](https://clients.terabix.net/register.php)
  - [4] 2026-11-07: the WHMCS cart prices all four cycles for CVM-4GB-Milan and the order summary shows USD 0.00 setup with no out-of-stock notice | capture: sha256:c4697e099273ec77c0967b4426ab724d29bb885804bdf3ad415ca90d236744f1 | quote: Choose Billing Cycle $6.00 USD Monthly $18.00 USD Quarterly $36.00 USD Semi-Annually $72.00 USD Annually
- sources:
  - [1] https://terabix.net/cloud-vm
  - [2] https://vpspricetracker.com/provider/Terabix/vps
  - [3] https://terabix.net/
  - [4] https://clients.terabix.net/index.php/store/cloud-vm-standard/cvm-4gb-milan
