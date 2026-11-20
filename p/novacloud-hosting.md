# NovaCloud-Hosting Storage VPS

> novacloud-hosting.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/novacloud-hosting/ | JSON https://fshy.ajam.dev/api/v1/entity/novacloud-hosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NovaCloud-Hosting Storage VPS

- `storage/novacloud-hosting-storage-vps` | qualifies-with-caveat | evidence reported | binding none | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T00:50:27.598Z (live) | stale on 2026-11-25
- url https://novacloud-hosting.com/vps-storage
- price $4.21/TB/mo at 2 TB (€7.50). At 5 TB: €3.50 base (2 TB) + 3 x €2 marginal = €9.50/mo = $10.67 for 5 TB = $2.13/TB — the €2/TB marginal rate is the lowest of the storage providers compared, if the provider will actually build the config. At 20 TB: €3.50 + 18 x €2 = €39.50/mo = $44.37 = $2.22/TB. Sold out. | parsed USD 2.13/TB-mo
- free tier: Storage Stellar: from7.50€ Monthly, 1 Intel XEON Core, 2GB DDR4 ECC, 20GB NVMe Storage (Raid 1), 2TB HDD Storage (Raid-6 + NVMe-Cached), Fair-Use Traffic, Up to 5 Gbit/s Uplink; Sold Out. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Fair-Use Traffic' with no published number on the storage page. The offer threads give '7,5 TB Traffic per month included' on the 2 TB plan and describe 'Unlimited @ 5Gbps shared' on the 1 TB special. Conflicting, so treat as 7.5 TB metered per 2 TB. Extra TB of HDD quoted at '+2€ (20€ Annually) per additional TB' in LET thread 217568. That marginal rate is the number worth having. | metered: yes
- identity: card | detail: We accept PayPal, card payments, Apple Pay, paysafecard, cryptocurrency, iDEAL, EPS, and Przelewy24.
- interface: rest, sftp, rsync, rclone
- limits note: per-object-cap: none. Storage Stellar and Cosmic both showed 'Sold Out' / 'Temporarily sold out' when read.
- interface detail: sftp, rsync, rest (self-hosted)
- tooling: rclone SFTP, root KVM
- composes with: Root KVM virtual server with 2.5 to 5 Gbps uplink. Incremental HDD storage is available at 2 EUR per TB.
- reliability: Small NL provider, active on LET as a Patron Provider. No data-loss reports surfaced. Sold-out status is persistent across two reads.
- notes: the same as the free tier
- evidence note: the storage-vps page lists the Stellar plan and marks it sold out
- extras:
  - price_verbatim: $4.21/TB/mo at 2 TB (€7.50). At 5 TB: €3.50 base (2 TB) + 3 x €2 marginal = €9.50/mo = $10.67 for 5 TB = $2.13/TB — the €2/TB marginal rate is the lowest of the storage providers compared, if the provider will actually build the config. At 20 TB: €3.50 + 18 x €2 = €39.50/mo = $44.37 = $2.22/TB. Sold out.
- evidence:
  - [1] 2026-10-21: Storage Stellar from €7.50 (2 TB HDD, 20 GB NVMe, 'Fair-Use Traffic', up to 5 Gbit/s), Storage Cosmic from €19.00 (6 TB), both 'Sold Out'
  - [2] 2026-10-21: 'Just 3,75€/Month or 37,50€/Annually ... +2€ (20€ Annually) per additional TB of HDD Storage'
  - [3] 2026-10-21: 'Storage-VPS M ... 2000GB HDD, 7.5TB, €3.50 (€4.31) /mo'
  - [1] 2026-11-09: the Stellar plan runs from 7.50 EUR a month with 2 TB HDD and 20 GB NVMe and is marked Sold Out | capture: sha256:b78c937aadcab6b503c93435e9ea039658224ace3035fe746b0cd31a61192c3c | quote: Sold Out ### Storage Stellar from7.50€ Monthly - 1 Intel XEON Core - 2GB DDR4 ECC - 20GB NVMe Storage (Raid 1) - 2TB HDD Storage (Raid-6 + NVMe-Cached) - Fair-Use Traffic - Up to 5 Gbit/s Uplink
  - [1] 2026-11-09: the page lists the payment methods it accepts, card payments among them | capture: sha256:b78c937aadcab6b503c93435e9ea039658224ace3035fe746b0cd31a61192c3c | quote: We accept PayPal, card payments, Apple Pay, paysafecard, cryptocurrency, iDEAL, EPS, and Przelewy24.
- sources:
  - [1] https://novacloud-hosting.com/vps-storage
  - [2] https://lowendtalk.com/discussion/217568/
  - [3] https://lowendtalk.com/discussion/210880/
