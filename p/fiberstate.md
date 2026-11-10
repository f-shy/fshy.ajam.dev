# FiberState

> fiberstate.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fiberstate/ | JSON https://fshy.ajam.dev/api/v1/entity/fiberstate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FiberState

- `compute/fiberstate` | paid-only | evidence documented | binding per-ip-shaping | category dedicated server | tier Intel Xeon E3-1240 v5, Instant Deploy
- needs card yes, phone yes, ID no, institution no | verified 2026-11-06T18:37:34.812Z (live) | stale on 2026-12-07
- url https://www.fiberstate.com/
- price parsed USD 49.95/mo
- free tier: no free tier; the cheapest listed server is USD 49.95/mo: Intel Xeon E3-1240 v5, 4 cores / 8 threads, 32 GB RAM, 1 TB NVMe, 1 Gbps port with unlimited transfer, Instant Deploy (online 5 to 10 minutes after order verification) | unit: none | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: bare metal, not a virtual machine; billed in advance and renewed automatically
- per-object cap: not applicable
- retention: billed in advance and renewed automatically each period until cancelled; after cancellation the hardware may be returned to inventory and all associated data permanently erased | source: [2]
- egress: 1 Gbps port with transfer listed as Unlimited on the entry server | metered: no | free allowance: unlimited transfer at 1 Gbps (entry server) | source: [1]
- identity: card | detail: an account is required at order: the registration form asks for first name, last name, email, street address, city, state, postcode and password, and carries a phone number field that is not marked required; no card field at registration, and payment is required at order; identity, payment, business or fraud verification may be required before or after activation, and orders go through fraud screening and payment verification; unverified: the accepted payment methods
- interface: unknown
- limits:
  - per-ip-shaping (binding): 1 Gbps port; transfer listed as Unlimited on the entry server; usage over the purchased allocation may be rate-limited or suspended [2]
- limits note: no limit beyond the 1 Gbps port is stated for the USD 49.95 row; the row sits in the Salt Lake City panel of the price page
- binding note: the 1 Gbps port is the only ceiling stated for the entry server; transfer is listed as Unlimited
- interface detail: IPMI access (reboot, install, console) is listed as included with every server; operating-system access and any API are unverified, not stated on the pages captured
- tooling: IPMI for reboot, install and console; a customer portal for service pages, credentials and cancellation
- composes with: Dedicated 4-core Xeon with 32 GB, 1 TB NVMe and a 1 Gbps unlimited-transfer port at USD 49.95 a month, delivered in minutes after order verification.
- reliability: after cancellation the hardware may be reclaimed and all data erased without further notice; usage over the purchased bandwidth allocation may be rate-limited or suspended; unverified: no incident or status history captured
- notes: Only dedicated servers and colocation appear in the billing store's category list (Customizable Dedicated Servers - SLC, UT; Instant Deploy Dedicated Servers - SLC, UT; Dedicated Servers - LA, CA; Dedicated Servers - NY, NY; Dedicated Servers - CHI, IL; Colocation - SLC, UT); no VPS product is listed.
- evidence note: the server row, its price, its network and its Salt Lake City location are read from the first-party site and quoted; the registration form is read and quoted; the accepted payment methods are unverified, and a live order would move the rung to measured
- extras:
  - shape.vcpu: 8
  - shape.vcpu_basis: 8 hardware threads on 4 physical cores
  - shape.cores: 4
  - shape.threads: 8
  - shape.ram_gib: 32
  - shape.ram_unit_as_printed: GB
  - shape.disk: 1 TB NVMe
  - billing_model: monthly-in-advance
  - term: monthly
  - monthly_usd: 49.95
  - port: 1 Gbps
  - traffic: Unlimited
  - location: Salt Lake City, Utah (SLC): the Instant Deploy group sits in the Salt Lake City panel of the price page and its order link reads 'Intel Xeon E3-1240 v5 in Salt Lake City'
  - ipv4_included: yes
  - ipv6_included: available; listed as IPv6 availability, not as included
  - stock: out of stock: the price page marks this row Out of stock on 2026-11-06, and orders are suspended until more stock is available; the storage server row on the same page reads '4 in stock', so the marker is per product
  - deploy_time: online 5 to 10 minutes after order verification
- evidence:
  - [1] 2026-10-28: the cheapest listed server is the Intel Xeon E3-1240 v5, 4 cores / 8 threads, 32 GB, 1 TB NVMe, 1 Gbps unlimited, USD 49.95 a month | capture: sha256:778aabaecfd6766f27f340829ada35b4ebf2222111c7e8cd034b5bebe81dfbf9 | quote: | Intel Xeon E3-1240 v54 Cores / 8 Threads | 32 GB | 1 TB NVMe | 1 Gbps · Unlimited | $49.95/mo | Order |
  - [1] 2026-10-28: the Instant Deploy section is online 5 to 10 minutes after order verification | capture: sha256:778aabaecfd6766f27f340829ada35b4ebf2222111c7e8cd034b5bebe81dfbf9 | quote: Instant DeployOnline 5 to 10 minutes after order verification
  - [1] 2026-10-28: the Custom Deploy section is provisioned within 24 to 48 hours | capture: sha256:778aabaecfd6766f27f340829ada35b4ebf2222111c7e8cd034b5bebe81dfbf9 | quote: Custom DeployProvisioned within 24 to 48 hours
  - [2] 2026-10-28: configuration, IP assignments, credentials and access details are delivered through a service page in the customer portal | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: Service configurations, IP assignments, credentials, hardware information, and access details will be provided through the applicable Service page in the customer portal.
  - [1] 2026-10-28: every server includes DDoS protection, a dedicated IPv4 address, IPv6 availability and IPMI access | capture: sha256:778aabaecfd6766f27f340829ada35b4ebf2222111c7e8cd034b5bebe81dfbf9 | quote: Every server includes DDoS Protection, a dedicated IPv4 address, IPv6 availability, IPMI access (reboot, install, console), and upgradeable configuration options.
  - [3] 2026-10-28: the price list is headed as dedicated servers; no VPS section appears on the page | capture: sha256:fbaf4f8043b4a376155e09f6a970e9dd783719cac7dd0ac41706d222d4f88ef9 | quote: #### Our Dedicated Servers
  - [2] 2026-10-28: identity, payment, business or fraud verification may be required before or after activation | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: You must provide accurate and current account, identity, billing, and contact information. FiberState may require identity, payment, business, or fraud verification before or after activating Services.
  - [2] 2026-10-28: orders are subject to fraud screening and payment verification | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: All orders are subject to acceptance, availability, fraud screening, and payment verification.
  - [2] 2026-10-28: activation can wait on verification and payment requirements | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: FiberState may delay activation until all requested verification and payment requirements have been completed.
  - [2] 2026-10-28: services are billed in advance | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: Services are billed in advance.
  - [2] 2026-10-28: recurring services renew automatically for periods of the same length | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: Recurring Services automatically renew for successive billing periods of the same length unless canceled in accordance with Section 4.
  - [2] 2026-10-28: after cancellation the hardware may be returned to inventory and all data permanently erased | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: After cancellation, dedicated hardware may be returned to inventory, and all associated data may be permanently erased without further notice.
  - [2] 2026-10-28: usage over the purchased allocation may be rate-limited or suspended | capture: sha256:50e7fbffa2bd3c6111ffcb5c2c2d8cc0892865c6a27521a53986920cb7d557b5 | quote: If usage exceeds the purchased allocation, FiberState may limit or rate-limit the Service, suspend it, or require the customer to upgrade to a higher-bandwidth plan.
  - [3] 2026-11-06: the order link of the USD 49.95 Instant Deploy server names Salt Lake City as its location | capture: sha256:a961b1e44c130d8cc1479ff2553b5aacb7d95591226f62b3ad1cadb5a7321bc9 | quote: Intel Xeon E3-1240 v5 in Salt Lake City
  - [3] 2026-11-06: the price table that holds the USD 49.95 row is the Salt Lake City table | capture: sha256:a961b1e44c130d8cc1479ff2553b5aacb7d95591226f62b3ad1cadb5a7321bc9 | quote: Dedicated servers in Salt Lake City
  - [4] 2026-11-06: the billing store lists six product categories, all dedicated servers or colocation, and no VPS category | capture: sha256:99e9e9bbff93941defc69b5405103555efb7e1d56642f3f5f568888da60c82f8 | quote: Customizable Dedicated Servers - SLC, UT Instant Deploy Dedicated Servers - SLC, UT Dedicated Servers - LA, CA Dedicated Servers - NY, NY Dedicated Servers - CHI, IL Colocation - SLC, UT
  - [3] 2026-11-06: the location of the row is read from the page, not inferred | capture: sha256:a961b1e44c130d8cc1479ff2553b5aacb7d95591226f62b3ad1cadb5a7321bc9 | quote: Intel Xeon E3-1240 v5 in Salt Lake City
  - [5] 2026-11-06: the registration form carries a phone number field that is not marked required | capture: sha256:648891d03821103f1c79a48983366eefbfa604bd35b1ac68dffc8a92ef281cd0 | quote: type="tel" name="phonenumber" id="inputPhone" class="form-control" placeholder="Phone Number" value="" autocomplete="off"
  - [3] 2026-11-06: the price page marks the USD 49.95 Instant Deploy row Out of stock, while the storage server row on the same page reads 4 in stock | capture: sha256:a961b1e44c130d8cc1479ff2553b5aacb7d95591226f62b3ad1cadb5a7321bc9 | quote: Out of stock<span class="sr-only"> Intel Xeon E3-1240 v5 in Salt Lake City</span>
  - [6] 2026-11-06: the order page of the USD 49.95 Instant Deploy server suspends orders while it is out of stock | capture: sha256:3778bf90f5404f107341a1992b05fc1dc24a37b5ec4d37312dbe4b4c07d7de0c | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available.
  - [7] 2026-11-06: the billing store's Instant Deploy category is titled Salt Lake City, Utah | capture: sha256:4445f9e1292b250219b6c2eca9b06451f82502e1948d3ff81cc44d6b9476a018 | quote: Instant Deploy Dedicated Servers - SLC, UT
  - [7] 2026-11-06: the Intel Xeon E3-1240 V5 is listed in the Instant Deploy category | capture: sha256:4445f9e1292b250219b6c2eca9b06451f82502e1948d3ff81cc44d6b9476a018 | quote: Intel Xeon E3-1240 V5 @ 3.5 Ghz (4 Cores/8 Threads)
  - [3] 2026-11-06: the USD 49.95 price of the Instant Deploy row is unchanged on the price page | capture: sha256:a961b1e44c130d8cc1479ff2553b5aacb7d95591226f62b3ad1cadb5a7321bc9 | quote: <span class="price">$49.95</span>
  - [8] 2026-10-28: FiberState lists data centers in Salt Lake City, Chicago, Los Angeles and New York | capture: sha256:c5238c5488ad1333d74447dcb46756731ca2228cc8a92eef1b0fe516955f947d | quote: FiberState data centers anchor a high-resilience IP backbone across Salt Lake City, Chicago, Los Angeles, and New York.
- sources:
  - [1] https://www.fiberstate.com/
  - [2] https://www.fiberstate.com/terms-of-service
  - [3] https://www.fiberstate.com/dedicated-servers
  - [4] https://billing.fiberstate.com/index.php?rp=/store
  - [5] https://billing.fiberstate.com/register.php
  - [6] https://billing.fiberstate.com/index.php?rp=/store/instant-deploy/intel-xeon-e3-1240-v5
  - [7] https://billing.fiberstate.com/index.php?rp=/store/instant-deploy
  - [8] https://www.fiberstate.com/datacenters
