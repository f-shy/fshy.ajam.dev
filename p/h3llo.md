# h3llo.cloud year-free package

> h3llo.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/h3llo/ | JSON https://fshy.ajam.dev/api/v1/entity/h3llo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## h3llo.cloud year-free package

- `compute/h3llo-cloud-year-free-package` | dead | evidence documented | binding none | category cloud VM
- needs card unknown, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://h3llo.cloud/promo
- free tier: A withdrawn offer that was the largest free compute package in the Russian market: twelve months of two virtual machines at 2 vCPU and 4 GiB each, one managed Postgres or MariaDB at 2 vCPU and 2 GiB, network disks up to 40 GB, 100 GB of object storage, one dedicated white IPv4 and a load balancer, for a balance top-up of RUB 5,000 by bank card. The rules page now carries a banner that the campaign is finished and that joining was open only until 8 March 2026 inclusive, with announced terms kept for those who joined earlier. The replacement for new clients is a 30-day trial credit. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-year
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the provider's comparison page on its second domain states outbound traffic free up to 100 GB and RUB 1.50 per GB above it, which does not reconcile with the .cloud tariff table listing object-storage egress at RUB 0.90 per GB with no free allowance | metered: no | source: [2]
- identity: country-phone | detail: an email address, a phone number and a bank-card top-up of at least RUB 5,000: rule 3.1 requires 'registration by email plus a top-up of at least RUB 5,000 by bank card', and the operator's launch article says registration needs an email and a phone number, with the phone requirement attributed to the Ministry of Digital Development. The card is charged rather than authorised, so no hold amount arises; whether a debit or prepaid card is accepted is not stated. The offer closed on 8 March 2026. | country: RU
- interface: unknown
- limits note: Withdrawn: the rules page states the campaign ended and that joining closed on 8 March 2026, so nothing binds now except the absence of the offer; for anyone who joined, a RUB 5,000 top-up was the gate and the package ran 12 months from the top-up date.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Had it survived it would have been the strongest chain among evaluated providers: 4 vCPU and 8 GiB running continuously for a year with a managed database and a white IP, for money that stayed on the balance as credit. What remains is the trial credit, which covers the same stack for 18 days.
- reliability: no reliability event recorded
- notes: Classified as dead rather than dropped, because the landing page still advertises the package and the deadline is visible only on the rules page. Two contradictions a reader should know: the launch article says the activation money is not refundable while rule 3.3 provides a refund minus consumption, and the article says the managed database is 2 vCPU / 4 GiB while the rules and the landing page say 2 vCPU / 2 GiB. The phone gate is described by the provider as a Russian ministry requirement, which is a constraint on who may register rather than on what is provided.
- extras:
  - facets.class: withdrawn-free-year
  - facets.free_tier_kind: free-year
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 8
  - facets.shape.gpu_count: 0
  - facets.shape.note: two machines of 2 vCPU / 4 GiB each, plus a managed database of 2 vCPU / 2 GiB
- evidence:
  - [1] 2026-10-22: the notice at the top of the rules page: the free-limits campaign is finished, joining was open until 8 March 2026 inclusive, announced terms are kept for earlier joiners, and the current offer is the trial credit, quoted and translated
  - [3] 2026-10-22: the landing page still sells the package and still carries the deadline: top up from RUB 5,000, two machines of 2 vCPU and 4 GB, load balancer, white IPv4, managed Postgres or MariaDB of 2 vCPU and 2 GB, network disks to 40 GB, object storage 100 GB, claim before 8 March 2026, quoted
  - [1] 2026-10-22: appendix 1 of the rules lists the package and section 3.1 requires registration by email plus a top-up of at least RUB 5,000 by bank card, while section 3.3 allows a refund of the deposit minus services consumed above the free limits
  - [4] 2026-10-22: the operator's launch article claims the package is the largest on the Russian market, says registration needs an email and a phone number and that the phone requirement comes from the Ministry of Digital Development, and states that after activation the balance money is not returned, contradicting rule 3.3
  - [5] 2026-10-22: at the tariff of 28 May 2026 the same bundle lists at about RUB 117,500 a year: two machines at 9.00 RUB an hour, database at 3.50 RUB an hour, 40 GB disk at 576 RUB a month, IP at 90 RUB a month, 9,791 RUB a month times 12, excluding load balancer and object storage
  - [6] 2026-10-22: edition of 18 August 2026, section 2.2: individuals receive RUB 4,000 and small or medium businesses RUB 20,000, the latter checked against the single register of small and medium enterprises by taxpayer number; section 3.1 gives 30 calendar days; section 3.3 annuls the unused balance, quoted and translated
  - [5] 2026-10-22: edition of 28 May 2026: virtual machines bill at RUB 1.25 per vCPU-hour and RUB 0.50 per GB of RAM per hour, capsules from RUB 545 a month, public IP RUB 90 a month, replicated SSD RUB 14.40 per GB-month, object storage RUB 2.15 per GB-month, quoted
  - [2] 2026-10-22: the provider's comparison page on its second domain states outbound traffic free up to 100 GB and RUB 1.50 per GB above it, which does not reconcile with the .cloud tariff table listing object-storage egress at RUB 0.90 per GB with no free allowance
- sources:
  - [1] https://h3llo.cloud/promo
  - [2] https://h3llo.pro/price
  - [3] https://limits.h3llo.cloud/
  - [4] https://habr.com/ru/companies/h3llo_cloud/articles/903518/
  - [5] https://h3llo.cloud/tariffs
  - [6] https://h3llo.cloud/trial-terms
