# Kitani

> kitani.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kitani/ | JSON https://fshy.ajam.dev/api/v1/entity/kitani.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kitani

- `inference/kitani` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://kitani.ai/docs
- free tier: No free allowance is stated. Create a pay-as-you-go key or hold a Kitani One subscription; the model catalog lists per-million-token prices with no free tier. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create a pay-as-you-go key in the console or buy a Kitani One subscription
- interface: rest
- limits:
  - volume-quota (binding): per-million-token prices across the model catalog with no free allowance [2]
- endpoint: https://api.kitani.ai/v1
- tooling: an OpenAI-compatible base URL with a PAYG or One key
- composes with: the per-token charge and the key are the scarce links; no free tier is published
- reliability: models are marked Hot, Warm or Cool according to whether they are on GPU, in local storage, or loaded on request; first-token latency varies with queue time
- notes: no standing free inference allowance is published; the catalog lists per-token prices and a PAYG key or subscription is required
- evidence:
  - [1] 2026-11-18: a pay-as-you-go key or a paid One subscription is required; the model catalog lists per-token prices with no free allowance | capture: sha256:59373f841e2e87940b0670319bfc41c0f08052e853e8571a76760693ca44f674 | quote: Create a PAYG key in the console, or a One key if you have a [Kitani One subscription](https://kitani.ai/dashboard/one).
- sources:
  - [1] https://kitani.ai/docs
  - [2] https://kitani.ai/models
