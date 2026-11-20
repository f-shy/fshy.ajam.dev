# Velohost

> velohost.de | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/velohost/ | JSON https://fshy.ajam.dev/api/v1/entity/velohost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Velohost (Compute)

- `compute/velohost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://velohost.de/
- free tier: EUR 2.60/month for KVM-XS in Velbert, Germany, after coupon LEB35: 4 GB RAM, 1 vCPU, 25 GB disk, 1 TB traffic, 2x 10 Gbit shared uplink, 1 IPv4 and a /64 IPv6, EUR 26.00/year on the annual term after the same coupon. The post's table prices KVM-M at EUR 9.10/month for 12 GB, 4 vCPU and 75 GB, KVM-L at EUR 11.70 for 18 GB, 6 vCPU and 100 GB, and KVM-XXL at EUR 22.75 for 32 GB, 10 vCPU and 250 GB, all with 1 TB traffic. Every figure in the table is a post-coupon figure; the pre-coupon list price is not printed. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on every plan in the offer table; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 1 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 TB a month on every plan in the table, including the 32 GB one, so the byte allowance binds long before the 2x 10 Gbit shared uplink does. No overage price and no post-allowance throttle are stated on either page read, and the post does not say whether the counter resets monthly or on the billing period. [1]
- limits note: 1 TB a month on every plan in the table, including the 32 GB one, so the byte allowance binds long before the 2x 10 Gbit shared uplink does. No overage price and no post-allowance throttle are stated on either page read, and the post does not say whether the counter resets monthly or on the billing period.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor runs a looking glass at lg.velohost.de with a 50 MB test file; no API or CLI is documented on the page read
- composes with: EUR 2.60/month for 4 GB and 25 GB with 1 TB of transfer is the cheapest 4 GB row among documented hosts and the only one whose vendor says it owns its hardware and added a second German site; 1 TB a month is the reason it is a worker and not a mover, and the coupon is what makes the price, so the record is only valid while LEB35 stands
- reliability: no reliability event recorded
- notes: Every price is post-coupon and the post prints no list price, so the pre-coupon rate and the renewal rate are both unverified: the post says 'Use promo code LEB35 to get 35% off all KVM plans starting from KVM-XS' and does not say whether the code is recurring or first-term only. Unverified: the KVM page at velohost.de/kvm-ipv4.php, which the homepage links and which this category did not fetch, and whether LEB35 survives renewal. The euro sign was dropped by the text extractor on the post table, so the currency is taken from the post's title line rather than from the garbled glyph.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 25
- evidence:
  - [2] 2026-10-22: third-party offer post, published 2026-10-13, quoted from its table: 'KVM-XS 4GB RAM 1x vCPU 25GB disk 1 TB Traffic 2x 10 Gbit (Shared) 1x IPv4/64 IPv6 Coupon: LEB35 2,60 EUR/month (after promo code) 26,00 EUR/year (after promo code)'; the three larger rows carry the same '1 TB Traffic'; host nodes are '1x AMD EPYC 7C13' and '2x AMD EPYC 7402P' with '512 GB RAM' and '2x 4TB NVMe-SSD'
  - [1] 2026-10-22: the vendor homepage was read and carries no KVM plan table or price at all: it shows a German navigation page with a KVM product link to velohost.de/kvm-ipv4.php and a domain search form, so no figure on this record could be corroborated first-party
- sources:
  - [1] https://velohost.de/
  - [2] https://lowendbox.com/blog/velohost-returns-with-even-cheaper-prices-get-a-4gb-vps-for-only-2-60e-month/

## Velohost (KVM-XS)

- `egress/velohost-kvm-xs` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Germany, KVM, IPv4 and IPv6) | tier KVM-XS
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://velohost.de/
- price EUR 2.60 per month (after promo code LEB35) with 1 TB per month included
- free tier: No free plan. KVM-XS is 4 GB RAM, 1 vCPU, 25 GB disk and 1 TB traffic at EUR 2.60 a month or EUR 26.00 a year after the promo code LEB35 (35 percent off); the post prints no list price. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1 TB per month is the reference value of the terms where no other volume is agreed; the terms reserve EUR 5.00 per started extra TB, and temporary suspension on excessive use of the agreed or fair-use traffic | metered: yes | free allowance: 1 TB per month on every KVM plan in the offer post, paid, no free tier | price per TB: EUR 5.00 per started terabyte over 1 TB, at the vendor's discretion | source: [1]
- identity: email | detail: unverified: the registration page renders no form fields; the offer post lists PayPal, credit cards, bank transfers and crypto as payment methods, and no card, phone or ID requirement is stated on a page read
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB per month, then EUR 5.00 per started extra terabyte or a temporary suspension at the provider's choice [1]
  - per-ip-shaping: outbound TCP ports 25, 465 and 587 are blocked by default and opened only after a review in the individual case [1]
- binding note: 1 TB per month is the only byte ceiling and the terms put a price (EUR 5.00 per started TB) and a suspension right on exceeding it.
- interface detail: a KVM guest with full root access, ordered through the provider's WHMCS store
- tooling: any SSH client; the provider's client area
- composes with: a plain KVM guest with one IPv4 address and a /64 IPv6 subnet on a shared 2x 10 Gbit uplink; outbound TCP 25, 465 and 587 are blocked by default and every other port is not stated as filtered
- reliability: no reliability event recorded
- notes: Not free. The cheapest KVM plan is EUR 2.60 a month after the promo code; the vendor's terms give 1 TB a month as the reference allowance and EUR 5.00 per started extra TB.
- evidence note: The traffic rule and the blocked mail ports are first-party terms; the plan table and the price come from a third-party offer post and are post-coupon figures. Inbound ports and UDP are not stated.
- extras:
  - nat: not stated; the plan lists one IPv4 address and a /64 IPv6 subnet
  - ipv6: a /64 IPv6 subnet is listed on every KVM plan
  - inbound: not stated beyond the default block on outbound TCP 25, 465 and 587
  - udp: not stated; a KVM guest with root
  - volume_stated: 1 TB Traffic
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own IPv4 or IPv6 address on the provider's network
- evidence:
  - [2] 2026-11-04: the 4 GB plan has 25 GB of disk and 1 TB of bandwidth | capture: sha256:3218b25cbb978f8a7b1d398f75680e85db0200f147d4ff568313a99c169c446c | quote: Eight months ago, they were selling a 4GB VPS with 25GB of disk and 1TB of bandwidth for 3.00€/month.
  - [2] 2026-11-04: the same package is now 2.60 EUR a month | capture: sha256:3218b25cbb978f8a7b1d398f75680e85db0200f147d4ff568313a99c169c446c | quote: Now they’re selling that same package for only 2.60€/month!
  - [2] 2026-11-04: the price rests on the promo code LEB35 | capture: sha256:3218b25cbb978f8a7b1d398f75680e85db0200f147d4ff568313a99c169c446c | quote: Use promo code LEB35 to get 35% off all KVM plans starting from KVM-XS.
  - [2] 2026-11-04: the KVM-XS row lists 1 TB traffic, a shared 2x 10 Gbit uplink and one IPv4 plus a /64 IPv6 | capture: sha256:3218b25cbb978f8a7b1d398f75680e85db0200f147d4ff568313a99c169c446c | quote: 4GB RAM1x vCPU25GB disk1 TB Traffic2x 10 Gbit (Shared)1x IPv4/64 IPv6
  - [2] 2026-11-04: payment methods include crypto and bank transfer | capture: sha256:3218b25cbb978f8a7b1d398f75680e85db0200f147d4ff568313a99c169c446c | quote: They accept PayPal, credit cards, bank transfers, and crypto.
  - [1] 2026-11-04: where no other volume is agreed, 1 TB per month is the fair-use reference | capture: sha256:fcdeb2fb48537aa02f8c63a785eafe6e92c982b50af49b9333a9f02d0e32f415 | quote: Ist nichts anderes vereinbart, gilt ein Richtwert von 1 Terabyte pro Monat im Rahmen einer „Fair Use“-Regelung als zulässig.
  - [1] 2026-11-04: exceeding 1 TB can be billed at 5.00 EUR per started terabyte | capture: sha256:fcdeb2fb48537aa02f8c63a785eafe6e92c982b50af49b9333a9f02d0e32f415 | quote: Sollte das Limit von 1 Terabyte pro Monat überschritten werden, behalten wir uns vor, pro angefangenen Terabyte Extraverbrauch 5,00€ zu berechnen.
  - [1] 2026-11-04: outbound TCP 25, 465 and 587 are blocked by default | capture: sha256:fcdeb2fb48537aa02f8c63a785eafe6e92c982b50af49b9333a9f02d0e32f415 | quote: Dies betrifft insbesondere die TCP-Ports 25, 465 und 587, welche üblicherweise für den Versand von E-Mails über SMTP verwendet werden.
  - [3] 2026-11-04: the registration page shows no form fields beyond the account heading | capture: sha256:12cc996a5e18c3d04f192b6b282007c8af4dcc60618ded6f2fa23c8d01d43fa3 | quote: Erstelle einen Velohost-Account.
- sources:
  - [1] https://velohost.de/tos.php
  - [2] https://lowendbox.com/blog/velohost-returns-with-even-cheaper-prices-get-a-4gb-vps-for-only-2-60e-month/
  - [3] https://velohost.de/register.php
