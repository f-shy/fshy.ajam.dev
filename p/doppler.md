# Doppler Team

> doppler.com | Developer services; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doppler/ | JSON https://fshy.ajam.dev/api/v1/entity/doppler.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Doppler

- `dev-services/doppler` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted secrets management and environment variable synchronization with a dashboard, REST API and CLI | tier Developer
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:26:47.756Z (live) | stale on 2026-12-20
- url https://www.doppler.com/pricing
- free tier: Developer plan: Free for 3 users, then USD 8 per month for each additional user, up to 25 users; includes the Doppler CLI for local development, service tokens, email alerts, 3 days of activity logs, secrets referencing, secret value types, API and webhooks access, and 5 config syncs | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The headline unit counted is the human user. Service tokens, CLI tokens and non-human identities are not billed as separate seats. The unit 'users' is the nearest schema term; the offer is per human seat with three free seats.
- per-object cap: Secret Value Size 50 KiB and Config Payload Size 500 KiB on every plan; 1,200 secrets per config on Developer | bytes: 51200 | source: [2] | note: The 50 KiB figure is the largest single secret value, which is the per-object cap; the bytes field holds 50 KiB = 51,200 bytes. A config payload can hold 500 KiB and at most 1,200 secrets.
- retention: Activity logs kept for 3 days on Developer; 90 days on Team and 1095 days on Enterprise. Secrets themselves persist until changed or deleted; no automatic secret expiry is stated on the pages read. | days: 3 | source: [2] | note: The 3-day figure is the activity log retention window, not a lifetime for stored secrets.
- egress: not applicable: a hosted secrets store, not a bulk transfer service. Secrets are read back through the REST API and CLI; API rate limits apply rather than a per-GB egress price. No per-GB egress charge or quota is stated on the pages read. | metered: no | source: [3]
- identity: email | detail: Sign-up page offers Google, GitHub and Email options; the Email option needs an email address and no card or phone is requested at registration. Pricing page Start for Free links to dashboard.doppler.com/register?plan=developer. Third-party pages state no card is required at signup, which is not confirmed by a first-party page read here.
- interface: rest, cli
- limits:
  - request-rate: API read 240/min, secret read 120/min, write 60/min on Developer; 429 response when the limit is hit [3]
  - per-object-cap: 50 KiB maximum secret value; 500 KiB config payload; 1,200 secrets per config [2]
  - volume-quota (binding): 5 config syncs, 10 projects, 4 environments, 10 configs per environment, 50 service tokens, 5 CLI tokens per user, 25 users on Developer [1]
  - retention-clamped: 3 days of activity logs on Developer [1]
- limits note: Config syncs count only syncs created in the dashboard or by the Secrets Sync API; Kubernetes Operator syncs and CLI secret fetches are excluded. Rate limits apply to direct API requests and to requests made by the CLI and Kubernetes Operator, and are per access token.
- binding note: The 5 config sync fill first for a project that syncs secrets to more than a few destinations, before the 240 reads per minute API rate is reached.
- interface detail: The Doppler API is organized around REST with predictable resource-oriented URLs, JSON-encoded request bodies and responses, and standard HTTP response codes. Authentication uses high entropy bearer tokens in the HTTP Authorization header, with CLI tokens, personal tokens, service tokens, service account tokens and SCIM and audit tokens. An official MCP Server and SDKs are listed on the pricing page.
- endpoint: https://api.doppler.com/v3
- tooling: Doppler CLI, the REST API with bearer tokens, official SDKs and the official MCP Server
- composes with: A hosted secrets store for local development and CI, with API and webhook access and 5 config syncs on Developer that push a config to destinations such as cloud platforms and infrastructure.
- reliability: The API answers 429 when a rate limit is hit; retry-after and rate limit headers are returned. No throttle, ban or data loss beyond the 3-day activity log window is stated on the pages read.
- notes: Doppler is a hosted secrets manager. Enterprise offers an on-prem or cloud deployment, but the Developer plan documented here is the hosted service the reader signs up for. Enforcement of the listed Developer limits and the identity cost beyond the registration options are unverified: behind a sign-up.
- evidence note: Plan limits, rate limits and per-object caps come from first-party pricing, API and platform-limits pages; the sign-up gate is read from the first-party registration page. No account was opened, so values only visible in an account are unverified.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the Developer plan is free for three users | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Free for 3 users
  - [1] 2026-11-19: each additional Developer user costs USD 8 per month | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: $8/mo per additional user
  - [1] 2026-11-19: Developer includes five config syncs | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Config syncs (5)
  - [1] 2026-11-19: Developer retains three days of activity logs | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: 3 days of activity logs
  - [1] 2026-11-19: the User ceiling is 25 on Developer and 500 on Team | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Users 25 500
  - [1] 2026-11-19: the project ceiling is 10 on Developer and 250 on Team | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Projects 10 250
  - [1] 2026-11-19: the Developer sign-up route is the registration page for the developer plan | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: [Start for Free](https://dashboard.doppler.com/register?plan=developer)
  - [3] 2026-11-19: the API is a REST interface with JSON over HTTPS | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: The Doppler API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
  - [3] 2026-11-19: API requests authenticate with a bearer token in the Authorization header | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: Authentication to the API is performed by providing a bearer token to the
  - [3] 2026-11-19: Developer rate limits are 240 reads, 120 secret reads and 60 writes per minute | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: Developer | 240 | 120 | 60 |
  - [3] 2026-11-19: exceeding a rate limit returns HTTP 429 | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: If you hit a rate limit, the API will respond with a 429 response code.
  - [2] 2026-11-19: a config holds at most 1,200 secrets | capture: sha256:15f8850de6f0d9d1ff435f61e0271d61ac73d6b11ea2bc01a42131ed824cfb43 | quote: Secrets per Config\* | 1,200
  - [2] 2026-11-19: a config payload is capped at 500 KiB | capture: sha256:15f8850de6f0d9d1ff435f61e0271d61ac73d6b11ea2bc01a42131ed824cfb43 | quote: Config Payload Size | 500 KiB
  - [2] 2026-11-19: a single secret value is capped at 50 KiB | capture: sha256:15f8850de6f0d9d1ff435f61e0271d61ac73d6b11ea2bc01a42131ed824cfb43 | quote: Secret Value Size | 50 KiB
  - [2] 2026-11-19: log retention is 3 days on Developer and 90 days on Team | capture: sha256:15f8850de6f0d9d1ff435f61e0271d61ac73d6b11ea2bc01a42131ed824cfb43 | quote: Logs | 3 days | 90 days
  - [4] 2026-11-19: the registration page presents the account creation options | capture: sha256:7fb6b1a0bb6278b59e05097d5ee0ec9b61341a98ff86d8a75ffcf28cc96820d7 | quote: Create an account using one of the following options.
  - [4] 2026-11-19: Google and GitHub are offered as registration options | capture: sha256:7fb6b1a0bb6278b59e05097d5ee0ec9b61341a98ff86d8a75ffcf28cc96820d7 | quote: Google ![](https://dashboard.doppler.com/imgs/github-inverse.png) GitHub
  - [4] 2026-11-19: an email registration option is offered | capture: sha256:7fb6b1a0bb6278b59e05097d5ee0ec9b61341a98ff86d8a75ffcf28cc96820d7 | quote: Email
- sources:
  - [1] https://www.doppler.com/pricing
  - [2] https://docs.doppler.com/docs/platform-limits
  - [3] https://docs.doppler.com/docs/api
  - [4] https://dashboard.doppler.com/register?plan=developer

## Doppler Team

- `dev-services/doppler-team` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted secrets management with config sync to deployment targets (SaaS; on-premises only on Enterprise) | tier Team
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:33:38.483Z (live) | stale on 2026-12-20
- url https://www.doppler.com/pricing
- free tier: Team plan: free for 14 days, then USD 21/mo per user; 90 Days of activity logs, 100 config syncs, 250 projects, 15 environments, 500 service tokens, SAML SSO, Role-Based Access Controls, automatic secret rotation and service accounts | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: Team is a 14-day trial followed by a per-human-seat charge; the bill counts human users, and the pricing page says AI agents and non-human identities ride free. The Developer plan above it is free for 3 users and USD 8/mo per additional user. USD 21 is the first paid tier with SSO and RBAC.
- per-object cap: unverified: the pricing and API pages state no size limit per secret; Doppler documents multi-line secrets such as PEM and SSH keys | source: [1]
- retention: Activity log retention is 90 days on Team, Custom on Enterprise; no expiry for stored secrets is stated on the pages read | days: 90 | source: [1] | note: The 90-day value applies to activity logs, not to secret values. No automatic expiry of stored secrets is stated on the pages read.
- egress: not applicable: a secrets management API; the pricing page names no traffic allowance or per-GB charge, and the API is reached over HTTPS at api.doppler.com | metered: no | source: [1]
- identity: email | detail: The sign-up page for the Developer plan says Create an account using one of the following options and offers Google, GitHub, Secure SSO or Email; no card, phone number or ID document is asked for on the sign-up page. The Team plan is a 14-day trial and the pricing page does not show whether a card is required to start it. Fields shown only after account creation are unverified: behind a sign-up.
- interface: rest, cli
- limits:
  - request-rate (binding): Team: 480 Reads/min, 240 Secret reads/min and 120 Writes/min per IP address; a further rate limit is tied to the API key [2]
  - volume-quota: 500 users, 250 projects, 15 environments, 500 service tokens and 100 config syncs on Team [1]
  - retention-clamped: 90 days of activity logs on Team [1]
  - write-gated: Add-ons on Team cost USD 9 per seat per month each for custom roles, user groups, or raising config syncs from 100 to 500; dynamic secrets, SCIM and on-premises need Enterprise [1]
- binding note: The per-IP rate limits apply to every API and CLI read; a workload pulling secrets through one CI address meets 480 Reads/min before the 500-user or 100-sync quotas are reached.
- interface detail: The Doppler API is organized around REST with predictable resource-oriented URLs, JSON request bodies and responses, and bearer-token authentication; base URL api.doppler.com. The open-source Doppler CLI injects secrets into a process with doppler run and reads values with doppler secrets get.
- endpoint: https://api.doppler.com/v3
- tooling: the Doppler CLI, the REST API at api.doppler.com, official SDKs, the MCP server and the web dashboard
- composes with: Secrets are delivered to apps and CI through the CLI, REST API, config syncs to deployment targets, and service tokens scoped to a single config.
- reliability: The API answers 429 when a rate limit is hit and sends x-ratelimit-limit, x-ratelimit-remaining, x-ratelimit-reset and retry-after headers; no data-loss event is stated on the pages read.
- evidence note: Plan limits, the rate-limit table and the sign-up fields are quoted from first-party Doppler pricing, API reference and registration pages. No account, trial or payment was created; any value visible only after registration is unverified.
- evidence:
  - [1] 2026-11-19: the Team plan is free for 14 days and then USD 21/mo per user | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Free for 14 days $21/mo per user
  - [1] 2026-11-19: human users are billed while AI agents and non-human identities are not | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Per-seat pricing for your team. AI agents and non-human identities ride free.
  - [1] 2026-11-19: Team includes 90 days of activity logs and 100 config syncs | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: 90 Days of activity logs
  - [1] 2026-11-19: Team includes 100 config syncs | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Config syncs (100)
  - [1] 2026-11-19: Team add-ons cost USD 9 per seat per month each | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Additional $9/seat per month
  - [1] 2026-11-19: the Developer plan is free for 3 users and USD 8/mo per additional user | capture: sha256:0661baba8eabc60d35a52768099ef95ad4ae8c7116b6fe47a89135a342baf4de | quote: Free for 3 users $8/mo per additional user
  - [2] 2026-11-19: the API is REST with JSON and bearer-token authentication | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: The Doppler API is organized around REST.
  - [2] 2026-11-19: the Team rate limits are 480 reads, 240 secret reads and 120 writes per minute | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: | Team | 480 | 240 | 120 |
  - [2] 2026-11-19: exceeding a rate limit answers 429 | capture: sha256:fe83ffd6b6129bac7d56dc5df587d05dcc2667bc6feccd4ebba50642d5a47816 | quote: If you hit a rate limit, the API will respond with a 429 response code.
  - [3] 2026-11-19: the sign-up page offers Google, GitHub, Secure SSO or Email and asks no card or phone field | capture: sha256:7fb6b1a0bb6278b59e05097d5ee0ec9b61341a98ff86d8a75ffcf28cc96820d7 | quote: Create an account using one of the following options.
  - [4] 2026-11-19: the Doppler CLI injects secrets across local development, CI/CD, staging and production | capture: sha256:10ad439bc77e581c82a8772e30df1690520a3bdb1f297e87d2d9f1ecfe5b6c4a | quote: The Doppler CLI provides access to your secrets in every environment, from local development, CI/CD, staging, and production.
- sources:
  - [1] https://www.doppler.com/pricing
  - [2] https://docs.doppler.com/reference/api
  - [3] https://dashboard.doppler.com/register?plan=developer
  - [4] https://docs.doppler.com/docs/cli
