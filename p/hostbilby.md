# HostBilby

> hostbilby.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostbilby/ | JSON https://fshy.ajam.dev/api/v1/entity/hostbilby.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostBilby

- `egress/hostbilby-bilbyboost-vds` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS: dedicated-core VDS with a metered monthly allowance | tier BilbyBoost VDS
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:55:17.627Z (live) | stale on 2026-12-05
- url http://hostbilby.com/max-vds
- free tier: No free tier. BilbyBoost VDS is USD 10.50: 1 vCPU, 8 GB RAM, 200 GB SSD, 1 IPv4, a routed /64 IPv6, 10 TB bandwidth. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 10 TB of bandwidth; the port speed, the overage action and the byte tolerance are not published on the plan page read. | metered: yes | free allowance: 10 TB, period not stated | source: [1]
- identity: card | detail: Payment is a credit card, a debit card (Canada) or PayPal, and the service is provisioned only after payment is verified; the registration fields were not read.
- interface: ssh
- limits:
  - volume-quota (binding): 10 TB bandwidth, period not stated; overage action not published [1]
- binding note: 10 TB is the only countable figure and is above 1 TiB a month; its overage action is not published.
- interface detail: Root VDS managed from a VirtFusion panel; outbound email is not allowed from its VPS and VDS servers.
- tooling: Any SSH client.
- composes with: A 10 TB VDS with a routed IPv6 /64 and one IPv4; outbound email is blocked, and other port restrictions are not published on the pages read.
- reliability: Outbound email from a VPS or VDS is not allowed by the vendor.
- notes: The plan page does not name a billing term.
- evidence note: Plan page and terms read on 2026-11-04. The serverdeals ServerDeals EXCLUSIVE VDS (USD 6.90 a month, 2 vCPU, 8 GB, 5 TB, 5Gbps) was not found on the vendor pages read.
- extras:
  - ipv6: /64 routed
  - virtualization: VDS
- evidence:
  - [1] 2026-11-04: the BilbyBoost VDS plan is listed | capture: sha256:a9b72e54f7d8a15c543835f65b9ec5f207cf2bec4b80bae4f96b6452ece78087 | quote: ### BilbyBoost VDS
  - [1] 2026-11-04: the plan costs USD 10.50 | capture: sha256:a9b72e54f7d8a15c543835f65b9ec5f207cf2bec4b80bae4f96b6452ece78087 | quote: $10.50 USD
  - [1] 2026-11-04: the plan lists 10 TB of bandwidth | capture: sha256:a9b72e54f7d8a15c543835f65b9ec5f207cf2bec4b80bae4f96b6452ece78087 | quote: 10 TB
  - [1] 2026-11-04: outbound email is not allowed on VPS and VDS servers | capture: sha256:a9b72e54f7d8a15c543835f65b9ec5f207cf2bec4b80bae4f96b6452ece78087 | quote: At HostBilby, we don’t allow email from our VPS/VDS servers, and there’s a good reason for it!
  - [2] 2026-11-04: payment is verified before provisioning | capture: sha256:5379f890d02271362df7eeb16181ad0ee5cf6b2bf193ca9c0dc1b1c7eb6a4947 | quote: Products and Services will be paid for in full when the services are ordered - they won't be provisioned until payment is verified and complete.
  - [2] 2026-11-04: the payment methods include a credit card | capture: sha256:5379f890d02271362df7eeb16181ad0ee5cf6b2bf193ca9c0dc1b1c7eb6a4947 | quote: - Credit Card
  - [3] 2026-11-04: serverdeals lists a HostBilby exclusive VDS at USD 6.90 a month with 5 TB, a listing not found on the vendor pages read | quote: ###### ServerDeals EXCLUSIVE VDS
- sources:
  - [1] http://hostbilby.com/max-vds
  - [2] https://www.hostbilby.com/terms
  - [3] https://serverdeals.cc/
