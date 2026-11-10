# Kimsufi

> kimsufi.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kimsufi/ | JSON https://fshy.ajam.dev/api/v1/entity/kimsufi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kimsufi (OVHcloud)

- `compute/kimsufi-windows` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Dedicated server | tier KS-3
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T02:17:36.631Z (live) | stale on 2026-12-03
- url https://www.kimsufi.com/en/ks/ks-3/
- price parsed USD 30/mo
- disagrees on verdict: `compute/kimsufi` says paid-only, `compute/kimsufi-windows` says qualifies-with-caveat
- free tier: no free tier; KS-3 is USD 30.00 a month for 4 cores and 8 threads, 32 GB of DDR4 ECC RAM and 2 x 480 GB of SSD, and the configure screen sells a Windows Server 2016 Standard 4-core licence as a priced option at USD 34.00 a month, so a Windows-ready box is USD 64.00 a month | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disks persist while the server is rented; the page states no deletion clock
- egress: 500 Mbps unmetered on the configure page, against 'Public 300 Mbps' on the KS range table; no byte quota and no overage price is printed on either | metered: no | free allowance: unmetered | source: [1]
- identity: card | detail: an account and a payment method at order; a card is registered with a small deduction that 'No amount will be charged' and it activates the card, while an order that fails or is cancelled leaves an 'authorisation hold, not a final payment' that clears 'within 15 days for a credit card payment'. Cards accepted are Visa, Mastercard and Maestro, plus PayPal and a prepaid account balance. OVHcloud accounts are region-scoped, and the range table shows this plan orderable from a subset of regions.
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): 500 Mbps unmetered per the configure page; 300 Mbps per the range table [1]
- limits note: the two pages disagree on the port: the KS range table says 'Public 300 Mbps' and the configure screen says 500 Mbps unmetered. The configure page is the one that charges the money and is the newer, so it is carried, with the table figure recorded beside it. RAM can be raised to 64 GB for USD 8.90 and the disk comes as 2 x 480 GB SSD or 2 x 2 TB HDD at the same price.
- binding note: the public port is the only published limit and it is the one that bites for a high-transfer workload: 300 to 500 Mbps is between a third and a half of what a 1 Gbps VPS row offers, and the licence adds USD 34.00 before the port matters.
- interface detail: a rented dedicated server with a public IPv4 on the machine and a rescue or install path from the OVHcloud manager; RDP once Windows is installed from the licence option
- tooling: any RDP client; the OVHcloud manager for install, rescue and billing
- composes with: the only row in the sweep with a published licence line item sold apart from the machine, which makes USD 34.00 a month the yardstick every licence-included claim is measured against; the machine is 32 GB of dedicated RAM for USD 30.00, so a workload that needs real memory rather than a vCPU share has no cheaper row.
- reliability: no reliability event observed; the same plan is priced differently on the range table and the configure screen, and the range table shows availability by region rather than everywhere.
- notes: The USD 34.00 licence is the number that makes this record useful: it is the only published licence price any lane in the sweep found, and every licence-included claim elsewhere can be read against it. Two disagreements are left standing rather than smoothed. The first is internal: the range table says 300 Mbps public and the configure screen says 500 Mbps unmetered. The second is across records: kimsufi.json carries USD 21.10 for KS-3 from the range page on 2026-10-22 and this record carries USD 30.00 from the configure screen today, so a reader comparing the two should treat the range page as a starting point that moves by region. The all-in figure is USD 64.00, which is 7.89 times the USD 8.11 floor used by the surrounding sweep.
- evidence note: the shape, the USD 30.00 base and the USD 34.00 Windows licence option are read from the KS-3 configure screen on 2026-10-26, and the licence is a printed line item rather than a sentence, which is why this record is the anchor for licence cost. Two things are weaker: the port figure contradicts the range table, and the existing catalogue record kimsufi.json prices KS-3 at USD 21.10 from the range page read on 2026-10-22. The higher of the two prices is carried here, per earlier readings rule on disagreeing figures.
- extras:
  - shape.vcpu: 4
  - shape.threads: 8
  - shape.ram_gib: 32
  - shape.disk_gib: 480
  - ram_upgrade_gib: 64
  - ram_upgrade_usd: 8.9
  - disk_options: 2 x 480 GB SSD; 2 x 2 TB HDD
  - billing_model: monthly
  - term: none
  - monthly_usd: 30.0
  - setup_fee_usd: 0.0
  - windows_licence_usd: 34.0
  - windows_licence: printed: Windows Server 2016 Standard, 4-core, USD 34.00 a month as a configure option
  - windows_ready_monthly_usd: 64.0
  - windows_images: Windows Server 2016 Standard (4-core licence option)
  - dedicated: yes
  - public_ipv4: yes
  - port_mbps: 500
  - port_mbps_range_table: 300
  - range_plan_url: https://www.kimsufi.com/en/
  - configure_url: https://www.kimsufi.com/en/ks/ks-3/
  - payment_methods.card_at_signup: yes at order, unless the order is paid from a prepaid account balance or by PayPal
  - payment_methods.debit: accepted, listed with the credit cards under the heading 'Credit/Debit cards': Visa, Mastercard and Maestro, with 3D Secure enabled and the cardholder details matching the account
  - payment_methods.prepaid: not published: https://www.ovhcloud.com/en/terms-and-conditions/payment/
  - payment_methods.virtual: not published: https://docs.ovhcloud.com/en/guides/account-and-service-management/managing-billing-payments-and-services/manage-payment-methods
  - payment_methods.hold_amount: not published
  - payment_methods.hold_detail: a card is registered by a small deduction that is not a charge: 'A small amount of money is deducted from your bank account to check your card details and their validity. No amount will be charged'. A failed or cancelled order leaves an 'authorisation hold, not a final payment' that clears 'within 15 days for a credit card payment'. The amount is not published on the payment methods page, the billing FAQ or the payment-method guide.
  - payment_methods.identity: an account, a card, PayPal or a prepaid account balance; 3D Secure must be enabled and the card details must match the account
  - payment_methods.source_url: https://docs.ovhcloud.com/en/guides/account-and-service-management/managing-billing-payments-and-services/faq-billing
  - payment_methods.read_on: 2026-11-02
- evidence:
  - [1] 2026-10-26: quoted from the configure screen: KS-3 at USD 30.00 a month, 4 cores and 8 threads, 32 GB DDR4 ECC with 64 GB at USD 8.90 more, 2 x 480 GB SSD or 2 x 2 TB HDD, no setup fee shown
  - [1] 2026-10-26: 
  - [1] 2026-10-26: the configure page states 500 Mbps unmetered while the KS range table states 'Public 300 Mbps' for the same plan, a contradiction inside the vendor's own site
  - [2] 2026-10-22: the range table read four days earlier prints KS-3 at USD 21.10 with 32 GB and 2 x 480 GB, which is the figure carried by compute/kimsufi and does not reproduce on the configure screen read
  - [3] 2026-11-02: registering a card makes a small deduction that OVHcloud states is not a charge, and publishes no amount | capture: sha256:a8772267eeda27cd745c6d11f4206db3cd400b87ce875a06933cc05754401a05 | quote: A small amount of money is deducted from your bank account to check your card details and their validity.
  - [4] 2026-11-02: an unsuccessful or cancelled order leaves an authorisation hold rather than a payment | capture: sha256:4ff8c89dd1803719da8c369709363303e6a1cad2a1312080175f887072613dd2 | quote: If your order was unsuccessful or was cancelled, the amount shown on your bank account corresponds to an authorisation hold, not a final payment.
  - [5] 2026-11-02: the accepted card networks are Visa, Mastercard and Maestro | capture: sha256:1bb040f010d78fc15cad2155da6cdc0195337f3af99e51d70c12b68810997e37 | quote: Cards accepted are Visa, Mastercard, Maestro.
- sources:
  - [1] https://www.kimsufi.com/en/ks/ks-3/
  - [2] https://www.kimsufi.com/en/
  - [3] https://docs.ovhcloud.com/en/guides/account-and-service-management/managing-billing-payments-and-services/manage-payment-methods
  - [4] https://docs.ovhcloud.com/en/guides/account-and-service-management/managing-billing-payments-and-services/faq-billing
  - [5] https://www.ovhcloud.com/en/terms-and-conditions/payment/

## Kimsufi KS-5 (OVH budget brand)

- `storage/kimsufi-ks-5` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category dedicated server, budget range
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.kimsufi.com/en/
- price $19.90 ÷ 8 TB = $2.49/TB/mo at the 2×4TB config; ÷ 12 TB (3×4TB) = $1.66/TB; ÷ 4 TB (2×2TB) = $4.98/TB. Unlimited traffic, but 300 Mbps. | parsed USD 1.66/TB-mo
- free tier: 2× 2 TB – 2× 4 TB HDD (configured up to 3× 4 TB) | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Unlimited traffic is included, so you won't have to pay extra.' Port is 'Public 300 Mbps'. The shape, not the volume, is the limit. | metered: no
- identity: card | detail: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 300 Mbps [1]
- limits note: 300 Mbps public port caps you near ~97 TB/mo theoretical. 32 GB RAM, Xeon E3-1270 v6. Regional availability varies (3/9 regions).
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: full root
- tooling: unrestricted
- composes with: MinIO / SFTP / NFS
- reliability: OVH's clearance brand — cheapest way into OVH's network with unlimited traffic.
- notes: the same as the free tier
- extras:
  - price_verbatim: $19.90 ÷ 8 TB = $2.49/TB/mo at the 2×4TB config; ÷ 12 TB (3×4TB) = $1.66/TB; ÷ 4 TB (2×2TB) = $4.98/TB. Unlimited traffic, but 300 Mbps.
- evidence:
  - [2] 2026-10-21: KS-5: 'Intel Xeon-E3 1270 v6, 4c/8t, 32 GB, 2 x 2 TB – 2 x 4 TB, Public 300 Mbps, US$19.90'; KS-5-B US$35.50 with 500 Mbps
  - withheld 2026-10-21: same page — 'For high performance, most of our servers come with network speeds from 100 Mbps to 1 Gbps … Unlimited traffic is included, so you won't have to pay extra.'
  - [1] 2026-10-21: configured options 2x 2TB HDD, 2x 4TB HDD, 3x HDD SATA 4TB Enterprise Class Soft RAID, 2x 1.2TB NVMe
- sources:
  - [1] https://www.kimsufi.com/en/ks/ks-5/
  - [2] https://www.kimsufi.com/en/

## Kimsufi

- `compute/kimsufi` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.kimsufi.com/en/
- disagrees on verdict: `compute/kimsufi` says paid-only, `compute/kimsufi-windows` says qualifies-with-caveat
- free tier: KS-5 at USD 19.90/month: Intel Xeon E3-1270 v6, 4 cores / 8 threads at 3.8 to 4.2 GHz, 32 GB RAM, 2 x 2 TB or 2 x 4 TB disk, public 300 Mbps, in 3 of 9 regions. KS-3 is USD 21.10 with 32 GB and 2 x 480 GB. KS-5-B is USD 35.50 with 64 GB RAM and 500 Mbps. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 300 Mbps public is a hard port cap with no published monthly byte allowance, so throughput is the wall and a daytime crawler is shaped rather than stopped [1]
- limits note: 300 Mbps public is a hard port cap with no published monthly byte allowance, so throughput is the wall and a daytime crawler is shaped rather than stopped
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 32 GB of RAM and 4 TB of disk for USD 19.90 is the cheapest way to hold the 20 TB dataset index and active data on one machine, with the cold bytes mirrored to a storage host.
- reliability: no reliability event recorded
- notes: This is the USD 20 row's ceiling: no VPS at that price among evaluated providers reaches 32 GB of RAM, and only a dedicated box reaches 8 threads with 4 TB of local disk. Availability is the gate: 3 of 9 regions for KS-5 and 1 of 9 for KS-3, so the price is not orderable from every country. json and ovh-gpu.json cover other OVH lines).
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 32
  - facets.shape.disk_gib: 4096
- evidence:
  - [1] 2026-10-22: KS-5 row: 'Intel Xeon-E3 1270 v6 4c / 8t - 3.8 GHz / 4.2 GHz', 32 GB, '2 x 2 TB - 2 x 4 TB', 'Public 300 Mbps', 'US$19.90', quoted from the server table
  - [1] 2026-10-22: KS-3 at USD 21.10 with 32 GB and 2 x 480 GB; KS-5-B at USD 35.50 with 64 GB and 500 Mbps; KS-A at USD 61.00
  - [1] 2026-10-22: the KS range is described as '6 references with 8 configurations available' and KS-5 is available in 3 of 9 regions
- sources:
  - [1] https://www.kimsufi.com/en/
