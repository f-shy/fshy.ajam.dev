# STRATO

> strato.de | Storage, Compute, Egress and tunnels; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/strato/ | JSON https://fshy.ajam.dev/api/v1/entity/strato.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## STRATO HiDrive Business

- `storage/strato-hidrive-business` | qualifies-with-caveat | evidence reported | binding none | category consumer/SMB cloud drive with protocol access
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.strato.de/cloud-speicher/hidrive-business/
- price 10 TB €90 ÷ 10 = €9.00/TB/mo. 5 TB €55 ÷ 5 = €11.00/TB. 3 TB €30 ÷ 3 = €10.00/TB. 1 TB €17.50/TB. ≈$10.44/TB at best. 4.4× Hetzner BX41 for the same capacity. | parsed USD 10.14/TB-mo
- free tier: 1 / 3 / 5 / 10 TB | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published as a volume on the pricing page. Protocol access (SFTP, WebDAV, SMB, rsync, SCP, Git) is tier-gated: 'Im Business Essential und Standard Tarif sind die Zugriffsmöglichkeiten WebDAV und SMB inklusive. Wenn Sie sich den Advanced oder Premium Tarif gesichert haben, sind alle genannten Zugriffsmöglichkeiten inklusive.'. I.e. rsync/SCP/SFTP may require the higher tier. | metered: no
- identity: card | detail: card
- interface: webdav, sftp, scp, rsync, smb, git, rclone
- limits note: Protocol access gated by tier. 20-user cap. Ends up 4.5× Hetzner per TB at the 10 TB tier.
- interface detail: WebDAV, SMB (lower tiers); + SFTP/SCP/rsync/Git (Advanced/Premium). rclone hidrive backend exists
- tooling: rclone `hidrive` backend
- composes with: rclone mount → Cloudflare
- reliability: STRATO is the German consumer-grade option.
- notes: the same as the free tier
- extras:
  - price_verbatim: 10 TB €90 ÷ 10 = €9.00/TB/mo. 5 TB €55 ÷ 5 = €11.00/TB. 3 TB €30 ÷ 3 = €10.00/TB. 1 TB €17.50/TB. ≈$10.44/TB at best. 4.4× Hetzner BX41 for the same capacity.
- evidence:
  - [1] 2026-10-21: 1 TB €17.50/mo, 3 TB €30/mo, 5 TB €55/mo, 10 TB €90/mo, setup €0.00, up to 20 users; promo rows 'danach 12,50 €/Mon.' (1TB), 'danach 25 €/Mon.' (3TB), 'danach 50 €/Mon.' (5TB), 'danach 85 €/Mon.' (10TB)
  - [2] 2026-10-21: consumer ladder Starter 500 GB €6, Basic 1 TB €7.50, Plus 2 TB €12.50, Family 2 TB €17.50
  - [2] 2026-10-21: protocol tier-gating clause and 'Zugriffsmöglichkeiten sind SFTP, WebDAV, SMB, rsync, SCP und Git' quoted verbatim
- sources:
  - [1] https://www.strato.de/cloud-speicher/hidrive-business/
  - [2] https://www.strato.de/online-speicher/

## Strato HiDrive — 1 TB for 12 months at €0 (Valentine's promo)

- `storage/strato-hidrive-1-tb-for-12-months-at-0` | trial-only | evidence reported | binding per-object-cap | category cloud-drive
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.strato.de/cloud-speicher/hidrive/
- free tier: 1 TB, 12 months, €0 (setup €0). Regular price after the free year is €5/month. Captured promo page states verbatim: 'HIDRIVE Basic | 1 TB | 12 Monate | 0 € | danach 5 €/Mon.' STATUS CAVEAT: the 2026 round closed on 15.02.26 ('Nur bis 15.02.26') and the live valentinsaktion URL now 301s away, so this is NOT orderable today — it is recorded as an annual recurring window (Feb), which is what makes it the slot's only repeatable >=1 TB free allocation. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap published on the plan page | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No traffic meter appears on the HiDrive plan page; the plan is sold on capacity only. Unverified whether egress is genuinely unmetered. Strato does not publish a traffic line for HiDrive, which in the German market usually means no byte meter. | metered: no
- identity: card | detail: card
- interface: rest, webdav, sftp, ftps, rsync, smb, ssh, rclone
- limits:
  - per-object-cap (binding): No per-file cap published on the plan page [1]
- limits note: Contract term 12 months; auto-renews at €5/mo unless cancelled before expiry. This is the real trap and the reason it is 'trial-like'. Signup requires a full checkout with payment details (card/SEPA/PayPal) even at €0. No per-file cap published on the plan page.
- interface detail: rest
- tooling: Features a first-class rclone 'hidrive' backend (added v1.59, Tier 1) along with WebDAV, SMB/CIFS, SFTP/FTPS, and rsync over SSH.
- composes with: One promo contract per customer per year, but the promo is ANNUAL and structural. LowEndTalk users state 'They do this every year' (Feb 2024, Feb 2025, Feb 2026 all ran a 1 TB-for-a-year campaign). So the repeatability is temporal, not per-account: N years x 1 TB with a cancel-before-renewal ritual, or N household members x 1 TB.
- reliability: Established German host (Strato/IONOS group), German datacentre, TÜV/DSGVO claims. The recurring failure mode reported on LET is billing, not data: forget to cancel and you are charged for year two. Data itself is not reported to vanish.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB, 12 months, €0 (setup €0). Regular price after the free year is €5/month. Captured promo page states verbatim: 'HIDRIVE Basic | 1 TB | 12 Monate | 0 € | danach 5 €/Mon.' STATUS CAVEAT: the 2026 round closed on 15.02.26 ('Nur bis 15.02.26') and the live valentinsaktion URL now 301s away, so this is NOT orderable today — it is recorded as an annual recurring window (Feb), which is what makes it the slot's only repeatable >=1 TB free allocation.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'HiDrive Valentins-Aktion / 1 TB Cloud-Speicher kostenlos nutzen … HIDRIVE Basic 1 TB 12 Monate 0 € danach 5 €/Mon.'
  - [2] 2026-10-21: 'Strato offers its HiDrive Cloud with 1TB for 0 euros until 15.02.26. The period is 12 months and without setup fee'; comment: 'They do this every year, its a contract though, if you don't cancel, you renew for another year and they charge you.'
  - [3] 2026-10-21: current plan page lists protocols 'WebDAV, SMB' and a 1 TB tier at 6 €/mo list price
  - [4] 2026-10-21: rclone backend exists, 'added in v1.59', Tier 1
- sources:
  - [1] https://web.archive.org/web/20260214235234id_/https://www.strato.de/cloud-speicher/valentinsaktion/
  - [2] https://lowendtalk.com/discussion/214190/strato-hidrive-1tb-12-months-for-free
  - [3] https://www.strato.de/cloud-speicher/hidrive/
  - [4] https://rclone.org/hidrive/

## STRATO (Windows V-Server VPS XL)

- `compute/strato-windows` | paid-only | evidence documented | binding per-ip-shaping | category Windows VPS | tier Windows V-Server VPS XL
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://www.strato.de/server/windows-vserver/
- price parsed USD 74.31/mo
- free tier: no free tier; VPS XL is EUR 79.00/month including 19% VAT, and the first three months of a 12-month term are EUR 48.00/month including VAT | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists for the contract term; the 12-month table prices the first three months at EUR 48.00 and the rest at EUR 79.00
- egress: unlimited traffic on a port up to 1,000 Mbit/s; no byte quota or rate is published | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: an account and a payment method at order; the order flow is account-gated and its instrument list was not read
- interface: unknown
- limits:
  - per-ip-shaping (binding): up to 1,000 Mbit/s port [1]
  - volume-quota: traffic is called unlimited and no rate is published [1]
- limits note: prices are printed including 19% VAT; the 1-month table adds EUR 9.00 setup, the 6-month table has no setup line, and the 12-month table has no setup line
- binding note: the 1 Gbit/s port is the first hard ceiling; traffic is unlimited without a published rate.
- interface detail: RDP over a public IPv4; no public API is documented on the page read
- tooling: any RDP client; the provider's control panel
- composes with: 8 vCPU and 16 GiB for about USD 74 net a month, which is the cheapest German-market row whose licence is bundled rather than itemised
- reliability: no reliability event recorded
- notes: The EUR 79.00 is VAT-inclusive, so a buyer outside the EU pays the net EUR 66.39 if the reverse-charge rule applies; both figures are recorded because the tax basis is not established. The EUR 48.00 first-quarter rate is a promo; the steady rate is EUR 79.00 including VAT.
- evidence note: the shape, the VAT-inclusive prices and the term tables are printed on the page read. The licence is included on the evidence of the same hardware costing EUR 39.00 on the Linux page against EUR 79.00 on the Windows page, a EUR 40.00 gap; the page does not itemise it.
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 16
  - shape.disk_gib: 480
  - billing_model: monthly, 6-month or 12-month
  - term: 12 months for the promo
  - price_eur_incl_vat: 79.0
  - price_eur_net: 66.39
  - promo_eur_incl_vat: 48.0
  - promo_eur_net: 40.34
  - promo_months: 3
  - setup_fee_eur_1mo: 9.0
  - monthly_usd: 74.31
  - first_month_usd: 45.15
  - monthly_usd_incl_vat: 88.43
  - monthly_usd_net: 74.31
  - first_month_usd_incl_vat: 53.73
  - first_month_usd_net: 45.15
  - fx.pair: EUR/USD
  - fx.rate: 1.1193
  - fx.date: 2026-10-23
  - vat_note: 19% German VAT is included in the printed price; a non-EU buyer may pay the net figure, which was not confirmed at checkout
  - windows_licence: included; derived from the EUR 40.00 Linux-to-Windows gap
  - ipv4_included: yes
  - port_mbps: 1000
  - traffic: unlimited, no published rate
  - stock: orderable; no stock count published
  - cart_url: https://www.strato.de/server/windows-vserver/
- evidence:
  - [1] 2026-10-26: quoted: 'VPS XL 8 vCores 480 GB NVMe Storage 16 GB RAM 48 EUR/Mon. Aktion fuer 3 Monate danach 79 EUR/Mon.' and 'Preise inkl. MwSt.'
  - [1] 2026-10-26: the term tables print EUR 79.00 on the 1-month table with EUR 9.00 setup, and EUR 48.00 for months 1 to 3 of the 12-month table followed by EUR 79.00
  - [2] 2026-10-26: the same VPS XL hardware is EUR 39.00 on the Linux page, a EUR 40.00 gap against the Windows price that is consistent with a bundled licence
- sources:
  - [1] https://www.strato.de/server/windows-vserver/
  - [2] https://www.strato.de/server/linux-vserver/

## STRATO (VPS S)

- `egress/strato-linux-vserver-vps-s` | paid-only | evidence documented | binding per-ip-shaping | category origin VM (paid VPS) | tier VPS S
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.975Z (live) | stale on 2026-12-05
- url https://www.strato.de/server/linux-vserver/
- price EUR 4 a month including VAT; EUR 9 setup | parsed USD 4.51/mo
- free tier: no free plan: VPS S (1 vCore, 2 GB RAM, 60 GB NVMe) is EUR 4 a month including VAT plus a EUR 9 setup fee, with unlimited traffic on a connection of up to 1,000 Mbit/s | unit: unlimited | metered on: unstated | read on: 2026-11-04 | source: [1] | note: Promotions list EUR 2 a month for the first 1 or 3 months, then EUR 4 a month; no byte cap is published as a number, and a third-party index adds that the traffic is limited by port speed and fair use.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic with no extra traffic charge, on a connection of up to 1,000 Mbit/s; one IPv4 address and IPv6 included; no byte cap is published as a number on the pages read; inbound UDP policy is not stated | metered: no | free allowance: unlimited traffic on a connection of up to 1,000 Mbit/s | source: [1]
- identity: email | detail: unverified: the order flow was not read for what registration asks | country: None
- interface: ssh
- limits:
  - per-ip-shaping (binding): unlimited traffic on a connection of up to 1,000 Mbit/s; a third-party index adds a fair-use limit with no published number [1]
- limits note: No byte cap and no fair-use threshold is published with a number on the pages read.
- binding note: the port speed, not a byte count, is the stated ceiling; no fair-use threshold is published
- interface detail: SSH to the VPS public address; the vendor also lists a VNC console and a rescue system
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 4 a month origin in Germany with no stated byte cap and a one-off EUR 9 setup fee
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read
- notes: The vendor FAQ names a VPN on a small VPS as an intended workload. A third-party index lists the plan at EUR 3.36 excluding VAT, which matches the vendor EUR 4 including VAT.
- evidence note: price, setup fee, unlimited traffic and port speed are quoted from vendor pages read on 2026-11-04; the fair-use wording is from a third-party index; identity cost is unverified; no server was ordered
- extras:
  - wg_path: native-conf
  - wg_detail: a full Linux guest; wg-quick binds UDP natively unless a firewall is added; inbound UDP was not probed
  - ingress: unverified: no inbound port policy is stated on the pages read
  - volume_stated: unlimited; up to 1,000 Mbit/s; fair-use wording on a third-party index only
  - bytes_transit: yes
  - transit_note: bytes leave through the VPS's own public address
- evidence:
  - [2] 2026-11-04: VPS S (1 vCore, 2 GB RAM, 60 GB NVMe) is EUR 4 a month including VAT with a EUR 9 setup fee | capture: sha256:98594a633f8c00ad7e864c9c5ab3a9b68e3cf302db4774f6ceb305396d936d9a | quote: | VPS S | 1 vCores | 60 GB NVMe Storage | 2 GB RAM | 4 €/Mon. Einrichtung: 9 € In den Warenkorb |
  - [1] 2026-11-04: the connection is up to 1,000 Mbit/s with unlimited traffic | capture: sha256:dcdd9a53951f70add1250ae960b991030191609ce07c980e56dbe99c2c519ac4 | quote: Bis zu 1.000 MBit/s Anbindung mit unlimitiertem Traffic: Sie übertragen so viele Daten, wie Ihr Projekt braucht.
  - [1] 2026-11-04: the vendor names a VPN as a workload that runs on a small VPS | capture: sha256:dcdd9a53951f70add1250ae960b991030191609ce07c980e56dbe99c2c519ac4 | quote: Ein VPN für unterwegs läuft schon auf einem kleinen VPS
  - [3] 2026-11-04: a third-party index lists the transfer as unmetered, limited by port speed and fair use | capture: sha256:cfa6e8f5f872c7c98b0faba17a97ac33db4847149868c095cf579b0e01316a94 | quote: Unmetered (limited by port speed and fair use)
  - [2] 2026-11-04: prices include VAT | capture: sha256:98594a633f8c00ad7e864c9c5ab3a9b68e3cf302db4774f6ceb305396d936d9a | quote: Preise inkl. MwSt.
- sources:
  - [1] https://www.strato.de/server/vserver-faq/
  - [2] https://www.strato.de/server/linux-vserver/
  - [3] https://serverworth.com/plans/strato/vps-s/

## hidrive (strato)

- `storage/hidrive` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.strato.de/cloud-speicher/
- free tier: None reachable: free 5 GB tier was discontinued. The free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a T. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free 5 GB tier was discontinued. The free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a T.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: free 5 GB tier was discontinued — the free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: free 5 GB tier was discontinued — the free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a…
  - [2] 2026-10-21: cited as the basis of the rejection: free 5 GB tier was discontinued — the free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a T
  - [3] 2026-10-21: cited as the basis of the rejection: free 5 GB tier was discontinued — the free plan ended 2020-04-30; current entry plan is 500 GB at 6 EUR/month. WebDAV endpoint still live (PROPFIND -> 405 unauthenticated) and rclone has a T
- sources:
  - [1] https://www.strato.de/cloud-speicher/
  - [2] https://free.arinco.org/storage/hidrive/
  - [3] https://webdav.hidrive.strato.com/
