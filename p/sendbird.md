# Sendbird Chat

> sendbird.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sendbird/ | JSON https://fshy.ajam.dev/api/v1/entity/sendbird.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sendbird Chat (free plan)

- `storage/sendbird-chat` | fails-quota | evidence documented | binding retention-clamped | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:54.247Z (live) | stale on 2026-12-04
- url https://sendbird.com/pricing
- free tier: Free trial plan: up to 1,000 MAUs, unlimited messages per month and 'Unlimited' message storage, but messages are retained for six months; no credit card required | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 6-MONTH RETENTION, stated twice on the pricing page | days: 180 | source: [1] | note: not stated
- egress: No per-GB egress line; file downloads go through Sendbird's API with an application ID and usually a session/access token. | metered: no
- identity: country-phone | detail: unverified: the sign-up form fields were not readable; the pricing page states 'No credit card required' for the free trial
- interface: rest
- limits:
  - retention-clamped (binding): messages are retained for 6 months on the free trial plan; extended retention is an Enterprise feature [1]
  - volume-quota: up to 1,000 MAUs and up to 20 peak concurrent connections [1]
- limits note: 6-MONTH RETENTION, stated twice on the pricing page. 'Unlimited' message storage is therefore a rate allowance, not a capacity. Extended retention is an Enterprise (paid) feature. The exact upsell that tells you retention is the metered axis.
- binding note: 'Unlimited' message storage is clamped by a 6-month retention window, so held bytes are bounded by the write rate over six months
- interface detail: rest
- tooling: sendbird-platform-api + the Chat SDKs (JS/iOS/Android/Flutter). Solid SDK, wrong product shape for a filesystem.
- composes with: Does not chain: unlimited storage is real only inside a 6-month sliding window, so total held bytes are bounded by write rate x 182 days.
- reliability: Free tier enforces automatic message and media truncation after 6 months despite marketing descriptions of unlimited message storage.
- notes: Free trial plan: up to 1,000 MAUs, 6-month message retention. Paid: Starter $349 /month billed annually, or $399/month billed monthly; Pro $499 /month billed annually, or $599/month billed monthly; Enterprise on request.
- evidence note: The 2026-11-03 evidence rows read https://sendbird.com/pricing for the 1,000 MAU free trial limit, six-month message retention, no credit card required and the Starter price. The retention clamp and quota that decide the fails-quota verdict cite vendor captures; the sign-up form fields are unverified.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Pricing page advertises 'Message storage: Unlimited' on the free tier — a number that is immediately contradicted by the retention row on the same page.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Message storage ... Please note messages will be retained for a period of six months. Extended message retention is available on Enterprise plan.'; and separately 'Message retention 6 months' and 'Message storage ... Unlimited'
  - [1] 2026-11-03: the free trial plan is limited to 1,000 monthly active chat users | capture: sha256:ac1532cdb7a453b22ca950ebb734679a1047e4286a971c58c5594bda16405f9f | quote: - MAUs Monthly Active Chat Users Up to 1,000
  - [1] 2026-11-03: messages are retained for six months | capture: sha256:ac1532cdb7a453b22ca950ebb734679a1047e4286a971c58c5594bda16405f9f | quote: Please note messages will be retained for a period of six months. Extended message retention is available on Enterprise plan.
  - [1] 2026-11-03: the free trial plan needs no credit card | capture: sha256:ac1532cdb7a453b22ca950ebb734679a1047e4286a971c58c5594bda16405f9f | quote: - No credit card required
  - [1] 2026-11-03: Starter is $349 per month billed annually or $399 per month billed monthly | capture: sha256:ac1532cdb7a453b22ca950ebb734679a1047e4286a971c58c5594bda16405f9f | quote: Starter 5K Get started with chat $349 /month Billed annually, or $399/month billed monthly
  - [1] 2026-11-03: the retention window is 6 months | capture: sha256:ac1532cdb7a453b22ca950ebb734679a1047e4286a971c58c5594bda16405f9f | quote: - Message retention 6 months
- sources:
  - [1] https://sendbird.com/pricing

## sendbird free plan 'unlimited message storage'

- `storage/sendbird-free-plan-unlimited-message-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://sendbird.com/pricing
- free tier: none reachable: Unlimited is a rate allowance; retention is 6 months and the same pricing page says so twice. Extended retention is the paid upsell. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Unlimited is a rate allowance; retention is 6 months and the same pricing page says so twice. Extended retention is the paid upsell.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Unlimited is a rate allowance; retention is 6 months and the same pricing page says so twice. Extended retention is the paid upsell.
- sources:
  - [1] https://sendbird.com/pricing
