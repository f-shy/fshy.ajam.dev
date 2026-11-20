# Descope

> descope.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/descope/ | JSON https://fshy.ajam.dev/api/v1/entity/descope.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Descope

- `dev-services/descope` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted customer identity and access management (passwordless, social, MFA, SSO, federated apps) | tier Free Forever
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:44.513Z (live) | stale on 2026-12-21
- url https://www.descope.com/pricing
- free tier: Free Forever plan at USD 0: 7,500 monthly active users, 10 monthly active tenants, 3 SSO connections, 1 federated app (OIDC), 5 test users, 10,000 M2M exchanges, 2,000 monthly active consents, 2,000 monthly active tokens, all auth methods, MFA, RBAC, no Descope watermark, community support and a 99% SLA; no overages, and an upgrade is required to exceed the limits | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: An MAU is any user that signs up or signs in over a 1-month period; a tenant is active when two or more users are associated and at least one logs in within a month. Multiple sign-ins by one user carry no extra charge. The paid tiers are Pro from USD 249/month, Growth from USD 799/month and a custom Enterprise plan.
- per-object cap: unverified: no per-object size cap is stated on the pages read; the platform applies a 200-task cap per flow and a 100-user cap on a batch create when a cleartext password is used | source: [2]
- retention: Audit events are retained for 1 week on Free Forever, 1 month on Pro and Growth, and a custom period on Enterprise | days: 7 | source: [1]
- egress: not applicable: a hosted authentication API; no traffic allowance or per-GB egress price is published | metered: no | source: [1]
- identity: email | detail: The console sign-in page asks for an email address and offers Google, GitHub, Microsoft and SSO as alternatives; the marketing sign-up page invites a Free Forever account. The pricing page states no credit card for Free Forever. Whether a later registration step asks for a phone number or a card is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 7,500 monthly active users on Free Forever [1]
  - volume-quota (binding): 10 monthly active tenants, 3 SSO connections and 1 federated app on Free Forever [1]
  - volume-quota (binding): 10,000 M2M exchanges, 2,000 monthly active consents and 2,000 monthly active tokens on Free Forever [1]
  - request-rate: the REST API allows 100 requests per 60 seconds with a 60-second backoff [2]
  - request-rate: user management paths under /v1/mgmt/user/* allow 1000 requests per 60 seconds; create paths allow 100 per 60 seconds [2]
  - retention-clamped: audit events kept 1 week on Free Forever [1]
- binding note: The 7,500-MAU ceiling binds first for a growing app; unlike paid tiers, Free Forever has no overages, so passing the user, tenant or SSO limit needs an upgrade.
- interface detail: A REST API over HTTPS with JSON request and response bodies, documented by a downloadable OpenAPI file. Sign-up and sign-in endpoints take the Project ID as a Bearer token; user-scoped endpoints take Project ID and Refresh JWT; management endpoints take a Management Key or Access Key. A 429 answer with a Retry-After header signals a rate limit.
- endpoint: https://api.descope.com
- tooling: Backend SDKs for Node, Python, Go, Java, Ruby, PHP and .NET, a descope CLI, the REST API with an OpenAPI description, the visual Flows builder, and embeddable admin widgets
- composes with: An OIDC or SAML identity provider in front of apps on free compute, with visual sign-in flows, passwordless and social login, MFA and RBAC; user management runs through the Management API.
- reliability: Rate-limited calls return HTTP 429 with a Retry-After header. Beyond 7,500 MAUs, 10 tenants or 3 SSO connections a warning email and a grace period apply before the app may lose access.
- notes: Descope also offers a managed SaaS for all tiers on this record. A paid startup plan offers Pro free for one year on application. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, retention and tier prices come from the first-party pricing page, and rate limits and API access from the first-party documentation. No probe was run and no account was opened; a sign-up would move the identity fields up a rung.
- evidence:
  - [1] 2026-11-19: the Free Forever plan includes 7,500 monthly active users | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: - 7,500 Monthly active users (MAUs)
  - [1] 2026-11-19: the Free Forever plan includes 10 monthly active tenants | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: - 10 Monthly active tenants
  - [1] 2026-11-19: the Free Forever plan includes 3 SSO connections | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: - 3 SSO connections
  - [1] 2026-11-19: the Free Forever plan has no overages and requires an upgrade to exceed its limits | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: No overages. Upgrade required to exceed limits.
  - [1] 2026-11-19: audit events are kept 1 week on Free, 1 month on Pro and Growth, and a custom period on Enterprise | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: | Audit Retention | 1 week | 1 month | 1 month | Custom |
  - [1] 2026-11-19: passing the Free Forever user, tenant or SSO limit requires an upgrade to Pro | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: You must move to the Pro tier if your app hits any of the limits–more than 7500 MAUs, 10 tenants, or 3 SSO connections.
  - [1] 2026-11-19: the definition of a monthly active user | capture: sha256:c422c95db8cb3419775456ac38f34f3b4eb7d4e170f7111d1c2a29e5985f8e41 | quote: A monthly active user is any user of your application that engages with Descope’s platform by signing up or signing in over a 1-month time period.
  - [2] 2026-11-19: the general REST API request rate is 100 per 60 seconds | capture: sha256:c0604d88bb8572d2b17a9736b37249964238daa8d3599b85193d663542e392ee | quote: Descope's API rate limits all traffic to 100 requests per 60 seconds with a 60-second backoff
  - [2] 2026-11-19: rate limits are keyed by IP for most calls and by project ID for user management | capture: sha256:c0604d88bb8572d2b17a9736b37249964238daa8d3599b85193d663542e392ee | quote: Descope calculates the rate limit based on IP address for most operations; however, rate limits for user management calls are limited based on project ID.
  - [2] 2026-11-19: user management paths allow 1000 requests per 60 seconds | capture: sha256:c0604d88bb8572d2b17a9736b37249964238daa8d3599b85193d663542e392ee | quote: Unless otherwise specified below, user management paths under `/v1/mgmt/user/*` are limited to 1000 requests per 60 seconds, with a 60-second backoff, whether initiated from the SDK or API.
  - [3] 2026-11-19: Descope exposes a REST API for authentication and management | capture: sha256:5a06fdd79dbc137ce06b87649113501e3b57ee0d4145914c92e31560758bbf17 | quote: The Descope REST API lets you implement every authentication method, every management function, and more directly in your own application.
  - [4] 2026-11-19: the console sign-in page asks for an email address | capture: sha256:c8ea5898f3f845f42973b3dc6dc292cb65de694b4acea60689a0074749e09f49 | quote: Email address
  - [5] 2026-11-19: the sign-up page offers a Free Forever account | capture: sha256:3eabf23aa4e25035095f0f261e37f7c22000916c899fc41e606c6363a151434e | quote: Sign up for a Free Forever account
  - [5] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:3eabf23aa4e25035095f0f261e37f7c22000916c899fc41e606c6363a151434e | quote: Sign up for a Free Forever account
- sources:
  - [1] https://www.descope.com/pricing
  - [2] https://docs.descope.com/rate-limiting
  - [3] https://docs.descope.com/api
  - [4] https://app.descope.com/login
  - [5] https://www.descope.com/sign-up
