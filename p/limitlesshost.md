# Limitless Hosting

> limitlesshost.net | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/limitlesshost/ | JSON https://fshy.ajam.dev/api/v1/entity/limitlesshost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Limitless Hosting (Compute)

- `compute/limitless-hosting` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://limitlesshost.net/
- free tier: USD 25.20/year for KVM VPS Starter in Chicago with coupon 10THVPS: 1 vCPU, 1 GB RAM, 10 GB SSD, 250 GB monthly bandwidth, 1 IPv4. KVM VPS 1 is USD 50.40/year for 2 vCPU, 2 GB, 20 GB and 500 GB; KVM VPS 2 is USD 86.40/year for 3 vCPU, 4 GB, 40 GB and 1 TB. The same sale prices shared hosting from USD 2.40/year for 1 GB of SSD and 50 GB of monthly bandwidth, and premium shared hosting from USD 4.32/year. All coupons are recurring for as long as the account renews annually, and every discount applies to annual plans only. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 250 GB a month on the Starter VPS, 500 GB on VPS 1 and 1 TB on VPS 2; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 250 GB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 250 GB a month on the Starter VPS is the smallest allowance among evaluated providers and the one that binds first by a wide margin: it is about 0.77 Mbit/s sustained, so the counter is the wall and the port is irrelevant. The shared plans carry 50 GB to 200 GB a month. No overage price and no post-allowance throttle are stated. [1]
- limits note: 250 GB a month on the Starter VPS is the smallest allowance among evaluated providers and the one that binds first by a wide margin: it is about 0.77 Mbit/s sustained, so the counter is the wall and the port is irrelevant. The shared plans carry 50 GB to 200 GB a month. No overage price and no post-allowance throttle are stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor sells cPanel, DirectAdmin and WHMCS licences alongside the plans and names a Blesta owned licence in the same sale; no API or CLI is documented for the VPS line on either page read
- composes with: USD 25.20/year is USD 2.10/month for a 1 GB machine with 250 GB of monthly transfer, which is the cheapest annual VPS among evaluated providers, and the same invoice can carry a mailbox and a small site; 250 GB a month is too little for a crawler, so the job it fits is a cron box, a monitor or a jump host.
- reliability: no reliability event recorded
- notes: json mentions the word for an unrelated reason). The record is reported because the vendor page carries no prices at all. verification criteria: whether 10THVPS still applies after the anniversary sale closes, and whether the Chicago VPS is the only location, since the post lists Frankfurt only for the EU shared and reseller lines. The post prices the same sale's shared plans in USD while the company describes itself as trading since 2015 and 2016 in two different paragraphs, which is a discrepancy in the prose and not in a number.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [2] 2026-10-22: third-party offer post, published 2026-09-01, quoted from its VPS table: 'KVM VPS Starter $25.20/year 1 vCPU 1 GB RAM 10 GB SSD 250 GB Bandwidth 1 IPv4 Coupon Code: 10THVPS'; notes section: 'All coupons are recurring for as long as you renew annually' and 'This is a limited-time 10th Anniversary Sale'; USA location given as 'Chicago, IL (US)' with test IPv4 169.197.131.90
  - [1] 2026-10-22: the vendor homepage was read and carries no plan table or price: it is a marketing page with product cards, '99% Uptime', and a history section; so the VPS prices rest on the offer post alone
- sources:
  - [1] https://limitlesshost.net/
  - [2] https://lowendbox.com/blog/limitless-hosting-10th-anniversary-sale-shared-hosting-reseller-hosting-and-vps-from-just-2-40-year/

## Limitless Hosting (KVM VPS Starter)

- `egress/limitless-hosting-kvm-vps-starter` | paid-only | evidence reported | binding volume-quota | category vps (hosted, Chicago, KVM, one IPv4) | tier KVM VPS Starter
- identity a placeholder: card and phone unknown | verified 2026-11-04T12:11:58.417Z (live) | stale on 2026-11-19
- url https://limitlesshost.net/
- price USD 25.20 per year with 250 GB bandwidth included (about USD 2.10 a month) | parsed USD 8.4/TB-mo
- free tier: No free tier. KVM VPS Starter is USD 25.20 a year with coupon 10THVPS, recurring on annual renewal: 1 vCPU, 1 GB RAM, 10 GB SSD, 250 GB bandwidth and one IPv4, in Chicago. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 250 GB bandwidth on the Starter (500 GB on KVM VPS 1 and 1 TB on KVM VPS 2). The terms say each plan has a predetermined traffic allowance and that accounts are monitored; overage price, port speed and post-allowance behaviour are not published in the pages read. | metered: yes | free allowance: 250 GB | source: [1]
- identity: email | detail: unverified: behind a sign-up. The post lists PayPal, cards, Bitcoin and Skrill; no phone or ID requirement is stated in the pages read.
- interface: ssh
- limits:
  - volume-quota (binding): 250 GB bandwidth on KVM VPS Starter; overage rule not published [1]
- binding note: The 250 GB bandwidth line is the only stated limit on the Starter; the overage rule is not published.
- interface detail: A KVM VPS; the panel and the access method were not read.
- tooling: ssh; the panel and guest tooling were not read.
- composes with: One IPv4 and no IPv6 or NAT statement; no port set is published.
- reliability: The coupon price is for annual plans only per the offer post; a sale page, so the price can be withdrawn.
- notes: Chicago KVM VPS with 250 GB bandwidth; IPv6 and port speed not stated.
- evidence note: Price, bandwidth and location come from a third-party offer post dated 1 September 2026; the vendor home page lists no VPS plan.
- extras:
  - nat: none stated; one IPv4 is listed
  - ipv6: not stated
  - inbound: not stated
  - udp: not stated
- evidence:
  - [1] 2026-11-04: KVM VPS Starter is USD 25.20 a year with 250 GB bandwidth and one IPv4 | capture: sha256:e3f053dc7b3c44000d4b1199f7e5643c50571cdb7e52a4aa3c6edba13aa8561d | quote: $25.20/year**1 vCPU1 GB RAM10 GB SSD250 GB Bandwidth1 IPv4
  - [1] 2026-11-04: the coupon price recurs on annual renewal | capture: sha256:e3f053dc7b3c44000d4b1199f7e5643c50571cdb7e52a4aa3c6edba13aa8561d | quote: All coupons are recurring for as long as you renew annually.
  - [1] 2026-11-04: PayPal, cards, Bitcoin and Skrill are accepted | capture: sha256:e3f053dc7b3c44000d4b1199f7e5643c50571cdb7e52a4aa3c6edba13aa8561d | quote: They accept PayPal, credit/debit cards, Bitcoin, and Skrill.
  - [1] 2026-11-04: the VPS location is Chicago | capture: sha256:e3f053dc7b3c44000d4b1199f7e5643c50571cdb7e52a4aa3c6edba13aa8561d | quote: Chicago, IL (US)
  - [2] 2026-11-04: the terms state a predetermined traffic allowance without a number or an overage rule | capture: sha256:60898507006badfe2918aa65f08ee83fa0fac5c13f9958ead6b45c8e1d582d01 | quote: All account plans come with a predetermined amount of traffic allowance. We monitor all accounts.
  - [1] 2026-11-04: the post is dated 1 September 2026 | capture: sha256:e3f053dc7b3c44000d4b1199f7e5643c50571cdb7e52a4aa3c6edba13aa8561d | quote: Sep 01, 2026 @ 7:00 am
- sources:
  - [1] https://lowendbox.com/blog/limitless-hosting-10th-anniversary-sale-shared-hosting-reseller-hosting-and-vps-from-just-2-40-year/
  - [2] https://limitlesshost.net/terms-of-service/
