# Saganetwork

> saganetwork.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/saganetwork/ | JSON https://fshy.ajam.dev/api/v1/entity/saganetwork.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Saganetwork

- `compute/saganetwork-windows` | qualifies-with-caveat | evidence unverified | binding none | category Windows VPS | tier VDS-16GB
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T13:30:00.000Z (live) | stale on 2026-11-10
- url https://www.saganetwork.net/vds-kiralama.html
- free tier: no free tier; the VDS-16GB plan is TRY 410.00 a month for 6 cores, 16 GB of DDR4 ECC, 120 GB of SSD and unlimited traffic, and the cart adds 20 per cent KDV for TRY 492.00 due today, which is USD 8.23 before tax and USD 9.88 paid at TRY 0.020085 | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 'Limitsiz' (unlimited) traffic on a 1 Gbps port, stated on the plan card; no byte quota, no fair-use threshold and no overage price is printed | metered: no | free allowance: unlimited, stated as 'Limitsiz' | source: [1]
- identity: card | detail: an account and a payment method at order; the rendered cart prints a due-today total of TRY 492.00 including KDV, so payment is required before the server exists
- interface: rest, cli
- limits:
  - volume-quota: unlimited traffic, stated as 'Limitsiz'; no threshold printed [1]
  - per-ip-shaping: 1 Gbps port [1]
- limits note: the cart prices four options: RAM 16 GB at TRY 190.00, CPU 6 cores at TRY 40.00, disk 80 GB at TRY 80.00 and an extra IP at TRY 0.00, on a TRY 100.00 base, which is the TRY 410.00 the product card prints. KDV at 20 per cent is added at the cart and the setup fee prints TRY 0.00. There is no operating-system field, so no licence delta exists to read.
- binding note: no quota in the seven-kind vocabulary binds: traffic is stated as unlimited and the port is the only published shaping value. What decides the row is the operating-system path, which the cart does not expose at all.
- interface detail: a KVM VDS whose admin path is RDP on the issued address once an operating system is installed; the cart exposes RAM, CPU, disk and an extra IP as its only options
- tooling: any RDP client; no API or console is described in the product page or the rendered cart
- composes with: the cheapest monthly-startable 16 GB machine in the sweep at USD 8.23 before tax, but the Windows path is FAQ prose and the cart configures no operating system, so it is a candidate for a buyer who will install and license Windows themselves rather than a licence-included row.
- reliability: no reliability event observed; the price is quoted in lira with 20 per cent KDV added at the cart, so the USD figure drifts with TRY and the FX rate reads in the evidence below set it.
- notes: The USD 8.23 is ex-KDV and the USD 9.88 is what the buyer pays today; a ranking that mixes the two is comparing a net figure with a gross one. The merge that raised this row used the TCMB rate and got USD 8.24, which is the same number to the cent. The cart renders client-side, so the totals are read from the rendered DOM rather than from the served HTML. The product card prints TRY 410.00 for a 120 GB disk while the cart's disk option reads 80 GB; both come from the same page and the contradiction is left standing rather than smoothed, because the recurring total agrees at 410.00 either way.
- evidence note: the plan, the shape, the monthly cycle, the option arithmetic, the 20 per cent KDV, the TRY 492.00 due today and the TRY 0.00 setup fee are documented twice: the product card prints TRY 410.00 and the rendered cart reproduces it as 100.00 plus 190.00 plus 40.00 plus 80.00. The record's rung is weaker than that because the verdict of a Windows row turns on the Windows path, and that is unverified: Windows Server appears only in the product page's FAQ prose, the cart carries no operating-system field, and no licence price is printed anywhere. A cart with an OS line, or a vendor reply naming the template and its licence, moves this rung to documented.
- extras:
  - shape.vcpu: 6
  - shape.ram_gib: 16
  - shape.disk_gib: 120
  - billing_model: monthly, 3-month, 6-month or yearly, no term discount
  - term: none monthly
  - monthly_try: 410.0
  - monthly_usd_ex_vat: 8.23
  - monthly_usd_paid: 9.88
  - vat_rate: 0.2
  - vat_try: 82.0
  - first_payment_try: 492.0
  - first_payment_usd: 9.88
  - setup_fee_try: 0.0
  - windows_licence: unresolved: Windows Server appears in the FAQ prose only, the cart configures no operating system and prints no licence price
  - ipv4_included: yes
  - port_mbps: 1000
  - traffic: unlimited, stated as 'Limitsiz'
  - fx: TRY 49.789069 per USD, open.er-api.com, 2026-10-26
  - product_url: https://www.saganetwork.net/vds-kiralama.html
  - cart_url: https://www.saganetwork.net/odeme/index.php?rp=/store/sanal-sunucu/sanal-sunucu-vds
- evidence:
  - [1] 2026-10-26: quoted from the VDS-16GB card: '6 Cekirdek', '16 GB' DDR4 ECC, '120 GB SSD Disk', 'Limitsiz', '1 Gbps', '410.00 TL /ay'
  - [2] 2026-10-26: quoted from the rendered cart: base 100.00, 'Ram: 16 GB 190.00', 'Cpu: 6 CPU 40.00', 'Disk boyutu: 80 GB 80.00', recurring total 410.00, 'KDV @ 20.00% 82.00', setup 0.00, 'Bugun Odenmesi Gereken 492.00'
  - [2] 2026-10-26: quoted from the cycle selector: monthly 100.00, 3-month 300.00, 6-month 600.00, yearly 1200.00, which is the base times 1, 3, 6 and 12 with no term discount, so the plan is not annual-only
  - [1] 2026-10-26: the FAQ states that Windows Server, Ubuntu, Debian and CentOS can be installed; the page prints no licence price and the cart has no operating-system field, so the Windows path is prose…
  - [3] 2026-10-26: TRY 49.789069 per USD with time_last_update_utc 2026-10-26T00:02:31Z, the rate behind the USD 8.23 and USD 9.88 figures; TRY 410.00 x 0.020085 = 8.23 and TRY 492.00 x 0.020085 = 9.88
- sources:
  - [1] https://www.saganetwork.net/vds-kiralama.html
  - [2] https://www.saganetwork.net/odeme/index.php?rp=/store/sanal-sunucu/sanal-sunucu-vds
  - [3] https://open.er-api.com/v6/latest/USD
