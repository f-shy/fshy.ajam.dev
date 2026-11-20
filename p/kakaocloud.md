# KakaoCloud Virtual

> kakaocloud.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kakaocloud/ | JSON https://fshy.ajam.dev/api/v1/entity/kakaocloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KakaoCloud Virtual Machine

- `compute/kakao-cloud` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:15.211Z (live) | stale on 2026-11-22
- url https://www.kakaocloud.com/services/virtual-machine/pricing
- free tier: no free tier: pay-as-you-go instances across general-purpose and accelerator families, with root and additional volumes billed separately as Block Storage | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): per-use billing across the m1ix, m3az, t1i, c1ix, gn1i and p2i families; the page states no free allowance [1]
  - per-object-cap: root and additional volumes are billed separately as Block Storage, so the instance price excludes disk [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the VM pricing page was read on 2026-10-22 and lists the instance families and the separate block-storage charge. It states no free tier, so the record's USD 220.92 credit is not established and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an instance bills while it exists; the page states no clock
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: Block Storage, billed separately from the instance
  - ps.durability: block volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 (Korean, 200 reporting no numeric status) and lists general-purpose instance families m1ix, m3az, t1i and c1ix with accelerator families gn1i (NVIDIA T4) and p2i (NVIDIA A100), billing per use and charging root and additional volumes separately as Block Storage
- sources:
  - [1] https://www.kakaocloud.com/services/virtual-machine/pricing

## KakaoCloud

- `compute/kakaocloud` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://kakaocloud.com/business/support/new
- free tier: KRW 300,000 of credit for new customers who register a payment method and apply within three months of signup, usable against most services. Outbound data is free up to 30 GiB a month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the cheapest Korean plan in the index is KakaoCloud t1i.nano at 2 vCPU and 0.5 GB for USD 2.98 a month with outbound 30 GiB free; a third-party price comparison, reported not documented | metered: no | source: [2]
- identity: institution | detail: a registered business is required before signup: the signup guide states a copy of the Korean business registration certificate (saeopja-deungnokjeung) must be prepared and that uploading it with its registration number is a mandatory first step, so the account needs a legal entity rather than a person's ID document; the KRW 300,000 credit then needs a payment method registered and an application within three months of signup. No hold is stated and debit or prepaid acceptance is not stated; the startup tracks, KRW 5,000,000 for a year and KRW 35,000,000 over two, need the same entity
- interface: unknown
- limits:
  - write-gated (binding): Signup itself requires a business registration certificate (saeopja-deungnokjeung) and a business registration number, so an individual outside Korea cannot open the account that holds the credit. [1]
- limits note: Signup itself requires a business registration certificate (saeopja-deungnokjeung) and a business registration number, so an individual outside Korea cannot open the account that holds the credit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: KRW 300,000 against a KRW-denominated 2 vCPU instance is several months of a small box, but the whole chain sits behind a Korean business registration number.
- reliability: no reliability event recorded
- notes: This refutes the common English roundup line that KakaoCloud is a cheap Korean cloud anyone can open: the gate is a business licence, not a phone. The startup track (KRW 5,000,000 for a year) is larger and needs a legal entity but no revenue. Classified as fails-identity with both figures visible so the subsequent evaluation does not re-chase the personal credit.
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the new-signup programme page states, in Korean, that a credit worth KRW 300,000 is granted to a customer who applies within 3 months of signup, usable against payment for various services, and lists the two steps as registering a payment method and then applying for the credit
  - [3] 2026-10-22: the signup guide states, in Korean, that a copy of the business registration certificate must be prepared before signup, and that uploading the business registration certificate and entering its registration number is a mandatory first step of the KakaoCloud signup procedure
  - [4] 2026-10-22: the startup programme blog states, in Korean, that the Launch track gives KRW 5,000,000 of credit usable for one year to every qualified startup, and that the Grow track gives KRW 35,000,000 over two years to companies backed by a partner VC or accelerator
  - [2] 2026-10-22: the cheapest Korean plan in the index is KakaoCloud t1i.nano at 2 vCPU and 0.5 GB for USD 2.98 a month with outbound 30 GiB free; a third-party price comparison, reported not documented
- sources:
  - [1] https://kakaocloud.com/business/support/new
  - [2] https://ssanvps.com/en/korea/
  - [3] https://docs.kakaocloud.com/start/quickstart-guide/sign-up
  - [4] https://blog.kakaocloud.com/94
