# ConfigCat

> configcat.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/configcat/ | JSON https://fshy.ajam.dev/api/v1/entity/configcat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ConfigCat

- `dev-services/configcat` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted feature flags and remote configuration | tier Forever Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:44.407Z (live) | stale on 2026-12-21
- url https://configcat.com/pricing
- free tier: Forever Free plan, USD 0 a month, no credit card required: 10 feature flags, 2 environments, 2 products, 5 million config JSON downloads a month, 20 GB network traffic a month, 7-day audit log, unlimited seats, service connections, MAUs and feature flag reads | unit: mixed | metered on: request-count | read on: 2026-11-19 | source: [1] | note: The plan is metered by config JSON downloads and network traffic, not by seats or monthly active users. The next plan, Pro, is USD 110 a month with 100 flags, 25 million downloads and 100 GB traffic. Downloads and traffic over the plan are soft limits: ConfigCat keeps serving config and contacts the account.
- per-object cap: unverified: no per-flag value size cap is stated on the pricing or subscription-limit pages read | source: [2]
- retention: 7-day audit log retention on Forever Free; 35 days on Pro and Smart; 2 years on Enterprise and Dedicated | days: 7 | source: [1] | note: This is audit-log retention; no retention period for flag values or identities is stated on the pages read.
- egress: not applicable: a flag service metered by config JSON downloads and network traffic; the Free plan includes 20 GB network traffic a month with soft limits, not a byte-price egress charge | metered: yes | free allowance: 20 GB network traffic a month | source: [1]
- identity: email | detail: The sign-up page offers sign up through Google, GitHub, Microsoft, Bitbucket or Active Directory, and a Company Account through SAML SSO; the pricing page states no card is required and the FAQ names the account email address. A direct email-and-password field was not present in the captured sign-up text; whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 5 million config JSON downloads a month on Forever Free [1]
  - volume-quota (binding): 20 GB network traffic a month on Forever Free [1]
  - per-object-cap: 10 feature flags, 2 environments and 2 products per account on Forever Free [1]
  - retention-clamped: 7-day audit log retention on Forever Free [2]
- limits note: Unlimited seats, service connections, MAUs, contexts and flag reads on every plan. ConfigCat calls downloads and traffic soft limits and continues serving config past them while contacting the account; the flag, environment and product counts are plan limits.
- binding note: The 5 million monthly downloads and 20 GB traffic bind first for a client-side app that refreshes flags on each page view; flag count is capped at 10 but does not grow with traffic.
- interface detail: A Public Management API at https://api.configcat.com based on HTTP REST with JSON, with an OpenAPI v3 description and a Swagger UI; it creates, reads, updates and deletes flags, configs, environments and products. The API is not used to evaluate flags: SDKs or the ConfigCat Proxy download config JSON from the CDN and evaluate flags locally.
- endpoint: part of interface detail
- tooling: ConfigCat SDKs for JavaScript, .NET, Java, Go, Python, Ruby, Angular, React, Node.js, PHP, Elixir, Android, iOS, Flutter, Kotlin Multiplatform, C++, Rust, Unity and Unreal Engine, or any HTTP client against the Management API
- composes with: Serve remotely controlled flags and config to an app on free compute, downloading config JSON from the CDN and evaluating locally to stay under 5 million downloads and 20 GB traffic a month.
- reliability: Downloads and network traffic are soft limits: ConfigCat continues serving config on a temporary spike and contacts the account on sustained overage. Uptime target is 99% on Forever Free; no SLA on the free plan. Support is best effort through Slack or email.
- notes: ConfigCat also publishes an on-premise deployment, which is software the reader runs and is the last resort after the hosted Forever Free plan; the hosted plan is recorded here. Revisit when the pricing page changes the free download quota, traffic allowance or 10-flag cap. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Every value is quoted from the first-party pricing page, subscription-limit page, Public Management API reference and sign-up page. No account was opened; the exact sign-up fields and any post-registration steps are unverified: behind a sign-up. No flag read was probed, so the record stays at documented rung.
- evidence:
  - [1] 2026-11-19: the Forever Free plan needs no card | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: No card required
  - [1] 2026-11-19: Forever Free includes 10 feature flags, 2 environments and 2 products | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: 10 Feature Flags
  - [1] 2026-11-19: Forever Free includes 5 million config JSON downloads a month | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: 5 million / mo
  - [1] 2026-11-19: Forever Free includes 20 GB network traffic a month | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: 20 GB / mo
  - [1] 2026-11-19: MAUs and contexts are unlimited on every plan | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: MAUs & Contexts
  - [1] 2026-11-19: Forever Free audit log retention is 7 days | capture: sha256:d49fa04d7f8e3f435d4100e537b901577f322c9d74d5c774406af1815b1c4ce9 | quote: 7 days
  - [2] 2026-11-19: the subscription-limit table lists 5 million monthly downloads and 20 GB monthly traffic on Free | capture: sha256:b650ef6009c74b30072f697caf8dc4540a8a4348f17eb6f63a7ebe9084f05e1d | quote: Config JSON downloads (million) 5 25 250 1000 6000 25 5 Network traffic (per month) 20GB 100GB 1TB 4TB 24TB 100GB 100GB
  - [2] 2026-11-19: Free audit log retention is 7 days | capture: sha256:b650ef6009c74b30072f697caf8dc4540a8a4348f17eb6f63a7ebe9084f05e1d | quote: Audit log retention (days) 7 35 35 750 750
  - [3] 2026-11-19: the Management API is HTTP REST at api.configcat.com with an OpenAPI v3 description | capture: sha256:c04d1c8f7e92f644528a2253e65d084bf69100cdbe708751a94979bb48619485 | quote: The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON format.
  - [3] 2026-11-19: the Management API is not for flag evaluation; SDKs or the Proxy do that | capture: sha256:c04d1c8f7e92f644528a2253e65d084bf69100cdbe708751a94979bb48619485 | quote: Do not use this API for accessing and evaluating feature flag values. Use the SDKs or the ConfigCat Proxy instead.
  - [4] 2026-11-19: the sign-up page offers SSO through several providers and company SAML | capture: sha256:521afb732d29ef89c4f2e883ab92132aca648ea34bd257d3bc5f257973578d2d | quote: Or sign up using
  - [4] 2026-11-19: a company account can sign up through SAML SSO | capture: sha256:521afb732d29ef89c4f2e883ab92132aca648ea34bd257d3bc5f257973578d2d | quote: Sign up using your own company account (SAML SSO)
  - [4] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:521afb732d29ef89c4f2e883ab92132aca648ea34bd257d3bc5f257973578d2d | quote: Sign up using your own company account (SAML SSO)
- sources:
  - [1] https://configcat.com/pricing
  - [2] https://configcat.com/docs/subscription-plan-limits/
  - [3] https://configcat.com/docs/api/reference/configcat-public-management-api/
  - [4] https://app.configcat.com/signup
