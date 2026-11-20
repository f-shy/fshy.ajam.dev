# prototype fund

> prototypefund.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prototypefund/ | JSON https://fshy.ajam.dev/api/v1/entity/prototypefund.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## prototype fund (germany)

- `storage/prototype-fund` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:57.505Z (live) | stale on 2026-12-04
- url https://hardware.prototypefund.de/en/apply/faq/
- free tier: none reachable: German residency and self-employment are required of individual applicants; a grant program, not hosted storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [2] | note: not applicable
- retention: not recorded | source: [2]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Residency-gated rather than nationality-gated: 'Wohnsitz und steuerpflichtig in Deutschland' / 'You're a German resident, self-employed and paying German taxes. (German citizenship is not…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Residency-gated rather than nationality-gated: 'Wohnsitz und steuerpflichtig in Deutschland' / 'You're a German resident, self-employed and paying German taxes. (German citizenship is not…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: Residency-gated rather than nationality-gated: 'Wohnsitz und steuerpflichtig in Deutschland' / 'You're a German resident, self-employed and paying German taxes. German citizenship is not re
  - [3] 2026-10-21: cited as the basis of the rejection: Residency-gated rather than nationality-gated: 'Wohnsitz und steuerpflichtig in Deutschland' / 'You're a German resident, self-employed and paying German taxes. German citizenship is not re
  - [1] 2026-11-19: single applicants must be German residents who are self-employed and pay taxes in Germany | capture: sha256:2eede041cb3776dcaef45581f0df4b16bdbe397316213d2491abf890c07d9d52 | quote: As individual developers, you must be residents of Germany, self-employed
  - probe:https://hardware.prototypefund.de/en/apply/faq/ 2026-11-19: the originally cited FAQ URL answered HTTP 404 on 2026-11-19 | capture: sha256:4770e9ac11bc1db21abf20af8af1c8a3ebb21fbd5bf24279d4a337afb4872e36 | quote: "status": 404
- sources:
  - [1] https://www.prototypefund.de/en/application
  - [2] https://hardware.prototypefund.de/en/apply/faq/
  - [3] https://www.prototypefund.de/en/about/mission
