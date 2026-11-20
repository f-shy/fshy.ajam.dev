# Hostodo

> hostodo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostodo/ | JSON https://fshy.ajam.dev/api/v1/entity/hostodo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostodo

- `compute/hostodo-black-friday-2025` | qualifies-with-caveat | evidence unverified | binding volume-quota | category VPS | tier BLACK FRIDAY SPECIAL 1 GB and 2.5 GB KVM VPS
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T15:56:55.347Z (live) | stale on 2026-11-21
- url https://www.hostodo.com/black-friday-2025
- price parsed USD 1/mo
- free tier: no free tier; the page offers 1 GB at USD 12 a year and 2.5 GB at USD 22 a year | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the term is paid; no deletion clock stated
- egress: 3 TB a month at 1 Gbit/s on the 1 GB tier, 4 TB on the 2.5 GB tier | metered: yes | free allowance: 3 TB | source: [1]
- identity: card | detail: signup at console.hostodo.com is required before the order links work; the page lists 'Credit Card, PayPal, AliPay, and Crypto Accepted'. No hold stated.
- interface: ssh
- limits:
  - volume-quota (binding): 3 TB a month at 1 Gbit/s on the 1 GB tier [1]
- binding note: The checkout, not the offer: the page is live, dated 2025 and priced, but console.hostodo.com renders client-side, so the price at checkout is unverified. The caveat is unreadability, not a known repricing.
- interface detail: root SSH, self-service control panel, one IPv4 plus a /64 IPv6 subnet
- tooling: any SSH client; the console at console.hostodo.com is a Next.js app whose deploy route needs a signed-in session
- composes with: USD 12 a year for 1 GiB with IPv6 would answer the WireGuard question, if the deploy route could be read without an account.
- reliability: no reliability event recorded
- notes: The sale page is live, dated 2025 and priced, and the order links are real console routes, but the console is a client-rendered app: the deploy URL returns the same 2,006 bytes for a valid plan code and a made-up one, so nothing about price or stock can be read without signing in. That control is the reason this row is unverified rather than a finding - without it the HTTP 200 would have looked like a working cart. Does not create accounts. The verdict is qualifies-with-caveat rather than dead because the page and its prices are first-party and current; it is not qualifies because nothing confirms the cart still charges them.
- evidence note: The sale page was read on 2026-11-06 and its prices are quoted. The cart is still unreadable: the deploy route answers 200 with 2,006 bytes and no price string, so the price at checkout is unverified rather than confirmed. The weakest field is the cart, which keeps the record unverified.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 20
  - billing_model: annual
  - term: annual, two-year or three-year prepay
  - m10h_usd: 1.0
  - m24h_usd: 1.0
  - price_arithmetic: USD 12 a year divided by 12 is USD 1.00 a month, paid once. The 2.5 GB tier is USD 22 a year, USD 1.8333 a month; its two-year price of USD 38 is USD 1.5833 a month.
  - renewal_usd: not published
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - sale_page_year: 2025
  - locations: Detroit MI (DET01), Tampa FL (TPA01), Las Vegas NV (LAS01)
  - price_on_page: USD 12.00/yr for 1 GB (page), USD 22.00/yr for 2.5 GB
  - cart_works: unknown
  - cart_note: the deploy URL resolves and renders a console, but no price line was readable in the server-rendered HTML; a control request with a bogus plan code returned byte-identical output, so the 200 establishes nothing about this plan
- evidence:
  - [1] 2026-10-24: quoted: 'BLACK FRIDAY SPECIAL 1GB RAM ... 20GB NVMe ... 3TB @ 1Gbit/s ... $12/year [ORDER NOW]'; '2.5GB RAM ... 40GB NVMe ... 4TB ... $22/year $38/2 years | $50/3 years'; the page reads 'LIMITED TIME OFFER - BLACK FRIDAY 2025'
  - probe:https://console.hostodo.com/instances/deploy/DET01/2025BF-1G20G1C 2026-10-24: HTTP 200, 2,006 bytes, sha256 ffc79d5dcba383e5... - a Next.js shell with an empty #__next div and no price in the bytes
  - probe:https://console.hostodo.com/instances/deploy/DET01/BOGUS-CODE-XYZ 2026-10-24: control: HTTP 200, 2,006 bytes, sha256 ffc79d5dcba383e5... - byte-identical to the real plan code, which proves the route does not encode a product and the 200 is not evidence of an offer
  - [2] 2026-10-24: redirects to /black-friday-2025, so the short path is the same page
  - [1] 2026-11-06: the 1 GB tier is still USD 12 a year on the live sale page | capture: sha256:a302cce7c26c0259dee6a4c9c36db11a3aca3d062b490a1d99f61d22c254fca6 | quote: $12/year
  - [1] 2026-11-06: the 1 GB tier still carries 3 TB a month at 1 Gbit/s | capture: sha256:a302cce7c26c0259dee6a4c9c36db11a3aca3d062b490a1d99f61d22c254fca6 | quote: 3TB @ 1Gbit/s
  - [1] 2026-11-06: the sale page still lists the accepted payment methods, a card among them | capture: sha256:a302cce7c26c0259dee6a4c9c36db11a3aca3d062b490a1d99f61d22c254fca6 | quote: Credit Card, PayPal, AliPay, and Crypto Accepted
  - probe:https://console.hostodo.com/instances/deploy/DET01/2025BF-1G20G1C 2026-11-06: the deploy route answers 200 with 2,006 bytes and no price string, the same answer the record's 2026-10-24 probe got, so the cart still cannot be read without an account | capture: sha256:a01458ed4a8a080ce0062b6b3af96a8739fb7b764de85049d9d6b9bbdf08ad7d | quote: "verdict": "no-price"
  - probe:https://console.hostodo.com/instances/deploy/DET01/2025BF-1G20G1C 2026-11-06: the cart still returns no price, which is the caveat the verdict rests on | capture: sha256:a01458ed4a8a080ce0062b6b3af96a8739fb7b764de85049d9d6b9bbdf08ad7d | quote: "verdict": "no-price"
- sources:
  - [1] https://www.hostodo.com/black-friday-2025
  - [2] https://www.hostodo.com/black-friday
