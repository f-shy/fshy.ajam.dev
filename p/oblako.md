# oblako.kz

> oblako.kz | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oblako/ | JSON https://fshy.ajam.dev/api/v1/entity/oblako.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## oblako.kz

- `compute/oblako-kz` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:40:26.615Z (live) | stale on 2026-12-05
- url https://oblako.kz/help/billing/testoviy-period
- free tier: A free test server for up to 5 days for legal entities and up to 3 days for individuals, capped at 8 CPU, 16 GB RAM and 200 GB disk, granted by a support ticket after phone confirmation. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The VDS page states 'Безлимитный интернет трафик' (unlimited internet traffic) with a configurable channel bandwidth; no overage price is published. | metered: no | source: [1]
- identity: any-phone
- interface: rest
- limits:
  - write-gated (binding): The test is not automatic: it requires a phone confirmation, a support ticket stating the purpose, and a support decision that the provider explicitly reserves the right to refuse without giving a reason. [1]
- limits note: The test is not automatic: it requires a phone confirmation, a support ticket stating the purpose, and a support decision that the provider explicitly reserves the right to refuse without giving a reason.
- binding note: the same as limits note
- interface detail: REST API documented at oblako.kz/rest-api (limits: 30 POST/PUT/DELETE and 1000 GET requests per 5 minutes); SSH to Linux VPS, and the web panel.
- tooling: the REST API at oblako.kz/rest-api is called over plain HTTP; the page names no CLI or client library.
- composes with: An 8 vCPU / 16 GiB box for three days is enough to run a benchmark or a bulk conversion and nothing that needs to persist; the value is the burst shape, not the duration.
- reliability: no reliability event recorded
- notes: Oblako offers a 3-day trial providing up to 8 vCPU, 16 GB RAM, and 200 GB disk in Kazakhstan. Trial access is granted at vendor discretion following account registration.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 16
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the help page states, in Russian, that the test period is up to 5 days for legal entities and up to 3 days for individuals, that a test server may not exceed 8 CPU, 16 GB RAM and 200 GB disk, that support staff make the final decision on the duration or on refusal, and that the provider reserves the right not to state a reason for refusal
  - [2] 2026-10-22: the product page prices VPS and VDS servers in Kazakhstani tenge with hourly, daily and monthly options, across data centres in Kazakhstan, Russia and Belarus
  - [2] 2026-11-03: unlimited internet traffic is stated for VDS | capture: sha256:a51fe7da3506ca464796be3ca2cd9dbba33de2baa68ceba7ce5b54b3b3367f8b | quote: Безлимитный интернет трафик
  - [3] 2026-11-03: REST API exists with request limits | capture: sha256:a57c9756a00171893afc5317e9f1bad05bcaa0c0fb2cf283c3bf730f7a2a4433 | quote: 1000: максимальное количество запросов типа GET в 5 минут
  - [3] 2026-11-04: the provider documents an API for automating its control panel; the page names no client library or CLI | capture: sha256:a57c9756a00171893afc5317e9f1bad05bcaa0c0fb2cf283c3bf730f7a2a4433 | quote: Вы можете использовать API для автоматизации работы с нашей панелью управления.
- sources:
  - [1] https://oblako.kz/help/billing/testoviy-period
  - [2] https://oblako.kz/products/vds-server
  - [3] https://oblako.kz/rest-api
