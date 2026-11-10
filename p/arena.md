# WebARENA Indigo

> arena.ne.jp | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arena/ | JSON https://fshy.ajam.dev/api/v1/entity/arena.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WebARENA Indigo

- `compute/webarena-indigo` | qualifies | evidence documented | binding per-ip-shaping | category cloud VM | tier メモリ1GB / Linux
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T05:24:50.431Z (live) | stale on 2026-12-05
- url https://web.arena.ne.jp/indigo/price/
- price parsed USD 2.86/mo
- free tier: no free tier and no setup fee; billing is hourly with a monthly cap, JPY 409 a month (JPY 449 with tax) for 1 GB, JPY 290 (JPY 319) for the IPv6-only 768 MB shape | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: the instance bills from creation to deletion, including while stopped: '停止中のインスタンスにも料金は発生します。' | source: [1]
- egress: no traffic volume quota stated; the port is capped at 100 Mbit/s on the 1 GB and 2 GB shapes and 500 Mbit/s on the 4 GB shape | metered: no | free allowance: unlimited: no data transfer volume limit; port speed capped per shape; no overage price | source: [1]
- identity: card | detail: the signup flow is email verification, then SMS or automated-voice phone verification, then card registration: 'メール認証', 'SMSまたは電話認証', 'クレジットカード登録'. No charge is raised at card registration: 'クレジットカード登録時点で料金は発生しません。インスタンス作成後に料金が発生します。' A separate eKYC identity check exists whose accepted documents are all Japanese (driving licence, My Number card, residence card, a Japanese-issued passport); which signup paths require it was not established
- interface: rest, ssh
- limits:
  - per-ip-shaping (binding): 100 Mbit/s port on the 1 GB shape [1]
- limits note: The entry shapes are capped at 100 Mbps and the 768 MB shape has no IPv4 address at all, so the first thing that fails is anything that needs a public IPv4 or a fast outbound path; the monthly floor of JPY 50 (JPY 55 with tax) is the second: a month with any usage at all costs at least that.
- binding note: the 100 Mbit/s port and the 20 GB disk bind before the traffic does; there is no traffic quota to run out of
- interface detail: The spec page documents a REST API (English-only API documentation at indigo.arena.ne.jp/userapi/, access token by POST to /oauth/v1/accesstokens) and public-key SSH login to instances.
- tooling: No client library or CLI is named: the spec page and the API document at indigo.arena.ne.jp/userapi/ were read and describe the REST API with cURL examples only.
- composes with: At JPY 0.48 an hour with no minimum term, a 768 MB instance costs about JPY 12 for a day, which is the cheapest way found in Japan to hold a reachable IPv6 box for a single job; the missing IPv4 pushes any client that needs one to the JPY 0.64 1 GB shape.
- reliability: no reliability event recorded
- notes: Prices on the page are shown pre-tax with the tax-inclusive figure in parentheses, and both are recorded. The 10 h/day figure uses the hourly rate because this product is billed hourly; the 24/7 figure is the monthly cap. The Japanese site is the only route; no English page was found.
- evidence note: the whole price table and the billing rules are from the vendor's own price page read; the signup steps from the vendor's own flow page
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.75
  - facets.shape.gpu_count: 0
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 20
  - billing_model: hourly with a monthly cap
  - term: hourly, capped monthly
  - m10h_usd: 1.34
  - m24h_usd: 2.86
  - price_arithmetic: 24/7: 730 h x JPY 0.70 = JPY 511, above the JPY 449 monthly cap, so the cap binds: 449/156.839696 = USD 2.86. 10 h/day: 300 h x JPY 0.70 = JPY 210 = USD 1.34
  - renewal_usd: 2.86
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
  - payment_methods: credit card; SMS or voice OTP at signup
- evidence:
  - [1] 2026-10-22: the price table gives 768MB/1vCPU/20GB at 0.48円 per hour with a 290円 monthly cap and IPv6 only, 1GB/1vCPU/20GB at 0.64円 capped at 409円 with IPv4, 2GB/2vCPU/40GB at 1.16円 capped at 740円, 4GB/4vCPU/80GB at 2.32円 capped at 1,482円 at 500Mbps, 8GB/6vCPU/160GB at 4.87円 capped at 3,100円 at 1Gbps, with 初期料金 and 最低利用期間 both none; the page also fixes a minimum monthly charge of 50円 (55円 with tax)
  - [2] 2026-10-22: the function list states 'データ転送量 制限はありません' and gives the network ceiling per shape as 100 Mbps up to the 2 GB plan, 500 Mbps at 4 GB and 1 Gbps at 8 GB and above
  - [1] 2026-10-24: quoted: '| 1GB | 1vCPU | 20GB | 100Mbps上限 | IPv4/IPv6 | 0.64円（税込0.70円） | 409円（税込449円） |'
  - [1] 2026-10-24: quoted: '| 768MB（※） | 1vCPU | 20GB | 100Mbps上限 | IPv6 | 0.48円（税込0.52円） | 290円（税込319円） |' and '（※）メモリタイプ768MBのインスタンスは、IPv6のIPアドレスに対応しています。IPv4アドレスには対応していません。'
  - [1] 2026-10-24: quoted: '停止中のインスタンスにも料金は発生します。' and '月額最大319円（税込）/1時間当たり0.52円（税込）～'
  - [3] 2026-10-24: quoted signup flow: 'メール認証 / SMSまたは電話認証 / クレジットカード登録' and 'クレジットカード登録時点で料金は発生しません。インスタンス作成後に料金が発生します。'
  - [2] 2026-11-03: a REST API is offered | capture: sha256:8f19ef4cd0a02889cb8bb3fc49aa027d7bac689863d62a75e212650db69e71cc | quote: | Rest-API | Rest-APIが利用できます。APIドキュメント（英語のみ）は[こちら](https://indigo.arena.ne.jp/userapi/) |
  - [2] 2026-11-03: instances are logged into over SSH | capture: sha256:8f19ef4cd0a02889cb8bb3fc49aa027d7bac689863d62a75e212650db69e71cc | quote: インスタンスへのログインは、公開鍵暗号方式のSSH接続です。
  - [2] 2026-11-03: data transfer volume is unlimited, so no overage price exists | capture: sha256:8f19ef4cd0a02889cb8bb3fc49aa027d7bac689863d62a75e212650db69e71cc | quote: | データ転送量 | 制限はありません。 |
  - [2] 2026-11-04: a REST API is offered with English-only API documentation | capture: sha256:8f19ef4cd0a02889cb8bb3fc49aa027d7bac689863d62a75e212650db69e71cc | quote: | Rest-API | Rest-APIが利用できます。APIドキュメント（英語のみ）は[こちら](https://indigo.arena.ne.jp/userapi/) |
  - [4] 2026-11-04: the API document describes token generation over plain HTTP requests with a cURL example and names no client library | capture: sha256:a7692facb793eb1f175fd198b22a47a450d0a50ba121667049fa496d8191197b | quote: To generate Access token, send a POST request to `/oauth/v1/accesstokens`.
- sources:
  - [1] https://web.arena.ne.jp/indigo/price/
  - [2] https://web.arena.ne.jp/indigo/spec/
  - [3] https://web.arena.ne.jp/indigo/
  - [4] https://indigo.arena.ne.jp/userapi/

## WebARENA SuitePRO V4 free trial

- `egress/webarena-suitepro-trial` | dead | evidence documented | binding retention-clamped | category vps (hosted, Japan) | tier free
- needs card no, phone no, ID no, institution yes | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://web.arena.ne.jp/suitepro/entry/trial.html
- price JPY 0 for 20 days; the paid SuitePRO V4 contract is separate and cannot be converted from the trial
- free tier: [translated] 'Period: 20 days. Provided environment: server type 4G (4 virtual CPU cores, 4 GB memory, 100 GB boot disk), disk point N200, no backup.' | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] The trial is 20 days including the day the activation notice is sent; no traffic allowance is stated. At the end the server is stopped and initialised and 'files installed on it cannot be retrieved'.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: [translated] 'Fill in the necessary items on the application form and post it to the address given on the form.' There is no online signup for the trial: NTTPC issues a test-server ID within five business days of receiving the paper form. | country: None
- interface: ssh, cli
- limits:
  - retention-clamped (binding): [translated] '20 days', then 'the server is stopped and initialised and data is deleted automatically; files cannot be retrieved' [1]
- binding note: The 20-day window ends long before 1 TiB/month accumulates, and the machine is wiped rather than throttled. No byte allowance is published, so no volume quota can bind first.
- interface detail: [translated] Access is by the issued test-server ID; the page documents an application form and a notification email, not an API.
- tooling: wg-quick inside the guest; SSH
- composes with: A 20-day 4-core Japanese guest would carry a measurement wave; it cannot be obtained today.
- reliability: The machine is stopped and initialised the day after the end notice and the data is unrecoverable by design; the trial is limited to verification work and may not be used as a live commercial site.
- notes: A 4-core 4 GB Japanese guest for 20 days with no card would be the best trial shape, and it is closed twice over: the paper form is a postal step with a five-business-day turnaround, and the page read on 2026-10-23 says new applications are temporarily suspended, pointing at a news item dated 2026-10-21. identity_kind 'institution' is the closest token for a posted, signed form; the gate is process, not a national ID. Country: Japan (NTTPC Communications). WebARENA's other line, VPS Cloud, ended its trial on 2018-02-16 per its own page.
- evidence note: The 20-day term, the 4G specification, the postal application and the suspension are all on the vendor page read on 2026-10-23. A probe would establish the actual public address and rate; that requires an accepted application, which is currently impossible.
- extras:
  - wg_path: native-conf
  - wg_detail: A root guest on a 4-core 4 GB server; the trial environment is stated to be 'the same specification and environment as the paid contract', so WireGuard runs in the guest and wg-quick writes the .conf.
  - ingress: tcp+udp
  - volume_stated: [translated] The trial is 20 days including the day the activation notice is sent; no traffic allowance is stated. At the end the server is stopped and initialised and 'files installed on it cannot be retrieved'.
  - bytes_transit: yes
  - transit_note: The guest's own address on NTTPC's Japanese network.
- evidence:
  - [1] 2026-10-23: [translated] 'Period: 20 days', 'server type 4G (4 virtual cores, 4 GB memory, 100 GB boot disk)', and 'the trial environment is the same specification and environment as the paid contract'.
  - [1] 2026-10-23: [translated] 'At present we are temporarily suspending acceptance of new applications.'
  - [1] 2026-10-23: [translated] 'Fill in the necessary items on the application form and post it to the address given on the form', with the test-server ID issued within five business days of receipt.
- sources:
  - [1] https://web.arena.ne.jp/suitepro/entry/trial.html
