# Shin VPS

> shin-vps.jp | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shin-vps/ | JSON https://fshy.ajam.dev/api/v1/entity/shin-vps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shin VPS

- `compute/shin-vps` | paid-only | evidence documented | binding retention-clamped | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.shin-vps.jp/service/price.php
- free tier: The 1 GB plan with 1 core and 30 GB NVMe is JPY 750 a month on a one-month term, JPY 671 on a twelve-month term and JPY 451 on a thirty-six-month term, with no setup fee. The vendor raised every plan on 2026-09-01: the 1 GB month-to-month price went from JPY 540 to 750, a rise of about 39 percent, and the 2 GB plan from 750 to 1,040. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: The minimum term is three months and the vendor runs no trial, so a one-month experiment costs three months of the monthly rate; the term floor, not the price, is what a short job cannot fit into. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - retention-clamped (binding): The minimum term is three months and the vendor runs no trial, so a one-month experiment costs three months of the monthly rate; the term floor, not the price, is what a short job cannot fit into. [1]
- limits note: The minimum term is three months and the vendor runs no trial, so a one-month experiment costs three months of the monthly rate; the term floor, not the price, is what a short job cannot fit into.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Shin VPS is the cleanest evidence among documented hosts that the Japanese floor moved: the same 1 GB box that cost JPY 540 in August cost JPY 750 in October, which is a 39 percent rise in two months, and the annual term is now the only way back below JPY 700.
- reliability: no reliability event recorded
- notes: The 36-month figure of JPY 451 is real and requires three years of commitment. Whether the rise reflects hardware cost or demand is the vendor's stated reason (' ') and is not independently verified.
- extras:
  - facets.class: regional-price-change
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the price table gives 月額 750円 for the 1 GB plan on a one-month term, 671円 on twelve months and 451円 on thirty-six months, with 初期費用 0円 and 30 GB of NVMe, and states 'シンVPSの最低利用期間は「3ヶ月」です'
  - [2] 2026-10-22: the vendor's notice dated 2026/08/03 states that all plans are revised from 2026-09-01, giving the 1 GB month-to-month price as 540円 before and 750円 after, the 2 GB as 750円 before and 1,040円 after, and the 64 GB as 24,000円 before and 33,121円 after, all tax included
  - [3] 2026-10-22: a third-party review states that Shin VPS has no free trial period and no prorated refund inside the three-month minimum; reported
- sources:
  - [1] https://www.shin-vps.jp/service/price.php
  - [2] https://www.shin-vps.jp/news/detail.php?view_id=2360
  - [3] https://streamrental.com/shin-vps/
