# magentacloud

> magentacloud.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/magentacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/magentacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## magentacloud (deutsche telekom)

- `storage/magentacloud` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:02.631Z (live) | stale on 2026-12-04
- url https://magentacloud.de/
- free tier: None reachable: The whole product now redirects to a login page whose only identity path is 'Login with Telekom'. A Telekom customer account. There is no standalone registration page (/register, /registrie. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: identity
  - dead_end.why: The whole product now redirects to a login page whose only identity path is 'Login with Telekom' — a Telekom customer account. There is no standalone registration page (/register…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The whole product now redirects to a login page whose only identity path is 'Login with Telekom' — a Telekom customer account. There is no standalone registration page /register, /registrie
  - [2] 2026-10-21: cited as the basis of the rejection: The whole product now redirects to a login page whose only identity path is 'Login with Telekom' — a Telekom customer account. There is no standalone registration page /register, /registrie
  - [3] 2026-10-21: cited as the basis of the rejection: The whole product now redirects to a login page whose only identity path is 'Login with Telekom' — a Telekom customer account. There is no standalone registration page /register, /registrie
  - [2] 2026-11-19: the product presents a Telekom login wall with no standalone sign-up, matching the rejection | capture: sha256:aba1c27ac6443f0a5047a5c368b373214a0d2377b7afd7706bec8e9048340337 | quote: Login with Telekom
- sources:
  - [1] https://magentacloud.de/
  - [2] https://magentacloud.de/login
  - [3] https://www.magentacloud.de/register
