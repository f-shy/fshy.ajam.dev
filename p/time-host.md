# Time_Host

> time-host.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/time-host/ | JSON https://fshy.ajam.dev/api/v1/entity/time-host.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Time_Host

- `compute/time-host` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T06:08:42.901Z (live) | stale on 2026-12-08
- url https://time-host.net/vds-nvme.html
- price parsed USD 1.71/mo
- free tier: KVM-MINI-NVMe at 139 RUB/month: 1 core, 768 MB RAM, 7 GB NVMe, channel up to 100 Mb/s, up to 8 IPv4, Moscow. The KVM-1-NVMe plan is 249 RUB/month with 1 GB and 20 GB, and the KVM SSD line starts at 199 RUB/month with 1 GB, 20 GB and a 100 Mb/s channel. The tracker quotes 139 RUB/month for the same KVM-MINI plan. The page publishes prepay discounts of 2 percent at 3 months, 5 percent at 6 months and 10 percent at 12 months; no annual plan price and no renewal price are printed. The card carries an order button and shows no out-of-stock notice. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the vendor card shows a traffic field with no value in the page text, so no first-party allowance was read; the tracker states 10,240 GB a month | metered: yes | free allowance: 10,240 GB per month, as reported by the tracker | source: [2]
- identity: email | detail: the order links lead to a BILLmanager registration page asking name, email, password and country, with sign-in via Google or VKontakte offered; the cart configuration sits behind that registration
- interface: rest
- limits:
  - volume-quota (binding): the tracker states 10,240 GB a month for this plan; the vendor card carries a traffic label with no visible value, so the allowance is reported and not confirmed. The 100 Mb/s channel is the second wall [1]
- limits note: the tracker states 10,240 GB a month for this plan; the vendor card carries a traffic label with no visible value, so the allowance is reported and not confirmed. The 100 Mb/s channel is the second wall
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the site offers an optional control-panel install ('ISPmanager' paid, 'FastPanel' free); no API is documented on the page read
- composes with: 768 MB and 7 GB for 139 RUB a month in Moscow is the lowest list figure among documented hosts and the only Russian host here, but the ranking against the EUR and USD plans depends on an exchange rate this category did not measure, so it stands as a Russia-region option for a latency probe or a small crawler exit; 7 GB of disk rules out anything that stores
- reliability: no reliability event recorded
- notes: Two disagreements with the tracker, both recorded: the tracker says a 0.2 Gbps port while the vendor card says up to 100 Mb/s, and the tracker's 10,240 GB monthly figure does not appear on the vendor card, whose traffic field renders with no value. The site is Russian-language and prices are in roubles with a RUB/EUR/USD display switch that was left on RUB. Unverified: the traffic allowance, which needs the plan's tooltip or the terms page rather than the card. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.75
  - facets.shape.disk_gib: 7
  - price_on_page: RUB 139/month for KVM-MINI-NVMe
- evidence:
  - [2] 2026-10-22: cheapest row: 'Time-Host - 139.00 RUB / month', '1 Intel Cores (shared)', '768 MB RAM', '7 GB NVMe', '10,240 GB/month bandwidth', '0.2 Gbps port speed', 'Moscow Russia'
  - [1] 2026-10-22: plan card, quoted from the Russian page with Cyrillic transliterated to ASCII: 'KVM-MINI-NVMe', '1 x Core', '768 Mb', '7 GB', 'do 100 Mb/s' (channel up to 100 Mb/s), '139 rub/mes' (139 RUB per month), IPv4 'do 8 sht'
  - [1] 2026-10-22: next cards: 'KVM-1-NVMe' at '249' RUB with 1,024 Mb and 20 GB; 'KVM-1-NVMe-Plus' at '349' RUB with 2,048 Mb; 'KVM-2-NVMe' at '319' RUB with 30 GB
  - [3] 2026-10-22: the SSD line starts at '199' RUB/month for 'KVM-1-SSD' with '1 x Core', '1024 Mb', '20 GB', '100 Mb/s'; the page lists term discounts of 2 percent for 3 months, 5 for 6 and 10 for 12
  - [1] 2026-11-07: the page states the three prepay discount percentages beside the plan card | capture: sha256:b60af92d758756c1a412c0a24b1a8caa9b16dd89023b35bb617f4af7b8320838 | quote: - 3 мес - 2% - 6 мес - 5% - 12 мес - 10%
  - [1] 2026-11-07: the KVM-MINI-NVMe card still prices 139 RUB per month | capture: sha256:b60af92d758756c1a412c0a24b1a8caa9b16dd89023b35bb617f4af7b8320838 | quote: 139 руб/мес
  - [4] 2026-11-07: the order flow opens on a registration form whose required fields are email, password and country | capture: sha256:f4e3b25515648760d3e08fc80484b3e4c2d81e03fb81df6ea4ee61a5b0c95638 | quote: Email address \* Password\* Re-enter the password Country\*
- sources:
  - [1] https://time-host.net/vds-nvme.html
  - [2] https://vpspricetracker.com/provider/Time_Host/vps
  - [3] https://time-host.net/vds-kvm.html
  - [4] https://my.time-host.net/manager/billmgr?func=register&redirect=startpage%3Dvds%26startform%3Dvds%252Eorder%252Eparam%26pricelist%3D1988%26period%3D1%26project%3D1
