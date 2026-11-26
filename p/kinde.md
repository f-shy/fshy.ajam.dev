# Kinde

> kinde.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kinde/ | JSON https://fshy.ajam.dev/api/v1/entity/kinde.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kinde

- `dev-services/kinde` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted authentication, authorization, feature flags and customer billing | tier Free
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T00:32:47.480Z (live) | stale on 2026-12-20
- url https://www.kinde.com/pricing
- free tier: Free plan at USD 0 forever: 10,500 monthly active users, 5 monthly active organizations, 2 custom roles and 10 permissions, 10 feature flags, 5 custom properties, 1 webhook, 2 environments (production and development), email, SMS and social login, MFA, organizations, a custom domain, M2M applications, subscriptions and billing, attack protection, unlimited dashboard seats and unlimited applications; no credit card required | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: An MAU is a user that authenticates in the month; users on paid subscription plans do not count toward the allowance. When the user bills customers through Kinde, MAU is free and Kinde takes 0.7% per transaction. The paid tiers are Pro at USD 25/month, Plus at USD 75/month and Scale at USD 250/month, each with 10,500 MAU included and per-extra-user charges.
- per-object cap: unverified: no per-object size cap is stated on the pages read; an imported OpenAPI file is capped at 20 MB, a limit on a paid-plan feature rather than on the hosted service | source: [1]
- retention: Audit logs are kept 1 day on Free, 7 days on Pro, 14 days on Plus and 30 days on Scale; runtime logs for custom pages and workflows are kept 1 hour on Free | days: 1 | source: [1]
- egress: not applicable: a hosted authentication API; no traffic allowance or per-GB egress price is published | metered: no | source: [1]
- identity: email | detail: The account creation steps in the first-party docs say to enter a first name, last name and email address, then verify the email with a one-time code; the sign-up page offers Google, GitHub and SSO alternatives. The pricing page states no credit card is required for Free. Business details later ask for a business name, a Kinde domain and a region; a business phone number is optional. Whether any identity document is requested is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 10,500 monthly active users included free [1]
  - volume-quota (binding): 5 monthly active organizations, 2 custom roles, 10 permissions, 10 feature flags and 1 webhook on Free [1]
  - volume-quota (binding): 2,000 M2M tokens and 10 SMS included free on Free [1]
  - retention-clamped: audit logs kept 1 day and runtime logs kept 1 hour on Free [1]
  - write-gated: API keys, API scopes and passkeys are not included on Free; these need a paid plan [1]
- binding note: The 10,500-MAU ceiling binds first at scale; Free has no overage rate, and the 5-organization and single-webhook caps bind sooner for a B2B app.
- interface detail: A Kinde Management API and an Account API, documented with an OpenAPI description. The Management API uses a machine-to-machine application and a Bearer token at https://<subdomain>.kinde.com/api/v1/; API keys are offered on paid plans only. Device-flow authentication supports TVs, IoT devices and command-line applications.
- endpoint: part of interface detail
- tooling: SDKs for more than 20 languages, the Kinde Management API, the Account API, the Kinde CLI and the dashboard; M2M applications give programmatic access on Free.
- composes with: An OIDC identity provider in front of apps on free compute, with email, phone and social login, MFA, organizations and a built-in billing module; user and organization data is reachable through the Management API.
- reliability: Audit data is retained only 1 day on Free, so longer forensics need a paid plan. The monthly prices are stated as indicative and can vary with actual usage.
- notes: The live sign-up page at app.kinde.com/register answered a WAF challenge, so the account-creation fields are quoted from the first-party onboarding docs. API keys and API scopes are paid-only, but M2M applications give programmatic access on Free.
- evidence note: Quota, retention and tier prices come from the first-party pricing page, signup fields from the first-party getting-started docs, and API access from the first-party API reference. No probe was run and no account was opened; the live sign-up page returned a WAF challenge, so the form fields are taken from the docs.
- evidence:
  - [1] 2026-11-19: the Free plan includes 10,500 monthly active users and needs no credit card | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: 10,500 monthly active users (MAU)No credit card required
  - [1] 2026-11-19: audit logs are kept 1 day on Free, 7 days on Pro, 14 days on Plus and 30 days on Scale | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: | Audit logs | 1 day | 7 days | 14 days | 30 days |
  - [1] 2026-11-19: Free includes 1 enterprise SSO connection | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: | Enterprise SSO SAML, Entra ID, Okta, etc. | 1 included | 1 included | Unlimited No additional costs | Unlimited No additional costs |
  - [1] 2026-11-19: Free includes 2,000 M2M tokens | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: | M2M tokens | 2,000 included free | 5,000 included free
  - [1] 2026-11-19: dashboard seats are unlimited on every plan, including Free | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: | Team member seats | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-19: the Free plan needs no credit card | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: Yes, our Free plan gives you 10,500 monthly active users at no cost, and does not require a credit card to get started.
  - [1] 2026-11-19: runtime logs are kept 1 hour on Free | capture: sha256:858768c98abacfce32488a1679283b5dd6d9dfcc9f8ef89f935155399db05821 | quote: | Runtime logs for custom pages | 1 hour | 1 day | 3 days | 3 days |
  - [2] 2026-11-19: account creation asks for a first name, last name and email address | capture: sha256:86af916a975227f7834a09dceb14a6c9575174310737c51295ed7001d44d6740 | quote: 2. Enter your First name, Last name, and Email address
  - [2] 2026-11-19: the email is verified with a one-time code | capture: sha256:86af916a975227f7834a09dceb14a6c9575174310737c51295ed7001d44d6740 | quote: 1. A one-time code will be sent to your email
  - [3] 2026-11-19: the Management API base URL is on the account's own Kinde subdomain | capture: sha256:67636f500cb50cb73eb01bca9de6fb8507404f6c7e1e65a3fb6bc06cc598a9b4 | quote: https://your\_kinde\_subdomain.kinde.com
  - [4] 2026-11-19: Kinde publishes a Management API | capture: sha256:b4bdd134bea97888ca1240627e93df89f490651a335c054230f3d7940032123b | quote: Kinde Management API
- sources:
  - [1] https://www.kinde.com/pricing
  - [2] https://docs.kinde.com/get-started/guides/first-things-first
  - [3] https://docs.kinde.com/kinde-apis/management/
  - [4] https://docs.kinde.com/kinde-apis
