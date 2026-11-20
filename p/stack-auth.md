# Stack Auth

> stack-auth.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stack-auth/ | JSON https://fshy.ajam.dev/api/v1/entity/stack-auth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stack Auth (Hexclave)

- `dev-services/stack-auth` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted authentication and user management (email, OAuth and magic links, teams, RBAC, analytics), managed Stack Auth now branded Hexclave | tier Free
- identity a placeholder: card and phone unknown | verified 2026-11-20T04:15:45.764Z (live) | stale on 2026-12-21
- url https://stack-auth.com/pricing
- free tier: Free: USD 0 forever, up to 10,000 auth users, 1 dashboard admin, 1,000 emails per month, email, OAuth and magic links, community support; the usage table also lists 100K analytics events per month and 2,500 session replays per month | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: An auth user is any user account in the project; inactive users still count toward the limit, but accounts can be deleted. This is a total-account count, not a monthly-active-user count. The first-party pricing and sign-in pages now use the name Hexclave for the product formerly called Stack Auth; the stack-auth.com domain still serves it.
- per-object cap: unverified: no per-object or user-profile size cap is stated on the pages read | source: [1]
- retention: unverified: no log or data retention period is stated on the pricing page; the page lists 2,500 session replays per month on every tier but does not state how long they are kept | source: [1]
- egress: not applicable: an authentication REST API; no traffic allowance or egress term is published | metered: no | source: [1]
- identity: email | detail: unverified: behind a sign-up. The hosted sign-in and sign-up pages run in a browser; no first-party capture of their form fields was obtained. The REST API uses a project ID with a publishable client key for client access or a secret server key for server access. No card requirement is stated on the pricing page, and the free tier starts at USD 0 forever. Whether the account form asks for a card, phone number or institution is unverified: behind a sign-up.
- interface: rest, browser
- limits:
  - volume-quota (binding): 10,000 auth users (total accounts, including inactive ones) on Free [1]
  - volume-quota (binding): 1,000 emails per month on Free [1]
  - volume-quota (binding): 1 dashboard admin on Free; extra admins are USD 29 each per month on paid tiers [1]
  - volume-quota (binding): 100K analytics events and 2,500 session replays per month on Free [1]
  - request-rate: REST API rate limits vary by endpoint and access type; exceeding them returns 429 Too Many Requests with retry headers [2]
- limits note: The analytics and session-replay allowances are per-month volumes with no dedicated vocabulary kind and are recorded as volume-quota rows. SAML SSO has no connections on Free (3 then USD 99 each on Growth).
- binding note: The 10,000 auth-user ceiling binds first because inactive accounts also count; below it, the 1,000-emails-per-month cap limits a product that sends verification or magic-link mail.
- interface detail: A REST API at api.hexclave.com/api/v1 for backends and frontends, authenticated with project ID plus a publishable client key for client access or a secret server key for server access; SDKs exist for Next.js, React, TanStack Start, JavaScript and TypeScript, with Python and other languages using the REST API. Hosted sign-in and sign-up component pages are served in a browser. The API answers 429 with retry headers when rate limited.
- endpoint: https://api.hexclave.com/api/v1/
- tooling: Hexclave SDKs (@hexclave/next, @hexclave/react, @hexclave/tanstack-start, @hexclave/js), the @hexclave/cli for local development and project commands, or any HTTP client against the REST API with project keys.
- composes with: Login, teams and RBAC for an app on free hosting, with email delivery on the Free plan limited to 1,000 messages a month. A self-hostable server Docker image that the reader installs and runs is offered under the same brand, listed last and not counted as a hosted tier.
- reliability: The API rate-limits by endpoint and access type and answers 429 with retry headers. The docs state the product changes rapidly and directs users to current documentation. No uptime SLA is on the Free tier; premium support and SLA are on Growth.
- notes: The first-party site now uses the name Hexclave for the product previously called Stack Auth; the scope name is kept as the record's provider label. The 10,000 free auth users is a total-account count, not an active-user count, and inactive accounts consume it. Self-hosting the server Docker image is a last-resort option and not a hosted tier. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Pricing, usage definitions and API access are quoted from first-party pricing, homepage and API documentation pages. The signup form fields could not be captured from a first-party page and are left unverified. No account was opened and no live API probe was run.
- evidence:
  - [1] 2026-11-19: the Free plan is USD 0 forever with up to 10,000 auth users, 1 dashboard admin and 1,000 emails per month | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: * Up to 10,000 auth users * 1 dashboard admin * 1,000 emails per month * Email, OAuth & magic links * Community support
  - [1] 2026-11-19: the usage table gives 10,000 auth users, 1 dashboard admin and 1,000 emails a month on Free | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: Auth users10,000 Dashboard admins1 Emails per month1,000
  - [1] 2026-11-19: Free includes 100K analytics events and 2,500 session replays per month | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: Analytics events / month100K Session replays / month2,500
  - [1] 2026-11-19: an auth user is any account in the project and inactive accounts still count toward the limit | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: An auth user is any user account in your project. Inactive users still count toward your limit, but you can delete accounts you no longer need.
  - [1] 2026-11-19: the product is now branded Hexclave and offers a self-hostable option the reader runs on their own infrastructure | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: Yes. Hexclave is open-source — client SDKs under MIT, server under AGPLv3 — and you can run the entire stack on your own infrastructure.
  - [1] 2026-11-19: email, social login, OIDC SSO and custom OIDC providers are listed on the Free tier | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: Email & social login Magic links & passkeys Custom branding OIDC / OAuth SSO
  - [3] 2026-11-19: the first-party homepage now names the product Hexclave and points to its documentation and API reference | capture: sha256:1722e687b8bc685dcb40c3724548fb38737b42197cac89ee370c67a16ef07e63 | quote: # Hexclave Hexclave is the open-source platform for everything user. It provides modular building blocks for authentication, payments, emails, analytics, teams, RBAC, webhooks, API keys, and secure data vaults that fit around your product.
  - [2] 2026-11-19: a REST API is available to backends and frontends of any language | capture: sha256:023c2fc3e2690b525fefde022a005e48290c870e693e63a114dd923ee6e8c6ca | quote: Stack offers a REST API for backends & frontends of any programming language or framework.
  - [2] 2026-11-19: the REST API is authenticated with a publishable client key for clients and a secret server key for backends | capture: sha256:023c2fc3e2690b525fefde022a005e48290c870e693e63a114dd923ee6e8c6ca | quote: | `X-Stack-Secret-Server-Key` | string | Server only | Required for server access. Never expose in client code. Starts with `ssk_`. |
  - [2] 2026-11-19: the API answers 429 with retry headers when rate limited | capture: sha256:023c2fc3e2690b525fefde022a005e48290c870e693e63a114dd923ee6e8c6ca | quote: Yes, Hexclave implements rate limiting to ensure fair usage and system stability. Rate limits vary by endpoint and access type. When you exceed the rate limit, you'll receive a `429 Too Many Requests` response with headers indicating when you can retry.
  - [1] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:1e9243ad807510c4916a8ae40b3478475ad5f3bd669e01a14d0cb0d742b0fe8a | quote: * Email, OAuth & magic links
- sources:
  - [1] https://stack-auth.com/pricing
  - [2] https://docs.stack-auth.com/api/overview
  - [3] https://stack-auth.com/
