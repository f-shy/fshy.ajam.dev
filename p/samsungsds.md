# Samsung SDS

> samsungsds.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/samsungsds/ | JSON https://fshy.ajam.dev/api/v1/entity/samsungsds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Samsung Cloud Platform

- `compute/samsung-cloud-platform` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.samsungsds.com/kr/event/samsung-cloud-platform-credit-promotion.html
- free tier: KRW 300,000 of credit to a new account that registers a payment method and is approved: '가입만 하시면, 30만 크레딧을 바로 드립니다'. The credit is one per account, valid three months, and usable on every product. GPU Server and Bare Metal Server need prior arrangement through a console enquiry before use. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: signup-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a payment method plus a vendor approval: the credit is granted on registering a payment method (the account application step), after signup and console login, followed by an approval mail and then the credit, so the gate is a manual approval on top of the payment method rather than a signup form. No authorisation or hold amount is stated, and whether the payment method may be a debit or prepaid card is not stated: unknown. GPU Server and Bare Metal Server need a 1:1 console enquiry first.
- interface: unknown
- limits:
  - write-gated (binding): The credit arrives only after an account application and a payment-method registration are approved by the vendor, so the gate is a manual approval rather than a signup form; the credit also expires in three months, which is what limits how much of it can be spent on a slow-building workload. [1]
- limits note: The credit arrives only after an account application and a payment-method registration are approved by the vendor, so the gate is a manual approval rather than a signup form; the credit also expires in three months, which is what limits how much of it can be spent on a slow-building workload.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: KRW 300,000 at Korean list prices buys roughly 15 months of a 1 vCPU box or 60 hours of a 16 vCPU box, and it is the largest Korean credit found that is not tied to a school.
- reliability: no reliability event recorded
- notes: This changes an existing record: compute/samsung-cloud carries Samsung SDS as paid-only with no free tier, and the vendor's own promotion page contradicts that. The page found is a 2023 event page (the prize draw ran 2023-08-09 to 2023-09-27), and the current freetrials page at cloud.samsungsds.com could not be read because it renders client-side; a partner article dated 2026-02-05 repeats the mechanic, so the programme is treated as live but the amount is dated. The GPU exclusion is the detail that matters, because the headline credit reads as GPU money and is not.
- extras:
  - facets.class: domestic-credit
  - facets.free_tier_kind: signup-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page states that a new signup receives 300,000 credits on registering a payment method, that the sequence is 회원가입, console login, 어카운트 신청 (payment method registration), approval mail, credit receipt, and that the credit is one per account, valid three months; it also states that GPU Server and Bare Metal Server need a 1:1 console enquiry first
  - [2] 2026-10-22: a Samsung partner's help article dated 2026-02-05 repeats the same mechanic: register a payment method in the created account and 300,000 원 of credit is granted; reported
- sources:
  - [1] https://www.samsungsds.com/kr/event/samsung-cloud-platform-credit-promotion.html
  - [2] https://help.megazone.com/hc/ko/articles/54902760366745--Samsung-Cloud-Platform-Samsung-Cloud-Platform%EC%9D%84-%EC%B2%B4%ED%97%98%ED%95%B4-%EB%B3%B4%EA%B3%A0-%EC%8B%B6%EC%8A%B5%EB%8B%88%EB%8B%A4

## Samsung SDS Cloud Platform

- `compute/samsung-cloud` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:51.922Z (live) | stale on 2026-11-22
- url https://cloud.samsungsds.com/serviceportal/pricing.html
- free tier: no free tier: services bill by the used hour, with a lower rate for a one- or three-year hourly commitment | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): hourly billing across the compute catalogue, with lower rates on a one- or three-year hourly commitment [1]
  - per-object-cap: block, file and object storage are separate services, each billed on its own [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states hourly billing and the commitment discounts across the compute catalogue. There is no free tier on it, so the record's USD 260 credit is not established
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: virtual servers bill by used hour; the page states no reap
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: block, file and object storage are separate priced services
  - ps.durability: block or file storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Charge by used hour' with 'With Cost Savings, you can use the service at a lower rate by committing to a 1- or 3-year hourly usage contract', and a service catalogue listing Virtual Server, Virtual Server DR, Accelerated Server, Auto-Scaling, Bare Metal, Multi-node GPU Cluster and Cloud Functions. No free tier appears
- sources:
  - [1] https://cloud.samsungsds.com/serviceportal/pricing.html
