# EnderHost

> enderhost.co | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/enderhost/ | JSON https://fshy.ajam.dev/api/v1/entity/enderhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EnderHost

- `egress/enderhost-budget-vps-4gb` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Toronto, KVM) | tier 4GB Budget VPS
- needs card yes, phone yes, ID no, institution no | verified 2026-11-03T07:36:42.856Z (live) | stale on 2026-12-04
- url https://enderhost.co/
- price USD 6.00 per month list, USD 3.84 per month with a coupon, 2TB/month included | parsed USD 3.84/mo
- free tier: No free tier. The 4GB Budget VPS lists USD 6.00 a month: 2 vCores on dual Intel Xeon E5-2690 V4 or equivalent, 4GB RAM, 40GB SSD, 2TB bandwidth, 1Gbps uplink, always-on DDoS protection. A third-party post quotes coupon LETSPECIAL96 at 36% off recurring for the Toronto Budget VPS, USD 3.84 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 2TB bandwidth on the 4GB plan on a 1Gbps uplink; each tier lists a monthly transfer allowance and the vendor asks to be told before ordering if a workload may exceed it. No overage rate is published. | metered: yes | free allowance: 2TB/month included in the 4GB Budget VPS | source: [1]
- identity: any-phone | detail: The registration form asks for First Name, Last Name, Email Address, Phone Number, a password and a billing address; only Company Name and Street Address 2 are marked Optional, so the phone number is not optional. Whether the number is verified is not stated. A third-party post lists PayPal, Credit/Debit Card, Zelle and Razorpay (UPI) as payment methods.
- interface: ssh
- limits:
  - volume-quota (binding): 2TB/month on the 4GB Budget VPS [1]
  - per-ip-shaping: 1Gbps uplink [1]
- binding note: 2TB/month is the ceiling the store lists for 4GB; a 1Gbps uplink can move that allowance in hours, so the allowance fails first.
- interface detail: KVM guest with root; the order page names an EnderHost Panel and the vendor VPS page names TenantOS.
- tooling: ssh; any daemon the KVM guest supports.
- composes with: A cheap Toronto KVM guest at USD 3.84 a month with the coupon; the pages read state no IPv6 allocation, no NAT and no inbound filter, so those three are unverified.
- reliability: The USD 3.84 coupon price is quoted by a third-party post, not by the vendor page read; the store page lists USD 6.00 a month.
- notes: Toronto Budget tier of a Florida-based host. The network page lists Source and UDP services among the protocols its DDoS filtering profiles cover.
- evidence note: The USD 6.00 price, the 2TB allowance and the 1Gbps uplink are vendor store lines read on 2026-11-03; the coupon price is reported by a third party. IPv6, NAT and inbound policy are not stated on any page read.
- extras:
  - nat: not stated
  - ipv6: not stated
  - inbound: not stated
  - udp: UDP services are named among the protocols the DDoS filtering covers; plan-level UDP policy not stated
- evidence:
  - [1] 2026-11-03: the cheapest Budget plan is the 4GB one | capture: sha256:f91c87a65b3290f95fbb13d8ef845952723a0b92b70817b5bb8556225e98900a | quote: ### 4GB Budget VPS
  - [1] 2026-11-03: the 4GB Budget VPS lists USD 6.00 monthly | capture: sha256:f91c87a65b3290f95fbb13d8ef845952723a0b92b70817b5bb8556225e98900a | quote: $6.00 USD
  - [1] 2026-11-03: the 4GB Budget VPS lists 2TB Bandwidth | capture: sha256:f91c87a65b3290f95fbb13d8ef845952723a0b92b70817b5bb8556225e98900a | quote: - 2TB Bandwidth
  - [1] 2026-11-03: the Budget VPS plans list a 1Gbps uplink | capture: sha256:f91c87a65b3290f95fbb13d8ef845952723a0b92b70817b5bb8556225e98900a | quote: - 1Gbps Uplink
  - [2] 2026-11-03: no overage rate is published; the vendor asks to be told before ordering if a workload may exceed the allowance | capture: sha256:89d7a534e9c3551b9241056714eeeb82db96fe128b5db9584cdab0addee207ad | quote: If your workload is likely to exceed the listed transfer, tell us before you order and we will talk through the options.
  - [3] 2026-11-03: with coupon LETSPECIAL96 the Toronto 4GB Budget VPS is USD 3.84 a month recurring with 2TB monthly transfer | capture: sha256:fd904828db1070a511ea6f9514dd6b69b6b1f214898c6a33f2be753ae4738f16 | quote: | 4GB Budget VPS$3.84/month recurring2 vCores4GB DDR4 RAM40GB SSD Storage2TB Monthly TransferKVM Virtualization
  - [3] 2026-11-03: the coupon takes 36% off the recurring price of the Toronto Budget VPS | capture: sha256:fd904828db1070a511ea6f9514dd6b69b6b1f214898c6a33f2be753ae4738f16 | quote: With coupon code LETSPECIAL96, customers receive 36% off recurring, bringing pricing down to $0.96/GB of RAM.
  - [4] 2026-11-03: the registration form asks for a phone number | capture: sha256:bd6fa43985bff3116be9239ad1063ccc1c6093855cd4e0528b2163fe991e71ae | quote: Phone Number
  - [4] 2026-11-03: the registration form marks only some fields Optional; Phone Number carries no such mark | capture: sha256:bd6fa43985bff3116be9239ad1063ccc1c6093855cd4e0528b2163fe991e71ae | quote: Company NameOptional
  - [3] 2026-11-03: payment methods accepted | capture: sha256:fd904828db1070a511ea6f9514dd6b69b6b1f214898c6a33f2be753ae4738f16 | quote: They accept PayPal, Credit/Debit Card, Zelle, and Razorpay (UPI).
  - [5] 2026-11-03: the network page lists Source and UDP services among the protocols its filtering profiles cover | capture: sha256:17416ac652c4e91aee128cb8e53a80619288f236166eff67308f1461a8a4beec | quote: - Source & UDP services
- sources:
  - [1] https://billing.enderhost.co/index.php?rp=/store/budget-vps-hosting
  - [2] https://enderhost.co/vps
  - [3] https://lowendbox.com/blog/cheap-vps-deals-in-toronto-from-enderhost-get-a-4gb-vps-for-only-3-84-month/
  - [4] https://billing.enderhost.co/register.php
  - [5] https://enderhost.co/network
