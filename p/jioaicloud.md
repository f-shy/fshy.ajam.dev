# jiocloud

> jioaicloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jioaicloud/ | JSON https://fshy.ajam.dev/api/v1/entity/jioaicloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## jiocloud / jioaicloud

- `storage/jiocloud-jioaicloud` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:02.631Z (live) | stale on 2026-12-04
- url https://www.jioaicloud.com/
- free tier: None reachable: 50 GB free and 'Proudly made in India, securely stored in India', but the entire auth surface is an OTP sent to a phone ('OTP verification — Enter the OTP sent to you on'), i.e. an Indian-nu. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 50 GB free and 'Proudly made in India, securely stored in India', but the entire auth surface is an OTP sent to a phone ('OTP verification — Enter the OTP sent to you on'), i.e. an…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 50 GB free and 'Proudly made in India, securely stored in India', but the entire auth surface is an OTP sent to a phone ('OTP verification — Enter the OTP sent to you on'), i.e. an…
  - [1] 2026-11-19: the vendor page still states a 50 GB free tier | capture: sha256:62cd4ed32be1844c2f74aab327ea12cde49dea9b40d2e01b68803d088a4933b9 | quote: Free 50 GB secure storage - for all that matters.
  - [2] 2026-11-19: registration requires a mobile number, which the record treats as an identity gate | capture: sha256:620e1d927e769a581fe1c48b5f108935b05743fd643e29ac4d2f5b16abd73d1f | quote: You can sign up for JioAICloud with your mobile number.
- sources:
  - [1] https://www.jioaicloud.com/
  - [2] https://www.jioaicloud.com/help/general/who-can-sign-up-for-jioaicloud
