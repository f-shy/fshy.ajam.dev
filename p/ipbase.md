# ipbase

> ipbase.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipbase/ | JSON https://fshy.ajam.dev/api/v1/entity/ipbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipbase

- `data-apis/ipbase` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ipbase.com/pricing/
- free tier: Free plan: 150 requests a month at 10 requests a minute, no credit card, batch lookups on every plan | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the next plan (Small) gives 65,000 requests
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: email sign-up, or Google, GitHub or GitLab sign-in; no credit card
- interface: rest
- limits:
  - volume-quota (binding): 150 requests a month [1]
  - request-rate: 10 requests a minute [1]
- tooling: any HTTP client
- composes with: 150 lookups a month is a test allowance only. Bulk path: batch lookups, inside the same 150
- reliability: no reliability notes published beyond the quota
- notes: Free requests: 150 a month. Rate limit: 10 a minute. Bulk path: batch lookups within the same quota.
- evidence note: the pricing and register pages were quoted on 2026-10-30 and 2026-10-31; no keyed lookup was made.
- extras:
  - bulk_path: batch lookups within the free quota
  - free_requests: 150 a month
- evidence:
  - [1] 2026-10-30: the free plan is 150 lookups a month | capture: sha256:c4779d95760fb479b53de66d7ecc90deafca7c417ff62c7a62a70608eddbb315 | quote: Start free with 150 lookups a month, including location, connection, time zone and currency data.
  - [1] 2026-10-30: the free plan allows 10 requests a minute | capture: sha256:c4779d95760fb479b53de66d7ecc90deafca7c417ff62c7a62a70608eddbb315 | quote: 10 Requests / Min.
  - [1] 2026-10-30: no card is needed | capture: sha256:c4779d95760fb479b53de66d7ecc90deafca7c417ff62c7a62a70608eddbb315 | quote: No credit card required
  - [1] 2026-10-30: the next plan gives 65,000 requests | capture: sha256:c4779d95760fb479b53de66d7ecc90deafca7c417ff62c7a62a70608eddbb315 | quote: 65,000 Requests
  - [2] 2026-10-31: email sign-up is offered | capture: sha256:2bd9c1c5f3f498ccbd838ba16d89c53418f037455ff13bf252763eff54709c69 | quote: Sign up with email
  - [2] 2026-10-31: GitLab sign-in is offered | capture: sha256:2bd9c1c5f3f498ccbd838ba16d89c53418f037455ff13bf252763eff54709c69 | quote: [Sign up with GitLab](https://app.ipbase.com/auth/gitlab/redirect)
- sources:
  - [1] https://ipbase.com/pricing/
  - [2] https://app.ipbase.com/register
