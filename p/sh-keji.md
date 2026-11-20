# Xuhui District AI

> sh-keji.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sh-keji/ | JSON https://fshy.ajam.dev/api/v1/entity/sh-keji.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xuhui District AI

- `compute/xuhui-district-ai` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card unknown, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.sh-keji.cn/kjcx/26125.html
- free tier: The support is a reimbursement against compute already rented between 2025-07-01 and 2026-06-30. | unit: none | metered on: wall-clock | read on: 2026-10-12 | source: [1] | note: reimbursement-voucher
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: No card, hold, debit or prepaid statement appears: unknown.
- interface: unknown
- limits:
  - write-gated (binding): The voucher reimburses compute already paid for by a registered entity and the pack demands a business licence, so an unaffiliated individual cannot use this category at all. [1]
- limits note: The voucher reimburses compute already paid for by a registered entity and the pack demands a business licence, so an unaffiliated individual cannot use this category at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It does not chain, and it is recorded only to close the door: it reimburses an invoice from a company that already rents compute, which presupposes both the company and the cash to front.
- reliability: no reliability event recorded
- notes: Shanghai Xuhui District AI compute vouchers reimburse computing expenses for registered corporate entities and research organizations operating within the district.
- extras:
  - facets.class: municipal-grant
  - facets.free_tier_kind: reimbursement-voucher
- evidence:
  - [1] 2026-10-12: 
  - [1] 2026-10-22: the text extractor returns nothing for this host, which is why an earlier re-read recorded a zero overlap
- sources:
  - [1] https://www.sh-keji.cn/kjcx/26125.html
