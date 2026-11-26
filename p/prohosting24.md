# ph24

> prohosting24.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prohosting24/ | JSON https://fshy.ajam.dev/api/v1/entity/prohosting24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ph24 (ProHosting24)

- `compute/ph24` | paid-only | evidence documented | binding volume-quota | category cloud VM | tier VPS S
- identity a placeholder: card and phone unknown | verified 2026-10-28T05:44:26.795Z (live) | stale on 2026-11-28
- url https://prohosting24.de/vps/2026-sale
- free tier: No free tier. Cheapest orderable monthly offer: Server XS, 1 vCPU at 3.1 GHz, 4 GB RAM, 100 GB NVMe on Ceph, 1 IPv4 and an IPv6 /64, 2 Gbit/s uplink, fair-use traffic with 10 TB included, EUR 5.00 per month, cancellable at any time, AMD 7003 (Milan) generation, in the maincubes data centre in Frankfurt am Main; prices include 19% VAT. unverified: the server price table of the hourly ph24 Cloud product is script-rendered, so its prices are unread. | unit: none | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: The record's tier, VPS S, is a sale-page plan with a larger shape than Server XS: 4 vCPU, 8 GB RAM, 100 GB NVMe at EUR 6.40 per month; VPS M is 6 vCPU, 12 GB RAM, 200 GB NVMe at EUR 9.60 per month; VPS L is 8 vCPU, 16 GB RAM, 300 GB NVMe at EUR 12.80 per month; the FLASH S plan with the same shape as VPS S at EUR 4.95 per month is marked sold out; a separate hourly ph24 Cloud product at ph24.io/cloud bills a public IPv4 per hour and its server price table did not render
- per-object cap: not applicable | source: [1]
- retention: not applicable: the unit is a machine, not stored bytes; the vendor states three daily backups are active by default | source: [2] | note: a machine record: what is lost is the running process and its disk
- egress: fair-use traffic with 10 TB a month included; the port is 2 Gbit/s on a 50 Gbit/s uplink; hypervisors are connected 2 x 25 Gbit/s (LACP, shared); no overage price was read | metered: yes | free allowance: 10 TB a month, fair use | source: [1]
- identity: email | detail: unverified: the sign-up page is script-rendered and returned no text, and no page listing accepted payment methods was read.
- interface: unknown
- limits:
  - volume-quota (binding): 10 TB a month of fair-use traffic included [1]
  - per-ip-shaping: 2 Gbit/s port limited on a 50 Gbit/s uplink [2]
  - per-object-cap: 100 GB of NVMe on VPS S [1]
- limits note: SMTP is closed by default and opened only on request; the shared vCPUs are not for continuous 24/7 100% CPU use.
- binding note: 10 TB a month of fair-use traffic binds before the 2 Gbit/s port speed does, and sustained full CPU use is capped by the fair-use rule on the shared vCPUs.
- interface detail: an in-house control panel with noVNC console, rDNS management, ISO mounting and automatic password reset; ph24 Cloud has its own client area; no API or CLI was read
- tooling: in-house panel; the vendor states Proxmox virtualization with ISO boot and 146 or more ISO images; no API, CLI or Terraform provider was read
- composes with: 4 vCPU, 8 GB RAM and 100 GB of NVMe at EUR 6.40 a month with 10 TB of fair-use traffic and monthly cancellation, in the maincubes FRA01 data centre, is a larger shape per euro than the entry plans of most budget hosts.
- reliability: unverified: no outage history was read; the FLASH plans show sold out on the order page.
- notes: ph24 is the short brand of ProHosting24, run by a German sole proprietorship (Einzelunternehmen); the.com domain prohosting24.com is a parked for-sale page and the live sites are prohosting24.de and ph24.io. The hourly ph24 Cloud product launched in 2025 Q1 and offers load balancers, volumes, floating IPs and managed Kubernetes; its instance prices were not readable.
- evidence note: Price, shape, uplink and VAT come from the vendor's German order page read on 2026-10-28; the data centre, SMTP and fair-use rules come from the vendor's own forum post. Reading the sign-up form and the price table of ph24 Cloud would raise the identity and hourly-cloud fields.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 100
  - billing_model: allocated
  - price.amount: 6.4
  - price.currency: EUR
  - price.term: month
  - price.vat: included (19%)
  - location: maincubes FRA01 (the code is not expanded on the pages read)
  - free_tier_kind: none
  - sold_out_plans: FLASH S; FLASH M; FLASH L
- evidence:
  - [1] 2026-10-28: VPS S costs EUR 6.40 per month, fixed monthly | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: ### VPS S # 6.40 € monthly fixed
  - [1] 2026-10-28: VPS S is 4 shared cores at 3.1 GHz, 8 GB RAM, 100 GB NVMe Ceph, IPv4, IPv6 /64, 2 Gbit/s uplink, 10 TB fair-use traffic included | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: #### 4 Kerne @ 3.1GHz Shared #### 8 GB Arbeitsspeicher #### 100 GB NVME CEPH #### IPv4 Adresse #### IPv6 /64 Subnetz #### 2 GBit/s uplink #### Fair-Use Traffic +10 TB Inkl.
  - [1] 2026-10-28: the plan can be cancelled at any time | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: #### Jederzeit kündbar
  - [1] 2026-10-28: the CPU generation is AMD 7003 (Milan) | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: #### AMD 7003/Milan Gen.
  - [1] 2026-10-28: VPS S has a live order link, which the sold-out FLASH plans lack | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: [Bestellen](https://prohosting24.de/cp/vserver/order/package/70)
  - [1] 2026-10-28: the FLASH S plan at EUR 4.95 per month is marked sold out | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: ### FLASH S # 4.95 € monthly fixed vpsoldsoldout
  - [1] 2026-10-28: every hypervisor has 2 x 25 Gbit/s shared LACP uplinks | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: Alle Hypervisor sind 2x mit 25GBit/s (LACP, Shared) angebunden.
  - [1] 2026-10-28: the operator is a sole proprietorship and prices include 19% VAT | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: ProHosting24 ... Einzelunternehmen | Alle Preise verstehen sich inklusive der gesetzlichen Mehrwertsteuer von 19%
  - [2] 2026-10-28: the machines are KVM on Proxmox with Ceph NVMe in maincubes FRA01 | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: Reliable and fast KVM-based VPS hosted in maincubes FRA01, utilizing Synlinq uplinks, Ceph NVMe storage, and Proxmox virtualization.
  - [2] 2026-10-28: 10 TB a month fair-use traffic, a 2 Gbit/s port on a 50 Gbit/s uplink | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: - 🌐 Fair-Use Traffic: 10 TB/month included, 2 gbps limited on 50gbps uplink
  - [2] 2026-10-28: SMTP is closed by default | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: - 📧 SMTP closed by default / only opened on request
  - [2] 2026-10-28: the vCPUs are not for sustained 100% CPU use | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: - ⚠️ Continuous 24/7 100% CPU usage prohibited (fair-use on vCPUs)
  - [2] 2026-10-28: three daily backups are included and active by default | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: - 💾 3× daily backups included (active by default)
  - [2] 2026-10-28: the forum post lists the same 4 core, 8 GB, 100 GB plan at EUR 6.40 | capture: sha256:c6b295975a0eb14de5288d25cf0d092d811bb53d700aa9cb5e893c1015d97b00 | quote: | BF S | 4 cores | 8 GB | 100 GB | ✔️ | /64 | 2 Gbit/s | 6.40 € |
  - [3] 2026-10-28: the hourly ph24 Cloud product bills a public IPv4 at EUR 0.002023 per hour; its server price table was empty in the capture | capture: sha256:a4b56af9a1586f27985c2848de21d4c4f20c5fd167f5205d6175a61a1a3f6122 | quote: | Public IP address | 0.002023 € / h1.5 € / Month |
  - [4] 2026-10-28: the offers feed carries the vendor's current thread | capture: sha256:a81634ee720527577633ad596d622494e62345d37e8729b0246a1522923386f6 | quote: [ph24 first vps deal in 2026 + flash sale (EPYC 7XX3)]
  - [5] 2026-10-28: the vendor's regular KVM page lists Server XS at EUR 5.00 per month, 1 core at 3.1 GHz, 4 GB RAM, 100 GB NVMe Ceph | capture: sha256:6fa9b6cb48c6d4c433feb41ff62b01044c82d474797593d36f8e4aaea23fc30a | quote: ### Server XS # 5.00 € Monatlich #### 1 Kerne @ 3.1GHz + #### 4 GB Arbeitsspeicher #### 100 GB NVME CEPH
  - [1] 2026-10-28: VPS S on the sale page costs EUR 6.40 per month, fixed monthly, with a live order link | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: ### VPS S # 6.40 € monthly fixed
  - [5] 2026-10-28: Server XS carries a live order link (package/3), cancellable at any time, AMD 7003 Milan generation | capture: sha256:6fa9b6cb48c6d4c433feb41ff62b01044c82d474797593d36f8e4aaea23fc30a | quote: #### Jederzeit kündbar #### AMD 7003/Milan Gen. --- [Bestellen](https://prohosting24.de/cp/vserver/order/package/3)
  - [1] 2026-10-28: FLASH S at EUR 4.95 per month is marked sold out | capture: sha256:b2fd29f0fc6cd46b4633d6a35ee961ec957267c15b4e4ae1ecb55810cf50d5e5 | quote: ### FLASH S # 4.95 € monthly fixed vpsoldsoldout
  - [5] 2026-10-28: the hypervisors are in the maincubes data centre in Frankfurt am Main | capture: sha256:6fa9b6cb48c6d4c433feb41ff62b01044c82d474797593d36f8e4aaea23fc30a | quote: Standort: Maincubes in Frankfurt am Main
  - [5] 2026-10-28: every Server plan includes 10 TB of fair-use traffic | capture: sha256:6fa9b6cb48c6d4c433feb41ff62b01044c82d474797593d36f8e4aaea23fc30a | quote: #### Fair-Use Traffic +10 TB Inkl.
- sources:
  - [1] https://prohosting24.de/vps/2026-sale
  - [2] https://lowendtalk.com/discussion/221060/ph24-first-vps-deal-in-2026-flash-sale-epyc-7xx3
  - [3] https://ph24.io/cloud
  - [4] https://lowendtalk.com/categories/offers
  - [5] https://prohosting24.de/vps
