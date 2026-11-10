# Infrawire

> infrawire.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infrawire/ | JSON https://fshy.ajam.dev/api/v1/entity/infrawire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infrawire

- `compute/infrawire` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T11:15:47.347Z (live) | stale on 2026-12-08
- url https://infrawire.net/vps/turkey
- free tier: EUR 8.30/month for VPS Entry in Istanbul, printed against a struck EUR 16.60 with the vendor stating 'Same price on renewal': 2 vCores, 4 GB DDR4, 40 GB NVMe, a 2.5 Gbps port, unlimited traffic, a dedicated IPv4 and IPv6, KVM, root access, all ports open except 25, DDoS protection and a 7-day money-back guarantee. VPS Bronze is EUR 14.55/month for 4 vCores, 8 GB and 80 GB at 5 Gbps; Silver is EUR 27.60 for 8 vCores, 16 GB and 150 GB; Gold is EUR 41.48 for 12 vCores, 24 GB and 180 GB at 10 Gbps; Platinum is EUR 52.20 for 16 vCores, 32 GB and 200 GB. Windows Server images are offered on the same line, and the offer thread adds a 15 percent first-month code. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic, no bandwidth caps, behind the plan port speed; no overage term exists because no volume is counted | metered: no | free allowance: unlimited at 2.5 Gbps on VPS Entry | source: [1]
- identity: email | detail: the console register form requires first name, last name, email and password, with Google sign-in offered; no phone or card; the page states 'Register with your real details' (read 2026-11-07)
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): traffic is stated as unlimited, so the 2.5 Gbps port is the wall on the entry plan and the byte counter is not. The vendor prints the discount as a standing price with 'Same price on renewal' rather than as a first-term promo, which is what makes the row usable at that port for a long run. [1]
- limits note: traffic is stated as unlimited, so the 2.5 Gbps port is the wall on the entry plan and the byte counter is not. The vendor prints the discount as a standing price with 'Same price on renewal' rather than as a first-term promo, which is what makes the row usable at that port for a long run.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor runs a looking glass at lg.infrawire.net and an app marketplace for order-time installs; no API or CLI is documented on the page read
- composes with: EUR 8.30 for 4 GB and 40 GB of NVMe with unlimited traffic on a 2.5 Gbps port, in Istanbul, is the only record among evaluated providers where the byte counter does not bind, which makes it the one to price first when the job is moving bytes rather than storing them; the other four locations are on the same product line and the same account.
- reliability: no reliability event recorded
- notes: The thread title says 'Starting at $9.30/mo' while the vendor page states EUR 8.30 and the thread itself prints 'VPS Entry: EUR 8.30/month (approx $9.55)', so the headline dollar figure in the title is neither the vendor currency nor the vendor's own conversion; the record uses the EUR figure and does not convert. verification criteria: whether the struck EUR 16.60 is the real list price or a standard-price anchor, and whether unlimited traffic carries an unwritten fair-use cut-off, since neither page states one. No conversion was performed in this record; the USD figures quoted are the vendor's own.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 40
  - monthly_price: EUR 8.30 per month for VPS Entry (2 vCores / 4 GB / 40 GB NVMe) in Istanbul, printed against a struck EUR 16.60; the page's structured data prices the five-plan line from 8.30 to 52.20 EUR monthly
  - annual_price: not published: no page read prints an annual figure; the checkout names quarterly, semi-annual and annual cycles but renders only in JavaScript
  - renewal_price: not published as a figure: the plan card states the phrase 'Same price on renewal'
  - billing_term: monthly, no commitment; the checkout names quarterly, semi-annual and annual cycles but prints no figure outside JavaScript
  - stock: in stock: the page's structured data marks all five plans InStock with a priceValidUntil of 2027-11-07
  - cart_price: unverified: behind a sign-up - the order flow is an in-page checkout at console.infrawire.net that asks the customer to create an account before payment; no guest cart URL exists
- evidence:
  - [1] 2026-10-22: plan block quoted: 'VPS Entry', 'Save 50%', 'EUR 16.60 EUR', 'EUR 8.30EUR/month', 'Same price on renewal', '2 vCores', '4 GB RAM DDR4', '40Go SSD NVMe', '2.5 Gbps', 'Unlimited traffic', 'Dedicated IPv4 & IPv6'; the page title is 'Turkey VPS - Istanbul Datacenter from EUR 8.30/mo'
  - [2] 2026-10-22: the offer thread, posted October 22, 2026, states: 'Full NVMe storage, dedicated IPv4+IPv6, and no bandwidth caps'; 'Live locations: France, Germany, United States, Hong Kong, Turkey'; 'Prices are set in EUR and shown with their USD equivalent (rate 1 EUR = 1.15 USD)'; 'Launch offer: use code LOWENDTALK at checkout for 15% off your first month. Valid for new customers only'
  - [1] 2026-11-07: the plan card prices VPS Entry at EUR 8.30 per month against a struck EUR 16.60 | capture: sha256:c96d58e5aa6c023e17e23bf9497a8578a70e28855475e3dd864732de30112a2c | quote: €8.30EUR/month
  - [1] 2026-11-07: the page's structured data carries one monthly price per plan and no annual figure | capture: sha256:db2e23dbc093d0a1ef5c1ebcfbcc44d0fbd324ab6c6493646419d4c6cea65c33 | quote: "lowPrice":"8.30","highPrice":"52.20","offerCount":5,"priceValidUntil":"2027-11-07","availability":"https://schema.org/InStock"
  - [1] 2026-11-07: the card states the renewal price equals the listed price | capture: sha256:c96d58e5aa6c023e17e23bf9497a8578a70e28855475e3dd864732de30112a2c | quote: *Same price on renewal
  - [1] 2026-11-07: the card prices monthly and states no commitment | capture: sha256:c96d58e5aa6c023e17e23bf9497a8578a70e28855475e3dd864732de30112a2c | quote: €8.30EUR/month No commitment
  - [1] 2026-11-07: the page's structured data marks the plans InStock | capture: sha256:db2e23dbc093d0a1ef5c1ebcfbcc44d0fbd324ab6c6493646419d4c6cea65c33 | quote: "lowPrice":"8.30","highPrice":"52.20","offerCount":5,"priceValidUntil":"2027-11-07","availability":"https://schema.org/InStock"
  - [1] 2026-11-07: the checkout asks for an account before payment | capture: sha256:db2e23dbc093d0a1ef5c1ebcfbcc44d0fbd324ab6c6493646419d4c6cea65c33 | quote: Create your account and complete payment to finalise your order.
  - [3] 2026-11-07: the console register form's required fields | capture: sha256:7c563f8eb614382c8b26a5b189c7b035b3164a5466dfbded5da5fbcf2ee87f4a | quote: First name Last name Email Password
  - [1] 2026-11-07: the entry plan's price and term are unchanged on 2026-11-07 | capture: sha256:c96d58e5aa6c023e17e23bf9497a8578a70e28855475e3dd864732de30112a2c | quote: €8.30EUR/month No commitment
- sources:
  - [1] https://infrawire.net/vps/turkey
  - [2] https://lowendtalk.com/discussion/222403/infrawire-vps-now-in-turkey-10-gbps-linux-windows-starting-at-9-30-mo
  - [3] https://console.infrawire.net/register
