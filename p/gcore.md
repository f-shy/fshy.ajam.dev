# Gcore

> gcore.com | Storage, Egress and tunnels, Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gcore/ | JSON https://fshy.ajam.dev/api/v1/entity/gcore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gcore Free CDN (1 TB/mo traffic, no card)

- `storage/gcore-free-cdn` | qualifies-with-caveat | evidence reported | binding none | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gcore.com/cdn
- price $0 for the first 1 TB/mo; $10/TB beyond (€0.01/GB). Object storage €0.04/GiB/mo ≈ €40/TB ≈ $46/TB — not a viable origin. | parsed USD 45.07/TB-mo
- free tier: 1 TB/month included traffic and 1 billion requests on the free PAYG plan at €0/month. Verified against Gcore's own pricing payload: 'Included FREE Traffic 1 TB/Month', 'Traffic overage (per GB) €0.01', 'Requests over 1B (per 1M) €0.75'. No trial period. It is a standing free plan. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: The free 1 TB/month IS the egress. Overage €0.01/GB (≈$10/TB). Separately, Gcore Object Storage has free egress to Gcore CDN and free ingress. | metered: yes | free allowance: 1 TB per month | price per TB: $10/TB
- identity: email | detail: email
- interface: rest
- limits note: per-object-cap: none published. The binding limit is the 1 TB/month traffic counter plus 1B requests. Gcore blocks Gcore storage if a plan payment fails, which can cascade into CDN suspension.
- interface detail: rest
- tooling: Standard CDN pull-zone config; origin can be any URL. No card needed for the CDN free plan (confirmed: 'CDN (Free) … Free plan has no trial period, but has a 1 TB traffic limit' with no card condition listed).
- composes with: Free plan includes 1 TB per month (~33 GB per day) across 210+ edge locations without credit card verification. Multiple email-only accounts each receive the standard monthly bandwidth allowance. Storage at rest costs €0.04 per GiB.
- reliability: 210+ PoPs, 200+ Tbps. Origin-shielding is 'Basic' on the free plan. Free tier has been reshaped before (was 100 GB until ~2025, then moved to 1 TB), so budget for the number moving.
- notes: the same as the free tier
- extras:
  - price_verbatim: $0 for the first 1 TB/mo; $10/TB beyond (€0.01/GB). Object storage €0.04/GiB/mo ≈ €40/TB ≈ $46/TB — not a viable origin.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 'CDN (Free) | Not available | Free plan has no trial period, but has a 1 TB traffic limit'
  - [3] 2026-10-21: S3 Standard €0.04/GiB/mo, 'Egress to CDN Free', 'Ingress Free'
- sources:
  - [1] https://gcore.com/pricing/edge-network
  - [2] https://docs.gcore.com/account-settings/billing/trial-conditions
  - [3] https://docs.gcore.com/storage/how-storage-is-billed

## Gcore Edge Proxy

- `egress/gcore-edge-proxy` | trial-only | evidence documented | binding none | category L4 reverse proxy (any TCP/UDP) | tier trial
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://gcore.com/security/edge-proxy
- price EUR 17 per month after the trial | parsed USD 19.03/mo
- free tier: Start for FREE; FREE Trial; 2-day free trial | unit: hours | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published for the trial; the paid plan is EUR 17 per month with rules priced by count; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: A Gcore account at auth.gcore.com. The trial is 2 days and the paid plan follows on the same account; the signup form was not opened. | country: None
- interface: rest
- limits:
  - volume-quota: 2-day free trial, then EUR 17/month [1]
  - request-rate: proxy rules are priced in bands: 2-5 rules EUR 10/mo, 6-10 EUR 8/mo each, 11+ EUR 6/mo each [1]
- binding note: The constraint that fails first is the trial length, which the vocabulary has no kind for. At 1 TiB/month the billable unit is the rule count and the monthly fee, not a byte allowance.
- interface detail: Portal at portal.gcore.com; the product onboards from an IP and port.
- tooling: portal configuration of a proxy rule, no agent
- composes with: Fronts a public origin by IP and port; with a free VM as the origin it would give that VM a UDP port for two days, then cost EUR 17/month.
- reliability: Trial expires in 2 days; the paid plan bills per proxy rule band.
- notes: Reverse proxy service supporting arbitrary TCP and UDP traffic on dedicated ports. Paid service starting at EUR 17 monthly, with temporary evaluation periods.
- evidence note: The 2-day trial and the EUR 17 plan are on the product page read. The trial's byte allowance and its egress billing are not published there and would need the portal.
- extras:
  - wg_path: inside-udp
  - wg_detail: Edge Proxy is L4 ingress for TCP and UDP to an origin, so a WireGuard listener would be reachable through it; but the free window is a 2-day trial.
  - ingress: tcp+udp
  - volume_stated: No byte allowance is published for the trial; the paid plan is EUR 17 per month with rules priced by count
  - bytes_transit: yes
  - transit_note: Gcore's edge filters and forwards the traffic
- evidence:
  - [1] 2026-10-23: Edge Proxy is volumetric-protected Layer 4 ingress for TCP and UDP services, filtering at the edge and forwarding clean traffic to an origin
  - [1] 2026-10-23: The offer is 'FREE Trial' and '2-day free trial'; the PAYG price is EUR 17 per month with flood traffic not billed
- sources:
  - [1] https://gcore.com/security/edge-proxy

## Gcore

- `egress/gcore-cloud-vm` | paid-only | evidence documented | binding none | category origin VM (paid VPS) | tier Standard
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:55:18.737Z (live) | stale on 2026-12-05
- url https://gcore.com/cloud/virtual-machines
- price EUR 8.93 a month for the Standard entry plan, with free outgoing traffic; no per-TB price | parsed USD 10.06/mo
- free tier: no free plan: Cloud virtual machines start 'From €8.93/month' with free egress traffic | unit: unlimited | metered on: none | read on: 2026-11-04 | source: [1] | note: No trial applies to Cloud virtual machines (third-party index); a balance of at least EUR 4 is needed to start.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Outgoing traffic is free on virtual machines and no byte allowance is published; the cheapest shared plan lists unmetered transfer limited by port speed (200 Mbps) and fair use on a third-party index; inbound UDP is allowed by adding a custom security-group rule | metered: no | free allowance: none published | source: [1]
- identity: card | detail: the Gcore docs say a self-service account pays with a card or wallet, adding a card triggers a verification hold of about 1 EUR or 1 USD, and at least EUR 4 must be on the balance; the services agreement lets Gcore require KYC documents (not stated to apply to every self-service sign-up); the sign-up page is a login application and was not read | country: None
- interface: ssh
- limits:
  - per-ip-shaping: 200 Mbps port on the Basic G2S 1 vCPU plan, with unmetered transfer 'limited by port speed and fair use' (third-party index) [2]
- binding note: at 1 TiB a month no byte quota is published because outgoing traffic is free; the 200 Mbps port on the shared plan would carry about 65 TB a month, so neither fails first; a balance of at least EUR 4 is the entry floor
- interface detail: SSH to the VPS public IPv4 address
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a low-priced origin with free outgoing traffic in 30+ regions; the wall is the account balance and the port speed, not a byte count
- reliability: unverified: services are suspended when payment fails from both the balance and the payment method; no throttle behaviour is stated on the pages read
- notes: A third-party index lists a shared Basic G2S 1 vCPU / 1 GB plan at EUR 0.71 a month excluding VAT plus EUR 2.11 for a separate IPv4 address; the vendor pages read show only the dedicated 'Standard' entry price of EUR 8.93. The existing Gcore Edge Proxy record is a different product.
- evidence note: free outgoing traffic, the entry price and the firewall behaviour are quoted from the vendor's own pages read on 2026-11-04; the Basic shared plan's port and price rest on a third-party index and are reported; no VM was ordered and no port was probed
- extras:
  - wg_path: native-conf
  - wg_detail: a KVM-class guest with root and a public IPv4; wg-quick binds UDP natively once a custom security-group rule opens the UDP port; inbound UDP was not probed
  - ingress: unverified: no inbound UDP port policy is stated on the pages read
  - volume_stated: outgoing traffic is free; no byte allowance published
  - bytes_transit: yes
  - transit_note: bytes leave through the VM's own public address on Gcore's network
- evidence:
  - [1] 2026-11-04: the Standard VM line states free egress traffic and billing only for active instances | capture: sha256:7b639e6c12bc607265db707a000b0d8b425f892ab6c4d0c71b44b1d3741401e4 | quote: Dedicated vCPUs, including free egress traffic and billing only for active instances.
  - [1] 2026-11-04: the vendor's own entry price for a VM is EUR 8.93 a month | capture: sha256:7b639e6c12bc607265db707a000b0d8b425f892ab6c4d0c71b44b1d3741401e4 | quote: From €8.93/month
  - [3] 2026-11-04: the billing page states that outgoing traffic is free for virtual machines | capture: sha256:bcba6b75cb0a616e7574a9a527cc19ee63e3261e1d8722432ad7e2cf81304b15 | quote: The Windows license is charged separately. Outgoing traffic is free.
  - [3] 2026-11-04: a balance of at least EUR 4 is needed to start using the services | capture: sha256:bcba6b75cb0a616e7574a9a527cc19ee63e3261e1d8722432ad7e2cf81304b15 | quote: To start using Edge Cloud services, add at least €4 or
  - [4] 2026-11-04: a self-service account pays with a card or a wallet | capture: sha256:b1c24a1df08a5c781c404ac4167e217a24ed7985acc5267e2fc137660489a1b7 | quote: Accounts under a signed contract pay by bank transfer, while an account opened through self-service signup pays with a card or wallet.
  - [4] 2026-11-04: adding a card triggers a verification hold of about EUR 1 | capture: sha256:b1c24a1df08a5c781c404ac4167e217a24ed7985acc5267e2fc137660489a1b7 | quote: Adding a payment card triggers a verification hold of about 1 EUR or 1 USD to confirm the card can be charged.
  - [5] 2026-11-04: the default security group allows ICMP, SSH and RDP inbound only | capture: sha256:4afc13fbe22f1ee4582ef695771ed96575ed8460c567c8a2b0454d06d198f1aa | quote: The default security group allows inbound traffic over ICMP, SSH (TCP/22), and RDP (TCP/3389 and UDP/3389).
  - [6] 2026-11-04: a custom rule or the All UDP template opens a UDP port, so a WireGuard listener can be allowed | capture: sha256:7545d44343b7cfe3cc085b6e6074d1419e8574fcffeae3ee68bf0735585149a5 | quote: Template rules (All TCP/All UDP/SSH/HTTP/HTTPS/MySQL/DNS TCP/DNS UDP/PostgreSQL/RDP TCP/RDP UDP): template rules come with pre-configured protocols and ports for typical connections
  - [6] 2026-11-04: outbound traffic is allowed by default | capture: sha256:7545d44343b7cfe3cc085b6e6074d1419e8574fcffeae3ee68bf0735585149a5 | quote: By default, all outbound traffic is allowed.
  - [7] 2026-11-04: the services agreement makes contracts contingent on a KYC check | capture: sha256:7e68cdd1420fece0f58a3ef7ee3bc44fd5007e63ca9dde088fa87694b5011d6a | quote: The Customer is required to furnish all necessary documentation for KYC verification, and all contracts with Gcore are contingent upon successful completion of the KYC check.
  - [2] 2026-11-04: a third-party index lists the cheapest Basic plan as unmetered, limited by port speed and fair use | capture: sha256:7a327816ccad256b6228fa72e5415c65f20fe3775e0a85c8c480f4b5fae3ffa9 | quote: Unmetered (limited by port speed and fair use)
  - [2] 2026-11-04: the cheapest Basic G2S 1 vCPU plan is listed at EUR 0.71 a month excluding VAT, before a separate IPv4 charge | capture: sha256:7a327816ccad256b6228fa72e5415c65f20fe3775e0a85c8c480f4b5fae3ffa9 | quote: Gcore lists this plan at 0.71 EUR excluding VAT.
  - [2] 2026-11-04: an IPv4 address is charged separately on that plan | capture: sha256:7a327816ccad256b6228fa72e5415c65f20fe3775e0a85c8c480f4b5fae3ffa9 | quote: Charged separately (£2.11/month, included in the price here)
  - [8] 2026-11-04: a third-party index reports no trial for Cloud virtual machines | capture: sha256:6b43fa979d5ed63431173c2bdf1b3f99449cf409f44c0195ff257803c15d0e0f | quote: | Free trial or credit | None | No trial for Cloud virtual machines
- sources:
  - [1] https://gcore.com/cloud/virtual-machines
  - [2] https://serverworth.com/plans/gcore/g2s-shared-1-1-25/
  - [3] https://docs.gcore.com/cloud/billing
  - [4] https://docs.gcore.com/account-settings/billing/payments
  - [5] https://docs.gcore.com/cloud/virtual-instances/create-an-instance
  - [6] https://docs.gcore.com/cloud/networking/add-and-configure-a-firewall
  - [7] https://gcore.com/legal
  - [8] https://serverworth.com/providers/gcore/

## Gcore Cloud / Functions / GPU

- `compute/gcore` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:58.000Z (live) | stale on 2026-11-22
- url https://gcore.com/cloud/virtual-machines
- price parsed USD 13.92/mo
- free tier: no free tier: VMs from EUR 8.93 a month, with egress free and billing only while an instance is active | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): from EUR 8.93 a month; billing applies only while an instance is active [1]
  - per-ip-shaping: egress traffic is free on every VM [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the product page was read on 2026-10-22 and prices from EUR 8.93 a month with free egress. The record's free-tier claim is contradicted, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: billing only for active instances, so a stopped instance costs nothing
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 5.8
  - m24h_usd: 13.92
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - burst_x: 1.0
  - ps.price: not stated on this page
  - ps.durability: instance disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the instance exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.allowance: egress free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Rent high-performance virtual machines across 30+ global regions. Free egress traffic, pay only for active instances' and 'Cloud Virtual Machine Hosting - Rent VMs from EUR 8.93/month', quoted
- sources:
  - [1] https://gcore.com/cloud/virtual-machines
