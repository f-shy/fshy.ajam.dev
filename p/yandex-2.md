# Yandex Cloud

> yandex.cloud | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yandex-2/ | JSON https://fshy.ajam.dev/api/v1/entity/yandex-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## yandex cloud object storage free tier

- `storage/yandex-cloud-object-storage-free-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:53.248Z (inherited) | stale on 2026-11-14
- url https://yandex.cloud/en/docs/storage/pricing
- free tier: Free every month in standard storage: the first 1 GB of storage, the first 10,000 PUT, POST, PATCH and LIST operations and the first 100,000 GET, HEAD and OPTIONS operations; the first 100 GB of outgoing traffic per month is also free. Unused free amounts reset at the end of the month. | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: In all calculations the page defines 1 GB as 2^30 bytes and 1 MB as 2^20 bytes.
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free tier includes 1 GB standard storage, 10,000 PUT requests, and 100,000 GET requests per month. Promotional credits operate on a time-limited trial basis.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: the first 1 GB of standard storage per month is free | capture: sha256:62d1e60cdfbe35305f8f28b008a738902e43af997785bccdc903c229487c07df | quote: The first 1 GB of data stored in standard storage per month is free of charge.
  - [2] 2026-10-30: the page's GB is 2^30 bytes | capture: sha256:8de5ff4a6b0688b562ce25a433b16192db901269f97eb8a50e7a8deb83d6a980 | quote: In all calculations: 1 GB = 2<sup>30</sup> bytes, 1 MB = 2<sup>20</sup> bytes.
  - [1] 2026-10-30: the first 100 GB of outgoing traffic per month is free | capture: sha256:62d1e60cdfbe35305f8f28b008a738902e43af997785bccdc903c229487c07df | quote: The first 100 GB of outgoing traffic per month for Object Storage are free of charge.
  - [1] 2026-10-30: unused free amounts reset at the end of each month | capture: sha256:62d1e60cdfbe35305f8f28b008a738902e43af997785bccdc903c229487c07df | quote: After you spend the free amount of services, you will be charged at the applicable rate. The unused balance of free services is reset at the end of the month.
  - [1] 2026-10-30: the monthly free amounts apply to standard storage | capture: sha256:62d1e60cdfbe35305f8f28b008a738902e43af997785bccdc903c229487c07df | quote: Standard storage resources are provided free of charge every month:
- sources:
  - [1] https://yandex.cloud/en/docs/storage/pricing
  - [2] https://docs.yandex.cloud/int/en/storage/pricing.md

## Yandex Cloud

- `compute/yandex-cloud` | dead | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://yandex.cloud/en/docs/getting-started/free-trial/concepts/quickstart
- free tier: Withdrawn: the live documentation states 'Currently, the trial period and introduction grant are unavailable for new clients', and the trial survives only for legal entities paying by wire transfer. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a registered legal entity paying by wire transfer: the docs state 'Currently, the trial period and introduction grant are unavailable for new clients' and 'The trial period is available only for businesses that selected Wire transfer as the payment method'. A wire transfer means a business bank account, so no card and no hold arises on the surviving route. Whether an individual can hold an account at all, and any debit or prepaid term, is not stated; for a new individual client there is no trial to reach.
- interface: unknown
- limits:
  - write-gated (binding): Nothing is granted now; what remains is a wire-transfer trial for registered legal entities, so an individual has no lane. [1]
- limits note: Nothing is granted now; what remains is a wire-transfer trial for registered legal entities, so an individual has no lane.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None: the grant is gone, and the remaining wire-transfer trial needs a Russian legal entity with a bank account.
- reliability: no reliability event recorded
- notes: A refutation that matters because the stale search index still sells the grant: the snippet advertises RUB 4,000 for residents, KZT 20,000 for Kazakhstan and USD 30 for non-residents, while the live docs issue none of it.
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'Currently, the trial period and introduction grant are unavailable for new clients.' and 'The trial period is available only for businesses that selected Wire transfer as the payment method', quoted
  - [2] 2026-10-22: the Russian page carries the same withdrawal for new clients, quoted
  - [3] 2026-10-22: the search snippet for this URL still describes a 60-day grant, but the live route returns 404 NoSuchKey, so the snippet describes a page that no longer exists
- sources:
  - [1] https://yandex.cloud/en/docs/getting-started/free-trial/concepts/quickstart
  - [2] https://yandex.cloud/ru/docs/getting-started/free-trial/concepts/quickstart
  - [3] https://docs.yandex.cloud/ru/ru/getting-started/usage-grant.md
