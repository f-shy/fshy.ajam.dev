# ConoHa VPS

> conoha.jp | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/conoha/ | JSON https://fshy.ajam.dev/api/v1/entity/conoha.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ConoHa VPS

- `compute/conoha-vps` | qualifies | evidence documented | binding none | category cloud VM | tier メモリ1GB (1 GB plan)
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T06:40:18.802Z (live) | stale on 2026-12-05
- url https://vps.conoha.jp/
- price parsed USD 4.86/mo
- free tier: no free tier; the plans start at JPY 460 a month for 512 MB and JPY 763 a month for 1 GB | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: the instance persists while the monthly plan is paid; the page prints the renewal price beside the first-term price | source: [1]
- egress: data transfer JPY 0 and 無制限 (unlimited) on the configuration examples on the plan page | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: email signup and a payment method: VISA, MasterCard, JCB, American Express and Diners Club, plus PayPal, Amazon Pay, convenience-store payment and bank transfer through the prepaid 'ConoHaチャージ' wallet. American Express and Diners Club are restricted to Japan residents, which implies the other cards and PayPal are not. No Japanese phone or ID step is documented on the payment or flow pages read; the signup form itself was not fetched
- interface: rest
- limits:
  - per-ip-shaping: no traffic quota stated; transfer is 無制限 (unlimited) [1]
- limits note: The coupon is JPY 360 once, so it buys days rather than a month, and the server keeps billing after the coupon is gone unless it is deleted.
- binding note: neither traffic nor time binds: the 1 GB of RAM is what fails first, and the 512 MB plan at JPY 460 exists precisely because 1 GB is the useful floor
- interface detail: REST API: an OpenStack-compatible public API (ConoHa VPS 3.0) for creating, deleting and resizing servers, documented at doc.conoha.jp; SSH public-key access to servers; the web control panel
- tooling: OpenStack CLI and a Terraform Provider, both documented by the provider; the public API reference is at doc.conoha.jp
- composes with: JPY 460 a month for 512 MB is the cheapest Japanese floor found, and the JPY 360 coupon is about 78 percent of one month on that plan, so the coupon is one free month at the bottom of the ladder rather than a trial of the useful sizes.
- reliability: no reliability event recorded
- notes: The site is Japanese only; the order flow was not walked. The 2 GB plan is JPY 1,007 first term and JPY 1,259 on renewal, so only the 1 GB row is under the line at renewal.
- evidence note: plan table and renewal prices from the plan page read; payment rails from the vendor's pricing and flow pages
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
  - shape.vcpu: 2
  - shape.ram_gib: 1
  - shape.disk_gib: 100
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 4.86
  - m24h_usd: 4.86
  - price_arithmetic: JPY 763 a month divided by the 2026-10-24 rate 156.839696 JPY/USD = USD 4.86; the page prints the same 763 on renewal
  - renewal_usd: 4.86
  - fx.pair: USD/JPY
  - fx.rate: 156.839696
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS that bills whether it runs or not
  - english: no; the site and console are Japanese only
  - payment_methods: VISA, MasterCard, JCB (Amex and Diners for Japan residents only), PayPal, Amazon Pay, convenience store, bank transfer
- evidence:
  - [2] 2026-10-22: the campaign page states, in Japanese, that a JPY 360 coupon is given to accounts newly registered from that page with a credit card registered, and publishes a table converting the coupon into free days per plan: about 11.5 days on 512 MB, 7.9 on 1 GB, 4.1 on 2 GB, 2.3 on 4 GB, 1.1 on 12 GB, 14.9 hours on 24 GB, 7.4 hours on 48 GB, 3.7 hours on 96 GB and 2.8 hours on 128 GB; GPU types are excluded; the campaign ended 2026-10-01 16:00
  - [3] 2026-10-22: the support FAQ states, in Japanese, that there is no free trial service, and points to a referrer programme instead
  - [4] 2026-10-22: the pricing page gives the ladder in Japanese yen: 512 MB with 1 core and 30 GB SSD at JPY 460 a month on hourly billing, and 1 GB with 2 cores and 100 GB at JPY 763 a month
  - [1] 2026-10-24: quoted: 'メモリ 1 GB ... 763 円/月 更新時 763 円/月 - CPU 2コア - SSD 100GB'
  - [1] 2026-10-24: quoted: 'メモリ 512 MB ... 460 円/月 更新時 460 円/月 - CPU 1コア - SSD 30GB'
  - [1] 2026-10-24: quoted from the configuration table: 'データ転送量 0円 無制限'
  - [4] 2026-10-24: quoted: 'VISA / MasterCard / JCB / American Express / Diners Club 各種クレジットカードをご利用いただけます。' and 'American Express / Diners Club は日本国内に在住の方のみご利用いただけます。' and the PayPal and Amazon Pay options
  - [1] 2026-11-04: an OpenStack-compatible API is published | capture: sha256:223d005f820e6e61c09a68f348b8459ee481da8590b022267b37f50ad6d9c47f | quote: API サーバー作成・削除・スペック変更をプログラムで自動化。OpenStack準拠のAPIを公開
  - [1] 2026-11-04: the VPS FAQ states a public OpenStack-compatible API for server operations | capture: sha256:223d005f820e6e61c09a68f348b8459ee481da8590b022267b37f50ad6d9c47f | quote: ConoHa VPS 3.0はOpenStack準拠の公開APIを提供しており、サーバーの作成・削除・スペック変更などをプログラムから操作できます。
  - [1] 2026-11-04: the FAQ states Terraform Provider support | capture: sha256:223d005f820e6e61c09a68f348b8459ee481da8590b022267b37f50ad6d9c47f | quote: Terraform Providerにも対応しているためインフラをコードで定義・管理（IaC）することが可能です。
- sources:
  - [1] https://vps.conoha.jp/
  - [2] https://vps.conoha.jp/campaign/freestart2026/
  - [3] https://support.conoha.jp/common/faq/subscription-q/
  - [4] https://vps.conoha.jp/pricing/

## conoha (jp) object storage

- `storage/conoha-object-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.conoha.jp/vps/faq/objectstorage-q/
- free tier: none reachable: ₩450/100 GB/mo = ¥4,500/TB = $28.50/TB. Its headline pitch is 'unlimited capacity, free data transfer', which is true and irrelevant at 6x the floor. Requires a Japanese payment method. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: ₩450/100 GB/mo = ¥4,500/TB = $28.50/TB. Its headline pitch is 'unlimited capacity, free data transfer', which is true and irrelevant at 6x the floor. Requires a Japanese payment method.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: ₩450/100 GB/mo = ¥4,500/TB = $28.50/TB. Its headline pitch is 'unlimited capacity, free data transfer', which is true and irrelevant at 6x the floor. Requires a Japanese payment method.
  - [2] 2026-10-21: cited as the basis of the rejection: ₩450/100 GB/mo = ¥4,500/TB = $28.50/TB. Its headline pitch is 'unlimited capacity, free data transfer', which is true and irrelevant at 6x the floor. Requires a Japanese payment method.
- sources:
  - [1] https://support.conoha.jp/vps/faq/objectstorage-q/
  - [2] https://vps.conoha.jp/pricing/
