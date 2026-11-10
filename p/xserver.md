# XServer VPS

> xserver.ne.jp | Compute, Egress and tunnels, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xserver/ | JSON https://fshy.ajam.dev/api/v1/entity/xserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XServer VPS

- `compute/xserver-vps` | paid-only | evidence documented | binding none | category cloud VM | tier 2GB plan
- identity a placeholder: card and phone unknown | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-24
- url https://vps.xserver.ne.jp/
- price parsed USD 8.07/mo
- free tier: no free tier; the entry plan is JPY 1,265 a month for 2 GB | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: monthly; the server persists while paid | source: [1]
- egress: no traffic quota was read on the product page | metered: no | free allowance: unstated | source: [1]
- identity: card | detail: unverified: the product and price pages were read, the signup path was not. The vendor is Japanese-language only and the order form is on a separate domain (secure.xserver.ne.jp), so a card and probably a Japanese phone are involved; neither is documented here
- interface: unknown
- limits:
  - volume-quota: traffic allowance not read [1]
- limits note: The free instance survives at most 24 hours and must be renewed by hand from the control panel each day.
- binding note: the price binds: there is no shape at this vendor under USD 5 a month
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains, because no new account can be opened: the value of the record is that a Japanese reader who saw ' VPS' in 2025 arrives at a closed door in 2026.
- reliability: no reliability event recorded
- notes: The lead was worth closing: XServer is one of the largest Japanese hosts and its floor is above the line. No under-USD-5 shape exists, so nothing here can qualify whatever the identity terms are.
- evidence note: price and shape from the vendor's product page today; identity explicitly unverified
- extras:
  - facets.class: regional-free-tier-refutation
  - facets.free_tier_kind: perpetual-allowance-renewed-daily
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
  - shape.vcpu: 3
  - shape.ram_gib: 2
  - shape.disk_gib: 50
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 8.07
  - m24h_usd: 8.07
  - price_arithmetic: JPY 1,265 / 156.839696 = USD 8.07
  - renewal_usd: 8.07
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
  - english: no; Japanese only
  - payment_methods: not read
- evidence:
  - [2] 2026-10-22: the plan table gives 無料VPS 2GB as 2 GB memory, 2 vCPU, 30 GB NVMe at 月額 0円 and 無料VPS 4GB as 4 GB memory, 3 vCPU, 30 GB NVMe at 月額 0円, with 初期費用 無料; the page carries the note 'ご利用にはクレジットカードの登録が必要になります' and the signup button reads '受付停止中'
  - [3] 2026-10-22: the vendor's notice dated 2026/07/10 states, in Japanese, that new applications for both free plans are suspended because server stock is short, and that existing free users are unaffected
  - [4] 2026-10-22: the vendor's notice states that from 2026-07-22 17:00 the free plan's usable period drops from 96 hours (2 GB) and 48 hours (4 GB) to 24 hours for both, and that renewal opens when 12 hours remain
  - [5] 2026-10-22: the launch release dated 2025-07-10 gives the shape as 2 GB or 4 GB memory, 2 or 3 cores, 30 GB disk, 30 Mbps, manual renewal every four days (2 GB) or two days (4 GB), image saving unavailable
  - [1] 2026-10-24: quoted: '月額1,265円～' and '2GB 月額1,265円～ 小規模サイトや個人開発に最適 メモリ 2GB vCPU 3コア NVMe SSD 50GB'
- sources:
  - [1] https://vps.xserver.ne.jp/
  - [2] https://vps.xserver.ne.jp/free.php
  - [3] https://vps.xserver.ne.jp/support/news_detail.php?view_id=18884
  - [4] https://vps.xserver.ne.jp/support/news_detail.php?view_id=18920
  - [5] https://prtimes.jp/main/html/rd/p/000000201.000076849.html

## XServer VPS free plan

- `egress/xserver-vps-free` | dead | evidence documented | binding write-gated | category vps (hosted, Japan) | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://vps.xserver.ne.jp/free.php
- price JPY 0 per month on the free plan; paid plans from JPY 792 per month | parsed USD 5.05/mo
- free tier: [translated] 'A completely free VPS service. There is no initial cost and no monthly payment, so you can use a domestic VPS casually.' The plan table lists a 2 GB and a 4 GB free VPS at 0 yen per month. | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] 0 yen per month for the 2 GB and 4 GB plans. No traffic allowance is stated on the page. The contract-renewal row says 'manual renewal (every 1 day)' for the free plans against 'automatic renewal' for the paid ones.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: [translated] 'A credit card must be registered to use this service.' | country: None
- interface: ssh, cli, rest
- limits:
  - write-gated (binding): [translated] 'manual renewal (every 1 day)' on the free plans; the paid plans renew automatically [1]
- binding note: A control-panel action every day stands between the account and the server surviving. That is a manual act, not a byte count, so it binds before any volume does. It is also moot today: the signup button for the free plans reads 'not accepting applications'.
- interface detail: [translated] 50+ OS and application images install automatically when the order completes; the panel restarts and reinstalls the guest.
- tooling: wg-quick inside the guest; SSH; the panel installs an OS or app image at order time
- composes with: If it reopens: a free Japanese root guest is the endpoint for everything else in this topic, and the daily renewal is the one job it needs.
- reliability: Daily manual renewal with deletion on a missed day; the page's own footnote says an automatic detection system may throttle guests that load the host excessively.
- notes: Read carefully because it looked like the answer: a Japanese 0-yen VPS with a root guest would pass the ingress test outright. Two facts kill it. The signup is closed ('not accepting applications'). And the renewal row means the server is deleted unless a human clicks a renewal every day, which no unattended workload survives. Country: Japan. The free plan carries 50 GB of disk standard with a 500 GB option per the page footnotes.
- evidence note: The 0 yen price, the card requirement, the daily manual renewal and the closed signup are all on the vendor page read on 2026-10-23. What no page establishes is whether a free guest gets a public IPv4; a probe would. Applications may reopen, which would make this the strongest Japanese free host.
- extras:
  - wg_path: native-conf
  - wg_detail: A KVM guest with root and a choice of 50+ OS images including Debian 12/13 and Ubuntu 22.04/24.04/26.04, so wg-quick runs in the guest. No configuration is issued by the vendor.
  - ingress: tcp+udp
  - volume_stated: [translated] 0 yen per month for the 2 GB and 4 GB plans. No traffic allowance is stated on the page. The contract-renewal row says 'manual renewal (every 1 day)' for the free plans against 'automatic renewal' for the paid ones.
  - bytes_transit: yes
  - transit_note: A domestic Japanese guest address carries the traffic.
- evidence:
  - [1] 2026-10-23: [translated] 'A completely free VPS service. There is no initial cost and no monthly payment.' Free plans are 2 GB and 4 GB at 0 yen per month.
  - [1] 2026-10-23: [translated] 'A credit card must be registered to use this service.'
  - [1] 2026-10-23: [translated] The free plans' contract-renewal row reads 'manual renewal (every 1 day)'; the paid plans read 'automatic renewal'. The free-plan signup button reads 'not accepting applications'.
- sources:
  - [1] https://vps.xserver.ne.jp/free.php

## xserver vps storage expansion

- `storage/xserver-vps-storage-expansion` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://vps.xserver.ne.jp/support/manual/man_server_storage_expansion.php
- free tier: none reachable: The 200 GB storage add-on was discontinued for all new signups on 2025-02-03; the maximum disk on any current plan is 2,400 GB and only on 4 GB+ plans. Not purchasable for a new customer… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: The 200 GB storage add-on was discontinued for all new signups on 2025-02-03; the maximum disk on any current plan is 2,400 GB and only on 4 GB+ plans. Not purchasable for a new customer…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 200 GB storage add-on was discontinued for all new signups on 2025-02-03; the maximum disk on any current plan is 2,400 GB and only on 4 GB+ plans. Not purchasable for a new customer…
  - [2] 2026-10-21: cited as the basis of the rejection: The 200 GB storage add-on was discontinued for all new signups on 2025-02-03; the maximum disk on any current plan is 2,400 GB and only on 4 GB+ plans. Not purchasable for a new customer and
- sources:
  - [1] https://vps.xserver.ne.jp/support/manual/man_server_storage_expansion.php
  - [2] https://vps.xserver.ne.jp/support/news_detail.php?view_id=14581
