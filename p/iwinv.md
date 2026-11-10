# iwinv

> iwinv.kr | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iwinv/ | JSON https://fshy.ajam.dev/api/v1/entity/iwinv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iwinv

- `compute/iwinv` | fails-identity | evidence documented | binding volume-quota | category cloud VM | tier vgna_1_n
- needs card no, phone yes, ID yes, institution no | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-24
- url https://www.iwinv.kr/server/server
- price parsed USD 4.23/mo
- free tier: no free tier; the smallest server is KRW 5,600 a month for 1 vCPU, 1 GB and 25 GB NVMe | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: monthly billing; the server persists while paid | source: [1]
- egress: 20 GB a day (600 GB a month) on the entry plan, and beyond that a tiered rate applies: '20 GB/일 (월 600 GB) * 초과시 구간 요금제 적용' | metered: yes | free allowance: 600 GB a month | source: [1]
- identity: national-id | detail: South Korean nationality and a Korean mobile phone are both required: '대한민국 국적의 만 14세 이상이며 핸드폰 인증이 가능한 사용자라면 누구나 회원가입 후 서비스 이용이 가능합니다.' Card registration needs a Korean public certificate: '정상적인 카드 등록을 위해 공동인증서가 필요합니다.' The collected fields on identity verification are name, mobile number, date of birth, address and a duplicate-registration identifier (DI) | country: KR
- interface: unknown
- limits:
  - volume-quota (binding): 20 GB a day, 600 GB a month, then a tiered rate [1]
- limits note: The traffic allowance is 20 GB a day and 600 GB a month, counted per server, with tiered billing above it; a load of more than 20 GB a day exceeds it, and the overage is metered rather than absorbed.
- binding note: 600 GB a month is the smallest monthly allowance on any sub-USD-5 row here, but the identity wall is what actually decides it
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At KRW 5,600 a month with NVMe and a per-day meter, iwinv is the cheapest Korean box found that can be staged for a single day of work and deleted; it chains with nothing because the 600 GB monthly allowance is gone in hours at the serving rate.
- reliability: no reliability event recorded
- notes: KRW 5,600 divided by 1,324.702169 = USD 4.23, which is the second-cheapest shape under the line, and it is unreachable without Korean nationality. Classified as a finding, not discarded: the price is real and the wall is the finding.
- evidence note: price table and traffic term read on the vendor's own server page; the nationality and certificate gates quoted from the vendor's own help pages
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 25
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 4.23
  - m24h_usd: 4.23
  - price_arithmetic: KRW 5,600 a month / 1,324.702169 KRW per USD = USD 4.23
  - renewal_usd: 4.23
  - fx.pair: USD/KRW
  - fx.rate: 1324.702169
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
  - english: no; Korean only
  - payment_methods: Korean credit or check card, with a Korean public certificate to register it
- evidence:
  - [1] 2026-10-22: the price table gives vgna_1_n as 1 vCPU, 1 GB, NVMe 25 GB, 20 GB a day (600 GB a month, tiered above) at 210 원 a day and 5,600 원 a month, and lists vgna_2_n at 13,100 원, vgna_4_n at 24,000 원, vgna_6_n at 35,000 원 and vgna_8_n at 46,000 원 a month
  - [2] 2026-10-22: the vendor's own manual states that billing is per day with a monthly consolidation, that a daily base transfer allowance is included, and that usage above it is settled monthly at a discount to the daily rate
  - [1] 2026-10-24: quoted: '| KR1-Z01 KR1-Z02 KR1-Z03 KR1-Lite1 | vgna_1_n | 1 | 1 GB | NVMe 25 GB | 20 GB/일 (월 600 GB) * 초과시 구간 요금제 적용 | 210 원 | 5,600 원 |'
  - [3] 2026-10-24: quoted: '대한민국 국적의 만 14세 이상이며 핸드폰 인증이 가능한 사용자라면 누구나 회원가입 후 서비스 이용이 가능합니다.'
  - [4] 2026-10-24: quoted: '정상적인 카드 등록을 위해 공동인증서가 필요합니다.'
  - [5] 2026-10-24: quoted: identity verification collects '성명, 휴대전화번호, 생년월일, 주소, 중복가입확인정보(DI)'
- sources:
  - [1] https://www.iwinv.kr/server/server
  - [2] https://help.iwinv.kr/manual/604
  - [3] https://help.iwinv.kr/manual/398
  - [4] https://www.iwinv.kr/guide/console
  - [5] https://www.iwinv.kr/treaty/treaty/person

## iwinv (kr) object storage and sata block

- `storage/iwinv-object-storage-and-sata-block` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:26.510Z (live) | stale on 2026-12-05
- url https://www.iwinv.kr/storage/obj
- free tier: none reachable: Priced per GB and it is expensive: ₩20/GB/mo = $15.09/TB for object, ₩39,000/TB = $29.42/TB for SATA block. On top of that, egress is separately metered on a declining scale (₩60/GB for the | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Outbound internet traffic is billed per GB on a declining scale: 60 won per GB from 1 GB to 1 TB a month, down to 40 won per GB above 4 TB (VAT excluded); inbound traffic is free | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: documented from the vendor page read on 2026-11-03 (https://www.iwinv.kr/storage/obj): the object storage rate of 20 won per GB and the outbound traffic rates from 60 to 40 won per GB. Identity, retention, per-object cap and the SATA block price were not read.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Priced per GB and it is expensive: ₩20/GB/mo = $15.09/TB for object, ₩39,000/TB = $29.42/TB for SATA block. On top of that, egress is separately metered on a declining scale (₩60/GB for the
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Priced per GB and it is expensive: ₩20/GB/mo = $15.09/TB for object, ₩39,000/TB = $29.42/TB for SATA block. On top of that, egress is separately metered on a declining scale ₩60/GB for the
  - [2] 2026-10-21: cited as the basis of the rejection: Priced per GB and it is expensive: ₩20/GB/mo = $15.09/TB for object, ₩39,000/TB = $29.42/TB for SATA block. On top of that, egress is separately metered on a declining scale ₩60/GB for the
  - [1] 2026-11-03: outbound internet traffic from 1 GB to 1 TB a month is 60 won per GB (VAT excluded) | capture: sha256:7832ead80609e5c10fac3c6e617e2733f0b2a36bd6d6b505242a3a68bc02d5e5 | quote: | 1 GB( 1,000MB ) ~ 1TB | 60 원 | | | |
  - [1] 2026-11-03: outbound internet traffic is billed per GB; the lowest rate, above 4 TB a month, is 40 won per GB (VAT excluded) | capture: sha256:7832ead80609e5c10fac3c6e617e2733f0b2a36bd6d6b505242a3a68bc02d5e5 | quote: | 4 TB 초과 ( 4,001GB ~ ) | 40 원 | | | |
  - [1] 2026-11-04: outbound internet traffic from 1 GB to 1 TB a month is 60 won per GB (VAT excluded) | capture: sha256:7832ead80609e5c10fac3c6e617e2733f0b2a36bd6d6b505242a3a68bc02d5e5 | quote: | 1 GB( 1,000MB ) ~ 1TB | 60 원 | | | |
  - [1] 2026-11-04: outbound traffic above 4 TB a month is 40 won per GB | capture: sha256:7832ead80609e5c10fac3c6e617e2733f0b2a36bd6d6b505242a3a68bc02d5e5 | quote: | 4 TB 초과 ( 4,001GB ~ ) | 40 원 | | | |
  - [1] 2026-11-04: object storage is 20 won per GB per month | capture: sha256:7832ead80609e5c10fac3c6e617e2733f0b2a36bd6d6b505242a3a68bc02d5e5 | quote: | Standard (SSD based) | 1Gbyte | 20 원 |
- sources:
  - [1] https://www.iwinv.kr/storage/obj
  - [2] https://iwinv.kr/storage/block
