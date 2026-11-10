# Ipregistry

> ipregistry.co | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipregistry/ | JSON https://fshy.ajam.dev/api/v1/entity/ipregistry.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ipregistry

- `data-apis/ipregistry` | trial-only | evidence documented | binding volume-quota | category IP geolocation API | tier Free start
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.114Z (live) | stale on 2026-12-04
- url https://ipregistry.co/pricing
- free tier: 20,000 credits once on sign-up, no credit card, no time limit; then plans from USD 29 a month for 100,000 credits | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an account with no credit card: the first step of the sign-up form asks for a work email, a first name and a last name and has a Next button, or signs in with GitHub or Google; what follows the Next button is unverified: behind a sign-up
- interface: rest
- limits:
  - volume-quota (binding): 20,000 credits once, not renewed [1]
- tooling: any HTTP client
- composes with: a one-time 20,000-credit allowance for testing; no recurring free quota. Bulk path: paid dataset subscriptions
- reliability: the free credits are a one-time grant; after them every lookup is paid
- notes: Free requests: 20,000 credits once. Rate limit: not stated. Bulk path: paid datasets only.
- evidence note: unverified: behind a sign-up: what follows the Next button of the sign-up form; the pricing page was quoted on 2026-10-30, and the first step of the form was read from a rendered copy on 2026-11-02
- extras:
  - bulk_path: paid datasets only
  - free_requests: 20,000 credits once
- evidence:
  - [1] 2026-10-30: 20,000 free credits to start | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: Start with 20,000 free credits, then pay only for what you use
  - [1] 2026-10-30: the credits come once, on sign-up | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: Every new account gets 20,000 credits on sign-up.
  - [1] 2026-10-30: no card and no time limit | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: No credit card, no time limit. Build, test, and see real results before you spend a cent.
  - [1] 2026-10-30: the first plan is 100,000 credits a month | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: 100,000 credits / mo
  - [1] 2026-10-30: the first plan is USD 29 a month (USD 24 yearly) | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: $29 $24 / month
  - [2] 2026-11-02: a rendered copy of the sign-up page shows a first step with work email, first name and last name, a Next button, and sign-up with GitHub or Google | capture: sha256:bce31f97bbaab96543dcd56c82018e59e81719ae00cc7fa2219edb0bb4a81c2e | quote: Work email First name Last name Next
  - [2] 2026-11-02: a rendered copy of the sign-up page shows the first step of the form and a Next button | capture: sha256:bce31f97bbaab96543dcd56c82018e59e81719ae00cc7fa2219edb0bb4a81c2e | quote: Work email First name Last name Next
  - [1] 2026-11-02: every new account gets 20,000 credits on sign-up, with no credit card and no time limit, and the first plan is 100,000 credits a month for USD 29 | capture: sha256:dddae43abda113aff5a3b4b03a9de2a57af1c55327de052ad353eccddb023d0b | quote: Every new account gets 20,000 credits on sign-up.
- sources:
  - [1] https://ipregistry.co/pricing
  - [2] https://dashboard.ipregistry.co/signup
