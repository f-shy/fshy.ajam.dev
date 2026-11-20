# nzbwolf

> nzbwolf.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbwolf/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbwolf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nzbwolf

- `debrid/nzbwolf` | paid-only | evidence documented | binding request-rate | category Usenet indexer (movies and TV only, Newznab API on paid plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://app.nzbwolf.com/
- free tier: The Free plan is browsing, watchlist, collection and preferences only: 'No NZB downloads or Newznab API'. Downloads start at the Basic plan, USD 15.00 per year. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: Paid plans: Basic USD 15 per year (3,000 API requests and 1,000 NZB downloads a day), Premium USD 20 (10,000 and 5,000), Ultra USD 30 (20,000 and 20,000).
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: not stated on the pages read; the index covers movie and TV releases only | source: [2] | note: unverified
- egress: No byte metering; the plans meter NZB downloads and API requests per day. | metered: no | source: [1]
- identity: email | detail: The free sign-up form asks for a display name, an email address and a password of at least 12 characters. Paid plans are paid in Bitcoin through BTCPay with no automatic renewal, so no card is taken.
- interface: rest
- limits:
  - request-rate (binding): Free plan: no NZB downloads and no Newznab API (0 per day); a yearly plan from USD 15 unlocks both [1]
  - request-rate (binding): Basic plan: 3,000 API requests and 1,000 NZB downloads per day, shared across API keys [1]
- binding note: The free plan's download counter is zero, so it binds before any paid counter; the vocabulary has no paywall term and request-rate is the nearest.
- interface detail: A web app for browsing plus a Newznab API for apps on the paid plans, with the limits shared across the account's API keys.
- endpoint: https://app.nzbwolf.com/
- tooling: The plans page states a Newznab API 'for your apps'; Prowlarr and NZBHydra2 add Newznab indexers with URL plus key, and the key sits behind a sign-up and a paid plan.
- composes with: At USD 15 per year with 1,000 downloads a day it is a cheap paid escape for movie and TV grabs; the free plan alone retrieves nothing.
- reliability: The service relaunched in May 2023 and was rebuilt as a new app; no outage was observed.
- evidence note: The plans page and the sign-up form are first-party text read; the paid counters were not exercised.
- extras:
  - price: USD 0 (browse only); USD 15 per year Basic
- evidence:
  - [1] 2026-11-03: the Free plan includes no NZB downloads and no Newznab API | capture: sha256:192a6c17aa8d92af59de5a096b8ff694935372304ecdf51c9e6b2c327e0875d3 | quote: - No NZB downloads or Newznab API
  - [1] 2026-11-03: the cheapest paid plan, Basic, costs USD 15.00 per year | capture: sha256:192a6c17aa8d92af59de5a096b8ff694935372304ecdf51c9e6b2c327e0875d3 | quote: $15.00 USD / year
  - [1] 2026-11-03: the Basic plan allows 1,000 NZB downloads a day | capture: sha256:192a6c17aa8d92af59de5a096b8ff694935372304ecdf51c9e6b2c327e0875d3 | quote: - 1,000 NZB downloads / day
  - [1] 2026-11-03: paid plans are paid in Bitcoin | capture: sha256:192a6c17aa8d92af59de5a096b8ff694935372304ecdf51c9e6b2c327e0875d3 | quote: Payment is in Bitcoin through BTCPay at the USD price.
  - [3] 2026-11-03: the free sign-up form asks for an email address | capture: sha256:ecb89b95787a7527000e2e3a1d0a30910445aca43e27005484f07deb1042016b | quote: Email address
- sources:
  - [1] https://app.nzbwolf.com/plans
  - [2] https://nzbwolf.com/
  - [3] https://app.nzbwolf.com/register
