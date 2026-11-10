# Virtarix

> virtarix.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/virtarix/ | JSON https://fshy.ajam.dev/api/v1/entity/virtarix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Virtarix

- `compute/virtarix-windows` | qualifies-with-caveat | evidence documented | binding none | category Windows VPS | tier WIN VPS M
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T13:30:00.000Z (live) | stale on 2026-11-26
- url https://virtarix.com/vps/windows-vps/
- price parsed USD 27.4/mo
- free tier: no free tier; WIN VPS M is USD 27.40 a month for 6 vCores, 16 GB of RAM and 100 GB of NVMe, and the Windows Server licence is printed inside that figure as a USD 16.00 operating-system template line: the Linux twin at the same shape is USD 11.40 a month, and 11.40 plus 16.00 is 27.40 | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 'Unlimited bandwidth' stated for this plan in the page's own comparison table; the checkout prints no byte quota and no overage price | metered: no | free allowance: unlimited | source: [2]
- identity: card | detail: an account and a payment method at checkout; the rendered checkout prints a total including VAT of USD 32.70, so payment is required before the server exists
- interface: rest, cli
- limits note: the checkout prints four cycles and no quota: 1 month at USD 27.40 renewing 27.40 on 01/12/2026, 3 months at 27.40 renewing 82.20, 6 months at 27.40 renewing 164.40, and 12 months at 24.66 with a 10 per cent saving renewing 295.92. The first-payment totals it prints are pro-rata figures: USD 32.70 on the monthly cycle and USD 275.65 on the 12-month cycle, neither of which reproduces exactly from the list rate.
- binding note: no byte quota, request rate, object cap or retention clamp is printed anywhere on the offer or the checkout, so nothing in the seven-kind vocabulary binds. The number that decides the row is a price decomposition, not a constraint: 27.40 is 11.40 of machine plus 16.00 of licence.
- interface detail: RDP with administrator access on the issued address; the checkout selects a Windows template and prints its price beside it, which no other row in this set does
- tooling: any RDP client; Virtarix client area for rebuild and billing
- composes with: the cheapest row in the sweep where the Windows licence is a printed, priced component rather than a sentence, so it is the row to compare against a bring-your-own-licence machine plus a USD 14.17-a-month licence channel.
- reliability: no reliability event observed; the vendor's own pages disagree on the price by USD 0.20, with the comparison bar printing 27.60 for the same 6 vCPU, 16 GB, 100 GB row that the offer JSON-LD and the checkout price at 27.40.
- notes: The licence is not an addition to the 27.40; it is a component inside it, and the checkout proves that by pricing the same plan at 11.40 on the Linux page. That makes this row the reference for what a Windows layer costs at a reseller, which is USD 16.00 a month, and it sits beside Kimsufi's separately invoiced USD 34.00 for a 4-core Standard licence. The caveat is arithmetic in the buyer's favour only if they wanted the licence: a buyer with their own key pays 27.40 for a machine whose Linux twin is 11.40.
- evidence note: the plan, the four cycles, the renewal dates, the first-payment totals and the USD 16.00 operating-system line are read from the rendered checkout on 2026-10-26, and the USD 27.40 is corroborated by the page's own offer JSON-LD. The decomposition into a USD 11.40 Linux twin plus a USD 16.00 licence is arithmetic on two printed vendor prices, not a printed sentence, and the two first-payment totals are pro-rata figures that reproduce to within about USD 0.20 rather than exactly.
- extras:
  - shape.vcpu: 6
  - shape.ram_gib: 16
  - shape.disk_gib: 100
  - billing_model: 1, 3, 6 or 12 months
  - term: none monthly; 12 months at 10 per cent off
  - monthly_usd: 27.4
  - annual_monthly_usd: 24.66
  - first_payment_monthly_usd: 32.7
  - first_payment_annual_usd: 275.65
  - setup_fee_usd: 0.0
  - windows_licence: printed: USD 16.00 a month as the OS template line inside the 27.40; USD 14.40 on the 12-month cycle
  - linux_twin_usd: 11.4
  - windows_layer_usd: 16.0
  - windows_images: Windows-2022; Windows-2022 (Screaming Frog preinstalled); Windows-2019; Windows-2016
  - page_price_conflict_usd: 27.6
  - ipv4_included: yes
  - traffic: unlimited, per the comparison table
  - location: Frankfurt
  - checkout_url: https://my.virtarix.com/opcheckout.php?pid=2&plan=M&cycle=monthly
- evidence:
  - [1] 2026-10-26: quoted from the rendered checkout: 'Selected plan: Windows VPS - Frankfurt - M', '6 vCores CPU, 16 GB Memory, 100 GB Storage', '1 month 27.40 USD / per month Renews at 27.40 on 01/12/2026'
  - [1] 2026-10-26: quoted from the operating-system select: 'Windows-2022 - $16.00 (OS Template)', 'Windows-2019 - $16.00', 'Windows-2016 - $16.00'; the same line reads 14.40 on the 12-month cycle, the same 10 per cent term discount
  - [1] 2026-10-26: quoted: '1 month $27.40', 'Pro Rata until 01/12/2026 $32.70', 'Setup Fee Free', 'Total (incl. VAT) $32.70'; cycles 3 months 82.20, 6 months 164.40, 12 months 24.66 per month renewing 295.92
  - [3] 2026-10-26: Plan M on the Linux page is 6 CPU cores, 16 GB RAM and 100 GB NVMe at '$9.12/month first 3 months with 20% discount, then $11.40/month', so 11.40 + 16.00 = 27.40 and the Windows layer is a printed licence line rather than an absorbed cost
  - [2] 2026-10-26: the page's comparison bar prints 'Virtarix $27.60 6 vCPU, 16 GB RAM, 100 GB NVMe, Unlimited bandwidth' for the row the checkout bills at 27.40, a self-contradiction on one page
- sources:
  - [1] https://my.virtarix.com/opcheckout.php?pid=2&plan=M&cycle=monthly
  - [2] https://virtarix.com/vps/windows-vps/
  - [3] https://virtarix.com/vps/linux-vps/
