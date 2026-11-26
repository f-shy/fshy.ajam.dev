# Strike

> strike.bz | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/strike/ | JSON https://fshy.ajam.dev/api/v1/entity/strike.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Strike

- `compute/strike` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:41.615Z (live) | stale on 2026-12-08
- url https://strike.bz
- price parsed USD 2.33/mo
- free tier: Budget line 'Pico' at EUR 25.00/year: 1 vCPU, 512 MB RAM, 10 GB NVMe SSD, 1 TB bandwidth, sold in Poland and the USA (the tracker names Gdansk and New Jersey). The page prices each plan at its shortest billing term, so the Pico plans are annual-only and no monthly price is published for them; the Budget 'Nano' is EUR 3.00/month with 1 GB and 15 GB, and the Pro line's 'Pico' is EUR 30.00/year with the same 512 MB and 10 GB shape. The order pages answer WHMCS 'Out of stock' with orders suspended, so the cart prices nothing while the suspension stands; no renewal price is published on any page read. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month is the stated allowance on this plan; the card states no overage price and no throttle, so the post-allowance behaviour is unverified | metered: yes | free allowance: 1 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month is stated on the plan card as 'Bandwidth 1TB'; the card states no port speed for this plan (the tracker claims 1 Gbps) and no overage rule [1]
- limits note: 1 TB a month is stated on the plan card as 'Bandwidth 1TB'; the card states no port speed for this plan (the tracker claims 1 Gbps) and no overage rule
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order links point at clientarea.strike.bz/index.php?rp=/store/... product pages; no API, panel or image documentation appears on the page read
- composes with: EUR 25.00 a year for 512 MB in Poland or New Jersey is a standing host for a webhook receiver, a certificate checker or an uptime monitor, where 1 TB is ample and the annual prepay is the only real cost; it is not a host for anything that moves bytes
- reliability: the order pages of Budget Pico in Poland and the USA, Budget Nano (Poland), Pro Pico Poland and Pro Nano (Poland) all answered WHMCS 'Out of Stock' with orders suspended on 2026-11-07; strike.bz still lists the plans and prices.
- notes: The vendor card states the annual price and the tracker states the monthly equivalent, so the two agree on the plan. The vendor's own no-KYC claim is recorded in the evidence rather than in identity_cost, because the signup page itself was not fetched and the field therefore stays at the email floor. Unverified: whether EUR 25.00/year renews at the same rate, and whether the 1 TB is enforced or shaped; the card states neither. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 10
  - monthly_usd: 2.33
- evidence:
  - [2] 2026-10-22: cheapest row: 'Strike - EUR 2.08 / month', 'yearly Service', '1 Intel Cores (shared)', '512 MB RAM', '10 GB NVMe', '1,000 GB/month bandwidth', '1 Gbps port speed', 'New Jersey U.S.A.' and a second identical row for 'Gdansk Poland'
  - [1] 2026-10-22: Budget 'Pico' card, quoted: 'Annual VPS for basic tasks', 'CPU 1 vCPU', 'RAM 512MB', 'Disk 10GB NVMe SSD', 'Bandwidth 1TB', 'Price EUR 25.00/yr', under the location columns 'Poland' and 'USA'
  - [1] 2026-10-22: Budget 'Nano' at 'EUR 3.00/mo' with '1GB' and '15GB NVMe SSD'; Pro 'Pico' at 'EUR 30.00/yr' with the same 512MB and 10GB; Pro 'Nano' at 'EUR 4.00/mo' with 1GB and 15GB
  - [1] 2026-10-22: identity, quoted from the FAQ list and the closing block: 'No KYC required - order without revealing your identity. Anonymous payment methods accepted. We collect minimal data by design.'
  - [1] 2026-11-07: the Budget Pico plan is still listed at EUR 25.00/yr with the same shape | capture: sha256:7be599cb5dedd6fcfbbcd999b6b0a944d05323234dcb0cf22550f253dc606378 | quote: | Pico Annual VPS for basic tasks. | 1 | 512MB | 10GB NVMe SSD | 1TB | €25.00/yr | Checking | |
  - [3] 2026-11-07: the Budget Pico USA order page suspends orders out of stock; the same page body served for the Poland pico, the Poland nano and both AMD pro plans checked | capture: sha256:97aa21e87d88d61546c9ad34a224a1f0d8d7eeba2377ca21dd9030519beaa3e4 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available.
  - [1] 2026-11-07: the Budget Pico card still prices EUR 25.00 per year with the same shape, and the page prices each plan at its shortest billing term | capture: sha256:7be599cb5dedd6fcfbbcd999b6b0a944d05323234dcb0cf22550f253dc606378 | quote: | Pico Annual VPS for basic tasks. | 1 | 512MB | 10GB NVMe SSD | 1TB | €25.00/yr | Checking | |
  - [3] 2026-11-07: the Budget Pico USA order page suspends orders out of stock, so the cart prices nothing while the suspension stands | capture: sha256:9e33c161f4c2f1d77f66f82fd22a0fdc0d73e12bd39ea7ba886960014a5a47a3 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available.
- sources:
  - [1] https://strike.bz
  - [2] https://vpspricetracker.com/provider/Strike/vps
  - [3] https://clientarea.strike.bz/index.php?rp=/store/intel-usa-vps-rdp-n/pico-intel-usa
