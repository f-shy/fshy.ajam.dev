# XeniaHosting

> xeniahosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xeniahosting/ | JSON https://fshy.ajam.dev/api/v1/entity/xeniahosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XeniaHosting

- `compute/xeniahosting` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM | tier VPS Eco, minimum configuration (Italy)
- needs card no, phone yes, ID no, institution no | verified 2026-11-06T18:42:24.886Z (live) | stale on 2026-11-21
- url https://xeniahosting.com/en/vps/eco
- free tier: no free tier; the cheapest VPS Eco configuration in the vendor's forum post is the minimum purchasable plan of 2 vCore, 2 GB RAM, 10 GB SSD NVMe on a 25 Gbit/s port (FairUse) in Italy at EUR 2.35 with the LET15 coupon (15% off, recurring), restated by the vendor from an initial EUR 2.13; the Eco page prints no price | unit: none | metered on: unstated | read on: 2026-10-28 | source: [1] | note: price and shape are the vendor's own statements on a third-party forum; the first-party Eco page is a configurator with no printed price
- per-object cap: not applicable
- retention: unverified: no retention, cancellation or deletion term is stated on the pages captured
- egress: 25 Gbit/s port (FairUse) in Italy and 10G in the Netherlands; no monthly transfer quota is stated in the vendor's post; the Fair Use Policy text is unverified | metered: no | source: [1]
- identity: any-phone | detail: the registration form at billing1.xeniahosting.com/register asks for first name, last name, email, password, password confirmation and a phone number with a country prefix, all required; Google and Discord OAuth registration are also offered, and whether either skips the phone is unverified; no card, postal address or ID document is asked at registration
- interface: unknown
- limits:
  - per-ip-shaping (binding): 25 Gbit/s port (FairUse); the vendor states very small configurations may not saturate it because the CPU becomes the bottleneck [1]
- limits note: the Eco tier has shared network and cores; the minimum purchasable plan is 2 vCore, 2 GB RAM and 10 GB disk
- binding note: the shared FairUse port is the only ceiling stated; no byte quota is stated
- interface detail: unverified: the access method is not described on the pages captured
- tooling: unverified: no control panel or API is described on the pages captured; the Eco page lists Ubuntu, CentOS, AlmaLinux, Fedora, OpenSuse and Windows Server images
- composes with: Italian or Dutch shared-core VPS from EUR 2.35 with a 25 Gbit/s port in Italy, payable by crypto, credit card, bank transfer or PayPal.
- reliability: shared network and cores on the Eco tier; the vendor states its Italian DDoS protection is in Beta (forum post); unverified: no incident or status history captured
- notes: XeniaHosting, a hosting provider with locations in Italy and the Netherlands. The first-party Eco VPS page is a configurator and prints no price; the checkout page serves a zero price to an anonymous visitor, and the vendor states the price is visible only after creating an account and adding the service to the cart. The price in the free-tier statement is the vendor's own figure from its LowEndTalk offer thread.
- evidence note: the plan, its price and the payment methods are the vendor's statements in a LowEndTalk offer thread, not on the vendor site; the Eco page and the checkout page print no price to an anonymous visitor, and the vendor states the price is visible only after creating an account; the post date is not shown in the capture; the vendor restated the first plan's price from EUR 2.13 to EUR 2.35 in a reply; the billing term and the registration form are first-party
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.ram_unit_as_printed: GB
  - shape.disk_gb: 10
  - shape.disk_type: SSD NVMe M.2
  - billing_model: monthly
  - term: monthly
  - price_eur: 2.35
  - price_eur_posted_first: 2.13
  - price_usd_stated: 2.78
  - coupon: LET15, 15% off, recurring
  - port: 25 Gbit/s (FairUse) in Italy; 10G in the Netherlands
  - traffic: unverified: no monthly quota stated
  - location: Italy (cheapest plan); the Netherlands is also offered
  - payment_methods_reported: crypto; credit card; bank transfer; PayPal
  - order_fee_reported_eur: 0.44
  - signup.url: https://billing1.xeniahosting.com/register
  - signup.form_fields: first name, last name, email, password, password confirmation and phone number with a country prefix, all required; Google and Discord OAuth registration are also offered
  - signup.source_url: https://billing1.xeniahosting.com/register
  - signup.read_on: 2026-11-06
- evidence:
  - [1] 2026-10-28: reported: the vendor states the minimum purchasable plan is 2 vCore, 2 GB RAM and 10 GB disk | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: The above plan is below the minimum amount of resources that can be purchased (2 vCore, 2GB RAM and 10GB Disk).
  - [1] 2026-10-28: reported: the vendor restated the first plan's price as 2.35 euro (2.78 dollar) | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: We are sorry, but in the first plan the price is wrong. The right price is: 2.35€ (2.78$)
  - [1] 2026-10-28: reported: the posted prices already include the 15% LET15 coupon and the discount is recurring | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: ² The discount is already applied to the price and is recurring.
  - [1] 2026-10-28: reported: the example VPS Eco configuration is located in Italy | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: Location:** Italy
  - [1] 2026-10-28: reported: the plans carry a 25 Gbit/s port under fair use | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: 25Gbit/s Port (FairUse)¹
  - [1] 2026-10-28: reported: the Netherlands location has 10G connectivity and Italy has 25G, included with all services | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: In the Netherlands, we offer 10G connectivity included with all services, while in Italy, we offer 25G connectivity with all services.
  - [1] 2026-10-28: reported: on very small configurations the CPU can keep the port from reaching 25 Gbit/s | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: On very small configurations (e.g. 1 core / 1GB RAM) the CPU can become a bottleneck by not ensuring the correct network speed, so you may not be able to saturate the 25Gbps.
  - [1] 2026-10-28: reported: the vendor accepts crypto, credit card, bank transfer and PayPal | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: Crypto, Credit Card, Bank Transfer, PayPal.
  - [1] 2026-10-28: reported: the vendor states an order management fee is created per payment gateway | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: The order management expenses are fees created based of payment gateway.
  - [1] 2026-10-28: reported: a customer saw an order management expense of 0.44 euro on the bill | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: Spese gestione ordine / Order management expenses €0,44 EUR
  - [1] 2026-10-28: reported: the Italian DDoS protection was in Beta | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: The protection is currently in Beta.
  - [2] 2026-10-28: the Eco VPS tier runs on AMD Epyc 7663 or dual Intel Platinum 8173M hosts with NVMe storage and shared network and cores | capture: sha256:f6f6db73ea42fde67ce13bf8df0466afdb4bbf4db1c09b9a4cb1a136b055aa4c | quote: - AMD Epyc 7663 / Dual Intel Platinum 8173M - RAM DDR4 ECC UnBuffered - SSD NVMe M.2 - Rete & core condivisi
  - [2] 2026-10-28: the Eco page lists Ubuntu, CentOS, AlmaLinux, Fedora, OpenSuse and Windows Server images | capture: sha256:f6f6db73ea42fde67ce13bf8df0466afdb4bbf4db1c09b9a4cb1a136b055aa4c | quote: Ubuntu CentOS AlmaLinux Fedora OpenSuse Windows Server
  - [2] 2026-10-28: the company has locations in Italy and the Netherlands | capture: sha256:f6f6db73ea42fde67ce13bf8df0466afdb4bbf4db1c09b9a4cb1a136b055aa4c | quote: XeniaHosting is a Hosting Provider, with locations in Italy and Netherlands.
  - [3] 2026-10-28: the registration URL returned a 404 page, so the signup form is unverified | capture: sha256:ca940cb4e4306e94eb3800011db0dd62ee2389f0f675b8b5ad519cfbce74aa0b | quote: Spiacenti, la pagina che stai cercando non è stata trovata.
  - [4] 2026-11-06: the checkout page labels the VPS Eco IT plan Monthly, so the billing term is monthly | capture: sha256:6eddc8b1aafec8d35dacc9caf46644e74846601942823aaca62e00a77021d2b5 | quote: VPS Eco IT · Monthly
  - [5] 2026-11-06: the registration form marks the phone number as a required field | capture: sha256:34174d03a7cb85fc9216d8b2a67fa3fc3661bba362e4e8ff27e053f56f9cb4c8 | quote: Telefono *
  - [1] 2026-11-06: the vendor restates the first plan's price as EUR 2.35 | capture: sha256:b6c97b38da4a0456dff5ea5a5c4bf285e993e3c4d185345f66ca389c952ac9a1 | quote: We are sorry, but in the first plan the price is wrong. The right price is: 2.35€ (2.78$)
  - [4] 2026-11-06: the checkout page serves a zero price to an anonymous visitor | capture: sha256:6eddc8b1aafec8d35dacc9caf46644e74846601942823aaca62e00a77021d2b5 | quote: €0,00 EUR
  - [6] 2026-11-06: the catalog endpoint the Eco configurator reads returns null per-unit prices, so the configurator cannot print a price | capture: sha256:5f7cef962811a16f848b6ee8c5aa71be209a1cb105f5cdd530ba30a9e4aad11d | quote: "price_vcore":null
  - [7] 2026-11-06: the vendor states the price is visible only after creating an account and adding the service to the cart | capture: sha256:10c6bdece7e110eb1781b778e9cf3fc25701f55f04af888c58a0e064752bccdc | quote: The price in dollars on the site is visible by creating an account and adding the service to the cart.
- sources:
  - [1] https://lowendtalk.com/discussion/214191/xeniahosting-com-high-performance-it-nl-vps-up-to-25g-it
  - [2] https://xeniahosting.com/en/vps/eco
  - [3] https://billing.xeniahosting.com/register.php
  - [4] https://billing1.xeniahosting.com/products/vps-eco/vps-eco-it
  - [5] https://billing1.xeniahosting.com/register
  - [6] https://xeniahosting.com/api/catalog/services?gid=23
  - [7] https://lowendtalk.com/discussion/214191/xeniahosting-com-high-performance-it-nl-vps-up-to-25g-it/p2
