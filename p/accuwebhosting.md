# AccuWeb Hosting

> accuwebhosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/accuwebhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/accuwebhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AccuWeb Hosting

- `compute/accuweb-windows` | paid-only | evidence documented | binding volume-quota | category Windows VPS | tier VPS Mellite
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://www.accuwebhosting.com/windows-vps-hosting.html
- price parsed USD 79.99/mo
- free tier: no free tier; VPS Mellite is USD 79.99/month and the Windows VPS range starts at VPS Emerald | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 2.5 TB of bandwidth a month; no overage price or post-allowance throttle is stated | metered: yes | free allowance: 2.5 TB per month | source: [1]
- identity: card | detail: an account and a payment method at order; the cart returned a Cloudflare challenge, so the instrument and any hold are unverified
- interface: unknown
- limits:
  - volume-quota (binding): 2.5 TB of bandwidth a month [1]
  - per-ip-shaping: the plan does not state a port speed [1]
- limits note: the order script's term toggle defaults to annual; the page does not print a setup fee
- binding note: 2.5 TB a month is the only byte ceiling published; the port speed is not stated.
- interface detail: RDP; the plan card states a Windows 2022/2019 licence is included and one IP address is included
- tooling: any RDP client; the provider's control panel
- composes with: 4 vCPU and 16 GiB for USD 79.99 a month with the licence printed as included, which makes it the reference row for a licence-included US seller
- reliability: no reliability event recorded
- notes: The USD 79.99 is the rendered monthly figure, but the order script defaults to an annual term, so the first payment may be twelve times that amount; the cart was behind a Cloudflare challenge and could not be read. The '50.00% Save' tag implies a list price near USD 159.98, which is unverified.
- evidence note: the shape, the price and the licence sentence are printed on the page read. The term and the list price are not printed: the card carries a 50% save tag and the order script defaults to annual.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 16
  - shape.disk_gib: 200
  - billing_model: monthly, with an annual default in the order script
  - term: annual default; monthly rate printed
  - monthly_usd: 79.99
  - first_month_usd: 79.99
  - first_payment_note: the cart was not read; an annual term would make the first payment USD 959.88
  - renewal_usd: 79.99
  - windows_licence: included, printed
  - ipv4_included: yes
  - traffic: 2.5 TB/month
  - stock: InStock, JSON-LD
  - cart_url: https://www.accuwebhosting.com/windows-vps-hosting.html
- evidence:
  - [1] 2026-10-26: quoted: 'VPS Mellite ... 16 GB ... 4 vCPU ... 200 GB ... 2.5 TB' and the rendered price '79.99'
  - [1] 2026-10-26: quoted: 'Windows 2022/2019 - License Included'
  - [1] 2026-10-26: the plan card carries a '50.00% Save' tag and the order script's term toggle defaults to annual; the list price is not shown
- sources:
  - [1] https://www.accuwebhosting.com/windows-vps-hosting.html
