# KAGOYA CLOUD VPS

> kagoya.jp | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kagoya/ | JSON https://fshy.ajam.dev/api/v1/entity/kagoya.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KAGOYA CLOUD VPS (Compute)

- `compute/kagoya-cloud-vps` | paid-only | evidence documented | binding none | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.kagoya.jp/vps/function-plan/
- free tier: Day-rate billing with a monthly ceiling: the 1 GB plan is JPY 20 a day with a JPY 550 monthly cap, 2 GB with 2 cores and 200 GB NVMe is JPY 28 a day capped at JPY 770, and 4 GB with 4 cores and 600 GB NVMe is JPY 63 a day capped at JPY 1,760. Annual prepayment on the smallest plan is JPY 6,072, which the vendor presents as JPY 506 a month. The vendor states that no metered charge arises from increased data transfer. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the vendor's renewal notice states that the smallest plan is 1 core, 1 GB and 100 GB from JPY 506 a month on annual billing, that every plan uses NVMe, and that no metered billing arises from increased data transfer | metered: yes | source: [2]
- identity: card | detail: a credit card or a bank transfer: the payment page states payment is by credit card or account transfer and that debit cards are explicitly not accepted. There is no free lane, so a payment method is required at order. Whether prepaid cards are accepted is not stated, and no authorisation amount is stated
- interface: unknown
- limits note: Nothing binds above the scale: 100 GB of NVMe on the entry plan, no metered transfer charge, and a daily meter that stops at JPY 20 for the smallest box; there is no free lane at all, so the cost of entry is the binding fact rather than a limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At JPY 20 a day the plan is the cheapest way found in Japan to hold a real 1 GB box for one day of a job: create the instance, run it, delete it, and pay for the day rather than the month.
- reliability: no reliability event recorded
- notes: Kagoya has no free trial on VPS; its two-week free trial is on the shared rental server product, not this one, and the support FAQ says plans other than the shared and mail products carry a setup fee and cannot be trialled free. The JPY 506 monthly figure is annual prepayment divided by twelve, which the vendor itself does, and the JPY 550 figure is the monthly-billing cap; both are recorded because they are different prices for the same box. The absence of metered transfer billing is the vendor's claim on its own news page and is not probed.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan table gives 1 GB with 1 core and 100 GB NVMe at 日額20円 with 月額上限550円, 2 GB with 2 cores and 200 GB at 日額28円 capped at 770円, and 4 GB with 4 cores at 日額63円 capped at 1,760円, with 初期費用無料 and NVMe SSD on every plan
  - [2] 2026-10-22: the vendor's renewal notice states that the smallest plan is 1 core, 1 GB and 100 GB from JPY 506 a month on annual billing, that every plan uses NVMe, and that no metered billing arises from increased data transfer
  - [3] 2026-10-22: payment is by credit card or account transfer; debit cards are explicitly not accepted
  - [4] 2026-10-22: a third-party comparison states that KAGOYA CLOUD VPS has no free or trial period, and that the day rate makes the minimum commitment 24 hours; reported, not vendor-confirmed
- sources:
  - [1] https://www.kagoya.jp/vps/function-plan/
  - [2] https://www.kagoya.jp/news/2025020631681/
  - [3] https://support.kagoya.jp/vps/charge/payment.html
  - [4] https://www.serversus.work/services/kagoya-cloud-vps/

## KAGOYA CLOUD VPS (paid)

- `egress/kagoya-cloud-vps` | paid-only | evidence documented | binding none | category vps (hosted, Japan) | tier paid
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.kagoya.jp/vps/
- price JPY 550 per month cap for the 1 GB plan (JPY 20 per day) | parsed USD 3.51/mo
- free tier: [translated] '1 GB: 20 yen per day, monthly cap 550 yen.' No free tier appears on the page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] No free allowance. Billing is per day with a monthly cap: '1 GB: 20 yen per day, monthly cap 550 yen', with no traffic figure on the page.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Signup is at signup.kagoya.jp. The pages read do not state what a new account must supply; the card or email requirement is not established here. | country: None
- interface: ssh, cli
- binding note: Nothing in the free sense binds because there is no free tier. At 1 TiB/month the binding factor is the price: a 1 GB plan at a 550 yen monthly cap is cheap but not zero, and no traffic allowance is published to fail first.
- interface detail: [translated] Signup and scaling are through signup.kagoya.jp; the page documents immediate scale-up and annual payment.
- tooling: wg-quick inside the guest; SSH
- composes with: A USD 3.5 per month Japanese root guest is the fallback if no free Asian endpoint survives; it also measures whether an address in Japan is what a target wants.
- reliability: Daily billing means a machine can be created for one day; nothing on the page suggests a reclamation risk on a paid plan.
- notes: The cheapest per-day Japanese VPS found, and the only named candidate whose price is low enough to matter monthly (about USD 3.5 at the cap). It is not free, so it cannot answer question. Country: Japan. Considered and not read: Xserver VPS paid line, ConoHa VPS.
- evidence note: The daily rate and monthly cap are vendor sentences with a date. A Japanese comparison site claims a 14-day free trial for KAGOYA; the vendor page read does not mention one, so it is not recorded.
- extras:
  - wg_path: native-conf
  - wg_detail: A root NVMe guest; WireGuard runs inside it and wg-quick writes the .conf.
  - ingress: tcp+udp
  - volume_stated: [translated] No free allowance. Billing is per day with a monthly cap: '1 GB: 20 yen per day, monthly cap 550 yen', with no traffic figure on the page.
  - bytes_transit: yes
  - transit_note: The guest's own address on KAGOYA's Japanese network.
- evidence:
  - [1] 2026-10-23: [translated] '1 GB: 20 yen per day, monthly cap 550 yen', and 'all plans have no initial cost', billed per day, month or year.
- sources:
  - [1] https://www.kagoya.jp/vps/
