# Cloudzy

> cloudzy.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudzy/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudzy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloudzy

- `compute/cloudzy-windows` | trial-only | evidence documented | binding volume-quota | category Windows VPS | tier Windows VPS 16 GB
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://cloudzy.com/windows-vps/
- price parsed USD 99.95/mo
- free tier: no free tier; the 16 GB Windows VPS is USD 49.98/month at the promotional rate against USD 99.95 list, and the Windows licence is a trial or bring-your-own | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 10 TB of transfer a month with no egress fees; no overage price is stated | metered: yes | free allowance: 10 TB per month | source: [1]
- identity: card | detail: an account and a payment method at order; the checkout was not read
- interface: rest, cli
- limits:
  - volume-quota (binding): 10 TB of transfer a month [1]
  - per-ip-shaping: 40 Gbps network [1]
- limits note: the page states 'Ships with a trial license so you can start working right away, or activate your own Windows license (BYOL)'; the trial length is not stated
- binding note: 10 TB a month is the published byte ceiling; the licence is the disqualifier, not a quota.
- interface detail: full administrator RDP over a dedicated IPv4 and IPv6; Cloudzy has an API and control panel
- tooling: any RDP client; Cloudzy control panel and API
- composes with: the cheapest shape at 8 vCPU and 16 GiB, but the licence is a trial or the buyer's own, so it cannot be ranked against the licence-included rows
- reliability: no reliability event observed; the promotional rate is 50% off the list price.
- notes: The row is the cheapest way to buy 8 vCPU and 16 GiB, and it fails the question's licence requirement: the Windows licence is a trial of unstated length or the buyer's own. It is recorded as a near miss rather than ranked, because a trial that expires leaves the machine unusable without a separate Microsoft licence.
- evidence note: the shape, the price, the discount and the trial/BYOL sentence are printed on the page read. The trial length is not stated, and the renewal is not confirmed.
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 16
  - shape.disk_gib: 350
  - billing_model: monthly or hourly
  - term: none
  - promo_usd: 49.98
  - list_usd: 99.95
  - discount_percent: 50
  - monthly_usd: 99.95
  - first_month_usd: 49.98
  - setup_fee_usd: 0.0
  - renewal_usd: 99.95
  - windows_licence: trial or BYOL; not supplied for the life of the machine
  - trial_length: not stated
  - ipv4_included: yes
  - ipv6_included: yes
  - port_mbps: 40000
  - traffic: 10 TB/month
  - stock: deploy in 60 seconds; no stock language
  - cart_url: https://cloudzy.com/windows-vps/
- evidence:
  - [1] 2026-10-26: quoted: '16 GB DDR5 ... $49.98/mo $99.95/mo -50% ... 8 vCPU @ EPYC ... 350 GB NVMe ... 10 TB ... 40 Gbps ... Dedicated IPv4 + IPv6 ... Full administrator RDP'
  - [1] 2026-10-26: quoted: 'Ships with a trial license so you can start working right away, or activate your own Windows license (BYOL)'
- sources:
  - [1] https://cloudzy.com/windows-vps/
