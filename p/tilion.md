# Tilion

> tilion.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilion/ | JSON https://fshy.ajam.dev/api/v1/entity/tilion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tilion

- `compute/tilion` | paid-only | evidence documented | binding request-rate | category browser host
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:42.693Z (live) | stale on 2026-12-26
- url https://tilion.com/pricing
- free tier: a free plan with $5 of credit once at sign-up, no card needed: 3 browsers at once, unlimited actions and CAPTCHA solves, datacenter and premium proxy; the cheapest paid plan is Developer at $40/month with 20 browsers at once and $40 of credit every month | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $2,000 a month for the single published plan [1]
  - write-gated: no self-serve free path is priced; the one plan is billed monthly [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and prices one plan at $2,000 a month. The record's free-tier claim is contradicted and the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.note: the page varies the GPU, screen, fonts, timezone, canvas and audio per launch
  - session_cap.restart_required: no
  - session_cap.note: each launch is a different machine; the page states no clock
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'A different, coherent machine on every launch: GPU, screen, fonts, timezone, canvas, audio' with '$2,000/month' and '24-hour Slack support', quoted
  - [1] 2026-11-25: the pricing page states a $0 Free plan with $5 sign-up credit and no card, and a Developer plan at $40/month with 20 browsers and $40 monthly credit | capture: sha256:fc54b5824462c35531a4b9790c3c32581c5be8ebe15f453ab584662a99470f19 | quote: Every account gets $5 of free credit when you sign up. No card needed. ... $0/month ... - 3 browsers at once - $5 of credit once, at sign-up - Unlimited actions and CAPTCHA solves - Datacenter and premium proxy ... $40/month ... - 20 browsers at once - $40 of credit every…
  - [1] 2026-11-25: the pricing page still states the free plan's credit, no-card condition and 3-browser allowance and the $40/month Developer plan | capture: sha256:fc54b5824462c35531a4b9790c3c32581c5be8ebe15f453ab584662a99470f19 | quote: Every account gets $5 of free credit when you sign up. No card needed. ... $0/month ... - 3 browsers at once - $5 of credit once, at sign-up - Unlimited actions and CAPTCHA solves - Datacenter and premium proxy ... $40/month ... - 20 browsers at once - $40 of credit every…
- sources:
  - [1] https://tilion.com/pricing
