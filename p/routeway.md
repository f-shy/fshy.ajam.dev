# Routeway

> routeway.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/routeway/ | JSON https://fshy.ajam.dev/api/v1/entity/routeway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Routeway

- `inference/routeway` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, free models
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:39:04.778Z (live) | stale on 2026-12-05
- url https://docs.routeway.ai/getting-started/rate-limits
- free tier: models whose id ends in :free cost $0.00; limits are 5 requests per minute and 200 requests per day on the rate-limits page, and 20 requests per minute and 200 requests per day on the FAQ page, so the two pages disagree on the per-minute figure | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the FAQ calls the limits hard caps with no way to increase them; paid models need a positive account balance
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the vendor lists 'a valid email address and payment method' among account-creation requirements; whether the dashboard enforces a payment method before issuing a key for :free models was not observed
- interface: rest
- limits:
  - request-rate (binding): rate-limits page: 5 requests per minute and 200 requests per day on :free models; FAQ page: 20 requests per minute and 200 requests per day; the daily figure agrees and resets at 00:00 UTC [1]
- binding note: 5 or 20 requests per minute, against a 200 requests per day cap that binds either way
- endpoint: https://api.routeway.ai/v1/chat/completions
- tooling: any OpenAI-compatible client at https://api.routeway.ai/v1; Anthropic-style /v1/messages for models that expose it
- composes with: a free :free model set behind one key, usable as a low-priority overflow lane next to the other gateways
- reliability: free models run in a lower-priority routing queue with more 502 upstream errors and can be removed at any time
- evidence note: limits and the queue statement are quoted from the vendor's docs; the two docs pages disagree on the per-minute figure and the sign-up enforcement was not observed.
- evidence:
  - [1] 2026-10-28: rate-limits page gives 5 requests per minute for :free models | capture: sha256:423784140d2efdc2fea45de474d3fba0a63e8b6152b5580ebe0ded85c7aa2f9c | quote: * 5 Requests Per Minute (RPM)
  - [1] 2026-10-28: rate-limits page gives 200 requests per day for :free models | capture: sha256:423784140d2efdc2fea45de474d3fba0a63e8b6152b5580ebe0ded85c7aa2f9c | quote: * 200 Requests Per Day (RPD)
  - [2] 2026-10-28: FAQ gives 20 requests per minute and 200 per day for :free models | capture: sha256:b25f44b54d9e28fdef6c51854a1b92ba3421332addde54ca41946134ed248af9 | quote: rate-limited to 20 requests/minute and 200 requests/day.
  - [2] 2026-10-28: FAQ states the free limits cannot be raised | capture: sha256:b25f44b54d9e28fdef6c51854a1b92ba3421332addde54ca41946134ed248af9 | quote: Rate limits are strict and shared. 20 RPM and 200 RPD are hard caps with no way to increase them.
  - [2] 2026-10-28: free models run at lower priority with more 502 errors | capture: sha256:b25f44b54d9e28fdef6c51854a1b92ba3421332addde54ca41946134ed248af9 | quote: Free tiers are lower priority in our routing stack, so you may see higher error rates, slower response times, and more frequent `502` upstream errors compared to PAYG models.
  - [3] 2026-10-28: account creation lists an email address and a payment method | capture: sha256:ca31e903249361e7c16129edec4e9647835f4acfd53709d0a0c80b78b0bf5aac | quote: * Provide a valid email address and payment method
  - [1] 2026-11-03: rate-limits page still gives 5 requests per minute for :free models | capture: sha256:256026cb13318a1fea959e97cbe1f9c0dddda401dc035144fc2751c71ff9d6cf | quote: * 5 Requests Per Minute (RPM)
  - [2] 2026-11-03: FAQ page still gives 20 requests per minute and 200 per day for :free models | capture: sha256:81148c1cb03a6ce32df3bc5993968048b8895e2100f2601ff0504bde3b41335d | quote: rate-limited to 20 requests/minute and 200 requests/day.
  - [3] 2026-11-03: terms list a valid email address and payment method among account requirements | capture: sha256:6af387802656e7e9dd7e54975bda825a0c4fc58cf0a7ffc29a2a5551c43c0925 | quote: Provide a valid email address and payment method
  - probe:https://api.routeway.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 403 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:44cf275f9fa968010c236223a26d45fb6d34df3b3de0efbcc2e01cc80d9c3524 | quote: "status": 403
- sources:
  - [1] https://docs.routeway.ai/getting-started/rate-limits
  - [2] https://docs.routeway.ai/getting-started/faq
  - [3] https://routeway.ai/terms
