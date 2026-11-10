# Gongji Compute individual

> suanli.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/suanli-2/ | JSON https://fshy.ajam.dev/api/v1/entity/suanli-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gongji Compute individual

- `compute/gongji-compute-individual` | qualifies | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:43.736Z (live) | stale on 2026-12-04
- url https://suanli.cn/activities/rfiuwpe9liory1kc25jcoxv2ntg/
- free tier: 'new-user trial: join the group, fill in the application form and immediately receive CNY 50 of compute credit, equivalent to 24 hours of a 4090' and 'deep support: after joining the group and submitting the form, individual developers who pass review receive from CNY 200 a month of ongoing compute support and up to CNY 1,500 in total compute resources'. Preferred profiles, any one of: a product with 10,000 monthly active users, a GitHub project with 100 or more stars, or technical content with 10,000 views or an account with 10,000 followers. Credit is issued as platform points and cannot be converted to cash. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card and no identity document are stated; the gate is a manual review: the offer page says "join the group, fill in the application form and immediately receive CNY 50 of compute credit", and the larger tier needs joining the group and submitting the form plus a review that prefers a product with 10,000 monthly active users, a GitHub project with 100 or more stars, or content with 10,000 views. The record does not state what the account itself uses as an identifier, any hold, or debit or prepaid acceptance
- interface: unknown
- limits:
  - write-gated (binding): The no-threshold tier is only CNY 50, about 24 hours of one 4090; anything above that needs a review and, in practice, an existing audience or repository. [1]
- limits note: The no-threshold tier is only CNY 50, about 24 hours of one 4090; anything above that needs a review and, in practice, an existing audience or repository. The offer page states per-second pay-as-you-go billing (秒级按量计费) and CNY 1.68 an hour as the lowest single-card 4090 price.
- binding note: part of limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It chains with nothing at this size, and that is the reason to record it: CNY 50 buys about 24 hours of a single 4090, which is a smoke test and not a workload. It is the honest floor that shows how far the CNY 1,000,000 award sits from anything an individual obtains without a review. Rate card on the vendor's pricing page, column '小时时长包 (8 卡)' (hourly duration pack, marked 8 cards, in CNY): RTX 4090 24 GB 15.84, L40S 48 GB 39.84, A100-80G 80 GB 91.20, H100 80 GB 180.00; the rows also carry 24-hour, 7-day and 30-day packs (RTX 4090 24 GB: 368.76, 2503.85, 9443.08), and only the hourly column is marked 8 cards. No L4 row. The pricing page states no minimum bill.
- reliability: no reliability event recorded
- notes: NAME COLLISION, and it matters: Gongji and Qiji are different companies whose names transliterate similarly. Searches for one surface the other. Gongji is a commercial shared-compute marketplace selling 4090 and H20 time by the second; Qiji is the accelerator running the municipal compute grant. Do not merge these records. Answering the subsidiary question directly: MiraclePlus publishes no trial tier, no GPU-hour taster and no self-service allocation. The only zero-friction thing it offers is the right to submit an application. This plan is the nearest genuine no-review trial found in the same search space, and it belongs to a different vendor at roughly one two-thousandth of the Qiji ceiling.
- extras:
  - facets.class: gpu-marketplace
  - facets.free_tier_kind: recurring-credit
  - facets.shape.ram_gib: 24
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: the CNY 50 trial and the up-to-CNY 1,500 tier with their conditions, quoted above; status 200 and live today.
  - [2] 2026-10-22: published rate card so the credit converts to hours: RTX 4090 24 GB at CNY 15.84 for an 8-card hour, RTX 5090 32 GB at CNY 28.00, H20 96 GB at CNY 96.00. Credit is denominated in CNY and not hours, so the trial is about 24 hours of one 4090 on the vendor's own equivalence.
  - [2] 2026-11-03: RTX 4090 24 GB costs 15.84 CNY in the hourly pack column and 368.76 CNY in the 24-hour pack | capture: sha256:60473726f093291afb0e6fb0754e1e267a7b6a6db0e52a883b64239869c71dc3 | quote: | RTX 4090 | 24 GB | 15.84 元 | 368.76 元 | 2503.85 元 | 9443.08 元 |
  - [2] 2026-11-03: H100 80 GB costs 180.00 CNY in the hourly pack column | capture: sha256:60473726f093291afb0e6fb0754e1e267a7b6a6db0e52a883b64239869c71dc3 | quote: | H100 | 80 GB | 180.00 元 | 4190.40 元 | 28452.82 元 | 107307.76 元 |
  - [2] 2026-11-03: A100-80G 80 GB costs 91.20 CNY in the hourly pack column | capture: sha256:60473726f093291afb0e6fb0754e1e267a7b6a6db0e52a883b64239869c71dc3 | quote: | A100-80G | 80 GB | 91.20 元 | 2123.14 元 | 14416.09 元 | 54369.27 元 |
  - [2] 2026-11-03: L40S 48 GB costs 39.84 CNY in the hourly pack column | capture: sha256:60473726f093291afb0e6fb0754e1e267a7b6a6db0e52a883b64239869c71dc3 | quote: | L40S | 48 GB | 39.84 元 | 927.48 元 | 6297.56 元 | 23750.78 元 |
  - [2] 2026-11-03: the hourly pack column header is marked 8 cards; the other pack columns are not | capture: sha256:60473726f093291afb0e6fb0754e1e267a7b6a6db0e52a883b64239869c71dc3 | quote: | 机型 | 显存 | 小时时长包 (8 卡) | 24 小时时长包 | 7 天时长包 | 30 天时长包 |
  - [1] 2026-11-03: per-second pay-as-you-go billing and a single-card 4090 lowest price of 1.68 CNY per hour | capture: sha256:7c141f917319c1b1af6e891c7a747856799f6a3fa0c1ec9a2f453103d33cae43 | quote: 秒级按量计费，单卡 4090 最低价！！1.68 元/h
  - [1] 2026-11-03: the trial is CNY 50 of credit, equal to 24 hours of a 4090 | capture: sha256:7c141f917319c1b1af6e891c7a747856799f6a3fa0c1ec9a2f453103d33cae43 | quote: 新手免费体验：扫码进群，填写申请表单立即领取** 50 元**（等价 24 小时 4090 显卡）算力体验积分
- sources:
  - [1] https://suanli.cn/activities/rfiuwpe9liory1kc25jcoxv2ntg/
  - [2] https://suanli.cn/pricing/
