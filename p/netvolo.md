# NetVolo

> netvolo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netvolo/ | JSON https://fshy.ajam.dev/api/v1/entity/netvolo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetVolo

- `compute/netvolo-windows` | qualifies-with-caveat | evidence documented | binding volume-quota | category Windows VPS | tier VPS-Windows-3
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T13:30:00.000Z (live) | stale on 2026-11-26
- url https://www.netvolo.com/en/hosting/vps-windows
- price parsed USD 13.98/mo
- free tier: no free tier and no monthly cycle: VPS-Windows-3 is EUR 12.49 a month against a EUR 24.99 list rate, but every product on the page is billed as a three-year invoice, this one at EUR 449.82, for 4 vCPU, 16 GB of RAM and 200 GB of NVMe. The strings monthly, quarterly and annually return zero matches on the page, and 12.495 x 36 is 449.82 exactly, so the 12.49 is a monthly equivalent of a prepayment rather than a rate a buyer can pay monthly | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 16 TB monthly bandwidth allowance documented in prior page terms; capture on 2026-10-26 lists 4 vCPU, 16 GB RAM and 200 GB NVMe without traffic figures. No overage pricing is published. | metered: yes | free allowance: 16 TB per month, not re-confirmed on the 2026-10-26 read | source: [1]
- identity: card | detail: an account and a payment method at order; the checkout was not read
- interface: rest, cli
- limits:
  - per-ip-shaping: 1 Gbps network speed guarantee [1]
- limits note: The 1 Gbps port is documented on 2026-10-26; 16 TB monthly transfer was documented in prior page readings. Pricing reflects three-year billing (EUR 449.82 every 3 years) with no monthly terms published.
- binding note: 16 TB a month is the only published byte ceiling, so it is the kind named. What a buyer actually meets first is not a quota at all but the term: EUR 449.82 is due before the machine starts, there is no monthly cycle in which to pay less, and a multi-year prepayment has no kind in the seven-value vocabulary.
- interface detail: RDP with administrator access; credentials are issued at setup
- tooling: any RDP client; no API is described on the page
- composes with: the cheapest way to buy 200 GB of NVMe with 16 GB of RAM on a Windows plan, but the price is a three-year prepayment. It suits a long-lived box and not a test.
- reliability: no reliability event observed; the plan is advertised for Europe only.
- notes: The monthly-cycle question is settled and the answer is that there is no such cycle: three-year prepayment is the only term the page sells, so the EUR 12.49 is a monthly equivalent of a EUR 449.82 invoice and not a rate a buyer can start on. Ranking it beside a monthly rate compares a three-year commitment with a month. The licence answer is conditional, the plan page does not itemise a licence line, and the renewal after the first term is not printed. The three-year total is the number to compare against twelve Rabisu months.
- evidence note: the shape, the discounted rate, the list rate, the three-year total and the absence of any monthly cycle are printed on the page and confirmed on 2026-10-26: all eight products carry a 'Billed as X EUR every 3 years' footnote, the words monthly, quarterly and annually do not occur, and 12.495 x 36 reproduces the 449.82 exactly. The licence sentence is conditional and the renewal after the first term is not stated, which is what keeps the record at documented rather than settled.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 16
  - shape.disk_gib: 200
  - billing_model: three-year prepayment, no monthly cycle printed
  - term: 36 months only
  - monthly_cycle_available: no
  - monthly_eur: 12.49
  - monthly_usd: 13.98
  - list_monthly_eur: 24.99
  - first_payment_eur: 449.82
  - windows_licence: unverified on this SKU; the page FAQ says a licence may be included depending on the plan and this plan page adds nothing
  - windows_images: Windows Server 2022; Windows Server 2019
  - ipv4_included: yes
  - port_mbps: 1000
  - traffic: 16 TB/month
  - location: Europe
  - cart_url: https://www.netvolo.com/en/hosting/vps-windows
- evidence:
  - [1] 2026-10-26: quoted: 'VPS-Windows-3 ... 24,99 EUR ... 12,49 EUR / month ... Billed as 449.82 EUR every 3 years ... 4 vCPU ... 16 GB RAM ... 200 GB NVMe SSD'
  - [1] 2026-10-26: quoted from the page's card data: '{"id":"windows-vps-96","name":"VPS-Windows-3","price":12.495,"originalPrice":24.99,"currency":"EUR","unit":"month","savePercent":50,"footnote":"Billed as 449.82 EUR every 3 years"}', and 12.495 x 36 = 449.82 exactly
  - [1] 2026-10-26: no monthly cycle exists: all eight products on the page carry a 'Billed as X EUR every 3 years' footnote (143.82, 251.82, 449.82, 899.82 and the rest) and the strings monthly, quarterly and annually return zero matches in the 394,313-byte page
  - [1] 2026-10-26: quoted: 'Depending on the plan, a Windows Server license may be included. Details are listed on each plan page.' The plan page states nothing further, so the licence on this SKU is unverified
- sources:
  - [1] https://www.netvolo.com/en/hosting/vps-windows
