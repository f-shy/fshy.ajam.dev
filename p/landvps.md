# LandVPS

> landvps.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/landvps/ | JSON https://fshy.ajam.dev/api/v1/entity/landvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LandVPS

- `compute/landvps` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T11:15:35.517Z (live) | stale on 2026-12-08
- url https://landvps.ru/virtual-servers/cloud-vps/
- free tier: RUB 90/month (RU-0): 1 vCore Intel Gold at 2.20 GHz, 768 MB RAM, 10 GB SSD, 100 Mbps network, 1 IPv4, Moscow. The vendor page states it in Russian, translated here: plan RU-0 at 90 roubles a month, '1 vCore Intel Gold @ 2.20GHz', '768 MB RAM', '10 GB SSD', '100 Mbps Network', '1 IPv4', Moscow. The tracker lists the same RUB 90 plan in Saint Petersburg, Moscow and Ufa at 5,120 to 5,500 GB/month on a 1 Gbps port; the vendor page read states 100 Mbps and no monthly traffic figure for RU-0. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the page prices RU-0 at 90 roubles a month on a monthly term; the FAQ adds quarterly, half-year and yearly payment with no prices printed, so the annual price is not published; no renewal price is printed; stock is not stated on the page; the order button leads to BILLmanager registration, so cart-only values sit behind a sign-up
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: fixed monthly volume of 1 to 35 TB depending on the plan, per the vendor FAQ; the RU-0 figure is not stated on the page read, and extra traffic is sold without a published price there | metered: yes | source: [1]
- identity: email | detail: the product page's order button links to my.landvps.ru/billmgr?func=register (BILLmanager registration); the order-form function answered 'insufficient rights' without an account session, so ordering requires an account
- interface: rest, cli
- limits:
  - volume-quota (binding): the vendor FAQ states every plan includes a fixed traffic volume of 1 to 35 TB a month and that extra traffic can be bought, but the RU-0 figure is not stated on the page read; the tracker states 5,120 GB a month for the Saint Petersburg variant. The 10 GB SSD and the 100 to 1,000 Mbps port are the other two limits [1]
- limits note: the vendor FAQ states every plan includes a fixed traffic volume of 1 to 35 TB a month and that extra traffic can be bought, but the RU-0 figure is not stated on the page read; the tracker states 5,120 GB a month for the Saint Petersburg variant. The 10 GB SSD and the 100 to 1,000 Mbps port are the other two limits
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: client portal at my.landvps.ru (BILLmanager) with a registration redirect straight into the VPS order form; the product page states deployment through the portal, a CLI or a REST API; registration by email, VK or Gosuslugi is offered on the homepage
- composes with: 768 MB and 10 GB SSD at RUB 90 is a probe, a scheduler or a small proxy inside Russia, not a storage host: the vendor caps its own cloud VPS line at 800 GB NVMe or 3 TB HDD, so the 10 TB active dataset does not fit here at any price.
- reliability: no reliability event recorded
- notes: The site is Russian-language and prices are in RUB, which the record does not convert. The /pricing/virtual-servers page rendered an empty filter table (JavaScript), so the price came from the plan cards on the cloud-vps page. Tracker and vendor disagree on port speed (1 Gbps against 100 Mbps) and the vendor states no monthly allowance for RU-0; both are recorded rather than reconciled.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.75
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-22: plan card, translated from Russian for ASCII: the plan name 'RU-0' and the Latin-script tokens '1 vCore Intel Gold @ 2.20GHz', '768 MB RAM', '10 GB SSD', '100 Mbps Network', '1 IPv4' appear verbatim; the price line prints the rouble sign followed by 90 and the Russian word for month, and the location line names Russia, Moscow. The page title translates as 'Cloud VPS server from 90 RUB a month with 5-minute setup'
  - [1] 2026-10-22: FAQ translated from Russian: 'Each plan includes a fixed free traffic volume (from 1 to 35 TB depending on the plan). If necessary, additional traffic can be purchased.' The same page states deployment through the client portal, a CLI or a REST API, and its filter lists Moscow, Saint Petersburg, Ufa, Amsterdam, Helsinki, New York and Frankfurt
  - [2] 2026-10-22: three cards at 90.00 roubles a month, quoted where the text is Latin script: Saint Petersburg '768 MB RAM', '10 GB SSD', '5,120 GB/month bandwidth', '1 Gbps port speed', 'IPv4'; Moscow '5,500 GB/month', 'IPv4 + IPv6'; Ufa '10.7 GB SSD', '5,500 GB/month'
  - [1] 2026-11-07: the RU-0 plan card still prices the plan at 90 roubles a month | capture: sha256:148486a97d7ebd091ff03a28255122f065324d1ce729468e0306effd06226d12 | quote: ₽ 90 /мес
  - [1] 2026-11-07: the FAQ offers quarterly, half-year and yearly payment without printing any price for them | capture: sha256:148486a97d7ebd091ff03a28255122f065324d1ce729468e0306effd06226d12 | quote: Наши тарифы на Облачные VPS начинаются от 90 Рублей в месяц, также доступна квартальная, полугодовая и годовая оплата.
  - [1] 2026-11-07: the RU-0 order button leads to the BILLmanager registration form, not to a guest cart | capture: sha256:148486a97d7ebd091ff03a28255122f065324d1ce729468e0306effd06226d12 | quote: [Заказать](https://my.landvps.ru/billmgr?func=register&redirect=startpagevdsstartformvds2Eorder2Eparampricelist29period1project2)
  - [3] 2026-11-07: the billing API denies the order-form function without an account session | capture: sha256:986c8197d8cb262b259fd7b006bc73e2012bc7243b9fabde23861e64392b9b04 | quote: У вас недостаточно прав на выполнение функции 'vds.order.param'
  - [3] 2026-11-07: the billing API still denies the order-form function without an account session | capture: sha256:68b1d9cf16d828802356158ae26c70b679dd380482de8dbb68805d06f9ec6d7c | quote: У вас недостаточно прав на выполнение функции 'vds.order.param'
  - [1] 2026-11-07: the FAQ still offers quarterly, half-year and yearly payment without printing a price for them | capture: sha256:1860c5955440b0e3813c92dbb3ba16a73b27490ec177a1ee1a7bc7e5889be97b | quote: Наши тарифы на Облачные VPS начинаются от 90 Рублей в месяц, также доступна квартальная, полугодовая и годовая оплата.
- sources:
  - [1] https://landvps.ru/virtual-servers/cloud-vps/
  - [2] https://vpspricetracker.com/provider/LandVPS/vps
  - [3] https://my.landvps.ru/billmgr?func=vds.order.param&pricelist=29&period=1&project=2&out=json
