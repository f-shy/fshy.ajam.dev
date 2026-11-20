# Onamae.com VPS

> onamae.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onamae/ | JSON https://fshy.ajam.dev/api/v1/entity/onamae.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Onamae.com VPS

- `compute/onamae-com-vps` | paid-only | evidence documented | binding retention-clamped | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.onamae.com/server/vps/price/
- free tier: The 1 GB plan gives 2 vCPU, 1 GB memory and 100 GB SSD at JPY 985 a month including tax on a monthly term, or an effective JPY 873 a month on a twelve-month term, with no setup fee and a three-month minimum period. The 2 GB plan is 3 cores and 200 GB at JPY 1,446 a month, and the ladder runs to 10 cores with 16 GB and 1 TB at JPY 16,636. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
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
- sources:
  - [1] https://www.onamae.com/server/vps/price/
  - [2] https://www.serversus.work/services/onamae-com-vps/
