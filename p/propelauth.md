# PropelAuth

> propelauth.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/propelauth/ | JSON https://fshy.ajam.dev/api/v1/entity/propelauth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PropelAuth

- `dev-services/propelauth` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted B2B customer identity and authentication (users, organizations, roles, sign-in and sign-up hosted pages) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.556Z (live) | stale on 2026-12-21
- url https://www.propelauth.com/pricing
- free tier: Free: $0 per month, includes 10,000 monthly active users, unlimited organizations, unlimited waitlist users, custom domain, 2FA and RBAC, customizable UIs, hosted org management UIs, passwords and passwordless magic links, SSO/social login, CAPTCHA and attack protection; email support; 30-day audit log retention | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: A monthly active user is counted only with login activity during the month. Waitlist users are not counted until invited and signed up. Transactional emails are capped at 10,000 on Free. Enterprise SSO, SCIM, API keys/M2M and MCP authentication are not on Free (Growth and up). Above 10,000 active users on Free the vendor emails the owner to upgrade and does not block logins.
- per-object cap: unverified: no per-user profile or per-object size cap is stated on the pricing, API or signup pages read
- retention: Audit Logs have 30 Day Retention on Free (60 days on Growth, 90 days on Growth Plus) | days: 30 | source: [1] | note: No retention period for user records or session lifetime is stated on the pages read; custom session duration is available on all plans.
- egress: not applicable: a hosted authentication API; no traffic allowance or egress term is published on the pricing page | metered: no | source: [1]
- identity: email | detail: The account sign-up page (auth.propelauth.com/en/signup) offers Sign up with Google, Sign up with GitHub, Sign up with Magic Link, Sign up with SSO, or Email and Password fields with a Sign up with email button; no credit card field is shown and the pricing page states Free at $0 per month. Whether a later dashboard step asks for a phone number or card is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 10,000 monthly active users on Free [1]
  - volume-quota (binding): 10,000 transactional emails on Free [1]
  - volume-quota (binding): 1 role mapping on Free (3 on Growth, Unlimited on Growth Plus) [1]
  - retention-clamped: Audit Logs kept 30 days on Free [1]
- limits note: Unknown number of API rate limits on Free: no numeric request-per-minute quota is published on the pages read.
- binding note: The 10,000 monthly active user count is the first hard ceiling reached; exceeding it does not block login but triggers an upgrade request, and enterprise SSO is unavailable at this tier.
- interface detail: A Backend REST API to manage users, organizations and API keys, called with an API key as an Authorization bearer token. Each environment (test, staging, production) has its own API key and its own Auth URL; the test URL is generated automatically (for example https://1581439057.propelauthtest.com) and staging and production use a custom domain such as https://auth.acme.com. Frontend SDKs and hosted sign-up, login and org-management pages are provided. User data export is available on request.
- endpoint: https://<your-auth-url>/api/backend/v1
- tooling: PropelAuth frontend and backend SDKs, hosted sign-up and login pages, a Postman collection, or any HTTP client against the Backend API with an API key bearer token.
- composes with: Login and multi-tenant organization store for a web app; a custom domain pairs with a name from domains-dns, and SAML or SCIM directory sync requires an upgrade to Growth or Growth Plus.
- reliability: No numeric API rate limit, throttle or ban behavior is stated on the pricing or API getting-started pages read; the vendor states it will email the owner above 10,000 active users on Free and will not prevent users from logging in.
- notes: PropelAuth also sells a self-hosted Bring-Your-Own-Auth option that adds features to an existing stack; the hosted Cloud Free plan is the offer recorded here, and the self-hosted option is not the answer while the hosted tier exists. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, retention and plan features are quoted from the first-party pricing page; identity gate from the first-party signup page and API access from the first-party API getting-started page. No account was opened, so signup fields past the first step are unverified and the rung stays documented.
- evidence:
  - [1] 2026-11-19: the Free plan costs $0 per month | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: ### Free - $0/month
  - [1] 2026-11-19: the Free plan includes 10,000 monthly active users | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: - Includes 10,000 MAUs
  - [1] 2026-11-19: Free has no additional-user charge; Growth charges $0.05 per extra user | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: | Additional monthly active users | No | $0.05 per user | Volume discounts |
  - [1] 2026-11-19: audit logs are retained 30 days on Free, 60 on Growth and 90 on Growth Plus | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: | Audit Logs | 30 Day Retention | 60 Day Retention | 90 Day Retention |
  - [1] 2026-11-19: exceeding 10,000 active users on Free prompts an upgrade email without blocking login | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: Congrats! We'll email you to ask you to upgrade. We will not prevent your users from logging in.
  - [1] 2026-11-19: the first paid plan, Growth, is $150 per month | capture: sha256:4b25dc3da3c9f32f64da3d1a45937ee1222d1b78a28e595c84fd5017f185f8ba | quote: ### Growth - $150/month
  - [2] 2026-11-19: the sign-up page offers a passwordless magic-link registration option | capture: sha256:314e1880f3227ccae6ac42372d00a3c0351137fca4289af8e05db3ed9f1e9a9f | quote: Sign up with Magic Link
  - [2] 2026-11-19: the sign-up page offers an email and password registration option | capture: sha256:314e1880f3227ccae6ac42372d00a3c0351137fca4289af8e05db3ed9f1e9a9f | quote: Sign up with email
  - [3] 2026-11-19: Backend API authentication uses an API key bearer token | capture: sha256:b4b2f07d71f26d9bf961e90318ec50528d977ef94cd882d3f18546585a22dccc | quote: The backend API requires an Authorization header with your API key set as a bearer token.
  - [2] 2026-11-20: the first-party sign-up form read 2026-11-20 shows email and password fields and no later steps | capture: sha256:314e1880f3227ccae6ac42372d00a3c0351137fca4289af8e05db3ed9f1e9a9f | quote: Email \* Password \*
- sources:
  - [1] https://www.propelauth.com/pricing
  - [2] https://auth.propelauth.com/en/signup
  - [3] https://docs.propelauth.com/reference/api/getting-started
