# hostdare hdd

> hostdare.com | Egress and tunnels, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostdare/ | JSON https://fshy.ajam.dev/api/v1/entity/hostdare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostDare

- `egress/hostdare-ssd1` | paid-only | evidence documented | binding volume-quota | category cheap KVM VPS | tier SSD1
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.032Z (live) | stale on 2026-12-05
- url https://www.hostdare.com/vps.html
- free tier: No free tier. SSD1 is USD 39.99 a year on the vendor's list: 1 core, 1024 MB RAM, 25 GB, 1000 GB bandwidth, 1 IPv4 and a /64 IPv6. The cheapest list tier, SSD0, is USD 25.99 a year with 500 GB. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The aggregator lists SSD1 at USD 16 a year with 2000 GB through a promo code; the vendor list read shows 1000 GB and USD 39.99, so the doubled allowance and the price are not on the vendor page.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 1000 GB bandwidth on SSD1 with no period on the table row; each cloud server is limited at 300 Mbps on a 1000 Mbps node uplink; no overage price is published on the page read. | metered: yes | free allowance: 1000 GB, period not stated on the row | source: [1]
- identity: email | detail: unverified: behind a sign-up. The registration page asks for an image captcha ('Please enter the characters you see in the image below'); its other fields and the payment methods are not shown to a text read.
- interface: ssh, sftp
- limits:
  - volume-quota (binding): 1000 GB bandwidth, period not stated on the row [1]
  - per-ip-shaping: each cloud server limited at 300 Mbps [1]
- binding note: 1000 GB is the first number to fail; RAM and disk bind what runs rather than what fails on a schedule.
- interface detail: Root SSH and SFTP on an SSD KVM VPS in Los Angeles; the page names no port or protocol filter.
- tooling: Any SSH client or SFTP client.
- composes with: A 300 Mbps Los Angeles box with a dedicated IPv4 and a /64 IPv6: about 1000 GB of outbound fits a small fetch or relay node; the refund clause is the only usage tolerance stated.
- reliability: unverified: no uptime or suspension statement was read on the page.
- notes: The vendor list is USD 25.99 to 130.99 a year for SSD0 to SSD3; the aggregator's USD 16 a year with 2000 GB is a promo-code price that the list does not show.
- evidence note: Price, allowance and port limit are quoted from the vendor's plan table and feature text. Identity fields and payment methods are behind a sign-up.
- extras:
  - location: Los Angeles
  - port_cap_mbps: 300
- evidence:
  - [1] 2026-11-04: SSD1 is USD 39.99 a year with 1 core, 1024 MB, 25 GB, 1000 GB bandwidth, 1 IPv4 and a /64 IPv6 | capture: sha256:a7f3bd7ec34bec28d0393f1aef5e9667a42a61ecfbe60d3b195c3933ca30c220 | quote: | SSD1 | 1 Core | 1024 MB | 25 GB | 1000 GB | 1 | /64 | $39.99/yr |
  - [1] 2026-11-04: the cheapest list tier SSD0 is USD 25.99 a year with 500 GB | capture: sha256:a7f3bd7ec34bec28d0393f1aef5e9667a42a61ecfbe60d3b195c3933ca30c220 | quote: | SSD0 | 1 Core | 512 MB | 10 GB | 500 GB | 1 | /64 | $25.99/yr |
  - [1] 2026-11-04: each cloud server is limited at 300 Mbps on a 1000 Mbps node uplink | capture: sha256:a7f3bd7ec34bec28d0393f1aef5e9667a42a61ecfbe60d3b195c3933ca30c220 | quote: All server nodes comes with 1000 Mbps uplink, while individual cloud servers are limited at 300 Mbps.
  - [1] 2026-11-04: the only stated usage tolerance is that 20 per cent or more of the monthly allocation can void a refund | capture: sha256:a7f3bd7ec34bec28d0393f1aef5e9667a42a61ecfbe60d3b195c3933ca30c220 | quote: refund requests may be declined if you've utilized 20% or more of your allocated bandwidth on a monthly basis
  - [1] 2026-11-04: root SSH and SFTP are available | capture: sha256:a7f3bd7ec34bec28d0393f1aef5e9667a42a61ecfbe60d3b195c3933ca30c220 | quote: You can use full root SSH and SFTP access to install programs and fine-tune your system to your liking.
  - [2] 2026-11-04: registration carries an image captcha; the other fields are not shown to a text read | capture: sha256:b716feedd314ae5eb801c4f1640bdacf422ef2e0819b3c893bdef03872be4e5a | quote: Please enter the characters you see in the image below into the text box provided. This is required to prevent automated submissions.
  - [3] 2026-11-04: the aggregator lists an SSD1 plan at USD 16 a year with 2000 GB, which differs from the vendor list | quote: ###### SSD1
- sources:
  - [1] https://www.hostdare.com/vps.html
  - [2] https://bill.hostdare.com/register.php
  - [3] https://serverdeals.cc/

## hostdare hdd vps

- `storage/hostdare-hdd-vps` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:54.245Z (live) | stale on 2026-12-04
- url https://www.hostdare.com/hddvps.html
- free tier: none: paid VPS only; the largest HDD plan is HDD8 with 900 GB of HDD storage and 8000 GB/mo of bandwidth at $151.99/yr | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 900 GB of HDD storage on the largest plan (HDD8), 8000 GB/mo of bandwidth [1]
- limits note: best price per TB is HDD8: $151.99/yr for 900 GB of HDD storage = about $14.07 per TB per month
- binding note: no plan exceeds 900 GB of HDD storage (HDD8, $151.99/yr); best price per TB is HDD8
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The HDD8 order cart answered 'out of stock' on 2026-11-03.
- notes: The HDD line maxes at 900 GB and the best $/GB is HDD8 (900 GB, 8 TB transfer) at $151.99/yr = $14.07/TB/mo. Nothing ≥1 TB exists, and the 'DEAL50' recurring coupon referenced in forums…
- evidence note: the 2026-11-03 evidence rows read the vendor plan page https://www.hostdare.com/hddvps.html (the HDD8 row: 900 GB, 8000 GB/mo, $151.99/yr) and the HDD8 order cart through a cart probe, which answered out of stock; sign-up fields were not read
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The HDD line maxes at 900 GB and the best $/GB is HDD8 (900 GB, 8 TB transfer) at $151.99/yr = $14.07/TB/mo. Nothing ≥1 TB exists, and the 'DEAL50' recurring coupon referenced in forums…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The HDD line maxes at 900 GB and the best $/GB is HDD8 (900 GB, 8 TB transfer) at $151.99/yr = $14.07/TB/mo. Nothing ≥1 TB exists, and the 'DEAL50' recurring coupon referenced in forums…
  - [1] 2026-11-03: HDD8 is the largest-storage plan listed: 900 GB, 8000 GB/mo, $151.99/yr | capture: sha256:931ebeb30231973fa8d6cc94a5e2c4bb255a3b615a2ff1fa6870111360b2c890 | quote: | HDD8 | 3 Cores | 4 GB | 900 GB | 8000 GB/mo | 1 | 500 mbps | $151.99/yr |
  - probe:hostdare-hdd8-cart 2026-11-03: the HDD8 cart page reported the plan out of stock | capture: sha256:494297f182ec526093e77fac18c1018aa7206f630e56024604ffc6ca9bfd834b | quote: "out of stock"
  - [1] 2026-11-03: the HDD plan table still tops out at 900 GB | capture: sha256:931ebeb30231973fa8d6cc94a5e2c4bb255a3b615a2ff1fa6870111360b2c890 | quote: | HDD8 | 3 Cores | 4 GB | 900 GB | 8000 GB/mo | 1 | 500 mbps | $151.99/yr |
- sources:
  - [1] https://www.hostdare.com/hddvps.html
