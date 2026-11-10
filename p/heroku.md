# Heroku

> heroku.com | Compute, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heroku/ | JSON https://fshy.ajam.dev/api/v1/entity/heroku.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Heroku Open Source

- `compute/heroku-open-source` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:32.966Z (live) | stale on 2026-12-05
- url https://www.heroku.com/open-source-credit-program/
- free tier: 'one year of platform credits to qualifying Open Source Software projects hosted on Heroku', paid as 'a set credit allocation every month for 12 months', usable on 'Heroku Dynos, Heroku Postgres, and Heroku Key-Value Store'. Salesforce 'will determine the credit allocation amount based on project need and use', so no figure is published. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: network bandwidth is soft limited at 2TB per app per month; no per-GB overage price is published on the limits page read | metered: yes | free allowance: 2TB per app per month (soft limit) | source: [1]
- identity: card | detail: A card is required before applying: the programme page states the account must be verified with a credit or debit card before applying and any monthly overage bills that card, so a debit card is accepted alongside credit. No hold or authorisation amount is stated, whether prepaid cards are accepted is not stated, and the programme adds a second gate. "you must be a maintainer on the open source software project and its supporting infra must run or intend to run on Heroku".
- interface: cli, rest
- limits:
  - write-gated (binding): The account must be verified with a credit or debit card before applying and any monthly overage bills the card; the allocation is set by Salesforce and unused credit is forfeited monthly. [1]
- limits note: The account must be verified with a credit or debit card before applying and any monthly overage bills the card; the allocation is set by Salesforce and unused credit is forfeited monthly.
- binding note: the same as limits note
- interface detail: the Heroku CLI and the Heroku Platform API
- tooling: the Heroku CLI (macOS, Windows, Linux) and the Platform API reachable with curl and a token
- composes with: Dynos plus Postgres plus Key-Value store on one monthly allocation covers a small always-on service with state, which is the piece most free student and OSS tiers leave out: a database that survives the free tier ending.
- reliability: no reliability event recorded
- notes: The gate that matters is directional: the project must run or intend to run on Heroku, so this does not pay for a workload hosted elsewhere. Heroku still sells dynos, so this is a live programme rather than a legacy one. Amount is null by design, not by omission: the terms hand the allocation to Salesforce.
- extras:
  - facets.class: vendor-oss-credits
  - facets.free_tier_kind: recurring-credit
- evidence:
  - [1] 2026-10-22: quoted the 12-month monthly allocation, the covered products, 'Any unused portion of the monthly credit allocation is forfeited', the card-verification requirement, the monthly review cadence, and 'The program is open people globally'
  - [1] 2026-10-22: quoted 'you must be a maintainer on the open source software project and its supporting infra must run or intend to run on Heroku'
  - [2] 2026-11-03: platform network bandwidth is soft limited at 2TB per app per month | capture: sha256:e221cf6e2d92fe3a56a1639dde471998168dad93eaa70f427c870cead69c334b | quote: Network bandwidth is soft limited at 2TB per app per month.
  - [3] 2026-11-03: a CLI manages apps | capture: sha256:a13e767a26d226e7a487a360813b2ae8300c1061f15839044b3764ba68acb191 | quote: The Heroku Command Line Interface (CLI) is an essential part of using Heroku.
  - [2] 2026-11-03: a Platform API exists with a stated rate limit | capture: sha256:e221cf6e2d92fe3a56a1639dde471998168dad93eaa70f427c870cead69c334b | quote: The Heroku Platform API rate limit is 4500 calls per hour.
- sources:
  - [1] https://www.heroku.com/open-source-credit-program/
  - [2] https://devcenter.heroku.com/articles/limits
  - [3] https://devcenter.heroku.com/articles/heroku-cli

## Heroku (Compute)

- `compute/heroku` | paid-only | evidence documented | binding write-gated | category platform host | tier none
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://www.heroku.com/pricing/
- free tier: no free dyno: the pricing page prices dynos as containers with no USD 0 row. The only free lane found is the Student Developer Pack, which needs degree enrolment. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: nothing free
- retention: not applicable
- egress: not stated on the pricing page read | metered: no | source: [1]
- identity: card | detail: a card for a paid dyno; the Student Developer Pack alternative requires enrolment in a degree- or diploma-granting programme
- interface: unknown
- limits:
  - write-gated (binding): no free dyno on the pricing page [1]
- binding note: there is no free tier to exhaust.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: earlier readings verdict was 'fails-identity' on the grounds that the student pack is gated by enrolment. The accurate verdict for the free-tier question is paid-only: there is no free dyno at any identity level, and the student pack is a credit programme, not a tier. This is a verdict change the parent should carry into history.
- evidence note: the pricing page was read and lists dynos, data services and AI without a free row; prices render dynamically and are not quoted
- extras:
  - keep_rate: 1.0
  - billing_model: monthly
  - session_cap.restart_required: no
  - session_cap.note: a dyno runs until stopped or scaled to zero
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - term: monthly
  - price_arithmetic: not computed: dyno prices render through a client-side widget and no figure appears in the text read
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Seamlessly sync data between Heroku Postgres and Salesforce with Heroku Connect. Start free with the Demo Edition.' quoted; the page carries no free dyno and no free tier
  - [2] 2026-10-22: 'If you are registered with the GitHub Student Developer Pack, you are eligible to receive platform credits worth $13 per month for 24 months (for a total value of $312)', quoted; the Gate is the Student Developer Pack, whose own requirements state the applicant must be 'enrolled in a degree- or diploma-granting program' and 'provide documents that prove your current student status'
  - [1] 2026-10-24: quoted: 'Dynos are the heart of every Heroku app—lightweight, isolated containers that handle your code, dependencies, and scaling', with no free plan or free dyno row on the page
- sources:
  - [1] https://www.heroku.com/pricing/
  - [2] https://www.heroku.com/github-students/

## Heroku (free)

- `egress/heroku` | paid-only | evidence documented | binding volume-quota | category paas l4 port | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://devcenter.heroku.com/changelog-items/2502
- price USD 0
- free tier: As of November 28th, 2022, Heroku is no longer offering free dynos, hobby-dev Heroku Postgres, or hobby-dev Heroku Data for Redis plans. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No free tier since 2022-11-28; the cheapest dyno is Eco, a paid plan.; ingress: http-only | metered: yes | free allowance: No free tier since 2022-11-28; the cheapest dyno is Eco, a paid plan. | source: [1]
- identity: card | detail: A paid account with a payment method; free dynos were withdrawn. | country: None
- interface: cli, git
- limits:
  - volume-quota (binding): no free dynos since 2022-11-28 [1]
- binding note: Nothing is provisionable without payment, so no byte is ever free.
- interface detail: Heroku CLI, git push deploys, and the Platform API.
- tooling: Heroku CLI and git push.
- composes with: Not free; no endpoint.
- reliability: None applicable; no free dyno exists.
- notes: Kept because a reader will ask. Four years after the withdrawal the free tier has not returned.
- evidence note: Documentation confirms Heroku free product plans were retired effective 2022-11-28.
- extras:
  - wg_path: none
  - wg_detail: No UDP path at any price on the public runtime; dynos receive HTTP through the router, and raw TCP is a Private Spaces feature.
  - ingress: http-only
  - volume_tib_month: 0
  - volume_stated: No free tier since 2022-11-28; the cheapest dyno is Eco, a paid plan.
  - bytes_transit: no
  - transit_note: Heroku's router terminates HTTP.
- evidence:
  - [1] 2026-10-23: "As of November 28th, 2022, Heroku is no longer offering free dynos"; existing free dynos converted to eco and scaled to 0
- sources:
  - [1] https://devcenter.heroku.com/changelog-items/2502
