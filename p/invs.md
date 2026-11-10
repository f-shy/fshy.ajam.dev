# Invs

> invs.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/invs/ | JSON https://fshy.ajam.dev/api/v1/entity/invs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Invs

- `compute/invs` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://invs.ru/servers/renting-a-dedicated-server/
- free tier: The page is titled 'Server rental from 1200 roubles' and its own line reads 'from 1200 RUB a month'. The list behind it holds a Xeon E3-1240v6 at 3.7 GHz with 64 GB DDR4 ECC and 4 x 4 TB SATA, several E3-1220v6 machines with 32 GB DDR4 ECC, a Core i3-2100 with 8 GB DDR3 and 2 x 500 GB Enterprise disks, and an E3-1220 at 3.1 GHz with 8 GB DDR3 ECC and 2 x 1 TB Enterprise disks marked 20 percent off. Every row includes built-in KVM over IP and IPMI access. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the dedicated-server rate card (the page title quotes '1200 rub.' and the body line reads 'Vsego ot 1200 rub./mes.', with the listed configurations, 'Absolyutno bezlimitnyy trafik' and prepayment discounts) but not the order form. Whether a card is required, what hold applies, and whether debit or prepaid is accepted are all not stated, so the stored card kind is unsupported by this record's evidence.
- interface: unknown
- limits note: No published limit binds above the scale on this page; the traffic claim is 'absolutely unlimited' with no rate, which is a discretionary throttle and not a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A Russian machine at RUB 1200 with IPMI and unlimited traffic is the cheapest dedicated hardware found anywhere among evaluated providers, and it composes with a Western front end because the machine is the back end and latency does not matter for batch work.
- reliability: no reliability event recorded
- notes: INVS provides dedicated servers in Russia with IPMI.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Xeon E3-1220 class
  - facets.shape.vcpu: 4
  - facets.shape.threads: 8
  - facets.shape.ram_gib: 8
  - facets.shape.disk: 2 x 1 TB Enterprise HDD
  - facets.shape.traffic: stated as unlimited
  - facets.shape.price_rub_month: 1200
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: page title 'Arenda servera za 1200 rub. - dostupnye tseny na vydelennye servery' and body line 'Vsego ot 1200 rub./mes.'
  - [1] 2026-10-22: configurations listed: 'Xeon E3-1240v6, 3,7 GHz | RAM 64 GB DDR4 ECC | 4x4000 GB SATA', 'Xeon E3-1220v6 3.0 GHz | RAM 32 GB DDR4 ECC | 2x2000 GB SAS + RAID', 'Core i3-2100 3,1 GHz | RAM 8 GB DDR3 | 2x0,5 TB HDD Enterprise RAID1/RAID0', 'XEON E3-1220 3,1 GHz skidka 20% | RAM 8 GB DDR3 ECC | 2x1 TB HDD Enterprise', each with 'vstroennyy KVM over IP, IPMI-dostup'
  - [1] 2026-10-22: the page states 'Absolyutno bezlimitnyy trafik' and 'Skidki do 60% pri opolate za 3, 6, 12 mesyatsev', so the monthly figure is the worst price and annual prepayment discounts up to 60 percent
  - [2] 2026-10-22: a Russian survey of dedicated rental puts entry at '110 RUB/mo at 4VPS, 139 RUB at RuVDS, 180 RUB at Timeweb, 200 RUB at Selectel, 235 RUB at REG.ru, 299 RUB at AdminVPS, 350 RUB at IQHost, 503 RUB at Fornex, 593 RUB at Ayeza and 605 RUB at ISHosting'
- sources:
  - [1] https://invs.ru/servers/renting-a-dedicated-server/
  - [2] https://vc.ru/top-raiting/3125817-top-servisov-arendy-vydelennogo-servera
