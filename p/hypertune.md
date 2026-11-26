# Hypertune

> hypertune.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hypertune/ | JSON https://fshy.ajam.dev/api/v1/entity/hypertune.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hypertune (feature flags)

- `dev-services/hypertune` | dead | evidence documented | binding volume-quota | category feature flags and experimentation, formerly hosted | tier Free
- identity a placeholder: card and phone unknown | verified 2026-11-20T04:15:44.827Z (live) | stale on 2026-12-21
- url https://www.hypertune.com/pricing
- free tier: The former Free plan, USD 0 a month, was for testing and evaluation, or small-scale deployments: 1m CDN requests, 1m analytics events, up to 3 team members, unlimited CDN bandwidth, service connections, MAUs/MTUs, environments, projects, feature flags and experiments; the offer is no longer reachable on the original domain | unit: mixed | metered on: request-count | read on: 2026-11-19 | source: [1] | note: The figures are read from a Wayback capture of the original first-party pricing page dated 2026-06-13, not from the live domain. The live hypertune.com/pricing now serves an unrelated PC game optimizer, hypertune.ai is a domain-parking page, and docs.hypertune.com returns a server-side failure.
- per-object cap: unverified: no per-flag value size cap is stated on the captured pages | source: [1]
- retention: unverified: no retention period for flags, analytics events or audit logs is stated on the captured pages | source: [1]
- egress: not applicable: a flag service formerly metered by CDN requests and analytics events; no traffic allowance or byte price is published on the captured pages | metered: no | source: [1]
- identity: email | detail: unverified: a third party reported that the service stopped taking new sign-ups, but no current first-party sign-up page is reachable; the archived pricing page showed Google SSO on the Free plan. No sign-up form was available to read, so the exact registration fields cannot be stated.
- interface: rest
- limits:
  - volume-quota (binding): 1m CDN requests a month on the former Free plan [1]
  - volume-quota (binding): 1m analytics events a month on the former Free plan [1]
  - per-object-cap: up to 3 team members on the former Free plan [1]
- limits note: Unlimited MAUs/MTUs, CDN bandwidth, service connections, environments, projects, feature flags and experiments were listed on the former Free plan. The original domain now serves an unrelated product.
- binding note: The 1m monthly CDN request and 1m analytics event quotas were the first thresholds on the former Free plan; the offer is no longer reachable.
- interface detail: The former product offered a GraphQL edge API and type-safe, Rust-powered SDKs for major languages. The live docs domain no longer serves the product documentation, so the interface could not be re-read on a first-party page.
- tooling: Former type-safe, Rust-powered SDKs for major languages; no longer reachable on the original domain.
- composes with: No current hosted offer: the original feature-flag domain now serves an unrelated product and the docs domain is unreachable, so there is no live hosted lane to chain.
- reliability: The original feature-flag pricing page no longer serves the product: hypertune.com/pricing now serves an unrelated PC game optimizer, hypertune.ai is a domain-parking page stating the registration expired, and docs.hypertune.com returned a 530 status. The last accessible first-party pricing text is a Wayback capture dated 2026-06-13.
- notes: The former Free plan is documented, but the original domain now serves an unrelated product and the docs domain is unreachable, so no hosted self-serve tier is currently available. A first-party shutdown date was not published, so none is stated here. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: The former plan figures are quoted from a Wayback capture of the original first-party pricing page, and the current state from captures of the live hypertune.com and hypertune.ai domains. The docs domain could not be read. The service is recorded as dead on first-party evidence that the original pages no longer serve the product.
- evidence:
  - [1] 2026-11-19: the live hypertune.com/pricing now serves an unrelated PC game optimizer, not the feature-flag product | capture: sha256:05cd8e1a93125bda41c9e4263214841d20ee843b0e8c63141c0464eb8ecad49f | quote: Boost your gaming
  - [2] 2026-11-19: the hypertune.ai domain registration expired and is parked | capture: sha256:98abb0e9b8f8c493d51f7b7a35fabf966323f0007c53ba119a48ba19ad204523 | quote: Domain registration has expired.
  - [3] 2026-11-19: the former Free plan was USD 0 a month for testing and evaluation | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: $0 / month
  - [3] 2026-11-19: the former Free plan included 1m CDN requests | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: 1m CDN requests
  - [3] 2026-11-19: the former Free plan included 1m analytics events | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: 1m analytics events
  - [3] 2026-11-19: the former Free plan allowed up to 3 team members | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: Up to 3 team members
  - [3] 2026-11-19: the former Free plan had unlimited MAUs and MTUs | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: Unlimited MAUs / MTUs
  - [3] 2026-11-19: the former Free plan offered Google SSO | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: SSO via Google
  - [3] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:7d24c6ac1c792c36de70d5c053b783590621a3af7284d2989791d6c232e47be9 | quote: Preview flag values, including experiment assignments, for any context
- sources:
  - [1] https://www.hypertune.com/pricing
  - [2] https://www.hypertune.ai/
  - [3] https://web.archive.org/web/20260613091436/https://www.hypertune.com/pricing?provider=wayback
