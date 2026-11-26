# Logto

> logto.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/logto/ | JSON https://fshy.ajam.dev/api/v1/entity/logto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Logto

- `dev-services/logto` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted authentication and authorization (OIDC, OAuth 2.1, SAML, passwordless, RBAC) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.037Z (live) | stale on 2026-12-21
- url https://logto.io/pricing
- free tier: Free plan at USD 0/month: up to 50,000 MAU, 50K access tokens, user authentication, one machine-to-machine app, Account APIs for account settings, audit logs and user management, 3 total applications, 3 social connectors and 1 custom domain; no credit card required | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: Only access tokens are counted for billing; ID tokens and refresh tokens are excluded. The Pro plan starts at USD 24/month with unlimited MAU, 50K tokens included and USD 0.08 per 100 extra, then paid add-ons. The pricing page does not state what happens when the Free MAU or token allowance is exceeded.
- per-object cap: unverified: no per-object size cap is stated on the pages read; the Free plan is limited by count of applications and access tokens instead | source: [1]
- retention: Audit logs are retained 3 days on Free and 14 days on Pro; the Enterprise period is set by contract | days: 3 | source: [1]
- egress: not applicable: a hosted authentication API; no traffic allowance or per-GB egress price is published | metered: no | source: [1]
- identity: email | detail: The cloud sign-up page shows a Create your account form with an Email field and a Use Single Sign-On option. The pricing page states no credit card is required for Free. Whether a phone number or an identity document is asked for at a later step is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): up to 50,000 monthly active users on Free [1]
  - volume-quota (binding): 50K access tokens per month, 3 total applications, 1 machine-to-machine app, 3 social connectors and 1 custom domain on Free [1]
  - retention-clamped: audit logs kept 3 days on Free [1]
  - write-gated: RBAC, Organizations, MFA, Enterprise SSO and SAML apps are add-ons and are not included on Free [1]
  - volume-quota (binding): 1 tenant member included on Free, with further members charged on Pro [1]
- binding note: The 50,000-MAU ceiling and the 50K-token allowance bind first; the 3-application cap binds sooner for a multi-app project, and RBAC and MFA need a paid add-on.
- interface detail: A Logto Management API for programmatic control of tenants and resources, plus Experience API and Account API endpoints; a Management API is reachable at openapi.logto.io. The cloud service exposes a Cloud API used to create and subscribe tenants.
- endpoint: https://{tenant}.logto.app/api
- tooling: End-to-end tutorials and SDKs for web, mobile and native frameworks, the Logto Management API, the Account API, and the Logto Cloud API; the Logto Console configures sign-in.
- composes with: An OIDC and OAuth 2.1 identity provider in front of apps on free compute, with password, passwordless, social and enterprise sign-in; user and tenant configuration is reachable through the Management API.
- reliability: The first-party page does not describe enforcement when the Free MAU or token allowance is exceeded, so service behaviour past the quota is unverified. Audit logs are kept only 3 days on Free.
- notes: Logto also distributes open-source software a reader can run on infrastructure of their own, listed under self-hosted plans on the same site; that option is separate from the hosted cloud offer recorded here and is the last resort. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quota, retention and add-on prices come from the first-party pricing page and the signup field from the first-party cloud sign-up page. No probe was run and no account was opened; a sign-up would confirm the post-quota behaviour and later identity fields.
- evidence:
  - [1] 2026-11-19: the Free plan needs no credit card | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: For starting out and trying Logto, no credit card required.
  - [1] 2026-11-19: the Free plan allows up to 50,000 monthly active users | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: - Up to 50,000 MAU
  - [1] 2026-11-19: the Free plan includes 50K access tokens | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: - 50K tokens
  - [1] 2026-11-19: audit logs are kept 3 days on Free and 14 days on Pro | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: How long user authentication actions are stored for issue resolution, security, and compliance needs | 3 days | 14 days | Contact |
  - [1] 2026-11-19: the Free plan allows 3 total applications | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: | Total applicationsThe total amount of applications needed for integration | 3 | Unlimited* | Contact |
  - [1] 2026-11-19: the Free plan allows 3 social connectors | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: Log in through popular social accounts, Google, Github etc | 3 | Unlimited* | Contact |
  - [1] 2026-11-19: the Free plan includes 1 tenant member | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: Number of collaborators who can access and manage the Logto cloud console. | 1 | 1 included
  - [2] 2026-11-19: the cloud sign-up page presents an account creation form | capture: sha256:d343259a40960de656153ef3e6aa76831cfcd00cf52b65c542416978ff0c27b3 | quote: Create your account
  - [2] 2026-11-19: the sign-up form asks for an email address | capture: sha256:d343259a40960de656153ef3e6aa76831cfcd00cf52b65c542416978ff0c27b3 | quote: Email
  - [2] 2026-11-19: the sign-up form offers single sign-on as an alternative | capture: sha256:d343259a40960de656153ef3e6aa76831cfcd00cf52b65c542416978ff0c27b3 | quote: Use Single Sign-On
  - [3] 2026-11-20: the first-party pricing page read 2026-11-20 states no card for the free tier; later sign-up steps remain behind an account | capture: sha256:d27a5d783295a43b4e44bd24a1f97174f3e602c9078459fd8e2e74a9ad185fb1 | quote: For starting out and trying Logto, no credit card required.
- sources:
  - [1] https://logto.io/pricing
  - [2] https://cloud.logto.io/?sign_up=true
  - [3] https://logto.io/pricing/
