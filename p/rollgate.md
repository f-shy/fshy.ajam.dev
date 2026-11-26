# Rollgate

> rollgate.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rollgate/ | JSON https://fshy.ajam.dev/api/v1/entity/rollgate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rollgate

- `dev-services/rollgate` | qualifies-with-caveat | evidence documented | binding volume-quota | category EU-hosted feature flags with local SDK evaluation | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:44:36.826Z (live) | stale on 2026-12-20
- url https://rollgate.io/pricing
- free tier: Free plan, EUR 0 a month, free forever, no card required: 500K requests a month, unlimited flags, 3 environments, 3 projects, 3 seats, all 12 SDKs, Discord support | unit: requests | metered on: request-count | read on: 2026-11-19 | source: [1] | note: Pricing is per SDK request, not per seat and not per monthly active user. The next plan, Starter, is EUR 45 a month billed monthly (EUR 39 annually) for 1M requests and 5 seats. The pricing page does not state what happens past 500K requests; the REST API docs say a request over the plan answers 429.
- per-object cap: unverified: no per-flag value size cap is stated on the pages read
- retention: unverified: no flag-data retention period is stated on the pricing or API pages read; the pricing comparison lists a 3-day audit log retention on Free | source: [2] | note: A 3-day audit log retention appears in the vendor's pricing-comparison blog table; the main pricing page read here does not state a retention period.
- egress: not applicable: a flag service metered by SDK request count; no traffic allowance or byte price is published | metered: no | source: [1]
- identity: email | detail: The quickstart says to sign up for a free Rollgate account with no credit card required; the architecture page lists user authentication by email and OAuth, and dashboard sign-in by Google and GitHub. The register page capture shows only a Terms and Privacy acceptance line, so the exact form fields are unverified: behind a sign-up; no card, phone or ID is stated at sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 500K SDK requests a month on Free [1]
  - per-object-cap: 3 environments, 3 projects and 3 seats on Free [1]
  - request-rate: the REST API answers 429 Too Many Requests when plan limits are exceeded [3]
  - per-object-cap: 1 SSE connection on the Free plan [3]
- limits note: Unlimited flags on every plan. The API docs list 500K requests, 1 SSE connection and 3 projects on Free; a request over the plan answers 429. The docs list 14-day free trials on paid plans.
- binding note: The 500K monthly request cap binds first for an app that polls flags frequently; a single SSE connection also caps concurrent streaming sessions on the Free plan.
- interface detail: A REST API manages flags, projects and users; SDKs for React, Vue, Angular, Svelte, browser, Node.js, Go, Python, Java, .NET, React Native and Flutter stream a resolved rules bundle over SSE and evaluate flags locally in-process, with no network hop per evaluation.
- endpoint: https://api.rollgate.io
- tooling: The 12 official SDKs, the REST API or any HTTP client; the SDK streams flag configuration and evaluates locally.
- composes with: Serve flags to an app from a worker that uses a Rollgate SDK, keeping the SDK request count under 500K a month; SSE streaming and caching lower the effective request volume.
- reliability: The API returns 429 when a plan limit is exceeded. A 99.9% uptime SLA appears on the Growth plan only. Self-hosting is not yet available and is on the roadmap.
- notes: Self-hosting is on the roadmap and not available, so this is a hosted offer. Revisit when the pricing page states the over-limit behaviour or changes the 500K request allowance.
- evidence note: Every value is quoted from first-party pricing, REST API docs, quickstart, architecture and homepage pages. No account was opened; the exact register fields are unverified: behind a sign-up. No live flag evaluation was probed, so the record stays at documented rung.
- evidence:
  - [1] 2026-11-19: the Free plan is EUR 0 a month, free forever | capture: sha256:29e8b8182793ec6185ea9ccb2083beb1ac736569d902b4d4956577f6afdc265f | quote: Free forever
  - [1] 2026-11-19: the Free plan includes 500K requests a month | capture: sha256:29e8b8182793ec6185ea9ccb2083beb1ac736569d902b4d4956577f6afdc265f | quote: 500K requests/mo
  - [1] 2026-11-19: the Free plan includes unlimited flags, 3 environments, 3 projects and 3 seats | capture: sha256:29e8b8182793ec6185ea9ccb2083beb1ac736569d902b4d4956577f6afdc265f | quote: - 500K requests/mo - Unlimited flags - 3 environments · 3 projects - 3 seats - All 12 SDKs - Discord support
  - [1] 2026-11-19: pricing is per request, not per user | capture: sha256:29e8b8182793ec6185ea9ccb2083beb1ac736569d902b4d4956577f6afdc265f | quote: Flat pricing. Pay per request, not per user.
  - [3] 2026-11-19: the API lists 500K requests, 1 SSE connection and 3 projects on Free and all plans include unlimited flags | capture: sha256:73bb978b4a931a34aa7823d791ef2ecb7098a3503ec772187073143a6ff99ab4 | quote: | Free | 500K | 1 | 3 |
  - [3] 2026-11-19: a request over the plan answers 429 and all plans include unlimited flags | capture: sha256:73bb978b4a931a34aa7823d791ef2ecb7098a3503ec772187073143a6ff99ab4 | quote: When limits are exceeded, the API returns `429 Too Many Requests`. All plans include unlimited flags.
  - [4] 2026-11-19: the free plan starts with no card and data is hosted in Germany | capture: sha256:5373bf58cac97a314ac392a45e409f5850d4a3201f5e3bd5590c61145a15229d | quote: Start free · no card required
  - [4] 2026-11-19: self-hosting is not yet available; the service is EU-hosted cloud | capture: sha256:5373bf58cac97a314ac392a45e409f5850d4a3201f5e3bd5590c61145a15229d | quote: Not yet. Self-hosting is on the roadmap. Join the waitlist and we'll tell you the moment it ships. Today, Rollgate runs as EU-hosted cloud.
  - [5] 2026-11-19: a free account needs no credit card | capture: sha256:463028f9e1e25525ce122f0bc56cfc674a1aa4971aaece19bf2f6679df64c31b | quote: Sign up for a free Rollgate account. No credit card required.
  - [6] 2026-11-19: user authentication uses email and OAuth and the dashboard supports Google and GitHub sign-in | capture: sha256:fd2c00313142b46244d23694585dcfad5ef59fd68d0c485bce957ece2f3ac675 | quote: • User authentication (email, OAuth)
- sources:
  - [1] https://rollgate.io/pricing
  - [2] https://rollgate.io/blog/feature-flags-pricing-comparison
  - [3] https://rollgate.io/docs/api
  - [4] https://rollgate.io/
  - [5] https://rollgate.io/docs/quickstart
  - [6] https://rollgate.io/docs/architecture
