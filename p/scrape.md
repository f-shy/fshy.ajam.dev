# Scrape.do

> scrape.do | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrape/ | JSON https://fshy.ajam.dev/api/v1/entity/scrape.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrape.do

- `crawler-scraper/scrapedo` | qualifies-with-caveat | evidence measured | binding request-rate | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:38:35.049Z (live) | stale on 2027-01-19
- url https://scrape.do/
- free tier: 1,000 successful calls a month | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a call | source: [1]
- retention: allowance resets monthly | source: [1]
- egress: not applicable: Markdown or JSON answers | metered: no | source: [1]
- identity: email | detail: signup is an account; no card stated
- interface: rest
- limits:
  - request-rate (binding): 1,000 successful calls a month and 5 concurrent
- binding note: 1,000 successful API credits per month on the Free plan, charged only on success, with 5 concurrent requests
- interface detail: REST, 5 concurrent on the free tier
- tooling: not established
- composes with: the same as tooling
- reliability: no reliability event recorded
- notes: Only successful calls are counted, which makes a retry free but a failure invisible in the quota.
- evidence note: Re-read on 2026-11-19: first-party pricing page reached live at HTTP 200 and a broker-fetched sign-up page confirmed the identity gate.
- evidence:
  - [1] 2026-10-22: 
  - probe:https://scrape.do/pricing 2026-11-19: the first-party pricing page answered a live HTTP GET with status 200 on 2026-11-19 | capture: sha256:f5c779dc776c68f529d095ff99fbe36def001a57f39a9052a3e45bc4a2fc4605 | quote: "status": 200
  - probe:https://scrape.do/pricing 2026-11-19: the first-party pricing page was live on 2026-11-19 | capture: sha256:f5c779dc776c68f529d095ff99fbe36def001a57f39a9052a3e45bc4a2fc4605 | quote: "status": 200
  - [2] 2026-11-19: the binding Free-plan constraint is the monthly successful-credit allowance with 5 concurrent requests | capture: sha256:643b33f63dc471598881db79a55e23ac22fbe2731b681d26c4d21f4fb30264f6 | quote: 1,000 Successful API Credits ... 5 Concurrent Requests
  - [2] 2026-11-19: the Free plan allowance is 1,000 successful calls per month and charges only successful calls | capture: sha256:5ac8c53022f2eab551c6e33313154b03fe9e1e02da5090320a4e59f0fda13763 | quote: The free plan includes 1,000 successful API calls per month with full access to residential and mobile proxies, geo-targeting, CAPTCHA handling, JavaScript rendering, and more—no credit card required.
  - [2] 2026-11-19: the first-party pricing page states the Free plan allowance and concurrency on 2026-11-19 | capture: sha256:643b33f63dc471598881db79a55e23ac22fbe2731b681d26c4d21f4fb30264f6 | quote: 1,000 Successful API Credits ... 5 Concurrent Requests
  - [3] 2026-11-19: the first-party sign-up page names the identity gate on 2026-11-19 | capture: sha256:2ef21736e0351742fb31568d25dbcc0516a31c1397762d14c143f2c592cfc1ca | quote: No credit card required for free trial. ... Continue with Google Continue with GitHub Continue with LinkedIn OR Email Continue
  - [1] 2026-11-19: the free plan grants 1,000 successful API credits at no charge | capture: sha256:9a03d2eb153f4961ce69f180e9fe817c27598b45e2daabc52ed22408c873ee62 | quote: Yes! Get 1,000 successful API credits with 5 concurrent requests, completely free.
  - [2] 2026-11-19: the Free plan allowance is 1,000 successful API credits with 5 concurrent requests | capture: sha256:643b33f63dc471598881db79a55e23ac22fbe2731b681d26c4d21f4fb30264f6 | quote: 1,000 Successful API Credits 5 Concurrent Requests
  - [3] 2026-11-19: sign-up is an account created with email or a social provider, and no card is required for the free trial | capture: sha256:85eae094d674f2dea28b88cfc583989e811921bdd8b93b3976b6088f762946fa | quote: No credit card required for free trial. Continue with Google Continue with GitHub Continue with LinkedIn OR Email
  - [1] 2026-11-19: only successful requests consume the credit allowance; failed requests are not charged | capture: sha256:9a03d2eb153f4961ce69f180e9fe817c27598b45e2daabc52ed22408c873ee62 | quote: Only successful requests use up API credits—failed requests won't be deducted from your balance.
- sources:
  - [1] https://scrape.do/
  - [2] https://scrape.do/pricing
  - [3] https://dashboard.scrape.do/sign-up
