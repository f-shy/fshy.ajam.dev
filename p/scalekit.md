# Scalekit

> scalekit.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scalekit/ | JSON https://fshy.ajam.dev/api/v1/entity/scalekit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scalekit

- `dev-services/scalekit` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted customer identity and authentication for B2B SaaS (sign-up, sign-in, sessions, organizations, SSO, SCIM) | tier Free (SaaSKit Auth for SaaS)
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.659Z (live) | stale on 2026-12-21
- url https://www.scalekit.com/pricing/auth-for-saas
- free tier: Free: $0 per month, 25,000 monthly active users (hard cap, no overages), 25 monthly active organizations (hard cap, no overages), first SSO connection and first SCIM connection free, community and email support, Scalekit branding on auth widgets and emails; auto-upgrades to Growth after 25 organizations or 1 SSO and 1 SCIM connection | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: A user counts as a MAU if they log in or sign up at least once in a billing month. An organization counts as a MAO if it has at least 2 users and at least 1 of them logs in during a billing month. Development, QA, UAT and Staging environments are free and their usage does not count toward production quotas. The separate AgentKit Agent Gateway plan has different limits (5 users, 10,000 tool calls, 5 MCP connectors, 7-day audit log retention), which are not this tier.
- per-object cap: unverified: no per-user profile or per-object size cap is stated on the pricing, API or signup pages read
- retention: unverified: a user-data or session retention period for the Auth for SaaS Free tier is not stated on the pages read; the pricing page lists a dashboard audit trail only on the Enterprise plan | source: [1] | note: The AgentKit Agent Gateway Free plan states 7 days of audit log retention, a different product with its own tier.
- egress: not applicable: an authentication API; no traffic allowance or egress term is published on the pricing page | metered: no | source: [1]
- identity: email | detail: The account sign-up page (auth.scalekit.com/a/auth/signup) offers Continue with Google or Email and a Continue button, with no credit card field shown; the pricing page labels the Free plan Get started free at $0 per month. Production beyond a Free-plan hard cap needs a payment method on the workspace for the automatic upgrade. Whether a later dashboard step asks for a phone number or card is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 25,000 monthly active users on Free (hard cap, no overages) [1]
  - volume-quota (binding): 25 monthly active organizations on Free (hard cap, no overages) [1]
  - volume-quota (binding): first SSO connection and first SCIM connection free; a second enabled connection requires Growth [1]
- limits note: Every additional SSO or SCIM connection on Growth is billed per connection per month with volume discounts; the vocabulary has no kind for a connection count.
- binding note: The hard cap of 25,000 MAUs or 25 organizations ends production use on Free with no overage; reaching more than 1 SSO or SCIM connection also forces an upgrade.
- interface detail: A REST API (OpenAPI 3.1.1, API version 1.0.0) covering AgentKit and SaaSKit. All requests use HTTPS with base URLs https://{your-subdomain}.scalekit.dev for development and https://{your-subdomain}.scalekit.com for production. Authentication uses OAuth 2.0 Client Credentials: POST to /oauth/token with client_id, client_secret and grant_type=client_credentials to get a token sent as a bearer credential. Resources include organizations, users, SSO, directory sync, RBAC and sessions.
- endpoint: part of interface detail
- tooling: Scalekit SDKs and hosted auth widgets, the npx @scalekit-inc/cli setup tool, or any HTTP client against the REST API with an OAuth client credentials token.
- composes with: Login and user store for a web app; SSO and SCIM add-ons integrate a customer's existing identity provider, and the modular BYOA tier adds SSO or SCIM on top of an in-house auth system.
- reliability: A rate-limited request answers 429 with a Retry-After header on the Frontend API; the pricing page states 99.99%+ uptime. No ban or data-loss behavior is stated on the pages read.
- notes: A distinct AgentKit Agent Gateway product has its own Free plan (up to 5 users, 10,000 tool calls and 5 MCP connectors per month, 7-day audit log retention), documented on a separate pricing page; it is not this SaaSKit Auth tier. Scalekit lists Enterprise as the only on-prem or private-cloud option. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, MAU and MAO definitions, hard-cap behavior and the connection allowance are quoted from the first-party pricing page; identity gate from the first-party signup page and API access from the first-party API reference. No account was opened, so signup fields past the first step are unverified and the rung stays documented.
- evidence:
  - [1] 2026-11-19: the Free plan includes 25,000 monthly active users as a hard cap with no overages | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: Free: 25,000 MAUs included (hard cap, no overages)
  - [1] 2026-11-19: the Free plan includes 25 monthly active organizations as a hard cap | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: Free: 25 orgs included (hard cap, no overages)
  - [1] 2026-11-19: the definition of a monthly active user | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: A user counts as active (MAU) if they log in or sign up to your app at least once in a billing month. You are billed only for active users.
  - [1] 2026-11-19: production use stops at the hard cap and requires an upgrade | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: The Free plan is a hard cap with no overages. When you hit 25,000 MAUs, 25 orgs, or need more than 1 SSO connection, you upgrade to Growth.
  - [1] 2026-11-19: the first SSO connection and the first SCIM connection are each free | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: Your first connection of each type is free.
  - [1] 2026-11-19: development environments are free and only production usage is billed | capture: sha256:2fb7dbc07a6d6d4651e03572034d8057363e0a453226a4122c4472d99650a7d0 | quote: No. Development (Dev, QA, UAT, Staging) environments are free. Charges apply only to production usage.
  - [2] 2026-11-19: the sign-up page offers a Google social sign-in option | capture: sha256:906059958271727b40b868fe7872055cf93905bb7966b5c4da6a6ba1d957581b | quote: Continue with Google
  - [2] 2026-11-19: the sign-up page states a free start with no feature gating | capture: sha256:906059958271727b40b868fe7872055cf93905bb7966b5c4da6a6ba1d957581b | quote: Start free. No feature gating
  - [3] 2026-11-19: the API authenticates with the OAuth 2.0 client credentials grant | capture: sha256:9a578a3ae76d31180791c4d6aa91b38f35c7046f2d71b9edd521f446aa102ca2 | quote: Scalekit uses OAuth 2.0 Client Credentials for API authentication.
  - [3] 2026-11-19: the production API base URL format | capture: sha256:9a578a3ae76d31180791c4d6aa91b38f35c7046f2d71b9edd521f446aa102ca2 | quote: https://{your-subdomain}.scalekit.com (Production)
  - [2] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:6e5ae6d44a361dac6dab6da6185d2bff8ceb77a7dc60cea4d3a68402c1df9e12 | quote: Already have an account?Login
- sources:
  - [1] https://www.scalekit.com/pricing/auth-for-saas
  - [2] https://auth.scalekit.com/a/auth/signup
  - [3] https://docs.scalekit.com/apis
