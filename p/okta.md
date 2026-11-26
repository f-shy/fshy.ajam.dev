# Okta

> okta.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/okta/ | JSON https://fshy.ajam.dev/api/v1/entity/okta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Okta

- `dev-services/okta` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted workforce and customer identity and access management (SSO, MFA, universal directory, developer APIs) | tier Integrator Free Plan (Okta Workforce Identity developer org)
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.139Z (live) | stale on 2026-12-21
- url https://www.okta.com/pricing/
- free tier: Okta Integrator Free Plan: a non-production developer org for up to 10 monthly active users; the org does not expire, 5 Workflows, API Access Management, adaptive MFA, lifecycle management and universal directory available, community developer-forum support only; a 30-day free trial is offered for the paid Workforce suites | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The Integrator Free Plan org deactivates after 90 consecutive days with no user sign-in unless an app is submitted to the OIN; the pricing FAQ states 180 days of inactivity, while the developer org-defaults document states 90 consecutive days, so the two first-party pages disagree. Paid Workforce Identity suites are per user per month billed annually with a USD 1,500 annual contract minimum (Starter USD 6, Core Essentials USD 14, Essentials USD 17); Customer Identity requires an Enterprise base platform at USD 3,000 per month billed annually.
- per-object cap: unverified: no per-user profile or per-object size cap is stated on the pricing, org-defaults, signup or API pages read
- retention: unverified: no user-data or event retention period for the Integrator Free Plan org is stated on the pages read | source: [1] | note: The org deactivates after inactivity (90 days per the org-defaults document, 180 days per the pricing FAQ) unless an app is submitted to the OIN; deactivation is an availability end, not a stated data-retention window.
- egress: not applicable: an identity and authentication API; no traffic allowance or egress term is published on the pricing page | metered: no | source: [1]
- identity: email | detail: The Integrator Free Plan signup form (developer.okta.com/signup) asks for first name, last name, corporate email, department, country or region, state, role selection and agreement to the Integrator Free Plan Agreement; the org-defaults document states a unique business email is required and no card is shown on the signup form. Whether a later activation step asks for a phone number as an authenticator is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 10 active users in the Integrator Free Plan org [2]
  - volume-quota (binding): 5 Workflows in the Integrator Free Plan org [2]
  - request-rate: 100 authentications per minute default rate limit on the Integrator Free Plan (paid plans start at 600 per minute, extendable with DynamicScale) [1]
  - write-gated: a unique business sign-up email is required; the same sign-up email cannot be used for multiple orgs and some addresses are ineligible by location or security considerations [2]
- limits note: The free org is non-production only; API Access Management is a paid add-on in production. The vocabulary has no kind for an environment-type restriction, stated in text.
- binding note: The 10-active-user ceiling and non-production-only scope bind first; each additional user past the free org needs a paid Workforce suite, which carries a USD 1,500 annual contract minimum.
- interface detail: REST APIs under {yourOktaDomain}/api/v1, HTTPS only, version in the path (for example https://{yourOktaDomain}/api/v1/users). Access with an OAuth 2.0 access token or an API token; scoped OAuth 2.0 tokens are recommended. API Access Management implements OAuth 2.0 and OpenID Connect and is available by default in the Integrator Free Plan org for testing; in production it is a paid add-on. Identity Governance request APIs use version v2.
- endpoint: part of interface detail
- tooling: Okta SDKs, the OIN Wizard and Submission Tester for integrators, Postman collections, or any HTTP client against the Management and Authentication APIs with an OAuth token or API token.
- composes with: Non-production SSO, MFA and user directory for building and testing integrations; submitting an app to the Okta Integration Network keeps the free org active and connects it to the enterprise customer base.
- reliability: A rate-limited request is governed by per-minute buckets; X-Rate-Limit response headers report the ceiling, remaining calls and reset. The free org deactivates after a period of no sign-ins unless an app is submitted to the OIN.
- notes: The two first-party pages disagree on the inactivity window before free-org deactivation: the pricing FAQ says 180 days, the org-defaults document says 90 consecutive days. Both are quoted in the record; the discrepancy is left open rather than resolved by guessing. Okta's on-prem Access Gateway is an Enterprise paid add-on, not the free offer. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Free-org scope, rate limit and paid entry price are quoted from the first-party pricing page; user count, Workflows cap, sign-up email rule and inactivity deactivation from the first-party org-defaults document; signup fields from the first-party signup page and API access from the first-party API reference. No account was opened, so later signup fields are unverified and the rung stays documented.
- evidence:
  - [1] 2026-11-19: the free developer org allows up to 10 active users in non-production and deactivates after 180 days of inactivity | capture: sha256:9ed91670815f1fb0536397856c6d9c0a62d1ae5b0c3ebfb03162dee8f536186a | quote: The [Okta Integrator Free Plan](http://developer.okta.com/signup) allows you to explore our platform capabilities in a non-production environment for up to 10 active users. The trial does not expire; however, orgs deactivate after 180 days of inactivity unless you submit an app to the OIN.
  - [1] 2026-11-19: the free org has a 100 authentications per minute default rate limit versus 600 on paid plans | capture: sha256:9ed91670815f1fb0536397856c6d9c0a62d1ae5b0c3ebfb03162dee8f536186a | quote: Our [Okta Integrator Free Plan](https://developer.okta.com/docs/reference/org-defaults/) has a default rate limit of 100 authentications per minute. Our paid plans start with a default rate limit of 600 authentications per minute
  - [1] 2026-11-19: Okta Customer Identity requires a paid Enterprise base platform at $3,000 per month | capture: sha256:9ed91670815f1fb0536397856c6d9c0a62d1ae5b0c3ebfb03162dee8f536186a | quote: Okta Customer Identity pricing starts with the required Enterprise base product at $3,000 per month, billed annually.
  - [1] 2026-11-19: Workforce suites are billed annually with a $1,500 annual contract minimum | capture: sha256:9ed91670815f1fb0536397856c6d9c0a62d1ae5b0c3ebfb03162dee8f536186a | quote: * All suites are billed annually. $1,500 annual contract minimum required for Okta Workforce Identity.
  - [1] 2026-11-19: the cheapest paid Workforce suite, Starter, is $6 per user per month | capture: sha256:9ed91670815f1fb0536397856c6d9c0a62d1ae5b0c3ebfb03162dee8f536186a | quote: Starter $6 per user/month
  - [2] 2026-11-19: creating the free org needs a name, location and business email | capture: sha256:b46d0c81f7c3f769ef0741f31c987bc86101df6d1cbbe45f0d03469ff35d70bf | quote: Enter your name, location, and a business email address to create a free Integrator Free Plan org.
  - [2] 2026-11-19: the Integrator Free Plan org is limited to 10 active users | capture: sha256:b46d0c81f7c3f769ef0741f31c987bc86101df6d1cbbe45f0d03469ff35d70bf | quote: | Number of active users | 10 |
  - [2] 2026-11-19: the org-defaults document states 90 consecutive days of inactivity before deactivation | capture: sha256:b46d0c81f7c3f769ef0741f31c987bc86101df6d1cbbe45f0d03469ff35d70bf | quote: | Availability | Integrator free plan orgs don't expire. However, they will deactivate if no users sign in for 90 consecutive days, unless you submit an app to the OIN. |
  - [2] 2026-11-19: a unique business sign-up email is required for the free org | capture: sha256:b46d0c81f7c3f769ef0741f31c987bc86101df6d1cbbe45f0d03469ff35d70bf | quote: | Sign-up email | An Integrator free plan organization requires a unique business sign-up email.
  - [3] 2026-11-19: the signup form asks for a corporate email address | capture: sha256:d7c86e881cf27ed2a8ffbc0a5a9be57582ce75691bf7be219a3eda0c1b3c4cd2 | quote: Corporate email\*
  - [4] 2026-11-19: API URLs use the org subdomain or configured custom domain | capture: sha256:3df5b9b62d2e2e00dfa8004aaaa01fefa5c7612e92a8064623ca99520bb5b784 | quote: All URLs listed in the documentation should be preceded with your org's subdomain (tenant) or configured custom domain.
  - [3] 2026-11-20: a first-party developer page was read on 2026-11-20; the sign-up steps past the form remain behind an account | capture: sha256:d7c86e881cf27ed2a8ffbc0a5a9be57582ce75691bf7be219a3eda0c1b3c4cd2 | quote: Join the Okta Integration Network to reach 17,000+ enterprise customers.
- sources:
  - [1] https://www.okta.com/pricing/
  - [2] https://developer.okta.com/docs/reference/org-defaults
  - [3] https://developer.okta.com/signup/
  - [4] https://developer.okta.com/docs/api/
