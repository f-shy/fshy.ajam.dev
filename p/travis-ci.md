# Travis CI

> travis-ci.com | CI runners, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/travis-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/travis-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Travis CI

- `ci-cd-runners/travis-ci` | paid-only | evidence documented | binding write-gated | category CI runner
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T17:29:39.667Z (live) | stale on 2026-12-04
- url https://docs.travis-ci.com/user/billing-overview/
- free tier: no free trial; OSS credits are granted by support rather than self-serve | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: there is no self-serve free allowance to cap
- retention: not applicable | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: a payment method for any plan, and no self-serve free tier
- interface: git
- limits:
  - write-gated (binding): OSS credits are granted by support, so the gate is a person and a queue [1]
- interface detail: a .travis.yml pipeline, once an account exists
- tooling: not relevant without an allowance
- composes with: no path: the free trial is withdrawn and the OSS path is a support request
- reliability: the 10,000-credit 14-day trial that appears in older comparisons no longer exists
- notes: The service is live and paid: the usage-based plan is USD 15 a month for 35,000 Linux build credits, and a standard Linux build minute costs 10 credits. The free trial is unavailable and OSS credits are granted by the support team on request.
- evidence note: the billing overview was read and states the trial is unavailable.
- evidence:
  - [1] 2026-10-22: the free trial plan is currently unavailable; open-source credits are granted on request rather than self-serve
  - [2] 2026-11-03: the vendor pricing page sells a paid usage-based plan with 35,000 Linux build credits a month | capture: sha256:fd2cb726f5483ca814d905cb31f2b20601af1ce6fc631c7cf76b31a0c758b847 | quote: 35,000 Linux build credits per month
  - [1] 2026-11-03: a standard Linux build minute costs 10 credits | capture: sha256:daaaf3fd77dcb1c876386a0685140a308ab7ab3b49d3e4ce51dbb9a018aeb680 | quote: | Build Job: Standard Linux/FreeBSD | 10 credits / minute | 10 credits / minute | |
  - [1] 2026-11-03: the free trial plan is unavailable | capture: sha256:daaaf3fd77dcb1c876386a0685140a308ab7ab3b49d3e4ce51dbb9a018aeb680 | quote: > Free Trial Plans are currently unavailable.
  - [3] 2026-11-03: OSS credits are granted by the support team on request | capture: sha256:08708d10f3925e37dc0b324d2b40c368e544c3abaa2f11712f528f75f7dac568 | quote: Travis CI may grant an amount of special OSS credits per month assigned to run builds only on public repositories.
- sources:
  - [1] https://docs.travis-ci.com/user/billing-overview/
  - [2] https://www.travis-ci.com/pricing/
  - [3] https://docs.travis-ci.com/user/billing-faq/

## travis ci artifacts

- `storage/travis-ci-artifacts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.travis-ci.com/user/uploading-artifacts/
- free tier: None reachable: The artifacts addon uploads to YOUR OWN S3 bucket. You supply ARTIFACTS_KEY/ARTIFACTS_SECRET/ARTIFACTS_BUCKET. Travis provides no storage at all; it is a BYO-bucket shim. Also unavailable o. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The artifacts addon uploads to YOUR OWN S3 bucket — you supply ARTIFACTS_KEY/ARTIFACTS_SECRET/ARTIFACTS_BUCKET. Travis provides no storage at all; it is a BYO-bucket shim. Also unavailable…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The artifacts addon uploads to YOUR OWN S3 bucket — you supply ARTIFACTS_KEY/ARTIFACTS_SECRET/ARTIFACTS_BUCKET. Travis provides no storage at all; it is a BYO-bucket shim. Also unavailable…
- sources:
  - [1] https://docs.travis-ci.com/user/uploading-artifacts/
