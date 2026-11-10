# CoolVDS

> coolvds.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coolvds/ | JSON https://fshy.ajam.dev/api/v1/entity/coolvds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoolVDS

- `compute/coolvds` | qualifies-with-caveat | evidence documented | binding volume-quota | category microVM (Firecracker), monthly reserved | tier SPARK XS
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T02:40:00.000Z (live) | stale on 2026-11-24
- url https://coolvds.com/pricing
- price parsed USD 4/mo
- free tier: No free tier published on the pricing page; the smallest plan is SPARK XS at USD 4 a month. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Not stated on the pricing page read; a monthly plan implies the disk persists while the plan is paid. | source: [1]
- egress: 1 TB of bandwidth included on SPARK XS; the price of traffic beyond it is not published on the pricing page. | metered: yes | free allowance: 1 TB | source: [1]
- identity: card | detail: A monthly plan implies a payment method at checkout; no card, hold or debit statement was read on the pricing page. Unverified.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB of bandwidth a month on SPARK XS [1]
- limits note: The shape is the first wall: 512 MB of DDR5 RAM and 10 GB of Gen5 NVMe, with no published resize or add-on disk path on the pricing page. Volume discount is 5% from USD 300 a month.
- binding note: 512 MB of RAM is the shape ceiling under USD 5, and the next plan (SPARK S, 2 vCPU / 2 GB) is USD 7; the 1 TB traffic cap is the metered wall behind it.
- interface detail: A Firecracker microVM with a deploy flow and an order page; 'API Access' is listed only on the SPARK M plan and above, so SPARK XS has no published API.
- tooling: SSH to a Linux microVM. The site is a small operator's storefront: no SDK, no CLI and no documented API at the USD 4 tier.
- composes with: The cheapest published monthly microVM with a dedicated 1 vCPU: USD 4 a month for 1 vCPU, 512 MB and 10 GB NVMe with 1 TB of transfer. Use it where a real always-on box is wanted and 512 MB is enough, which rules out anything with a JVM, a database and an agent runtime on the same box.
- reliability: waitlist only: the order page says "All Slots Currently Occupied" and offers no order button
- notes: Verification items: checkout page for accepted payment methods, and documentation for SSH and overage rates.
- evidence note: The plan name, price, shape and traffic allowance are quoted from the pricing page. automated retrieval served a stored snapshot of that page captured at 01:49 UTC rather than a live fetch, so the page was read but not re-fetched. SSH, the payment method and the overage rate are not on the page.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 10
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 4.0
  - m24h_usd: 4.0
  - price_arithmetic: Monthly plan: USD 4.00 a month bills whether it runs or not, so 24/7 = USD 4.00 and 10 h/day = USD 4.00. No hourly rate is published.
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.ports: not published on the pricing page
  - session_cap.restart_required: no
  - session_cap.note: none published; a monthly plan
  - aggregator_gross_usd_month: 4.0
  - aggregator_note: sandboxprices.com ranks CoolVDS #11 at USD 4.00 gross for this same SPARK XS shape; the two agree exactly because the product is a fixed monthly plan.
- evidence:
  - [1] 2026-10-24: quoted: 'SPARK XS $4/mo - 1 vCPU (Firecracker), 512 MB DDR5 RAM, 10 GB Gen5 NVMe, 1 TB Bandwidth, 99.9% Uptime SLA'
  - [1] 2026-10-24: plan ladder: 'SPARK S $7/mo' 2 vCPU / 2 GB / 25 GB / 2 TB; 'SPARK M $13/mo' 4 vCPU / 4 GB / 50 GB / 4 TB; 'SPARK L $25/mo' 8 vCPU / 8 GB / 100 GB / 8 TB
  - [2] 2026-10-24: payment: 'Accepted Payment Methods: Stripe, PayPal ... All major credit cards accepted'
  - [3] 2026-10-24: quoted: '125ms Boot Time', '$0.00 Ingress Fees', 'Firecracker MicroVMs starting at $3.90/mo' (the meta description's USD 3.90 does not match the USD 4 shown on the plan card)
  - [1] 2026-10-24: quoted: 'Entry MicroVM SPARK XS $4/mo - 1 vCPU (Firecracker) - 512 MB DDR5 RAM - 10 GB Gen5 NVMe - 1 TB Bandwidth - 99.9% Uptime SLA'
  - [1] 2026-10-24: quoted: 'SPARK S $7/mo - 2 vCPU (Firecracker) - 2 GB DDR5 RAM - 25 GB Gen5 NVMe - 2 TB Bandwidth'; 'SPARK M $13/mo ... API Access'
- sources:
  - [1] https://coolvds.com/pricing
  - [2] https://coolvds.com/order?plan=SPARK+XS&category=microvms
  - [3] https://coolvds.com/
