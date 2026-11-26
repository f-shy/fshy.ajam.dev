# Codemagic artifacts

> codemagic.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codemagic/ | JSON https://fshy.ajam.dev/api/v1/entity/codemagic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codemagic (mobile CI)

- `compute/codemagic` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T11:38:11.670Z (live) | stale on 2026-12-25
- url https://codemagic.io/pricing/
- free tier: the managed hosted Patch service is free below 100,000 monthly active users, and the individual mobile CI plan gives 500 free macOS M2 build minutes refilled every month with 30-day build history and artifact storage | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: the Free plan retains build history and artifacts for 30 days | days: 30 | source: [1] | note: Build history and artifacts are retained 30 days on the Free plan.
- egress: Egress traffic and data storage are included in Codemagic Patch pricing, with no bandwidth fees | metered: no | source: [1]
- identity: email | detail: The signup form asks for an email address with no phone field and no card field on the form.
- interface: unknown
- limits:
  - request-rate (binding): free below 100,000 monthly active users of the user's own app. [1]
  - write-gated: the trial and custom plans are arranged through sales, not self-serve [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The free tier is metered on monthly active users rather than machine execution time.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the free tier is bounded by a user's own MAU, not by a build or session clock
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - net.out: yes
  - net.in: yes
  - net.allowance: egress included
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Is a free tier available? Yes. If you have under 100K monthly active users you can use our managed hosted Patch service for free.' and 'Egress traffic and data storage are included in Codemagic Patch pricing'…
  - [1] 2026-11-03: egress traffic is included in Patch pricing | capture: sha256:9c3c529a8ee7d60d10b6278f19fb167117d2c3756084a0b6c7e8222a5f7781f8 | quote: No. Egress traffic and data storage are included in Codemagic Patch pricing.
  - [1] 2026-11-03: no bandwidth fees | capture: sha256:9c3c529a8ee7d60d10b6278f19fb167117d2c3756084a0b6c7e8222a5f7781f8 | quote: There are no hidden infrastructure or bandwidth fees.
  - [1] 2026-11-24: the Patch free tier below 100K MAU is unchanged | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: Yes. If you have under 100K monthly active users you can use our managed hosted Patch service for free.
  - [1] 2026-11-24: the pricing page publishes a second free tier of 500 build minutes a month | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: Single-user plan with unlimited number of applications and 500 free build minutes refilled every month.
  - [1] 2026-11-24: one free tier is denominated in build minutes while Patch is denominated in users | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: 500 free macOS M2 minutes / month
  - [1] 2026-11-24: the individual tier meters build minutes while Patch meters monthly active users | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: 500 free macOS M2 minutes / month
  - [1] 2026-11-24: the individual plan includes free build minutes every month | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: 500 free macOS M2 minutes / month
  - [1] 2026-11-24: the Free plan retains build history and artifacts for 30 days | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: Build history & artifact storage 30 days
  - [1] 2026-11-24: the Free plan retention is 30 days | capture: sha256:0fcddef36a2975cef50173d689c28024f86f0bc3fc4523858ae2dd55c0be724c | quote: Build history & artifact storage 30 days
  - [2] 2026-11-24: an email address creates the account | capture: sha256:c09de9e63384cb8dd8b6502e0f20460a1bad91ad605e2661b823043fc3dd53d2 | quote: Email Create your account
  - [2] 2026-11-24: the registration gate is an email address | capture: sha256:c09de9e63384cb8dd8b6502e0f20460a1bad91ad605e2661b823043fc3dd53d2 | quote: Email Create your account
- sources:
  - [1] https://codemagic.io/pricing/
  - [2] https://codemagic.io/signup

## Codemagic artifacts

- `storage/codemagic-artifacts` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:09.481Z (live) | stale on 2026-12-04
- url https://codemagic.io
- free tier: 500 free build minutes/month on macOS M2 (individuals). No free storage allowance advertised. Artifact retention is per-team policy; Enterprise default is 1 year. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Artifact retention is now documented: Personal accounts 30 days; Teams on Pay-as-you-go 60 days; Teams on Fixed Annual 1 year; Enterprise 1 year by default; after the period artifacts are automatically deleted. | source: [1] | note: not stated
- egress: Free via api.codemagic.io artifact URLs; 'No expiration' download links are a documented option. | metered: no
- identity: email
- interface: rest
- limits note: 500 min/month free. 'No expiration' applies to the LINK, not the artifact. Retention policy still deletes the file (explicit in their KB). Build dashboards give only 24-hour artifact links.
- interface detail: rest
- tooling: POST /artifacts/:secureFilename/public-url with expiresAt, returning a public URL; GET /artifacts/:secureFilename. API token required (`x-auth-token`).
- composes with: Unlimited accounts x 500 free minutes; artifact volume is bounded by what you can build in 500 min/month. 'No expiration' links mean the URL outlives nothing. The artifact is still deleted by team retention policy.
- reliability: Artifact retention is documented and finite: Personal 30 days, Pay-as-you-go Teams 60 days, Fixed Annual and Enterprise 1 year; a No expiration link stops working once the artifact is removed. 500 free build minutes per month is a hard build ceiling.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 500 free build minutes/month on macOS M2 (individuals). No free storage allowance advertised. Artifact retention is per-team policy; Enterprise default is 1 year.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'the artifact itself is still subject to your team's artifact retention policy ... Enterprise plan users have a default artifact retention period of 1 year'
  - [3] 2026-10-21: public-url creation API
  - [1] 2026-10-21: '500 free minutes per month on macOS M2'
  - [4] 2026-10-21: probe: curl -> 404; random artifact path -> 401 (no anonymous enumeration)
  - [1] 2026-11-19: the 500 free build minutes per month on macOS M2 for individuals is unchanged | capture: sha256:23e1157de4bdc546e6ac244cc7c5dee3fece97d3c6823168c2529e623bd47b65 | quote: Individuals receive 500 free minutes per month on macOS M2 machines on a personal account.
  - [3] 2026-11-19: the documented artifact API creates a public download URL via a POST to the public-url endpoint | capture: sha256:395bc148c502fc225384c5ad4edcdd81f53870913e7debf18d8876c26f76d986 | quote: POST /artifacts/:secureFilename/public-url
  - [2] 2026-11-19: the No expiration option keeps the link alive but the artifact is still removed by the team retention policy | capture: sha256:bc84be7205d0e8d258e3b5cb0d30dbe0ad3ea3f390fd0552d6a31177e7571357 | quote: the artifact itself is still subject to your team's artifact retention policy
  - [1] 2026-11-19: retention periods are documented on the pricing page and artifacts are deleted after them | capture: sha256:23e1157de4bdc546e6ac244cc7c5dee3fece97d3c6823168c2529e623bd47b65 | quote: Build history and artifact retention periods depend on your account type and pricing plan. We retain your build records, logs, and artifacts stored in Codemagic for the applicable retention period, after which they are automatically deleted.
  - [1] 2026-11-19: concrete per-plan artifact retention periods are published | capture: sha256:23e1157de4bdc546e6ac244cc7c5dee3fece97d3c6823168c2529e623bd47b65 | quote: | Personal accounts | 30 days | | Teams on Pay as you go plan | 60 days | | Teams on Fixed Annual plan | 1 year | | Enterprise plans | 1 year by default |
- sources:
  - [1] https://docs.codemagic.io/billing/pricing/
  - [2] https://help.codemagic.io/articles/1948706793-how-does-the-no-expiration-artifact-download-link-option-work
  - [3] https://docs.codemagic.io/rest-api/artifacts/
  - [4] https://api.codemagic.io/artifacts/
