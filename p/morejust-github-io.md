# morejust store

> morejust.github.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/morejust-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/morejust-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## morejust store (morejust.store)

- `storage/morejust-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.048Z (live) | stale on 2026-12-04
- url https://morejust.github.io/store/
- free tier: not stated: https://morejust.github.io/store/ prints no free allowance; the page says the project was banned by GitHub and is usable for test purposes only | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the Chrome extension repository kirillovmr/mjsChrome, last committed in January 2019, describes the service as free unlimited cloud storage without an amount or period
- per-object cap: stated-absent: the operator's project page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the operator's project page states no retention period for stored bytes | source: [1]
- egress: stated-absent: the operator's project page states no egress terms | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the operator's project page states no storage client interface
- tooling: not documented
- composes with: stated-absent: the operator's project page states no way to chain the service with other storage offers
- reliability: Repository kirillovmr/mjsChrome links to a Chrome Web Store listing for cloud storage, but project documentation indicates the organization was closed and marked test-only.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [1] 2026-10-30: the project page prints no allowance and says the project is usable for test purposes only | capture: sha256:6e0f0cfe32094a980df49c709bc173feb5c40c03e804e6b5c7053f82e758ade8 | quote: But You still can use our project for test purposes only.
  - [2] 2026-10-30: the extension repository describes the service as free unlimited cloud storage, with no amount, unit or period | capture: sha256:45de19e4044331aacfc65a1387775dcf7ae53fcf26dd64d0b0ae03d388cfba75 | quote: Chrome extension for Morejust Store - Free Unlimited Cloud Storage
  - [1] 2026-10-30: the project page states that the project was banned by GitHub | capture: sha256:6e0f0cfe32094a980df49c709bc173feb5c40c03e804e6b5c7053f82e758ade8 | quote: We were banned by GitHub :(
  - [1] 2026-11-19: the operator's page still says the project was banned by GitHub, matching the recorded rejection | capture: sha256:6e0f0cfe32094a980df49c709bc173feb5c40c03e804e6b5c7053f82e758ade8 | quote: We were banned by GitHub :(
  - [1] 2026-11-19: the page still says the project is usable for test purposes only, so no free allowance is stated | capture: sha256:6e0f0cfe32094a980df49c709bc173feb5c40c03e804e6b5c7053f82e758ade8 | quote: But You still can use our project for test purposes only.
- sources:
  - [1] https://morejust.github.io/store/
  - [2] https://github.com/kirillovmr/mjsChrome
