# NAVER Cloud

> ncloud.com | Compute, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NAVER Cloud / LINE-NAVER scope

- `compute/naver-cloud` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:28.282Z (live) | stale on 2026-11-22
- url https://www.ncloud.com/product/compute/server
- free tier: no free tier: pay-as-you-go servers across Standard, High CPU and High Memory families, billed hourly or monthly, with SSD IOPS scaled to allocated storage | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): hourly or monthly billing across six general families plus High Memory-g1 [1]
  - per-object-cap: SSD IOPS scale with the allocated storage size, so the disk size sets the throughput ceiling [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the server product page was read on 2026-10-22 and publishes the family table and both billing modes. It states no free tier, so the record's claim is contradicted and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a server bills while it exists; the page states no clock
  - free_tier_kind: none
  - burst_x: 2.0
  - burst_bill: rounds to 1 h
  - ps.price: block storage priced with the server
  - ps.durability: SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the server exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the Korean pricing page was read on 2026-10-22 and lists server families S-g3, C-g3, M-g3, S-g2, C-g2, M-g2 and M-g1 with a '시간 요금제' and '월 요금제' (hourly and monthly) table; it states no free tier
- sources:
  - [1] https://www.ncloud.com/product/compute/server

## NAVER Cloud Platform

- `compute/naver-cloud-platform` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.ncloud.com/main/creditEvent
- free tier: KRW 100,000 of signup credit, valid 3 months, usable on any NAVER Cloud Platform service except free-tier and marketplace products, granted after a payment method is registered. A separate 1-year free Micro Server exists but the page states ', ' (offered only if the country of residence is Korea). | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a payment method registered plus real-name mobile verification, and Korean residence for the free server: the credit event page says the KRW 100,000 credit applies only after registering a payment method, and the record's limits row states the account is real-name verified by mobile phone; the one-year free Micro Server is offered "only if the country of residence is Korea", and the signup form asks for country of residence, member type and language. The record does not state which cards the Korean signup accepts, any hold, or debit or prepaid acceptance. The student Green Rookie credit separately needs a partner-institution email address
- interface: unknown
- limits:
  - write-gated (binding): The credit is granted only after a payment method is registered and the account is real-name verified by mobile phone, and the perpetually free Micro Server is limited to residents of Korea, so the free lane that survives is a 3-month KRW 100,000 credit behind a card. [1]
- limits note: The credit is granted only after a payment method is registered and the account is real-name verified by mobile phone, and the perpetually free Micro Server is limited to residents of Korea, so the free lane that survives is a 3-month KRW 100,000 credit behind a card.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A KRW 100,000 credit over 3 months buys roughly a small Standard server for part of that window, and the 1-year Micro Server that would make it a real host is closed to non-residents, so the credit is a sandbox rather than a host.
- reliability: no reliability event recorded
- notes: The credit is live on the separate event page. Two live pages disagree on the size (KRW 100,000 vs 'up to KRW 300,000'), and neither explains the gap; the 300,000 figure appeared in a 2022 blog post as a 200,000+100,000 stack, so the 300,000 is probably an older promotion left up. The KRW 200,000 Green Rookie credit and the exam voucher are for students and staff of a participating institution, which is an institution gate rather than a trial any account can start.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: ' 100,000 . ( 3 )' (KRW 100,000 discount credit for new customers, valid 3 months), ' ' (apply after registering a payment method), quoted
  - [1] 2026-10-22: '1 1 Micro Server ', ' 1 ', ' , ' (one Micro Server per person, free for one year from payment-method registration, but offered only when the country of residence is Korea), quoted
  - [2] 2026-10-22: ' 30 ' (up to KRW 300,000 in free credit for new customers) on the Micro promotion page, which is a higher headline figure than the 100,000 on the main credit page and is not reconciled by either page, quoted
  - [3] 2026-10-22: the signup form asks for 'Country of residence', 'Member Type' (Business or Personal) and language, and states ' ' (the payment currency is fixed by country of residence and cannot be changed after signup), quoted; no CPF-equivalent or business-number gate appears on the form
  - [4] 2026-10-22: 
- sources:
  - [1] https://www.ncloud.com/main/creditEvent
  - [2] https://micro.ncloud.com/promotion/
  - [3] https://www.ncloud.com/join/info
  - [4] https://www.fin-ncloud.com/main/creditEvent

## NAVER Cloud Platform Micro Server

- `egress/naver-cloud-micro` | fails-identity | evidence documented | binding none | category vps (hosted, South Korea) | tier free
- needs card yes, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.ncloud.com/main/creditEvent
- price KRW 0 for one year for a Korean resident; billed after that
- free tier: [translated] 'One Micro Server can be created per person. Free use for one year from the moment payment information is registered. A Micro Server not returned when the free period ends is billed automatically. However, this is provided only when the country of residence is Korea.' | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] One year of a Micro Server, one per person. No traffic allowance is stated for it on the page. The separate new-signup credit is '100,000 won of discount credit, valid for 3 months'.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: national-id | detail: [translated] 'However, this is provided only when the country of residence is Korea.' The page adds: 'If you register payment information after signing up, you can create a Micro Server', so a payment method is a second gate behind the residence one. The 200,000 won Green Rookie credit goes further and requires an email at a partner Korean school or university. | country: None
- interface: rest, cli, ssh
- binding note: The account is refused before any quota is reached: a Korean residence is the first constraint and no byte allowance matters behind it.
- interface detail: [translated] The console creates the server; the platform documents an API and CLI for its services.
- tooling: console and API (the platform ships an OpenAPI and CLI); WireGuard would run in the guest
- composes with: Unreachable, so it chains with nothing.
- reliability: The free server is billed automatically if not returned at the end of the year; the discount credit expires after three months and cannot be applied to products that already have a free period.
- notes: A free Korean VPS for a year with no card charge would be the answer to Korean question, and the country clause closes it. The page also carries a 300-man won credit promotion on a separate micro site, which is a trial credit requiring a payment method, not a free tier. Country: South Korea. The Green Rookie route needs a partner-institution email address, which is the same wall in a different shape.
- evidence note: The residence restriction is a vendor sentence on the credit-event page read on 2026-10-23. What would change the verdict is a Korean residence, which is not held here; nothing measurable on the network side would.
- extras:
  - wg_path: native-conf
  - wg_detail: A root Korean guest would run WireGuard in the guest; nothing is issued by NAVER. Moot: the account cannot be opened from outside Korea.
  - ingress: tcp+udp
  - volume_stated: [translated] One year of a Micro Server, one per person. No traffic allowance is stated for it on the page. The separate new-signup credit is '100,000 won of discount credit, valid for 3 months'.
  - bytes_transit: yes
  - transit_note: The guest's Korean address would carry the traffic.
- evidence:
  - [1] 2026-10-23: [translated] 'One Micro Server can be created per person', 'free use for one year from the moment payment information is registered', 'However, this is provided only when the country of residence is Korea.'
  - [1] 2026-10-23: [translated] 'We give new customers 100,000 won of discount credit applicable to payment for all services (valid for 3 months)', claimable only after 'registering a payment method'.
- sources:
  - [1] https://www.ncloud.com/main/creditEvent
