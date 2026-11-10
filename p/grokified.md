# Grokified

> grokified.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/grokified/ | JSON https://fshy.ajam.dev/api/v1/entity/grokified.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Grokified

- `inference/grokified` | trial-only | evidence documented | binding volume-quota | category inference gateway, prepaid Grok API at half list price, one-time signup credit
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://grokified.com/pricing
- free tier: a one-time $5 signup credit spent at 50% off list price, usable on chat, images and video; there is no recurring free tier | unit: credits | metered on: unstated | read on: 2026-11-04 | source: [1] | note: the terms page says the $5 welcome credit unlocks with the first payment, while the pricing page, the quickstart and the login page say it is spendable from signup; a first payment of $4.99 or more adds $5 more once per account
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the login page carries an email field; the Sep 17, 2026 changelog entry says no card is asked, stored or verified; image and video generation unlock on a first payment
- interface: rest
- limits:
  - volume-quota (binding): $5 signup credit, once; when the balance runs out a key gets 402 insufficient_quota [1]
  - request-rate: Grokified applies no rate limit of its own; a 429 means the shared upstream account is over its rate [2]
- binding note: the $5 credit is the only free allowance and a zero balance returns 402
- endpoint: https://api.grokified.com/v1/chat/completions
- tooling: any OpenAI-compatible client at https://api.grokified.com/v1 with a gk_live_ or gk_test_ key; a first-party CLI and a VS Code extension exist
- composes with: the signup credit then prepaid top-ups from $5 at the same 50% rate
- reliability: 429 responses come from the shared upstream account and carry no reliable Retry-After; accounts flagged for abuse are suspended
- notes: the card requirement of the Aug 28, 2026 changelog entry, with 20 free requests before the card, was reversed by the Sep 17, 2026 entry and is not a current term
- evidence:
  - [1] 2026-11-04: the pricing page states the $5 signup credit at 50% off | capture: sha256:de3c6895fa37a9c7499b6dca2d6076da5f5dd633e1c3f7f5e81544a0466ed16f | quote: $5 in free credits on signup, ready to spend, at the same 50% rate.
  - [1] 2026-11-04: the pricing FAQ says sign-up needs no card | capture: sha256:de3c6895fa37a9c7499b6dca2d6076da5f5dd633e1c3f7f5e81544a0466ed16f | quote: Signing up needs no card.
  - [3] 2026-11-04: the Sep 17, 2026 changelog entry removes the card requirement | capture: sha256:60e38192c27d6ebadbc17ffee216fe3dc4462a8d9e01b96c54357149ce22b16f | quote: The card requirement from Aug 28 is gone. Nothing on Grokified asks for a card to be stored or verified, and we no longer keep one.
  - [3] 2026-11-04: image and video generation unlock on a first payment | capture: sha256:60e38192c27d6ebadbc17ffee216fe3dc4462a8d9e01b96c54357149ce22b16f | quote: Image and video generation now unlock on your first payment instead
  - [2] 2026-11-04: no recurring free tier exists | capture: sha256:dcd08042049a82b4aaac642ed4612a99301cc36db2f7c2eb6fb5ddca7671fe00 | quote: There is no free tier beyond the signup credit
  - [2] 2026-11-04: 429 comes from the shared upstream account | capture: sha256:dcd08042049a82b4aaac642ed4612a99301cc36db2f7c2eb6fb5ddca7671fe00 | quote: A `429 rate_limit_exceeded` has one source: the shared account behind Grokified is over its request or token rate for the moment.
  - [4] 2026-11-04: the terms page says the welcome credit unlocks with the first payment, which conflicts with the pricing page | capture: sha256:294b104224824857f83fce3189bc7a129acb9f17e2a51fa01b7be3c836fa6a93 | quote: The signup welcome credit is $5. It unlocks with your first payment and spends at the same 50% rate as any other usage.
  - [5] 2026-11-04: the quickstart says a new key works on the signup credit | capture: sha256:a1920009f6b1339c5af7ed7111d00f130a8b112113616068ade1558039aef505 | quote: A brand-new key works on its signup credit straight away.
  - [6] 2026-11-04: the login page carries an email field | capture: sha256:58b028665aeaf51c0a5a18510ed671aac785cff2dc49b1e1e82b0e7223e2217a | quote: for="email">Email</label>
  - probe:https://api.grokified.com/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:8d59857efa7df9b68df58f5771f99773db01828ec70ad2bf5930e63fbe132550 | quote: "status": 401
- sources:
  - [1] https://grokified.com/pricing
  - [2] https://grokified.com/docs/rate-limits
  - [3] https://grokified.com/changelog
  - [4] https://grokified.com/terms
  - [5] https://grokified.com/docs/quickstart
  - [6] https://grokified.com/login
