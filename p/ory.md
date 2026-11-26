# Ory

> ory.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ory/ | JSON https://fshy.ajam.dev/api/v1/entity/ory.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ory

- `dev-services/ory` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted identity, authentication, OAuth 2.0 and OpenID Connect, and fine-grained authorization APIs | tier Developer
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.349Z (live) | stale on 2026-12-21
- url https://www.ory.com/pricing
- free tier: Developer plan, free: 1 member, 0 production environments, 2 development environments, 0 staging environments, no included monthly credit, no per-aDAU price, no per-M2M-token price and no per-permission-check price; the administrative interface and zero-downtime migrations are available | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The free tier is a development tier: it has no production or staging environments and no included usage credit, so running production traffic needs the Production plan at USD 770/year, which includes a USD 21 monthly credit and charges USD 0.14 per average daily active user per month beyond it. Ory prices by average daily active users (aDAU), not MAU.
- per-object cap: unverified: no per-object size cap is stated on the pages read; the Developer tier is constrained by environment counts and usage credit instead | source: [1]
- retention: unverified: no identity or audit-log retention period is stated on the first-party pricing or rate-limit pages read | source: [1]
- egress: not applicable: a hosted identity and authorization API; no traffic allowance or per-GB egress price is published | metered: no | source: [1]
- identity: email | detail: The account registration page asks for a work email and a name and offers ChatGPT, GitHub and Google sign-up alternatives; The page states no card requirement. Whether a later step asks for a phone number or an identity document is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 1 member, 0 production environments and 2 development environments on the free Developer tier [1]
  - volume-quota (binding): no included monthly credit and no per-aDAU, per-token or per-check allowance on Developer [1]
  - request-rate: per-project rate-limit buckets with burst and sustained thresholds that depend on subscription tier and environment [2]
  - write-gated: flexible API rate limits, Console SSO and multi-region failover are Enterprise features and are not on Developer [1]
- binding note: The 0 production environments and absent usage credit on Developer bind first: the free tier cannot carry production traffic, and the first paid tier is USD 770/year with per-aDAU overage.
- interface detail: A set of REST APIs for identities, OAuth2 clients, permissions and project configuration, with public endpoints for end-user flows and administrative endpoints behind a Personal Access Token; a unified ory_client SDK targets https://{project_slug}.projects.oryapis.com/. Ory is headless and has no mandatory UI; the Account Experience supplies prebuilt screens. Rate limits are grouped into per-project buckets with burst and sustained thresholds that depend on the tier and environment.
- endpoint: part of interface detail
- tooling: Auto-generated SDKs from OpenAPI specifications, the Ory CLI, the Ory Console, and the prebuilt Ory Account Experience and Elements UI components
- composes with: A headless identity and OAuth 2.0 provider in front of apps on free compute, with bring-your-own login and consent screens; Kratos handles identities, Hydra handles OAuth2 and OIDC, and Keto handles permission checks.
- reliability: Rate limits are applied per project as shared buckets, so endpoints in one bucket compete for the same threshold. The free Developer tier has no production environments and no usage credit.
- notes: Ory also distributes open-source identity components a reader can run on their own infrastructure, listed as self-hosted plans on the same site; that option is separate from the managed Ory Network offer recorded here and is the last resort. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, environment counts and usage prices come from the first-party pricing page, rate-limit structure from the first-party guide, and registration fields from the first-party registration page read through a pinned route. No probe was run and no account was opened; a sign-up would confirm later identity fields.
- evidence:
  - [1] 2026-11-19: the free Developer tier allows 1 member | capture: sha256:00c97c0843a62d82450e1cd2d19909114b34b0dcd79b68c16d893609241b7c8f | quote: Developer: 1
  - [1] 2026-11-19: the free Developer tier allows 2 development environments | capture: sha256:00c97c0843a62d82450e1cd2d19909114b34b0dcd79b68c16d893609241b7c8f | quote: Developer: 2
  - [1] 2026-11-19: the free Developer tier allows 0 production and 0 staging environments and has no price per aDAU | capture: sha256:00c97c0843a62d82450e1cd2d19909114b34b0dcd79b68c16d893609241b7c8f | quote: Developer: 0
  - [1] 2026-11-19: the Production plan charges USD 0.14 per average daily active user per month | capture: sha256:00c97c0843a62d82450e1cd2d19909114b34b0dcd79b68c16d893609241b7c8f | quote: Production: $0.14 / aDAU / month
  - [1] 2026-11-19: the paid plans include a monthly usage credit while Developer has none | capture: sha256:00c97c0843a62d82450e1cd2d19909114b34b0dcd79b68c16d893609241b7c8f | quote: Included Monthly Credit
  - [2] 2026-11-19: rate-limit buckets are shared by the endpoints they contain | capture: sha256:8b89842dda2dcaeb9c802658c599a616ae92430792f3ba09fd35ec8f330f650b | quote: A bucket counter is shared across all endpoints in the same bucket.
  - [2] 2026-11-19: the free Developer tier supports only development environments | capture: sha256:8b89842dda2dcaeb9c802658c599a616ae92430792f3ba09fd35ec8f330f650b | quote: The Developer tier only supports Development environments.
  - [3] 2026-11-19: the hosted API is served on a per-project subdomain | capture: sha256:942f64d88d21e6d2e33cd3ed85da327abe257acb88966f8063aa0fcaeba2c419 | quote: targeting your project's API at `https://{project_slug}.projects.oryapis.com/`
  - [4] 2026-11-19: registration accepts a work email or a social provider | capture: sha256:179c99f9c5931976efba18d1c677831c724d390410138a74bcdbaffa5eb38e03 | quote: Sign up with a social provider or your Work email
  - [4] 2026-11-19: the registration form asks for a work email | capture: sha256:179c99f9c5931976efba18d1c677831c724d390410138a74bcdbaffa5eb38e03 | quote: Work email
  - [4] 2026-11-20: the first-party registration console answered with a browser/cookie gate on 2026-11-20, so the form fields were not visible | capture: sha256:02e8f0cbd8b89feda803d15cd28063c122516c5270ab4d665c189e8636c57b10 | quote: This page was opened in another browser, or cookies are turned off. Ory Console needs cookies to continue.
- sources:
  - [1] https://www.ory.com/pricing
  - [2] https://www.ory.com/docs/guides/rate-limits-project
  - [3] https://www.ory.com/docs/reference/reference-overview
  - [4] https://console.ory.com/registration
