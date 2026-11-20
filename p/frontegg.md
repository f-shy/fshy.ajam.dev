# Frontegg

> frontegg.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frontegg/ | JSON https://fshy.ajam.dev/api/v1/entity/frontegg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Frontegg

- `dev-services/frontegg` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted customer identity and access management for B2B SaaS (hosted login, users, tenants, SSO, SCIM) | tier Pay as you go
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:44.618Z (live) | stale on 2026-12-21
- url https://frontegg.com/pricing
- free tier: Pay as you go: $0 per month for up to 7,500 monthly active users, 5 enterprise connections (SSO/SCIM), unlimited organizations, fully customized hosted login and a custom domain; no credit card needed to start; unlimited team seats | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: A monthly active user is a user who logs in at least once in a calendar month. SSO and SCIM are counted separately, so a customer using both counts as two connections; the 5 included connections are shared across both types. The pricing page states pay only for what you use starting free up to 7,500 users and shows a calculator for M2M tokens, but does not publish a per-user price past the free allowance.
- per-object cap: unverified: no per-user profile or per-object size cap is stated on the pricing, API or quickstart pages read
- retention: unverified: no user-data, session or audit-log retention period for the Pay as you go plan is stated on the pricing, API or rate-limit pages read | source: [1] | note: Enterprise adds audit log streaming; no retention duration is stated on the pricing page.
- egress: not applicable: a hosted authentication API; no traffic allowance or egress term is published on the pricing page | metered: no | source: [1]
- identity: email | detail: The first-party quickstart states: sign up with your email or GitHub/Google account from frontegg.com Start for free; the pricing page states no credit card is needed to start. The rendered form fields of the signup portal (portal.frontegg.com/signup) are unverified behind a login wall. Whether a later step asks for a phone number or card is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 7,500 monthly active users on Pay as you go [1]
  - volume-quota (binding): 5 enterprise connections (SSO/SCIM) on Pay as you go [1]
  - request-rate: general API rate limit 100 requests per minute per IP on the Launch tier (1,000 per minute on Scale and Enterprise); 429 on exceed [2]
  - per-ip-shaping: user sign-up 5 per minute per VendorId on Launch (10 per minute per IP on Scale); user password authentication 10 per minute per VendorId on Launch [2]
- limits note: Many per-endpoint rate limits are keyed per IP or per VendorId (environment ID); the vocabulary has no separate kind for a per-environment key, so per-environment-key limits are named in text.
- binding note: The 7,500 monthly active user ceiling and the 5 shared SSO/SCIM connections are the first limits reached; per-IP and per-VendorId rate limits bind on individual high-volume endpoints.
- interface detail: REST APIs grouped as Authentication APIs (login, MFA, passwordless, social login, usually no authorization required), Management APIs (configuration, require an environment token) and Self-service APIs (user and tenant actions, user or environment token). Regional gateways are https://api.frontegg.com (EU), https://api.us.frontegg.com (US), https://api.au.frontegg.com (AU) and https://api.ca.frontegg.com (CA). A bearer token from POST /auth/vendor with a Client ID and API Key authorizes Management calls; OpenAPI specifications and generated SDKs are published.
- endpoint: part of interface detail
- tooling: Frontegg frontend SDKs (React, Next.js, Angular, Vue, JavaScript) and backend SDKs (Node.js, Python, Java) or JWKS token validation, a generated TypeScript SDK from the OpenAPI spec, or any HTTP client against the REST APIs.
- composes with: Hosted login and tenant store for a web app; a custom domain pairs with a name from domains-dns, and SSO or SCIM enterprise connections consume the 5 included allowances on Pay as you go.
- reliability: An API request that exceeds a rate limit answers HTTP 429 Too Many Requests; the vendor recommends a back-off strategy. Limits are scoped per IP address or per environment ID (Vendor ID).
- notes: Frontegg also offers private or on-prem deployment under Enterprise; the hosted Pay as you go plan is the offer recorded here and is not self-hosted. The per-user price above 7,500 MAUs is not published on the pricing page, so the free allowance is quoted and no marginal price is invented. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, connection allowance and no-card statement are quoted from the first-party pricing page; rate limits from the first-party developer docs and API access from the first-party API overview. The signup gate is from the first-party quickstart; the login-walled signup form itself was not readable, so its fields are unverified and the rung stays documented.
- evidence:
  - [1] 2026-11-19: the Pay as you go plan is free up to 7,500 MAUs and 5 enterprise connections with no credit card | capture: sha256:a4f7b591f253971e65c3f8a803db3a8cb0839f272c81a6b228a5af76f95bbed3 | quote: Yes. The Pay as you go plan is $0 a month for up to 7,500 monthly active users and 5 enterprise SSO/SCIM connections, with unlimited organizations, a fully customized hosted login and a custom domain. No credit card is needed to start.
  - [1] 2026-11-19: the definition of a monthly active user | capture: sha256:a4f7b591f253971e65c3f8a803db3a8cb0839f272c81a6b228a5af76f95bbed3 | quote: A user who logs in at least once in a calendar month.
  - [1] 2026-11-19: SSO and SCIM connections are counted separately against the 5-connection allowance | capture: sha256:a4f7b591f253971e65c3f8a803db3a8cb0839f272c81a6b228a5af76f95bbed3 | quote: SSO and SCIM are counted separately, so a customer can have SSO without SCIM or the other way around.
  - [1] 2026-11-19: the plans do not bind by seat or organization count | capture: sha256:a4f7b591f253971e65c3f8a803db3a8cb0839f272c81a6b228a5af76f95bbed3 | quote: No. Both plans include unlimited team seats and unlimited organizations (tenants).
  - [2] 2026-11-19: the general API rate limit is 100 per minute per IP on Launch | capture: sha256:ad6484391a005cf0b7e819a6033ebf3b5d0bc6f14bf35d996e3264bf6e92967e | quote: General rate limit | | | 100/min per IP | 1000/min per IP | 1000/min per IP |
  - [2] 2026-11-19: exceeding a rate limit answers HTTP 429 | capture: sha256:ad6484391a005cf0b7e819a6033ebf3b5d0bc6f14bf35d996e3264bf6e92967e | quote: When rate limits are exceeded, Frontegg responds with an HTTP Status Code 429 (Too Many Requests).
  - [3] 2026-11-19: Management APIs need an environment token | capture: sha256:4525b894f1c0cc1c18baa7fa5fb5436735ed58c6a884463497396b6471cd4223 | quote: Management APIs require environment-level authorization, can only be used with your environment token
  - [3] 2026-11-19: the EU API gateway endpoint | capture: sha256:4525b894f1c0cc1c18baa7fa5fb5436735ed58c6a884463497396b6471cd4223 | quote: | EU | https://api.frontegg.com |
  - [4] 2026-11-19: the first-party quickstart states signup needs an email or a GitHub or Google account | capture: sha256:ec3b3c064acaf65137c22a3b14bb78321ff69931e1389e35faae2e0ac4924aba | quote: 2. Sign up with your email or GitHub/Google account.
  - [4] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:ec3b3c064acaf65137c22a3b14bb78321ff69931e1389e35faae2e0ac4924aba | quote: 2. Sign up with your email or GitHub/Google account.
- sources:
  - [1] https://frontegg.com/pricing
  - [2] https://developers.frontegg.com/ciam/guides/env-settings/rate-limits
  - [3] https://developers.frontegg.com/ciam/api/overview
  - [4] https://developers.frontegg.com/ciam/guides/getting-started/quick-start
