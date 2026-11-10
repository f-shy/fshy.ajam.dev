# windowsvps.host

> windowsvps.host | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/windowsvps/ | JSON https://fshy.ajam.dev/api/v1/entity/windowsvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## windowsvps.host

- `compute/windowsvps-host-windows` | qualifies-with-caveat | evidence documented | binding none | category Windows VPS | tier DeluxeBox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:20:51.331Z (live) | stale on 2026-12-05
- url https://windowsvps.host/buy-rdp/
- price parsed USD 36/mo
- free tier: no free tier; DeluxeBox is USD 36.00 a month for 4 cores, 16 GB of RAM and 125 GB of NVMe on the marketing page, which reads 'starting at $36 /month', and the store render for the same plan prints USD 37.00 a month | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: unmetered data transfer on a shared 1 Gbps network port is stated on every plan card, DeluxeBox included; no overage price is stated | metered: no | source: [1]
- identity: card | detail: an account and a payment method at order; the store render stopped at the plan card and no order total was read
- interface: rest, cli
- limits note: no byte quota, port speed, request rate or object cap is printed on the plan line, so limits[] is empty rather than filled with a kind the vocabulary does not cover. The differentiator the page does print is the licence sentence, and it prints no term beyond monthly.
- binding note: nothing in the seven-kind vocabulary binds because the vendor publishes no quota at all. The open question is a price, not a limit: whether the order screen charges the USD 36.00 the marketing page headlines or the USD 37.00 the store render prints.
- interface detail: RDP with administrator access; the plan card states 'Windows license INCLUDED' and names the Datacenter edition
- tooling: any RDP client; no API or console is described on the pages read
- composes with: the cheapest row in the sweep whose page claims a Datacenter-edition licence inside the price, which makes it the natural comparison against a bring-your-own row plus a licence channel; the claim is a sentence, not an invoice line.
- reliability: no reliability event observed; the marketing page and the store render disagree by one dollar on the same plan, and the Datacenter-edition claim is not corroborated anywhere else on the site.
- notes: WindowsVPS.host provides Windows VPS hosting starting from USD 36.00 to USD 37.00 monthly for 4 vCPU, 8 GB RAM, and 125 GB storage with Windows OS licensing.
- evidence note: the shape, the USD 36.00 headline and the USD 37.00 store figure are both first-party reads on 2026-10-26, and the licence sentence is a vendor statement on the same page. The rung is not higher because no order total was reached and the two pages disagree by a dollar; the Datacenter claim is a sentence with no corroboration. A rendered cart moves the price question to settled without touching the licence sentence.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 16
  - shape.disk_gib: 125
  - billing_model: monthly
  - term: none
  - monthly_usd: 36.0
  - store_monthly_usd: 37.0
  - windows_licence: included per the page's 'Windows license INCLUDED'; Datacenter edition claimed and uncorroborated
  - ipv4_included: yes
  - plan_url: https://windowsvps.host/buy-rdp/
- evidence:
  - [1] 2026-10-26: quoted: 'DeluxeBox starting at $36 /month' on the marketing page
  - [1] 2026-10-26: quoted from the rendered plan card: 'Deluxebox $ 37.00 USD /mo', '4 Core', '16GB', '125GB NVMe'
  - [1] 2026-10-26: quoted on the licence: 'Windows license INCLUDED', Datacenter edition named; no licence price and no separate licence line appear on either page read
  - [1] 2026-11-04: the plan cards state unmetered data transfer | capture: sha256:844fdb326cb974a26ae4e53a9e3a49f3f11b61fd8bdcf7d0a656fb6ba4fc9c64 | quote: Unmetered Data Transfer
  - [1] 2026-11-04: the plan cards state a shared 1 Gbps port | capture: sha256:844fdb326cb974a26ae4e53a9e3a49f3f11b61fd8bdcf7d0a656fb6ba4fc9c64 | quote: Shared 1 Gbps Network Port
- sources:
  - [1] https://windowsvps.host/buy-rdp/
