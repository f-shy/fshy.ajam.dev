# Brave Search API

> brave.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/brave/ | JSON https://fshy.ajam.dev/api/v1/entity/brave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Brave Search API

- `crawler-scraper/brave-search` | fails-identity | evidence documented | binding request-rate | category search API
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T01:02:26.755Z (live) | stale on 2026-12-03
- url https://api-dashboard.search.brave.com/app/subscriptions/subscribe
- free tier: USD 5 of free credits every month, applied automatically; Search is priced at USD 5.00 per 1,000 requests, so the credit covers about 1,000 Search requests a month | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: no standalone free plan exists: each plan carries its own USD 5 monthly credit, reached by activating the plan with a card and setting the prepay amount to USD 0
- per-object cap: not applicable: the unit is a query | source: [2]
- retention: credit resets monthly | source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: card | detail: an email address and a password open the account, and a credit card is asked at the second step, when a plan is activated; the card is checked with a USD 0 or USD 1 hold that is refunded, some cards fail that check, and on a prepaid plan the service pauses when the balance reaches USD 0; the product FAQ answers 'Why do you ask for a credit card?' with 'To prevent abuse'
- interface: rest
- limits:
  - request-rate (binding): Search 50 requests per second and Answers 2 requests per second, drawn from a monthly credit of USD 5 [1]
  - request-rate (binding): a 1-second sliding window counts requests per plan, beside a monthly window; a request over the limit answers 429 [3]
- binding note: the monthly USD 5 credit, about 1,000 Search requests, is spent long before 50 requests per second binds
- interface detail: REST search API, 50 QPS on search, 2 QPS on answers
- tooling: not established
- composes with: the same as tooling
- reliability: no reliability event recorded
- notes: The signup gate is the whole finding: the allowance is real, a credit card is asked when a plan is activated, no standalone free plan exists, and a call without an API key is refused.
- evidence note: free tier, capacity and the card requirement quoted from first-party pages; the quickstart places the card at plan activation, after an account that needs an email address and a password
- evidence:
  - [2] 2026-10-22: 409 from the reader: the page is behind an authenticated dashboard and could not be read
  - [1] 2026-10-30: the Search plan includes USD 5 of free credits every month, at USD 5.00 per 1,000 requests | capture: sha256:7f5e060da618c003c472a509d73e6fde83dcf1df901ae49413577cd7236c2196 | quote: Includes free $5 in credits every month.
  - [1] 2026-10-30: Search capacity is 50 requests per second; the Answers plan on the same page states 2 requests per second | capture: sha256:7f5e060da618c003c472a509d73e6fde83dcf1df901ae49413577cd7236c2196 | quote: Capacity 50 requests per second
  - [3] 2026-10-30: a 1-second sliding window counts requests per plan; the same page states that an over-limit request answers 429 and that plans also carry a monthly window | capture: sha256:54eaa26e22e436f81ac3c9055833140c1e3358bc5efcdaca18db5ab608672f73 | quote: Rate limits are enforced using a 1-second sliding window to count requests per plan.
  - [4] 2026-10-30: the FAQ entry 'Why do you ask for a credit card?' answers that a card is asked to prevent abuse and only bought prepaid credits are charged | capture: sha256:04f88c46ab5236eaf90554a74584e5ccddfea320daeac3f752dd800fcd41e45d | quote: To prevent abuse. Brave uses prepaid credits, not subscriptions, so you’re only charged for credits you choose to buy.
  - [5] 2026-11-01: the plan activation runs a credit card check with a USD 0 or USD 1 hold even when the prepay amount is USD 0 | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: Note that even if you intend to set your spend to $0, the service will still need to complete the automatic credit card check with a $0 or $1 charge hold.
  - [6] 2026-11-01: the card is entered at the second step, plan activation, after the account exists | capture: sha256:e809eac99664e73b8796cb6fc613fc87a3d17358e9ea361f8e984bfe999374f8 | quote: Once your account is created, you'll need to activate a plan to access the API:
  - [5] 2026-11-01: no standalone free plan exists; each plan carries its own USD 5 monthly credit | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: We do not offer a standalone free plan. However, each plan receives $5 in free credits that renew every single month, which allows users to run proofs of concept and power small-scale projects.
  - [6] 2026-11-01: the quickstart lists a credit card as a prerequisite to activate a plan | capture: sha256:e809eac99664e73b8796cb6fc613fc87a3d17358e9ea361f8e984bfe999374f8 | quote: A credit card to activate a plan
  - [6] 2026-11-01: an account is created with an email address and a password, confirmed by a link sent to the address | capture: sha256:e809eac99664e73b8796cb6fc613fc87a3d17358e9ea361f8e984bfe999374f8 | quote: Enter your email address and create a secure password
  - [5] 2026-11-01: the USD 0 or USD 1 hold on the card is refunded at once | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: This is strictly a measure to prevent credit card fraud — any $0 or $1 hold placed on your credit card will be immediately refunded.
  - [5] 2026-11-01: some cards fail the card check and the FAQ points to a Visa or Mastercard credit or debit card | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: Try a different Visa or Mastercard credit or debit card, which works reliably with our authorization flow
  - [5] 2026-11-01: on a prepaid plan the service pauses when the balance reaches USD 0 | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: On a prepaid plan, further usage draws down your prepaid balance, and the service pauses once that balance reaches $0
  - [6] 2026-11-01: every request to the REST API carries the API key in the X-Subscription-Token header | capture: sha256:e809eac99664e73b8796cb6fc613fc87a3d17358e9ea361f8e984bfe999374f8 | quote: All requests require your API key in the `X-Subscription-Token` header.
  - probe:https://api.search.brave.com/res/v1/web/search?q=test 2026-11-01: a GET to the search endpoint without an API key answers HTTP 422 | capture: sha256:4f669ddb6671c994f3b6acae339118b9a9cb8bdff7451358d1d403ca9d2a4584 | quote: "status": 422
  - probe:https://api.search.brave.com/res/v1/web/search?q=test 2026-11-01: the 422 answer names the missing header x-subscription-token as a required field | capture: sha256:09dc98b2079e40b0822355c1bddfbecf2900a7f14db5362c113b97f539d1e432 | quote: "loc":["header","x-subscription-token"],"msg":"Field required","type":"missing"
  - [1] 2026-11-01: the Search plan capacity is 50 requests per second | capture: sha256:7f5e060da618c003c472a509d73e6fde83dcf1df901ae49413577cd7236c2196 | quote: Capacity 50 requests per second
  - [1] 2026-11-01: the Answers plan capacity is 2 requests per second | capture: sha256:7f5e060da618c003c472a509d73e6fde83dcf1df901ae49413577cd7236c2196 | quote: Capacity 2 requests per second
  - [3] 2026-11-01: a 1-second sliding window counts requests per plan | capture: sha256:54eaa26e22e436f81ac3c9055833140c1e3358bc5efcdaca18db5ab608672f73 | quote: Rate limits are enforced using a 1-second sliding window to count requests per plan.
  - [5] 2026-11-01: the free monthly credit is replaced each month and not carried over | capture: sha256:3c7a4a4c5883a3bc5e22a9bc1de14a22e084259b4a279e2ed4150ed15f4fcb1b | quote: Free monthly credits are the exception — those are replaced each month rather than carried over.
  - [1] 2026-11-01: the Search plan includes USD 5 of free credits every month | capture: sha256:7f5e060da618c003c472a509d73e6fde83dcf1df901ae49413577cd7236c2196 | quote: Includes free $5 in credits every month.
- sources:
  - [1] https://api-dashboard.search.brave.com/documentation/pricing
  - [2] https://api-dashboard.search.brave.com/app/subscriptions/subscribe
  - [3] https://api-dashboard.search.brave.com/documentation/guides/rate-limiting
  - [4] https://brave.com/search/api/
  - [5] https://api-dashboard.search.brave.com/documentation/resources/help-feedback
  - [6] https://api-dashboard.search.brave.com/documentation/quickstart
