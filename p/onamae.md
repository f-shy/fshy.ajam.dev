# Onamae.com VPS

> onamae.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onamae/ | JSON https://fshy.ajam.dev/api/v1/entity/onamae.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Onamae.com VPS

- `compute/onamae-com-vps` | paid-only | evidence documented | binding retention-clamped | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-25T16:38:12.334Z (live) | stale on 2026-12-26
- url https://www.onamae.com/server/vps/price/
- free tier: | 初期費用 | 無料 | 無料 | 5,951円(税込) | 10,142円(税込) | 17,474円(税込) | | 1ヶ月払い | 985円(税込) | 1,446円(税込) | 4,065円(税込) | 8,255円(税込) | 16,636円(税込) | | 12ヶ月払い | 10,475円(税込) 実質873円/月 | 14,505円(税込) 実質1,209円/月 | 40,771円(税込) 実質3,398円/月 | 82,790円(税込) 実質6,899円/月 | 166,831円(税込) 実質13,902円/月 | | 最低利用期間 | 3ヶ月 | | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: The minimum period is three months, so the true entry cost of the JPY 985 shape is JPY 2,955; the vendor also reserves the right to add a service-maintenance surcharge to the listed price, which means the number on the page is not a ceiling. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the JPY 985 to 16,636 monthly ladder, the three-month minimum period and the absence of a current free trial, and its own notes record that the card cost was inferred from the billing model rather than read, so nothing in the record states a card, an email, a phone or an identity document
- interface: unknown
- limits:
  - retention-clamped (binding): The minimum period is three months, so the true entry cost of the JPY 985 shape is JPY 2,955; the vendor also reserves the right to add a service-maintenance surcharge to the listed price, which means the number on the page is not a ceiling. [1]
- limits note: The minimum period is three months, so the true entry cost of the JPY 985 shape is JPY 2,955; the vendor also reserves the right to add a service-maintenance surcharge to the listed price, which means the number on the page is not a ceiling.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Two cores and 100 GB of SSD for JPY 985 makes this the best Japanese shape per core below JPY 1,000, and it beats Sakura's 1 GB shape on both core count and disk at a similar price; the unlimited transfer claim is the part that would make it usable as a serving box if confirmed.
- reliability: no reliability event recorded
- notes: The unlimited-transfer claim comes from a third-party table and is not on the vendor price page read, so it is recorded as reported. A 2011 blog describes a fifteen-day free trial with a 5 Mbps downstream cap on this product; the current third-party comparison says no trial exists, and the vendor page does not mention one, so the trial is treated as withdrawn rather than current. The two sources disagree and the newer one wins, which is the finding.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the price table gives the 1 GB plan at 985円 including tax on one-month payment, 873円 a month equivalent on twelve months, with setup free on 1 GB and 2 GB shapes, a 3-core 2 GB shape at 1,446円 and a 10-core 16 GB shape at 16,636円, and states that the minimum period is three months and that a service-maintenance surcharge may be added
  - [2] 2026-10-22: a third-party comparison lists the 1 GB shape as 2 cores, 1 GB, 100 GB SSD with unlimited transfer and a three-month minimum, and states that no free trial is offered; reported
  - [1] 2026-11-25: the vendor price table states the setup and one-month prices from the free-setup 1 GB plan to the 16 GB plan | capture: sha256:75237b5b0eb492e3506a88bd7bad80f66baa463aba3f3167c8b7810790061ab7 | quote: | 初期費用 | 無料 | 無料 | 5,951円(税込) | 10,142円(税込) | 17,474円(税込) | | 1ヶ月払い | 985円(税込) | 1,446円(税込) | 4,065円(税込) | 8,255円(税込) | 16,636円(税込) |
  - [1] 2026-11-25: the vendor price table still states the setup and one-month prices from the free-setup 1 GB plan to the 16 GB plan | capture: sha256:75237b5b0eb492e3506a88bd7bad80f66baa463aba3f3167c8b7810790061ab7 | quote: | 初期費用 | 無料 | 無料 | 5,951円(税込) | 10,142円(税込) | 17,474円(税込) | | 1ヶ月払い | 985円(税込) | 1,446円(税込) | 4,065円(税込) | 8,255円(税込) | 16,636円(税込) |
  - [1] 2026-11-25: the vendor price table states the setup fee, one-month price and twelve-month effective price for each plan and a three-month minimum period | capture: sha256:75237b5b0eb492e3506a88bd7bad80f66baa463aba3f3167c8b7810790061ab7 | quote: | 初期費用 | 無料 | 無料 | 5,951円(税込) | 10,142円(税込) | 17,474円(税込) | ... | 1ヶ月払い | 985円(税込) | 1,446円(税込) | 4,065円(税込) | 8,255円(税込) | 16,636円(税込) | ... | 12ヶ月払い | 10,475円(税込) 実質873円/月 | 14,505円(税込) 実質1,209円/月 | 40,771円(税込) 実質3,398円/月 | 82,790円(税込) 実質6,899円/月 | 166,831円(税込) 実質13,902円/月 | ... | 最低利用期間は3ヶ月間となります。
  - [1] 2026-11-25: the vendor price table still states the setup fees, one-month prices and effective twelve-month monthly prices for all five plans | capture: sha256:75237b5b0eb492e3506a88bd7bad80f66baa463aba3f3167c8b7810790061ab7 | quote: | 初期費用 | 無料 | 無料 | 5,951円(税込) | 10,142円(税込) | 17,474円(税込) | ... | 1ヶ月払い | 985円(税込) | 1,446円(税込) | 4,065円(税込) | 8,255円(税込) | 16,636円(税込) | ... | 12ヶ月払い | 10,475円(税込) 実質873円/月 | 14,505円(税込) 実質1,209円/月 | 40,771円(税込) 実質3,398円/月 | 82,790円(税込) 実質6,899円/月 | 166,831円(税込) 実質13,902円/月 |
- sources:
  - [1] https://www.onamae.com/server/vps/price/
  - [2] https://www.serversus.work/services/onamae-com-vps/
