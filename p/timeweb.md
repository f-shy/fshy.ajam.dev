# timeweb cloud

> timeweb.cloud | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/timeweb/ | JSON https://fshy.ajam.dev/api/v1/entity/timeweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## timeweb cloud s3

- `storage/timeweb-cloud-s3` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.962Z (live) | stale on 2026-11-19
- url https://timeweb.cloud/services/s3-storage
- disagrees on verdict: `storage/timeweb-cloud-s3` says paid-only, `storage/timeweb-cloud-s3-2` says fails-quota
- free tier: none reachable: Priced from 1 RUB/GB/mo with an auto-upgrade ladder (79 RUB for 10 GB, 349 for 100 GB, 'unlimited' 639 RUB/mo capped at 250 GB included then 4 RUB/GB), and egress is only 100 GB/month free. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: 100 GB per month of outgoing traffic is free; beyond it outgoing traffic is billed at 1.3 RUB per GB, and no cap is stated. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: read 2026-11-03: https://timeweb.cloud/services/s3-storage (100 GB/month free outgoing traffic, 1.3 RUB per GB beyond); the storage price ladder behind the no-free-tier verdict carries the 2026-10-21 evidence rows only.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Priced from 1 RUB/GB/mo with an auto-upgrade ladder (79 RUB for 10 GB, 349 for 100 GB, 'unlimited' 639 RUB/mo capped at 250 GB included then 4 RUB/GB), and egress is only 100 GB/month free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Priced from 1 RUB/GB/mo with an auto-upgrade ladder (79 RUB for 10 GB, 349 for 100 GB, 'unlimited' 639 RUB/mo capped at 250 GB included then 4 RUB/GB), and egress is only 100 GB/month free.
  - [1] 2026-11-03: the free outgoing traffic limit is 100 GB per month | capture: sha256:fd2e689710a001436def0bd332df90b8e83ba72fe7b728b89d51de83c977a67c | quote: Бесплатный лимит трафика составляет 100 ГБ в месяц.
  - [1] 2026-11-03: outgoing traffic is billed at 1.3 RUB per GB | capture: sha256:fd2e689710a001436def0bd332df90b8e83ba72fe7b728b89d51de83c977a67c | quote: Исходящий трафик 1.3 ₽/ГБ
  - [1] 2026-11-04: outgoing traffic is billed at 1.3 RUB per GB | capture: sha256:a65526bd3c532d580b0cc3ae13c68fe4df328399d8e27a8ac13fdfbf84a503d1 | quote: Исходящий трафик 1.3 ₽/ГБ
- sources:
  - [1] https://timeweb.cloud/services/s3-storage

## Timeweb Cloud grant

- `compute/timeweb-cloud-grant` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID yes, institution no | verified 2026-11-03T08:50:54.215Z (live) | stale on 2026-12-04
- url https://timeweb.cloud/grant
- free tier: 'Грант на облако: до 1 000 000 ₽, до 6 месяцев' (cloud grant: up to RUB 1,000,000 for up to 6 months), one bonus equal to one rouble. The rules define the participant as 'резидент Российской Федерации, в том числе: индивидуальный предприниматель; юридическое лицо' (a resident of the Russian Federation, including a sole proprietor or a legal entity), and exclude 'выделенных серверов, серверов с GPU и ИИ-агентов' (dedicated servers, GPU servers and AI agents) from the grant. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id
- interface: unknown
- limits:
  - write-gated (binding): The door is Russian tax residency plus a registered or: a private individual cannot apply at all, and the grant excludes GPU servers, so the largest single number in the Russian market buys no GPU time even for a company that qualifies. [1]
- limits note: The door is Russian tax residency plus a registered or: a private individual cannot apply at all, and the grant excludes GPU servers, so the largest single number in the Russian market buys no GPU time even for a company that qualifies.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None reachable: the grant needs a Russian legal entity and excludes precisely the GPU servers that would make it interesting, so it composes with nothing in documented records.
- reliability: the Timeweb GPU servers page (timeweb.cloud/services/gpu) states that grant issuance is temporarily suspended, read 2026-11-03
- notes: A refutation of the biggest Russian number. Kept separate from the Cloud4Y and Reg.ru checks because those are different companies.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: grant
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page title is ' : 1 000 000 , 6 ' and the rules define ' : , : ; ', quoted
  - [1] 2026-10-22: ' : , , GPU - ' (excluding dedicated servers, GPU servers and AI agents) and '1.3. ... ' (no free test period under this campaign), quoted
  - [2] 2026-10-22: asked whether a cloud server can be tested free: ' , . ' (yes, but requests are reviewed individually, write to Telegram), quoted, so there is no self-serve trial
  - [3] 2026-11-03: the GPU servers page states that issuance of grants is temporarily suspended | capture: sha256:efdce82946bb65988e94045fb76dc8a34355caeef92e1b4f9b1d45cefb881838 | quote: Выдача грантов временно приостановлена
  - [3] 2026-11-03: the GPU servers page lists RTX 4090, H100 80GB, A100 80GB and L4 24GB cards with no hourly price on the page, and states charges are taken once an hour | capture: sha256:efdce82946bb65988e94045fb76dc8a34355caeef92e1b4f9b1d45cefb881838 | quote: Тарифы формируются за месяц, а списания — раз в час.
- sources:
  - [1] https://timeweb.cloud/grant
  - [2] https://timeweb.cloud/services/cloud-servers
  - [3] https://timeweb.cloud/services/gpu

## timeweb cloud s3 (russia)

- `storage/timeweb-cloud-s3-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://timeweb.cloud/services/s3-storage
- disagrees on verdict: `storage/timeweb-cloud-s3` says paid-only, `storage/timeweb-cloud-s3-2` says fails-quota
- free tier: None reachable: The 'Unlimited' storage tier is 639 ₽/mo and immediately reveals itself: «В тариф включено 250 ГБ. Свыше лимита. 4 ₽/ГБ». 250 GB included, then ₽4/GB, so 'unlimited' costs ₽4,096 per TB on. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The 'Unlimited' storage tier is 639 ₽/mo and immediately reveals itself: «В тариф включено 250 ГБ. Свыше лимита — 4 ₽/ГБ» — 250 GB included, then ₽4/GB, so 'unlimited' costs ₽4,096 per TB…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 'Unlimited' storage tier is 639 ₽/mo and immediately reveals itself: «В тариф включено 250 ГБ. Свыше лимита — 4 ₽/ГБ» — 250 GB included, then ₽4/GB, so 'unlimited' costs ₽4,096 per TB…
  - [2] 2026-10-21: cited as the basis of the rejection: The 'Unlimited' storage tier is 639 ₽/mo and immediately reveals itself: «В тариф включено 250 ГБ. Свыше лимита — 4 ₽/ГБ» — 250 GB included, then ₽4/GB, so 'unlimited' costs ₽4,096 per TB on
- sources:
  - [1] https://timeweb.cloud/services/s3-storage
  - [2] https://serverdelo.ru/rejtingi/s3-hranilishche/
