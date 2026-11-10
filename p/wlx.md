# WLX

> wlx.hk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wlx/ | JSON https://fshy.ajam.dev/api/v1/entity/wlx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WLX

- `compute/wlx` | paid-only | evidence documented | binding volume-quota | category dedicated server | tier AMD Ryzen 9 5950X
- needs card yes, phone no, ID no, institution no | verified 2026-10-28T04:25:21.504Z (live) | stale on 2026-11-28
- url https://wlx.hk/
- price parsed USD 199/mo
- free tier: No free tier. Lowest listed server is USD 199/month for AMD Ryzen 9 5950X, 16 cores / 32 threads, 128 GB RAM, 2 TB NVMe, and 20 TB at 1 Gbps in Hong Kong (status Restocking). Lowest in-stock server is Intel Core Ultra 9 285HX with RTX 4070 at USD 449/month. | unit: none | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: bare metal, not a virtual machine; no VPS product is listed on the store menu
- per-object cap: not applicable
- retention: billed in advance; cancellation must be submitted before the renewal date through the customer portal, service plan, quotation or written agreement; unverified: what happens to a cancelled server's data | source: [2]
- egress: 20 TB a month at 1 Gbps on every listed server; the vendor states traffic is counted as combined inbound plus outbound transfer; the price beyond the allowance is unverified | metered: yes | free allowance: 20 TB per month | source: [1]
- identity: card | detail: an account and payment in advance at order; the terms state that identity, business, payment, beneficial ownership, network use-case, KYC or KYB information may be required before provisioning; the vendor lists Alipay, credit or debit card, cryptocurrency and bank transfer as payment methods (forum post); unverified: the registration form fields are not extractable from the register page and whether a given order triggers KYC is not stated
- interface: unknown
- limits:
  - volume-quota (binding): 20 TB per month at 1 Gbps; counted as combined inbound and outbound transfer [1]
  - per-ip-shaping: 1 Gbps port [1]
- limits note: stock: the cheapest listed server shows Restocking; the only row with an Order button is the USD 449/mo Intel Core Ultra 9 285HX
- binding note: the 20 TB monthly allowance is the first byte ceiling; the 1 Gbps port is second
- interface detail: unverified: no console, IPMI or API is described on the pages captured
- tooling: unverified: not stated on the pages captured
- composes with: Hong Kong dedicated server with a /29 IPv4 subnet (5 usable addresses), a /48 IPv6 subnet and 20 TB a month of transfer at 1 Gbps.
- reliability: single Hong Kong site; the cheapest listed server shows Restocking; the vendor states A/B power redundancy and redundant network connectivity (forum post); in-stock servers are typically provisioned within 6 business hours on Hong Kong business days (forum post)
- notes: WLX Limited, Hong Kong, AS150670. The store menu lists dedicated servers and IP and ASN services only, so no VPS product is sold although the terms name virtual private servers in their scope. A forum promotion at USD 169/mo for the Ryzen 9 5950X ended on 2026-08-28; the storefront list price is USD 199/mo.
- evidence note: the price table, specifications and location are read from the first-party storefront and quoted; payment methods, provisioning time, the USD 169 promotion and the traffic counting rule come from the vendor's forum post and are reported; the registration form and KYC practice are unverified
- extras:
  - shape.vcpu: 32
  - shape.vcpu_basis: 32 hardware threads on 16 cores
  - shape.cores: 16
  - shape.threads: 32
  - shape.ram_gib: 128
  - shape.ram_unit_as_printed: GB
  - shape.disk: 2 TB NVMe
  - billing_model: monthly-in-advance
  - term: monthly
  - monthly_usd: 199
  - cheapest_orderable.server: Intel Core Ultra 9 285HX with RTX 4070, 192 GB, 2 x 2 TB PCIE 5.0 NVMe
  - cheapest_orderable.monthly_usd: 449
  - cheapest_orderable.delivery: 12h
  - promo_reported.monthly_usd: 169
  - promo_reported.ended: 2026-08-28
  - promo_reported.rung: reported
  - port: 1 Gbps
  - traffic: 20 TB per month
  - location: Hong Kong
  - ipv4_included: 1x /29 subnet (5 usable IPs)
  - ipv6_included: 1x /48 subnet
  - stock: Restocking on the cheapest row; Order button only on the USD 449 row
  - payment_methods_reported: Alipay; credit or debit card; cryptocurrency; bank transfer
  - signup.url: https://wlx.hk/register.php
  - signup.form_fields: unverified: the register page text holds navigation only
  - signup.source_url: https://wlx.hk/register.php
  - signup.read_on: 2026-10-28
- evidence:
  - [1] 2026-10-28: the cheapest listed server is the AMD Ryzen 9 5950X, 128 GB, 2 TB NVMe, 20 TB at 1 Gbps, USD 199 a month, shown as Restocking | capture: sha256:925ef86d56a79a92087ab75e916f52ec6b70edcd339140aa56c5554097d1e97c | quote: | AMD Ryzen 9 5950X 16 Cores / 32 Threads | 128 GB | 2 TB NVMe | 20 TB @ 1 Gbps | $199/mo Restocking | [Notify me](https://wlx.hk/public/company/quote/?service=dedicated&restock=1&cpu=5950x) |
  - [1] 2026-10-28: the only row with an Order button is the Intel Core Ultra 9 285HX with RTX 4070, 192 GB, 2 x 2 TB NVMe, USD 449 a month, delivery in 12h | capture: sha256:925ef86d56a79a92087ab75e916f52ec6b70edcd339140aa56c5554097d1e97c | quote: | **Intel Core Ultra 9 285HX *RTX 4070*** 24 Cores (8P+16E) Delivery in 12h | 192 GB | 2 × 2 TB PCIE 5.0 NVMe | 20 TB @ 1 Gbps | $449/mo Almost gone | [Order](https://wlx.hk/cart.php?a=add&pid=6) |
  - [3] 2026-10-28: the Ryzen 9 5950X server is in Hong Kong with a /29 IPv4 subnet (5 usable IPs), a /48 IPv6 subnet and 20 TB of bandwidth at 1 Gbps | capture: sha256:e6923b5e2b97afa0bc8a55afb6d4a4da3ff6637c92b84679989c9784d1f22c3c | quote: Server Specifications（Hong Kong） • AMD Ryzen 9 5950X (16C / 32T) • 128 GB DDR4 Memory • 2 TB NVMe SSD Storage • 1x /29 IPv4 Subnet (5 Usable IPs) • 1x /48 IPv6 Subnet (Included) • 20TB Bandwidth @ 1Gbps
  - [4] 2026-10-28: the store menu lists dedicated servers (HK, CN) and IP and ASN services; no VPS group | capture: sha256:d5c99210816580a2b5cb91de436e832602439cc1bcc02685d7ef8e10dccd7afe | quote: [Browse All](https://wlx.hk/store) [Dedicated Servers - HK, CN](https://wlx.hk/store/dedicated-servers-hk-cn) [IP & ASN Services](https://wlx.hk/store/ip-and-asn-services)
  - [2] 2026-10-28: the terms name virtual private servers within the scope of services, though the store menu lists none | capture: sha256:6d8661e74e6bf64cadadf12b7821c671592e3f22a34ed3c4c38ec5241a50f253 | quote: including but not limited to virtual private servers, virtual dedicated servers, dedicated servers, colocation, IP transit, BGP connectivity, LIR coordination services
  - [2] 2026-10-28: identity, business, payment, beneficial ownership, KYC, KYB and sanctions information may be required before provisioning | capture: sha256:6d8661e74e6bf64cadadf12b7821c671592e3f22a34ed3c4c38ec5241a50f253 | quote: WLX may require identity, business, payment, beneficial ownership, network use-case, routing policy, KYC, KYB, sanctions, anti-abuse, or other verification information before provisioning, renewing, modifying, or continuing a service.
  - [2] 2026-10-28: recurring services are billed in advance | capture: sha256:6d8661e74e6bf64cadadf12b7821c671592e3f22a34ed3c4c38ec5241a50f253 | quote: Unless otherwise agreed, recurring services are billed in advance and usage-based charges may be billed in arrears.
  - [2] 2026-10-28: cancellation must be submitted before the renewal date | capture: sha256:6d8661e74e6bf64cadadf12b7821c671592e3f22a34ed3c4c38ec5241a50f253 | quote: Unless otherwise agreed, cancellation must be submitted before the renewal date.
  - [5] 2026-10-28: reported: the vendor's forum post lists Alipay, credit or debit card, cryptocurrency and bank transfer as payment methods | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: - Alipay - Credit / Debit Card - Cryptocurrency - Bank Transfer
  - [5] 2026-10-28: reported: a promotion priced the Ryzen 9 5950X at USD 169 a month | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: ### AMD Ryzen 9 5950X — $169/month
  - [5] 2026-10-28: reported: the promotion ended on 2026-08-28 at 23:59 UTC+8 | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: Promotion ends on August 28, 2026 at 23:59 UTC+8
  - [5] 2026-10-28: reported: traffic is counted as combined inbound plus outbound transfer | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: Traffic is calculated as combined inbound + outbound transfer.
  - [5] 2026-10-28: reported: in-stock servers are typically provisioned within 6 business hours on Hong Kong business days | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: In-stock servers are typically provisioned within 6 business hours during Hong Kong business days (UTC+8).
  - [5] 2026-10-28: reported: the infrastructure has A/B power redundancy and redundant network connectivity | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: For reliability, our infrastructure is designed with A/B power redundancy and redundant network connectivity to reduce the impact of single-path failures or maintenance.
  - [5] 2026-10-28: reported: WLX Limited is a Hong Kong registered provider on AS150670 | capture: sha256:1e084d2c763e4142b0d22ff715e84eb580f2f6cc810fe63680b78641245f329d | quote: We are WLX Limited / AS150670, a Hong Kong registered cloud infrastructure provider primarily serving customers in Hong Kong and the Asia-Pacific region.
- sources:
  - [1] https://wlx.hk/
  - [2] https://wlx.hk/announcements/2/Terms-of-Service.html
  - [3] https://wlx.hk/store/dedicated-servers-hk-cn
  - [4] https://wlx.hk/register.php
  - [5] https://lowendtalk.com/discussion/220184/wlx-ryzen-sale-from-169-5950x-9955hx-9950x-class-performance-apac-dedicated-servers
