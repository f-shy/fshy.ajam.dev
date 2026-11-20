# Linkup

> linkup.so | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linkup/ | JSON https://fshy.ajam.dev/api/v1/entity/linkup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linkup

- `crawler-scraper/linkup` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:01:46.988Z (live) | stale on 2026-12-03
- url https://docs.linkup.so/pages/documentation/platform/pricing.md
- free tier: USD 20 credited on signup with a professional email address and topped back up to USD 20 each month; a standard or fast search with raw results costs USD 0.005, about 4,000 searches a month | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: The marketing page states the same allowance as 4,000 queries for free. Deep search costs USD 0.05 a call (USD 20 / USD 0.05 = 400 deep searches).
- per-object cap: not applicable | source: [1]
- retention: eligible accounts are topped back up to USD 20 each month | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: the signup form asks for a name, a professional email address and a password, or Google, GitHub or Microsoft sign-in, and a form sign-up is completed from the inbox; a professional email address is credited automatically with no card; any other sign-up is not eligible for free credits by default and adds a card, with no payment required, to unlock them (amount not stated)
- interface: rest
- limits:
  - request-rate (binding): USD 20 a month for professional-email accounts; USD 0.005 per standard or fast search with raw results, USD 0.006 with a sourced answer, USD 0.05 per deep search; the API answers 429 when the balance runs out [1]
  - request-rate (binding): 10 queries a second per organization on search and fetch; x402 requests are limited per IP address instead [2]
- binding note: the monthly USD 20 balance, about 4,000 searches, runs out long before 10 queries a second does
- interface detail: POST https://api.linkup.so/v1/search with a Bearer API key; fetch, research and tasks endpoints on the same balance; an x402 route takes USD 0.01 a request in USDC on Base with no account or key
- endpoint: part of interface detail
- tooling: Python SDK (pip install linkup-sdk), JavaScript SDK (npm i linkup-sdk) and a CLI (linkup-search-cli)
- composes with: A recurring search leg of about 4,000 raw-result searches a month beside Tavily's 1,000 credits, where the account has a professional email; the x402 route is a paid, account-free fallback at USD 0.01 a request
- reliability: an exhausted balance answers 429, the same status as a rate limit; no throttle or ban event recorded
- notes: The free balance renews monthly, which sets it apart from one-time signup grants in this class. The pricing page names professional email addresses as the eligible ones. The app tells any other sign-up that free credits are not granted by default and that adding a card, with no payment required, unlocks them; the amount unlocked, and whether the monthly top-up then applies, is not stated. An archived copy of the pricing page from June 2026 states the credit with no email condition, and one from August 2026 states it for professional email addresses. The x402 route bills a flat USD 0.01 a request on search and fetch.
- evidence note: the monthly top-up, the per-call prices, the rate limit and the no-card statement are quoted from first-party pages; no keyed search was made, so the read path is unprobed; the app's own text says only organizations signed up with a professional email address are eligible for free credits by default and that other sign-ups add a card, with no payment required, to unlock them; the amount a webmail account receives after that step is behind a sign-up and a card, so it is unverified
- evidence:
  - [1] 2026-10-30: USD 20 on signup with a professional email, topped back to USD 20 monthly | capture: sha256:55ce46f7125d6cc9dd137136e0af02ec96a53561afc083da27138c8d53c5b679 | quote: When you first sign up with a professional email address, your account is automatically credited with \$20. We will top up eligible accounts back to \$20 each month.
  - [1] 2026-10-30: an exhausted balance answers 429 | capture: sha256:55ce46f7125d6cc9dd137136e0af02ec96a53561afc083da27138c8d53c5b679 | quote: If your account runs out, the API will respond with a `429` HTTP error.
  - [3] 2026-10-30: the free allowance is stated as 4,000 queries | capture: sha256:6d83025fd07837d6084dcee4a8db8a39c4e77123c82813516f63c1c87acf474c | quote: Run 4,000 queries for free.
  - [2] 2026-10-30: search and fetch are limited to 10 queries a second per organization | capture: sha256:3e395d309fca3ef0c841209b543031849c8a559701de9c184e5f116dd64c1e05 | quote: our rate limits are currently set at `10 queries per second` per organization
  - [2] 2026-10-30: x402 requests are rate-limited per IP address | capture: sha256:3e395d309fca3ef0c841209b543031849c8a559701de9c184e5f116dd64c1e05 | quote: rate limits are applied per IP address instead of per organization
  - [4] 2026-10-30: the signup form asks for a professional email, with Google, GitHub and Microsoft sign-in as alternatives | capture: sha256:cfba42e83e6b166167676f8ab5e7f4983828216fb4b5885e55150cd20be18a5a | quote: Professional email
  - [5] 2026-10-30: an account-free paid route exists through x402 | capture: sha256:0cc79b8f951fd4151f233226f1a6a25d30e6e95ae12122c0dcc3ae80747f3cec | quote: pay per request in USDC on the Base network, with no account or API key required
  - [6] 2026-10-30: a Python SDK, a JavaScript SDK and a CLI are published | capture: sha256:d17a2ad88bd99395d23f33f431231492d5cc396ea7005129a134ce9613f4924a | quote: pip install linkup-sdk
  - [7] 2026-10-30: the monthly free top-up rose from 5 to 20 in May 2026 | capture: sha256:277f09530789535eddafe5c32cb31178c88a000452f4b861b49af2c853a15417 | quote: the monthly free top-up for eligible accounts quadruples from \$5 to \$20
  - [8] 2026-11-01: the app states that only organizations signed up with a professional email address are eligible for free credits by default, and that adding a card, with no payment required, unlocks them | capture: sha256:0eab2d6cc523585a543bd3c5b81c139747f92b0eb5a6824a820dde918a16cbcb | quote: Only organizations signed up with a professional email address are eligible for free credits by default. Add a card to unlock your free credits and future gifts. <strong>No payment required.</strong>
  - [9] 2026-11-01: the blog states USD 20 of free credit and no card requirement for new accounts, without the professional-email condition that the pricing page and the app state | capture: sha256:2ea812c0e2eec7b49bf33666bf6aadcc45cc97a60c5a429cd1d99aebebff23d1 | quote: New accounts start with $20 of free credit. No credit card required.
  - [8] 2026-11-01: the app confirms that a card added through its card-verification step unlocks the account's free credits, and states no amount | capture: sha256:0eab2d6cc523585a543bd3c5b81c139747f92b0eb5a6824a820dde918a16cbcb | quote: Your card was added successfully. Your free credits will be unlocked shortly.
  - [8] 2026-11-01: a sign-up through the form is completed from the inbox | capture: sha256:0eab2d6cc523585a543bd3c5b81c139747f92b0eb5a6824a820dde918a16cbcb | quote: Account created successfully, check your inbox to complete your registration.
  - [4] 2026-11-01: the signup page offers Google, GitHub and Microsoft sign-up beside a form that asks for a name, a professional email and a password | capture: sha256:d94c958fa721037f2e7927dbaca13231367ab3b19bc43f642f233ed3e1bc2da1 | quote: Sign up via GoogleSign up via GithubSign up via Microsoft OR Name Professional email Password
  - [7] 2026-11-01: the changelog states the monthly USD 20 free top-up for accounts created with a professional email address | capture: sha256:277f09530789535eddafe5c32cb31178c88a000452f4b861b49af2c853a15417 | quote: For accounts created with a professional email address, the monthly free top-up is now \$20.
  - [10] 2026-11-01: an archived copy of the pricing page from June 2026 states the USD 20 credit and monthly top-up with no email condition | capture: sha256:b096e04ea91688e828ea892bf48a1a7a4e31fa77f04b09adaa81a4ae45b8f623 | quote: When you first sign up, your account is automatically credited with $20. We will top up your credits back to $20 each month.
  - [11] 2026-11-01: an archived copy of the pricing page from August 2026 states the USD 20 credit and monthly top-up for professional email addresses | capture: sha256:339362e629ab510f224f052fba125e57ad49e1c764d91a0b41ed0adeb72fbb09 | quote: When you first sign up with a professional email address, your account is automatically credited with $20. We will top up eligible accounts back to $20 each month.
  - [12] 2026-11-01: a third-party catalogue reports that the app asks sign-ups without a professional email address to add a card, with no charge, to unlock the credit | capture: sha256:3760e5dc91e5a542b01d22ed48c2e694773b42bb69e1692c7a6ee40cb88ca841 | quote: Linkup's app asks other sign-ups to add a card, with no charge, to unlock the credit.
  - [1] 2026-11-01: the pricing page states the USD 20 credit on signup and the monthly top-up for professional email addresses | capture: sha256:55ce46f7125d6cc9dd137136e0af02ec96a53561afc083da27138c8d53c5b679 | quote: When you first sign up with a professional email address, your account is automatically credited with \$20. We will top up eligible accounts back to \$20 each month.
- sources:
  - [1] https://docs.linkup.so/pages/documentation/platform/pricing.md
  - [2] https://docs.linkup.so/pages/documentation/platform/rate-limits.md
  - [3] https://www.linkup.so/pricing
  - [4] https://app.linkup.so/sign-up
  - [5] https://docs.linkup.so/pages/documentation/platform/x402.md
  - [6] https://docs.linkup.so/pages/documentation/get-started/quickstart.md
  - [7] https://docs.linkup.so/pages/changelog/usd-pricing.md
  - [8] https://app.linkup.so/assets/index-BhsjN0f5.js
  - [9] https://www.linkup.so/blog/how-to-migrate-from-serp-apis-to-linkup
  - [10] https://web.archive.org/web/20260605231546/https://docs.linkup.so/pages/documentation/platform/pricing
  - [11] https://web.archive.org/web/20260814161743/https://docs.linkup.so/pages/documentation/platform/pricing
  - [12] https://agentdeals.dev/vendor/linkup
