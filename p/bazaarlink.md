# BazaarLink

> bazaarlink.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bazaarlink/ | JSON https://fshy.ajam.dev/api/v1/entity/bazaarlink.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BazaarLink

- `inference/bazaarlink` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway, free models with a daily weighted-unit cap
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://bazaarlink.ai/en/free
- free tier: 5 enabled free models at the time read; accounts without credit get 10 requests per minute and 60 weighted units a day, accounts with credit 20 per minute and 120 a day, shared across free models and reset at 00:00 UTC | unit: mixed | metered on: request-count | read on: 2026-11-04 | source: [1] | note: longer inputs use more daily units; site-wide free cap 20 requests per minute; 2 concurrent free requests per account; an additional IP guard applies
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the login page offers an email field with a verification code plus Google, GitHub and Microsoft sign-in; the FAQ says a key can be created without adding a credit card
- interface: rest
- limits:
  - request-rate: 10 requests per minute without credit, 20 with credit; 2 concurrent free requests per account [1]
  - volume-quota (binding): 60 weighted units a day without credit, 120 with credit [1]
- binding note: 60 weighted units a day binds before the 10 requests per minute
- endpoint: https://api.bazaarlink.ai/v1/chat/completions
- tooling: OpenAI-compatible client at https://api.bazaarlink.ai/v1; auto:free routes to a free model
- composes with: at $5 of credit the paid tier raises the request rate to 200 per minute
- reliability: free models and quotas change dynamically; the free page prints a last-24h probe success of 96% to 100% per model
- notes: free quota rules are configured dynamically per the vendor FAQ
- evidence:
  - [1] 2026-11-04: the free limits per account class | capture: sha256:7e5b5fc31ef4547de58f03a96c6e7c67ec832df038e1c551d2fa18c5bab7c5ee | quote: Free use has shared account limits: 10/20 RPM and 60/120 weighted units per day for no-credit/credited accounts.
  - [1] 2026-11-04: 2 concurrent free requests per account | capture: sha256:7e5b5fc31ef4547de58f03a96c6e7c67ec832df038e1c551d2fa18c5bab7c5ee | quote: Concurrent free requests per account`2`
  - [2] 2026-11-04: no card is needed to register and use free models | capture: sha256:33ab3fe06f7dce31628e88f07fc44bb060b36d2aac1fb9620473238c47e7cd27 | quote: You can register and create an API key without adding a credit card first, then use the free models or auto:free routes available at that time.
  - [3] 2026-11-04: a paid account with $5 of credit gets 200 requests per minute | capture: sha256:37091d29020e3355104fe2c27ae20e3d4e0299008917b53bff201b97f4cf866d | quote: Paid (≥ $5 credits)200 RPM
  - [4] 2026-11-04: the login page offers Google sign-in | capture: sha256:f9d01c007f2801ca7607f755ba808d70c04cf6a716611f207982fcfb0be8a076 | quote: Continue with Google
  - [4] 2026-11-04: the login page offers an email field | capture: sha256:f9d01c007f2801ca7607f755ba808d70c04cf6a716611f207982fcfb0be8a076 | quote: type="email"
  - probe:https://api.bazaarlink.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:e2876fe13f58128975c35800d0a7c1f988fabfe2c9d1bda7122c6afb07a49be0 | quote: "status": 401
- sources:
  - [1] https://bazaarlink.ai/en/free
  - [2] https://bazaarlink.ai/en/faq
  - [3] https://bazaarlink.ai/en/docs
  - [4] https://bazaarlink.ai/login
