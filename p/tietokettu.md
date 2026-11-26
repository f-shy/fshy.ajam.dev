# Tietokettu

> tietokettu.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tietokettu/ | JSON https://fshy.ajam.dev/api/v1/entity/tietokettu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tietokettu

- `compute/tietokettu` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:41.618Z (live) | stale on 2026-12-08
- url https://tietokettu.net/store/vps-palvelimet
- price parsed USD 2.82/mo
- free tier: Mini VPS at EUR 2.50/month on the vendor store: 2 GB RAM, 1 vCPU, 20 GB SSD, 1 TB monthly bandwidth, Lempaala Finland, Linux and FreeBSD. The cart offers monthly EUR 2.50, quarterly EUR 7.48, semi-annually EUR 14.95 and annually EUR 29.90; no renewal price is printed and no out-of-stock notice is shown. | unit: GiB | metered on: wall-clock | read on: 2026-11-07 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: 1 TB a month is stated on the vendor plan card ('1TB Kuukausittaista kaistaa'); no overage price and no throttle are stated on the pages read | metered: yes | free allowance: 1 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month is stated on the vendor plan card; no overage rate and no port speed are published on the pages read [1]
- limits note: 1 TB a month is stated on the vendor plan card; no overage rate and no port speed are published on the vendor pages read; the tracker's 0.5 Gbps port figure is unconfirmed by the vendor
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated: neither page read documents a panel, an API or an image list
- composes with: 2 GB of RAM for EUR 2.50 a month in Finland is the cheapest two-gigabyte machine, so it fits an EU monitoring or DNS node
- reliability: no reliability event recorded
- notes: Prices confirmed in the vendor WHMCS cart on 2026-11-07: EUR 2.50 monthly, EUR 7.48 quarterly, EUR 14.95 semi-annually and EUR 29.90 annually. The vendor pages state no port speed, so the tracker's port figure stands unconfirmed, and the tracker's separate HDD row does not appear on the vendor VPS category.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - price_on_page: EUR 2.50/month for Mini
- evidence:
  - [2] 2026-10-22: cheapest row: 'Tietokettu - EUR 2.50 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '20 GB SSD', '1,000 GB/month bandwidth', '0.5 Gbps port speed', 'Lempaala Finland', 'IPv4 + IPv6'; the page opens 'starting at EUR 2.50 per month'
  - [2] 2026-10-22: company profile: firm 'HD-decor Oy (Tietokettu)', website https://tietokettu.net, address 'Rantaharju 15, 37500 Lempaala, Finland'
  - [1] 2026-11-07: the vendor's own VPS category page lists the Mini plan at 2.50 EUR monthly | capture: sha256:cf826c4d7e19880bbfac4f9c7fb61ce42caa39c4fa6c90e1e760ceda15f98302 | quote: ### Mini 2.50 € kuukausittain
  - [3] 2026-11-07: the cart configuration page for the Mini plan prices all four billing cycles and shows no out-of-stock notice | capture: sha256:c5dcf1d1791a75a9c94b52e30390517a54cd0d137adf3f8b86e2f480740ced67 | quote: ### kuukausittain 2.50 € ### neljäsosavuosittain 7.48 € ### puolivuosittain 14.95 € ### vuosittain 29.90 €
  - [1] 2026-11-07: the vendor plan card states 1 TB monthly bandwidth, 2 GB RAM, 1 vCPU, 20 GB SSD and prints no port speed | capture: sha256:cf826c4d7e19880bbfac4f9c7fb61ce42caa39c4fa6c90e1e760ceda15f98302 | quote: ### Mini 2.50 € kuukausittain * 2GB RAM-muisti * 1x vCPU * 20GB SSD Levytila * 1TB Kuukausittaista kaistaa
  - [3] 2026-11-07: the WHMCS cart configurator for the Mini plan prices all four billing cycles and renders no out-of-stock notice | capture: sha256:c5dcf1d1791a75a9c94b52e30390517a54cd0d137adf3f8b86e2f480740ced67 | quote: ### kuukausittain 2.50 € ### neljäsosavuosittain 7.48 € ### puolivuosittain 14.95 € ### vuosittain 29.90 €
- sources:
  - [1] https://tietokettu.net/store/vps-palvelimet
  - [2] https://vpspricetracker.com/provider/Tietokettu/vps
  - [3] https://tietokettu.net/cart.php?a=add&pid=60
