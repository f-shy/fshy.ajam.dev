# Fluence Inference

> fluence.cloud | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fluence/ | JSON https://fshy.ajam.dev/api/v1/entity/fluence.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fluence Inference

- `inference/fluence-inference` | paid-only | evidence documented | binding volume-quota | category inference gateway, invite-only beta, prepaid credits
- needs card yes, phone no, ID no, institution no | verified 2026-10-28T04:36:19.314Z (live) | stale on 2026-11-28
- url https://inference.fluence.cloud/
- free tier: None: access is invite-only during the private beta and every call draws on prepaid USD credits with a minimum purchase of USD 5. A first top-up of USD 10 or more earns a USD 5 bonus while the offer lasts, and an invite link can add sign-up credit up to the limit it shows. | unit: none | metered on: unstated | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an invitation to an email address is required during the private beta, sign-in is by one-time code or link, and credits are bought through Stripe checkout with a USD 5 minimum; other payment methods are not listed on the page read
- interface: rest
- limits:
  - request-rate: unpublished at account level; a key can carry its own per-minute and per-day request caps, a concurrency cap and a monthly USD budget set by its owner [1]
  - volume-quota (binding): minimum credit purchase USD 5; a first top-up of USD 10 or more earns a USD 5 bonus; HTTP 402 when available credit is insufficient [1]
- binding note: access is by invitation and every call spends prepaid credit, so there is no free allowance to run out first
- endpoint: https://api.fluence.cloud/v1/chat/completions
- tooling: OpenAI-compatible REST at https://api.fluence.cloud/v1 and an Anthropic-compatible Messages endpoint at https://api.fluence.cloud; one key with the inference permission
- composes with: routes each request to one of several providers behind one key and one base URL; the invitation and the prepaid balance gate every call
- reliability: no reliability event recorded
- notes: Fluence Inference routes each request to one of its providers; GPU rental from the same company is recorded separately (compute/fluence).
- evidence note: documentation page only; the size of an invite-link credit is unverified
- evidence:
  - [1] 2026-10-28: access is by invitation during the private beta | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: Access is invite-only during the private beta.
  - [1] 2026-10-28: requests are routed to one of Fluence's providers behind one key and one endpoint | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: Fluence routes each request to one of its providers.
  - [1] 2026-10-28: an invitation to an email address, or an invite link, is the way in | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: Ask your Fluence contact to invite your email, or open an invite link
  - [1] 2026-10-28: credits are prepaid with a USD 5 minimum purchase | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: 2. Add prepaid USD credits in Billing. The minimum purchase is $5, and a first top-up of $10 or more can earn a bonus.
  - [1] 2026-10-28: a first top-up of USD 10 or more earns a USD 5 bonus and an invite link can add sign-up credit | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: While the offer lasts, a first top-up of $10 or more before tax earns a $5 bonus; an invite link can add sign-up credit and a share of the first top-up, up to the limit it shows.
  - [1] 2026-10-28: per-key caps on rate, concurrency and monthly budget are set by the key owner | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: A key can also limit requests per minute and day, concurrency, a monthly USD budget that resets each UTC month, expiry, its access list and IPv4 or IPv6 addresses or CIDRs.
  - [1] 2026-10-28: payment runs through Stripe checkout | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: Stripe runs checkout, taxes, card details and fraud checks
  - [1] 2026-10-28: an empty balance returns 402 | capture: sha256:0e30f8cdbe74ff10f67e0b6684dcdd9fce954ec45ad18c5ceba228e89cb4446f | quote: | 402 | Insufficient available credits |
- sources:
  - [1] https://inference.fluence.cloud/docs
