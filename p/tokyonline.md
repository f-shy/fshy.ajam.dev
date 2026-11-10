# Tokyonline

> tokyonline.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokyonline/ | JSON https://fshy.ajam.dev/api/v1/entity/tokyonline.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tokyonline

- `ip-proxy/tokyonline-so-net-vps` | paid-only | evidence documented | binding none | category ISP-registered VPS | tier Tokyo zone So-Net Standard, Pro, Extreme and Unlimited
- needs card yes, phone yes, ID no, institution no | verified 2026-11-03T07:35:32.672Z (live) | stale on 2026-12-04
- url https://www.tokyonline.com/cart.php
- free tier: No free tier. So-Net Standard is JPY 8,800 a month: 2 vCPU, 2 GB RAM, 30 GB HDD, 1 Tokyo-zone IPv4, 10240 GiB transfer, 200 Mbps port. So-Net Pro is JPY 12,800 a month (4 GB RAM, 50 GB, 15360 GiB, 300 Mbps) and the Unlimited plan is JPY 25,800 a month with unlimited transfer at a 300 Mbps port. All displayed prices are stated as tax included. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: Prices are in Japanese yen as the vendor prints them. The cart showed stock counts beside each So-Net plan (5, 14, 10 and 1 available).
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented machine and its address, not stored bytes. The terms on non-payment are unverified: the cart and home page state none. | source: [1]
- egress: Transfer is allowed per month in GiB per plan: 10240 GiB on So-Net Standard, 15360 GiB on So-Net Pro, 30720 GiB on Extreme, unlimited on the Unlimited plan. No overage price is stated. Each plan also carries a notice that BitTorrent and banking-web use is banned. | metered: yes | free allowance: 10240 GiB per month on So-Net Standard; unlimited on So-Net Unlimited | source: [1]
- identity: any-phone | detail: The registration form asks for family name, given name, email address, phone number, city and postal code and a captcha; only the company name is marked optional. The form as read stops before the payment step, so any identity check at payment is unverified. A review states payment by credit card and Alipay.
- interface: unknown
- limits:
  - volume-quota: 10240 GiB per month on So-Net Standard, 15360 GiB on So-Net Pro; unlimited on So-Net Unlimited [1]
- limits note: The vendor's own pages sell a Tokyo-zone So-Net or KDDI address and do not use the word residential. The double-ISP residential label comes from a third-party review. No test address is published on the pages read, so no registry lookup was possible.
- binding note: The smallest monthly allowance, 10240 GiB, is far above a low-volume exit, so no quota binds. What decides the record is the registration class of the delivered address, which is unverified.
- interface detail: A virtual server with one fixed Tokyo-zone IPv4 address. The access method (SSH or RDP) is not stated on the cart or home page; the vendor describes a self-service console.
- tooling: An SSH or RDP client, whichever the image supports, plus a proxy or tunnel daemon the user installs on the machine. The vendor publishes no proxy endpoint and no API on the pages read.
- composes with: A Worker opens an outbound connection to the server's fixed IPv4 and the server makes the upstream request, so the upstream sees an address in the So-Net or KDDI network the plan names instead of AS13335.
- reliability: Stock is shown per plan, with one So-Net Unlimited unit available when read. Bandwidth peaks are port rates; the review sites report the plan names but this record holds no measurement of delivered throughput.
- notes: Tokyonline's own pages sell Tokyo-zone KVM servers on So-Net and KDDI networks priced in yen; the residential or double-ISP label is third-party.
- evidence note: Prices, allowances and the registration form fields are documented from the vendor's cart and registration page. That the addresses are residential or double-ISP is reported by a third-party review and is unverified here. Nothing was measured.
- extras:
  - rung: 5
  - rung_note: The offer is a claim about the address class and no test address is published, so no registry check was possible.
- evidence:
  - [1] 2026-11-03: So-Net Standard is priced JPY 8,800 a month | capture: sha256:6100aae2879c07f72a9e11bc33cb1e21159018f87948709e5aa9bff9c1df868a | quote: ¥8,800JPY
  - [1] 2026-11-03: So-Net Standard includes 10240 GiB of transfer | capture: sha256:6100aae2879c07f72a9e11bc33cb1e21159018f87948709e5aa9bff9c1df868a | quote: 10240GiB Transfer Data
  - [1] 2026-11-03: the Unlimited plan has unlimited transfer | capture: sha256:6100aae2879c07f72a9e11bc33cb1e21159018f87948709e5aa9bff9c1df868a | quote: Unlimited Transfer Data
  - [1] 2026-11-03: each plan bans BitTorrent and banking-web use | capture: sha256:6100aae2879c07f72a9e11bc33cb1e21159018f87948709e5aa9bff9c1df868a | quote: BT/PT・銀行ウェブ禁止
  - [2] 2026-11-03: So-Net Pro is JPY 12,800 a month | capture: sha256:37651ddec6b660aa90e5cc417b8e4758f015d6a9c22dc4648e78628536bd13cb | quote: JPY 12,800
  - [2] 2026-11-03: So-Net Pro includes 15360 GiB of bandwidth | capture: sha256:37651ddec6b660aa90e5cc417b8e4758f015d6a9c22dc4648e78628536bd13cb | quote: 15360 GiB Bandwidth
  - [3] 2026-11-03: the registration form asks for a phone number | capture: sha256:df2fb71a4933c18ade73559d222721e66f93e9929d14803fa628c6d8da64a3a2 | quote: 電話番号
  - [3] 2026-11-03: only the company name is marked optional on the registration form | capture: sha256:df2fb71a4933c18ade73559d222721e66f93e9929d14803fa628c6d8da64a3a2 | quote: 会社名（個人の場合、記入不要） (オプショナル)
  - [4] 2026-11-03: a third-party review calls the addresses double-ISP residential | capture: sha256:3412714fa886ba3f07f1cc9bfabbb89f92ceadad8a36bbf21c869bbd3766986e | quote: IP有特色为双ISP属性/住宅IP
  - [4] 2026-11-03: a third-party review states payment by credit card and Alipay | capture: sha256:3412714fa886ba3f07f1cc9bfabbb89f92ceadad8a36bbf21c869bbd3766986e | quote: 支持信用卡、支付宝付款。
- sources:
  - [1] https://www.tokyonline.com/cart.php
  - [2] https://www.tokyonline.com/
  - [3] https://www.tokyonline.com/register.php
  - [4] https://www.zhujiceping.com/74468.html
