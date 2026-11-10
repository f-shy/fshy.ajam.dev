# AffordableBytes

> affordablebytes.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/affordablebytes/ | JSON https://fshy.ajam.dev/api/v1/entity/affordablebytes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AffordableBytes (Compute)

- `compute/affordablebytes` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-12-08
- url https://affordablebytes.com/
- price parsed USD 3.93/mo
- free tier: EUR 3.49 per month for the Xeon Gold 6150 entry plan in Frankfurt: 1 vCore, 6 GB DDR4, 45 GB RAID 1 NVMe, 5 TB traffic, 1 Gbit uplink, 1 IPv4 plus a /64 IPv6, AS203446 DDoS protection; the ladder above it is EUR 7.99 (4 vCore, 11 GB, 100 GB, 15 TB), EUR 14.99 (6 vCore, 22 GB, 200 GB, 25 TB) and EUR 24.99 (8 vCore, 40 GB, 150 GB, 40 TB). The cart rents by a 30-day unit on a runtime slider of 30 to 360 days paid upfront at the same monthly rate, the renewal amount row is filled with the same computed price as due today, and no annual price is published. One exception: the 22 GB plan's cart prices EUR 15.99 against the marketing page's EUR 14.99. Every cart visited renders a 'Sold out' banner above a checkout that still prices the plan, so whether a plan can actually be provisioned is unverified: the banner's subject is not printed. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month on the entry plan; the S3 line adds 10 TB of egress included per TB of storage bought. No overage price and no post-allowance throttle stated | metered: yes | free allowance: 5 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest, cli, s3-compatible
- limits:
  - volume-quota (binding): 5 TB a month on the 6 GB plan, 15 TB on the 11 GB, 25 TB on the 22 GB and 40 TB on the 40 GB, each stated per plan. The allowance is the wall before the 1 Gbit uplink is: 5 TB a month averages well under 1 Gbit, so the counter binds first. No overage price and no post-allowance throttle are stated on either page read. [1]
- limits note: 5 TB a month on the 6 GB plan, 15 TB on the 11 GB, 25 TB on the 22 GB and 40 TB on the 40 GB, each stated per plan. The allowance is the wall before the 1 Gbit uplink is: 5 TB a month averages well under 1 Gbit, so the counter binds first. No overage price and no post-allowance throttle are stated on either page read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor advertises its own control panel and published node statistics; no API or CLI is documented on the page read
- composes with: EUR 3.49 for 6 GB and 45 GB with 5 TB is the lowest cost per gigabyte of RAM among evaluated providers by a wide margin, which is what makes it a candidate for a memory-resident index or a build worker rather than for moving bytes; the same vendor's S3 line at EUR 4.95 per TB per month with 10 TB of egress per TB is the paired answer when the same bytes have to be stored as well as processed.
- reliability: no reliability event recorded
- notes: The two pages agree on the 6 GB and 11 GB rows and disagree on two others: the post prices the 22 GB plan at EUR 15.99 while the vendor page prints EUR 14.99, and the post gives the 40 GB plan 20 TB of traffic while the vendor page gives it 40 TB. The vendor page is the later and the first-party of the two, so the record takes its numbers; the disagreement itself is recorded here because it means the offer post is not a reliable copy of the plan table. The euro sign was dropped by the text extractor on the post, so the currency is taken from the vendor page rather than from the garbled glyph.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 6
  - facets.shape.disk_gib: 45
  - price_on_page: EUR 3.49/month for the Xeon Gold 6150 entry plan (6 GB)
- evidence:
  - [1] 2026-10-22: vendor plan block quoted: 'Xeon Gold 6150', 'EUR 3.49 / month', '1 vCore', '6 GB DDR4 Memory', '45 GB RAID 1 NVMe Storage', '5 TB Bandwidth', '1x IPv4 Address', '1x /64 IPv6 Subnet', '1 Gbit Uplink', 'AS203446 DDoS Protection'; the next rows print 'EUR 7.99 / month' with '11 GB' and '15 TB Bandwidth', and 'EUR 24.99 / month' with '40 GB' and '40 TB Bandwidth'
  - [2] 2026-10-22: third-party offer post, published 2026-10-08: 'Xeon Gold | 6GB ... 1x vCore - Xeon Gold 6150 ... 6 GB DDR4 Memory ... 45 GB RAID 1 NVMe Storage ... 5 TB Traffic ... 1 Gbit Uplink ... EUR 3.49 / month'; body text: 'And service renews at the same price!'; the post prints 'EUR 15.99 / month' for the 22 GB plan and '20 TB Traffic' for the 40 GB plan
  - [1] 2026-11-07: the marketing page prices the entry plan at EUR 3.49 per month and prints the full plan ladder | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: € 3.49 / month
  - [3] 2026-11-07: the cart prices the 22 GB plan at EUR 15.99 renewal and due today, above the marketing page's EUR 14.99 | capture: sha256:938290f5259d4df76955785892bcd7da5ae824f4298eb4f21fe56946aac54ab4 | quote: Renewal amount (30 Days) 15.99 €
  - [1] 2026-11-07: the marketing page's plan cards print 5 TB Bandwidth on the entry plan and the EUR 3.49 / 7.99 / 14.99 / 24.99 monthly prices | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: 5 TB Bandwidth
  - [4] 2026-11-07: account creation at the order flow asks a username, an e-mail and a password, with a 2FA code field on sign-in; no phone or card is asked before payment | capture: sha256:85b8be5b31dfe94d57ebfbf51e3b1f6f3cd05cdc4a50204c9edb3f17ca0fb978 | quote: Username E-Mail Password
  - [4] 2026-11-07: the 6 GB plan's own cart prices its base configuration at EUR 3.49 and rents by a 30-day unit | capture: sha256:1f7938afcf5dd0b38c9c53136ea33292bc7b78ed2528eb6bb6bffa445dadc4f6 | quote: var basePrice = 3.49;
  - [3] 2026-11-07: the 22 GB plan's own cart prices its base configuration at EUR 15.99 against the marketing page's EUR 14.99 | capture: sha256:e89a199bc03977b1e4d998ba5b721eeca780dbe1b7caa9156ee732d2e2874361 | quote: var basePrice = 15.99;
  - [1] 2026-11-07: the marketing page's plan cards still print the 5 TB allowance and the EUR 3.49 / 7.99 / 14.99 / 24.99 ladder | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: 5 TB Bandwidth
  - [1] 2026-11-07: the vendor's own marketing page prices the entry plan at EUR 3.49 a month | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: € 3.49 / month
- sources:
  - [1] https://affordablebytes.com/
  - [2] https://lowendbox.com/blog/high-ram-low-prices-must-be-an-affordablebytes-offer-get-a-6gb-vps-for-only-e3-49-month/
  - [3] https://panel.affordablebytes.com/order/config/2/40a23cee-c4c2-4775-beb9-190bf97c95ce/2
  - [4] https://panel.affordablebytes.com/order/config/2/74dc787e-f807-4efa-addc-16582b71a58e/2

## AffordableBytes (Xeon Gold 6 GB)

- `egress/affordablebytes-xeon-gold-6gb` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Frankfurt, KVM, IPv4 and IPv6) | tier Xeon Gold 6 GB
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://affordablebytes.com/
- price EUR 3.49 per month with 5 TB per month included | parsed USD 0.7864/TB-mo
- free tier: No free plan and no free trial. The entry plan is EUR 3.49 a month: 1 vCore, 6 GB DDR4, 45 GB RAID 1 NVMe, 5 TB bandwidth, 1 Gbit uplink, one IPv4 and a /64 IPv6 subnet. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 5 TB bandwidth per month on the 6 GB plan, 15, 25 and 40 TB on the larger ones, on a 1 Gbit uplink; behaviour past the quota is not stated on the pages read; SMTP is blocked by default and unblocked on a ticket | metered: yes | free allowance: 5 TB per month on the entry plan, paid, no free tier | source: [1]
- identity: email | detail: unverified: the order panel could not be read; the FAQ lists PayPal, Stripe and cryptocurrency as payment methods and a 48-hour money-back guarantee, and no card, phone or ID requirement is stated on a page read
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB per month on the 6 GB plan [1]
  - per-ip-shaping: SMTP is blocked by default and unblocked on a ticket; 1 Gbit uplink [1]
- binding note: 5 TB per month is the only published byte ceiling and no overage price or throttle is stated.
- interface detail: a KVM guest in Frankfurt on a custom panel
- tooling: any SSH client; the provider's own panel and ticket system
- composes with: a KVM guest with one IPv4 address and a /64 IPv6 subnet on a 1 Gbit uplink; SMTP is blocked by default and unblocked on a ticket, and no other port policy is stated
- reliability: no reliability event recorded
- notes: Not free. A 6 GB KVM plan in Frankfurt on a 1 Gbit uplink with 5 TB a month included; the vendor also sells S3-compatible storage under a separate offer.
- evidence note: Bandwidth, price and the SMTP rule are on the vendor's own page; the offer post agrees on the entry plan and prices larger plans differently.
- extras:
  - nat: not stated; the plan lists one IPv4 address and a /64 IPv6 subnet
  - ipv6: a /64 IPv6 subnet on every plan
  - inbound: not stated beyond the default SMTP block
  - udp: not stated; a KVM guest
  - volume_stated: 5 TB Bandwidth
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own address on the provider's network
- evidence:
  - [1] 2026-11-04: the entry plan lists 5 TB bandwidth | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: 5 TB Bandwidth
  - [1] 2026-11-04: the entry plan is EUR 3.49 a month | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: € 3.49
  - [1] 2026-11-04: SMTP is blocked by default and unblocked on a ticket | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: SMTP are blocked by default to prevent abuse, but can be unblocked by opening a simple ticket and explaining your use-case.
  - [1] 2026-11-04: payment methods include crypto | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: We offer different payment options for your convenience. You can choose to pay through PayPal, Stripe, or Cryptocurrency.
  - [1] 2026-11-04: no free trial is offered | capture: sha256:7e9ff7203e37594881ec63b618f671491f58a4ad4a059114de5e74b4d19a54e5 | quote: We don't provide free trials or discounts as our services are already fairly priced and we offer a 48-hour money-back guarantee.
  - [2] 2026-11-04: the post states the plan renews at the same price | capture: sha256:ee08c31881722c9016ff48044a4648121ce901b529fff4d82a7027ce412bf209 | quote: And service renews at the same price!
- sources:
  - [1] https://affordablebytes.com/
  - [2] https://lowendbox.com/blog/high-ram-low-prices-must-be-an-affordablebytes-offer-get-a-6gb-vps-for-only-e3-49-month/
