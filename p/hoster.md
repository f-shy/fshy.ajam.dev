# Hoster.kz

> hoster.kz | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hoster/ | JSON https://fshy.ajam.dev/api/v1/entity/hoster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hoster.kz

- `compute/hoster-kz` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://hoster.kz/cloud/vps/
- free tier: A 7-day free test of a cloud server, requested through an online form, on a ladder whose smallest plan is KZT 3,100 a month for 1 vCPU, 1 GB RAM and 25 GB NVMe in Almaty, Astana or Karaganda. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: The free window is seven days and is granted on application rather than on signup, so nothing accumulates and the clock starts only when sales approves. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: any-phone
- interface: unknown
- limits:
  - retention-clamped (binding): The free window is seven days and is granted on application rather than on signup, so nothing accumulates and the clock starts only when sales approves. [1]
- limits note: The free window is seven days and is granted on application rather than on signup, so nothing accumulates and the clock starts only when sales approves.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: KZT 3,100 a month for 1 vCPU and 1 GiB is roughly USD 6, which puts the Kazakh market at the same price floor as the cheapest European VPS, with a seven-day free look before any commitment.
- reliability: no reliability event recorded
- notes: The Kazakh market's free lane is uniformly seven days by application: Hoster.kz, AdminVPS.kz and oblako.kz all run it, and PS.kz offers a 14-day refund instead of a free server. That is the finding: there is no perpetual free tier in Kazakhstan, only a week-long look. The comparison page notes that Serverspace's bonus size is only shown after registration, which makes it unquotable.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the cloud server page lists, in Russian, Cloud 1-1-25 with 25 GB NVMe, 1 GB RAM, 1 vCPU and 1 IP address at KZT 3,100 a month, and Cloud 1-2-50 with 50 GB NVMe, 2 GB RAM and 1 vCPU at KZT 4,800 a month, in Almaty, Astana and Karaganda
  - [2] 2026-10-22: the provider's own knowledge base states, in Russian, that configurations can be ordered with an online request for a free test of the service of up to 7 days
  - [3] 2026-10-22: a Kazakhstan price comparison dated 2026-08-28 gives Hoster.kz at KZT 3,100 a month with 7 free days, PS.kz at KZT 3,120 with a refund in the first 14 days rather than a free server, AdminVPS.kz at KZT 3,235 with 7 free days, and Serverspace with a welcome bonus whose size is shown only after registration
- sources:
  - [1] https://hoster.kz/cloud/vps/
  - [2] https://hoster.kz/support/oblachnyy-server/8451/
  - [3] https://www.clex.kz/articles/vps-v-kazahstane-sravnenie-serverov-i-tarifov-2026-goda
