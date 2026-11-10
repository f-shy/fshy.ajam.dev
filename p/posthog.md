# PostHog

> posthog.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/posthog/ | JSON https://fshy.ajam.dev/api/v1/entity/posthog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PostHog

- `dev-services/posthog` | qualifies-with-caveat | evidence documented | binding volume-quota | category product analytics, session replay, feature flags and error tracking | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-02T00:37:34.248Z (live) | stale on 2026-12-03
- url https://posthog.com/pricing
- free tier: Free every month, reset monthly, with or without a card on file: 1M analytics events, 5K session recordings, 1M feature flag requests, 100K exceptions, 1500 survey responses; 1 project, 1-year data retention, unlimited team members; no credit card required | unit: mixed | metered on: request-count | read on: 2026-10-30 | source: [1] | note: Each product has its own monthly count (events, recordings, flag requests, exceptions, survey responses), so no single unit of the vocabulary fits; analytics is counted in events, and one batch request can carry many events, so request-count is only the nearest metered_on term. Usage across projects shares one free allowance. On the free plan, events past the allowance are permanently dropped and feature flags return a quota-limited response, so usage stops rather than bills.
- per-object cap: Events over 1 megabyte after processing are discarded; a distinct_id is limited to 200 characters | source: [2] | note: A /batch request body must be less than 20MB, with no limit on the number of events in it.
- retention: Events and metadata: 1 year on a free plan (7 years on paid). Session recordings: 1 month on the free plan. Logs: 14 days by default. | source: [1] | note: After 1 year data may move to cold storage, and data past its retention period may be deleted.
- egress: unverified: no egress term on the pages read; data is read back through the private API, rate limited per personal API key (240/minute and 1200/hour on analytics endpoints) | metered: no | source: [3]
- identity: email | detail: An account is tied to an e-mail address: the wizard creates one from an e-mail address and a region. The pricing and sign-up pages state no credit card is required, and the allowance is the same with or without a card on file. Whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 1M analytics events per month; further events are permanently dropped on the free plan [1]
  - volume-quota (binding): 5K session recordings, 1M feature flag requests, 100K exceptions and 1500 survey responses per month; 1 project [1]
  - request-rate: 240 per minute and 1200 per hour on analytics endpoints, per personal API key [3]
  - retention-clamped: events 1 year, session recordings 1 month on the free plan [1]
- binding note: Events past 1M in a month are permanently dropped on the free plan, so the monthly event count is the first ceiling for an app with traffic; the API rate applies only to reads with a personal key.
- interface detail: Public POST-only endpoints (event capture at /i/v0/e, flag evaluation at /flags) take a project token and are not rate limited; private GET, POST, PATCH and DELETE endpoints take a personal API key or OAuth. The US app host us.posthog.com answered 401 to /api/projects/ without a key. The data region (US or EU) is fixed when the account is made.
- endpoint: https://us.posthog.com/api/
- tooling: PostHog SDKs, the @posthog/wizard command (run with npx), which can create the account and install the SDK, and any HTTP client with a personal API key for the private API
- composes with: Event capture and feature flags for the front end of a free-hosted app, up to 1M events a month, with error tracking in the same project; over the allowance events are dropped, not billed.
- reliability: Events above the free allowance are permanently dropped and feature flags return a quota-limited response.
- notes: The free plan stops at its limits instead of billing, so an app sending more than 1M events a month loses the excess. Moving to pay-as-you-go needs a card and raises the project count to 6 and event retention to 7 years.
- evidence note: Every limit is quoted from a first-party page, and the private API host answered 401 without a key. No account was opened; an authenticated query from a free project would move it to measured.
- evidence:
  - [1] 2026-10-30: the free allowance resets monthly and does not depend on a card | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Resets monthly. Same allowance whether or not you have a card on file.
  - [1] 2026-10-30: the free allowance includes 1M analytics events, 5K session replays and 1M feature flag requests | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: PostHog is free to use and each product has a generous free monthly allowance (1M events for analytics, 5K session replays, 1M feature flag requests, and more).
  - [1] 2026-10-30: the free allowance includes 100K exceptions | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: 100K exceptions
  - [1] 2026-10-30: the free allowance includes 1500 survey responses | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: 1500 responses
  - [1] 2026-10-30: the free plan has 1 project and 1-year data retention | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: 1 project, 1-year data retention
  - [1] 2026-10-30: the free plan has unlimited team members | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Unlimited team members
  - [1] 2026-10-30: events are kept 1 year on a free plan and 7 years on paid | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Events and metadata are guaranteed to be retained for 7 years on any paid plan and 1 year on a free plan.
  - [1] 2026-10-30: session recordings are kept 1 month on the free plan | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Recordings on the free plan are retained for 1 month.
  - [1] 2026-10-30: logs are kept 14 days by default | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Logs are retained for 14 days by default.
  - [1] 2026-10-30: on the free plan, events past the allowance are dropped and flags return a quota-limited response | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: On the free plan, any additional events are permanently dropped and feature flags will return a default quota limited response.
  - [1] 2026-10-30: projects share one free allowance | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Adding projects doesn't add extra free usage.
  - [1] 2026-10-30: the paid plan raises the project count from 1 to 6 | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: 6 projects – up from 1
  - [1] 2026-10-30: higher limits need a card | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: Just add a card whenever you need higher limits.
  - [1] 2026-10-30: data past its retention period may be deleted, and after 1 year may move to cold storage | capture: sha256:a242294a095a661ab343024d634718f5f890b22f7d1f519db728044e33ee6c27 | quote: After 1 year, data may be moved into cold storage so queries may run more slowly.
  - [4] 2026-10-30: the sign-up page states no credit card is required | capture: sha256:a2c86e41315e3d53a68f93894a31fa941496f30501147ca521898904ddca5c4d | quote: Every product has a monthly free tier, and no credit card is required.
  - [5] 2026-10-30: an account is created from an e-mail address and a region | capture: sha256:d7d65ccec35d58a68bc4e40074b81d6d8fcc3e0ef4048ac18e5ea9ea8c8912c6 | quote: The wizard creates the account tied to `you@example.com`, provisions a project in the region you pick, drops the project credentials into your codebase, and installs the SDK.
  - [3] 2026-10-30: private endpoints are rate limited and public POST-only endpoints are not | capture: sha256:47400233a421ece7a0ed3d8240fc955f7ebabcbe4a28236853b7ca3f71fb1532 | quote: Private `GET`, `POST`, `PATCH`, `DELETE` endpoints are rate limited. Public POST-only endpoints are not rate limited.
  - [3] 2026-10-30: analytics endpoints allow 240 per minute and 1200 per hour | capture: sha256:47400233a421ece7a0ed3d8240fc955f7ebabcbe4a28236853b7ca3f71fb1532 | quote: For all analytics endpoints (such as calculating insights, retrieving persons, or retrieving session recordings), the rate limits are `240/minute` and `1200/hour`.
  - probe:https://us.posthog.com/api/projects/ 2026-10-31: the private API host answers 401 without a key | capture: sha256:ed004fca5138f23ad5f53ca577bd7b1017c465ddb8d19c53ba73b76726137d1f | quote: "status": 401
  - [2] 2026-11-01: PostHog discards events larger than 1 megabyte after processing | capture: sha256:0d0c6f1d9d39da94ae9110f45febb666a957ce93c8ff10f90d66e34bfdd8f251 | quote: PostHog discards events exceeding 1 megabyte in size after processing.
  - [2] 2026-11-01: a distinct_id longer than 200 characters is shortened to its first 200 characters | capture: sha256:0d0c6f1d9d39da94ae9110f45febb666a957ce93c8ff10f90d66e34bfdd8f251 | quote: PostHog shortens any `distinct_id` longer than 200 characters to its first 200 characters and ingests the event under the shortened ID.
  - [6] 2026-11-01: a /batch request body must be under 20MB with no limit on the number of events in it | capture: sha256:b7ea16b34e241b99f1a12b636c60d53518f453ee28f869ef8e9d868e914b6bfa | quote: There is no limit on the number of events you can send in a batch, but the entire request body must be less than 20MB by default.
  - [6] 2026-11-01: one /batch request carries multiple events, so an event count is not a request count | capture: sha256:b7ea16b34e241b99f1a12b636c60d53518f453ee28f869ef8e9d868e914b6bfa | quote: You can capture multiple events in one request with the `/batch` API route.
  - [6] 2026-11-01: a distinct_id is limited to 200 characters | capture: sha256:b7ea16b34e241b99f1a12b636c60d53518f453ee28f869ef8e9d868e914b6bfa | quote: `distinct_id` is limited to 200 characters.
- sources:
  - [1] https://posthog.com/pricing
  - [2] https://posthog.com/docs/data/ingestion-warnings
  - [3] https://posthog.com/docs/api
  - [4] https://us.posthog.com/signup
  - [5] https://posthog.com/docs/ai-engineering/wizard-signup
  - [6] https://posthog.com/docs/api/capture
