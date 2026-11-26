# Hostwinds

> hostwinds.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostwinds/ | JSON https://fshy.ajam.dev/api/v1/entity/hostwinds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostwinds

- `compute/hostwinds-windows` | paid-only | evidence documented | binding volume-quota | category Windows VPS | tier Managed Windows SSD Cloud 7
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://www.hostwinds.com/vps/windows
- price parsed USD 182.99/mo
- free tier: no free tier; Managed Windows SSD Cloud 7 is USD 182.99/month, discounted to USD 118.94 for the first cycle | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 5 TB of bandwidth a month; no overage price or post-allowance throttle is stated | metered: yes | free allowance: 5 TB per month | source: [1]
- identity: card | detail: an account and a payment method at order; the buy page returns an account form, so the instrument and any hold are unverified
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 TB of bandwidth a month [1]
  - per-ip-shaping: the page does not state a port speed [1]
- limits note: the managed page states 'Windows VPS licenses are provided by Hostwinds when you order your Windows VPS'; the unmanaged page does not carry that sentence
- binding note: 5 TB a month is the only byte ceiling published; the port speed is not stated.
- interface detail: RDP with administrator access; Hostwinds has a control panel and API
- tooling: any RDP client; Hostwinds control panel and API
- composes with: 6 vCPU and 16 GiB for USD 118.94 in the first cycle, then USD 182.99, which makes the first cycle the only competitive number and the renewal the trap
- reliability: no reliability event recorded
- notes: The first-cycle price is a 35% discount; the renewal is USD 182.99, which is 54% higher. A reader who budgets the first cycle understates the steady bill by USD 64.05 a month.
- evidence note: the shape, the list price, the first-cycle discount and the licence sentence are printed on the managed Windows page read. The cart was not read.
- extras:
  - shape.vcpu: 6
  - shape.ram_gib: 16
  - shape.disk_gib: 300
  - billing_model: monthly
  - term: monthly
  - first_cycle_usd: 118.94
  - renewal_usd: 182.99
  - first_cycle_multiplier: 0.65
  - monthly_usd: 182.99
  - first_month_usd: 118.94
  - setup_fee_usd: 0.0
  - windows_licence: included, printed on the managed page
  - ipv4: not stated on the page
  - traffic: 5 TB/month
  - stock: orderable; no stock count published
  - cart_url: https://www.hostwinds.com/vps/windows
- evidence:
  - [1] 2026-10-26: quoted: 'CPU 6 CPU RAM 16 GB Storage 300 GB Bandwidth 5 TB Price $182.99/mo $118.94/mo'
  - [1] 2026-10-26: quoted: 'Windows VPS licenses are provided by Hostwinds when you order your Windows VPS'
  - [1] 2026-10-26: the page's embedded plan data carries id 391 and a firstCycleDiscountMultiplier of 0.65, which produces USD 118.94 from USD 182.99
- sources:
  - [1] https://www.hostwinds.com/vps/windows
