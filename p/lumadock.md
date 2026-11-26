# LumaDock

> lumadock.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lumadock/ | JSON https://fshy.ajam.dev/api/v1/entity/lumadock.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LumaDock

- `compute/lumadock-vps-s1` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category VPS | tier VPS.S1
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T19:33:06.061Z (live) | stale on 2026-12-07
- url https://lumadock.com/vps-hosting
- price parsed USD 4.99/mo
- free tier: no free tier; VPS.S1 at USD 4.99 is the cheapest plan on the ladder | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the site advertises a 30-day money-back guarantee on the first order
- egress: '1 Gbps network' on the plan card and 'Unmetered bandwidth' on the site; no traffic number is published | metered: no | free allowance: unmetered | source: [1]
- identity: card | detail: no order page was opened on 2026-10-24, so card acceptance, debit acceptance and any hold are unverified. The seller is a UK private limited company whose register entry was read on 2026-10-24.
- interface: ssh
- limits:
  - per-ip-shaping (binding): bandwidth described as unmetered on a 1 Gbps network; no fair-use number is published [1]
- binding note: unmetered traffic on a 1 Gbps port, so the 2 GB of RAM and 2 vCPU are the real ceiling.
- interface detail: the plan card and site state KVM, 'Full root access', SSH keys, reboots and reinstalls from the control panel, plus a dedicated IPv4 and IPv6
- tooling: any SSH client; the vendor's own order panel
- composes with: a 2 GiB KVM box from a UK-registered seller with a verified active company record; poor value per GiB but the cleanest counterparty in evaluated offerings.
- reliability: no reliability event recorded
- notes: Recorded mainly as the counterparty check evaluated offerings asked for. LUMADOCK LTD, company 15844051, is Active at Companies House, was incorporated on 17 July 2024 and was named LIFEINCLOUD LTD until 27 March 2026; its last accounts run to 31 July 2025 and its confirmation statement was filed on 16 July 2026, so it is trading. Two things do not line up: the site says the company is 'based in London W1S 1HN' while the register gives a Harrow HA3 8DP registered office, which is a formation-agent address, and the seller operates Romanian infrastructure with a +40 phone number. None of that makes it NATKVM, which was dissolved while still selling; it makes it a two-year-old company with a renamed history, which is worth knowing before paying a year up front. The price is also a 17% discount off USD 5.99, so the renewal is over the line.
- evidence note: shape, both prices and the unmetered term are quoted from the vendor's own plan ladder, parsed from the page source today. The company status is quoted from Companies House. The payment fields are unverified.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 30
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 4.99
  - m24h_usd: 4.99
  - price_arithmetic: USD 4.99 a month against a USD 5.99 list, a 17% discount; no conversion needed.
  - out_of_pocket_usd: 4.99
  - renewal_usd: 5.99
  - renewal_note: USD 5.99 list price, which is the renewal if the 17% discount is withdrawn
  - promo: yes
  - over_line: no
  - fx.pair: USD/USD
  - fx.rate: 1.0
  - fx.date: 2026-10-24
  - fx.source: not applicable
  - gib_per_usd: 0.4008
  - locations: Romania (Bucharest offer), with France, Finland and the Netherlands also listed
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted from the page source: 'VPS.S1 | $5.99 | Save | 17 | % | $4.99 | Monthly | 2 vCPU | AMD EPYC | 2 GB RAM | MEMORY | 30 GB NVMe | STORAGE'
  - [2] 2026-10-24: 
  - [3] 2026-10-24: quoted: 'LumaDock(R) is a registered trademark of LumaDock LTD, based in London W1S 1HN, United Kingdom, and registered in England and Wales under company number 15844051.'
  - [2] 2026-11-06: company 15844051 is an active private limited company, incorporated on 17 July 2024 | capture: sha256:3a9c3fae805778e81233e9b8eacf39924b28281386d77ead82876af34965f479 | quote: Company status Active Company type Private limited Company Incorporated on 17 July 2024
- sources:
  - [1] https://lumadock.com/vps-hosting
  - [2] https://find-and-update.company-information.service.gov.uk/company/15844051
  - [3] https://lumadock.com/
