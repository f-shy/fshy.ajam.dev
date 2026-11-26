# ZITADEL Cloud

> zitadel.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zitadel/ | JSON https://fshy.ajam.dev/api/v1/entity/zitadel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZITADEL Cloud

- `dev-services/zitadel-cloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted identity and access management: OIDC and OAuth 2.0 login, hosted login page, organizations, service users (managed ZITADEL Cloud) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:46.080Z (live) | stale on 2026-12-21
- url https://zitadel.com/pricing
- free tier: Free: USD 0 per month, all security features, data residency in the EU, US, Switzerland and Australia, unlimited stored users, unlimited organizations, 100 daily active users, service users and agents, 3 identity providers and custom workflows | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The counted unit is the daily active user (DAU), not the monthly active user. A unique user counts once per day for a login, a token refresh or a machine-to-machine service-user authentication; the monthly total is the sum of each day's count. The unit vocabulary has no term for daily active users; users is the nearest term and the true unit is named here. The pricing page does not state what happens when a Free instance exceeds 100 DAU.
- per-object cap: unverified: no per-object or user-profile size cap is stated on the pages read | source: [2]
- retention: On the Free plan the Audit Trail History is kept 1 day and logs are kept 30 minutes (2 weeks and 1 day respectively on Pro) | days: 1 | source: [2] | note: The retention figures are for audit trail events and access and runtime logs, not for stored user records; no expiry for user records is stated on the pages read.
- egress: not applicable: an authentication and identity API; no traffic allowance or egress term is published | metered: no | source: [1]
- identity: email | detail: The register page states 'No credit card needed' and 'No commitment'. The quickstart says a new account verifies its email and sets up a Portal Team; an instance then needs a name, a region and an Instance Administrator, and the quickstart recommends passkeys for the account. Whether a phone number is asked for at signup is unverified: behind a sign-up.
- interface: rest, browser
- limits:
  - volume-quota (binding): 100 daily active users on Free (each unique user counted once per day) [1]
  - request-rate: 5,000 Management API requests included on Free [2]
  - retention-clamped: Audit Trail History 1 day and logs 30 minutes on Free [2]
  - volume-quota (binding): 3 active external identity providers, 1 instance and 1 administrator on Free [2]
- limits note: The dashboard-seat and identity-provider counts have no dedicated vocabulary kind and are recorded as volume-quota rows.
- binding note: The 100 daily active users per day is the smallest ceiling: a user who signs in on twenty days spends twenty units, so a small returning user base passes it before the 5,000 Management API requests are used.
- interface detail: A Management API with 5,000 requests included on Free and 500,000 on Pro, served on the instance domain; applications integrate over OIDC with a PKCE login on the ZITADEL-hosted login page, and the docs publish an API reference. The login page is hosted, so a browser reaching it is required for the interactive sign-in flow.
- endpoint: https://{instance}.zitadel.cloud
- tooling: An OIDC client or OAuth 2.0 library against the hosted login page, the Management API for administration, and ZITADEL SDKs for the chosen framework.
- composes with: An OIDC identity provider in front of an app on free hosting; a generated instance domain is provided, and the Pro plan adds a custom domain. A separate offer of the same software that the reader installs and runs exists as ZITADEL Enterprise Self-Hosted, listed here last and not counted as a hosted tier.
- reliability: The pricing page gives no uptime guarantee to the Free plan; guarantees start at Pro (99.5 percent, add-on 99.95 percent). Login-policy misconfiguration can lock out an instance, and the quickstart advises a backup personal access token and a second administrator.
- notes: The DAU meter makes the 100-unit Free allowance much smaller than a 100-MAU allowance: a user who signs in on twenty days spends twenty units. Pro is USD 100 a month with 25,000 summed DAU included and a custom domain. A self-hosted Enterprise option exists but is not counted as a hosted offer. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Every limit is quoted from first-party pricing, pricing-detail, help-centre and quickstart pages. No account was opened and no probe was run; the Management API is on a per-instance domain. A login and an API call on a Free instance would move the token request toward measured.
- evidence:
  - [1] 2026-11-19: the Free plan is USD 0 a month and includes unlimited stored users, unlimited organizations and 100 daily active users | capture: sha256:75a107da5af05ab295e0e1894de62ea1061d867b42daab3be223c5e63a21f394 | quote: US$0/Month All security features Data Residency: EU, US, Switzerland, Australia Store unlimited Users Unlimited Organizations 100 Daily Active Users
  - [1] 2026-11-19: the Free plan also includes service users, 3 identity providers and custom workflows | capture: sha256:75a107da5af05ab295e0e1894de62ea1061d867b42daab3be223c5e63a21f394 | quote: Service Users / Agents 3 identity providers Custom workflows
  - [2] 2026-11-19: Free has 100 DAU, 3 external identity providers, 5,000 Management API requests and 1 administrator | capture: sha256:1d32d9b68dae20d4b17c2cd921dda6d79daa225fdbe1ff878c977470ff8e4435 | quote: | Daily Active Users | 100 | 25'000 included | | | | Active External Identity Providers | 3 | 3 included | Volume Price | Volume Price | | Management API requests | 5,000 | 500'000 included | | | | Administrators | 1 | 3 included | | |
  - [2] 2026-11-19: Free keeps audit trail history 1 day and logs 30 minutes | capture: sha256:1d32d9b68dae20d4b17c2cd921dda6d79daa225fdbe1ff878c977470ff8e4435 | quote: | Audit Trail History | 1 day | 2 weeks | | | | Logs | 30 min | 1 day | | |
  - [2] 2026-11-19: Free has 1 instance | capture: sha256:1d32d9b68dae20d4b17c2cd921dda6d79daa225fdbe1ff878c977470ff8e4435 | quote: | Instances | 1 | | | |
  - [3] 2026-11-19: a DAU is a unique user counted once per day for a login, token refresh or service-user authentication | capture: sha256:0ec745d0e288bb51f5c1a2dd8ba071a0e208a3a75067e757d0c1992a9f5127c3 | quote: A user is considered "active" on a specific day if they perform an authentication event. Specifically: - Logging in (using a local account or an external provider like Google or Microsoft). - Refreshing a token (when an application keeps a user logged in). - Service User authentication (Machine-to-Machine API access).
  - [3] 2026-11-19: each unique user counts once per day regardless of the number of logins or refreshes | capture: sha256:0ec745d0e288bb51f5c1a2dd8ba071a0e208a3a75067e757d0c1992a9f5127c3 | quote: Key Rule: Each unique user is only counted once per day, no matter how many times they log in or refresh tokens within that 24-hour period.
  - [3] 2026-11-19: the monthly bill is the sum of each day's DAU count, so a user signing in on twenty days is twenty units | capture: sha256:0ec745d0e288bb51f5c1a2dd8ba071a0e208a3a75067e757d0c1992a9f5127c3 | quote: To calculate your monthly total, we sum the DAU count of every single day in that month.
  - [4] 2026-11-19: the register page states no credit card and no commitment are needed | capture: sha256:c2a6414c20750bf53ca8e56d8b0bfd7e1647a58805286b53ed024a425d405e72 | quote: No credit card needed No commitment
  - [5] 2026-11-19: signup verifies the email and sets up a Portal Team | capture: sha256:2a7d525e9f3a05ddc5881b5f0ae53fc917da220dc5e5bba6a0ff1cf0232d8c55 | quote: 2. Onboarding: Follow the prompts to verify your email and set up your Portal Team.
  - [5] 2026-11-19: the quickstart recommends passkeys for the account | capture: sha256:2a7d525e9f3a05ddc5881b5f0ae53fc917da220dc5e5bba6a0ff1cf0232d8c55 | quote: - Tip: We recommend using Passkeys for a secure, passwordless login experience.
  - [5] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:2a7d525e9f3a05ddc5881b5f0ae53fc917da220dc5e5bba6a0ff1cf0232d8c55 | quote: 1. Sign Up: Go to [zitadel.com](https://zitadel.com/) and select Sign Up.
- sources:
  - [1] https://zitadel.com/pricing
  - [2] https://zitadel.com/pricing/detail
  - [3] https://help.zitadel.com/how-is-daily-active-users-calculated
  - [4] https://zitadel.com/register
  - [5] https://zitadel.com/docs/guides/start/quickstart
