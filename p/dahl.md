# Dahl Inference

> dahl.global | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dahl/ | JSON https://fshy.ajam.dev/api/v1/entity/dahl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dahl Inference

- `inference/dahl-inference` | trial-only | evidence documented | binding volume-quota | category inference API on the Gonka network, one-time 100M-token grant, anonymous account
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://inference.dahl.global/docs/tokens/
- free tier: a one-time gift of 100 million tokens to the account pool at signup, with no monthly reset; a new key holds 0 tokens until tokens are allocated from the pool | unit: tokens | metered on: unstated | read on: 2026-11-04 | source: [1] | note: creating extra keys does not grant more free tokens; paid top-ups are about $0.02 per 1M tokens
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: an account is a username and a generated fingerprint that is the password; there is no email recovery by design; sign-up runs a Cloudflare browser check
- interface: rest
- limits:
  - volume-quota (binding): 100 million tokens once per account, spent on input plus output tokens [1]
  - request-rate: parallel-request limits per key and per account and a per-model concurrency cap return 429; free accounts queue behind paid ones at peak; no numbers published [2]
- binding note: the one-time 100M-token grant is the whole free allowance
- endpoint: https://inference.dahl.global/v1/chat/completions
- tooling: OpenAI-compatible client at https://inference.dahl.global/v1 with a Bearer key; sign-up is browser-only behind a Cloudflare check
- composes with: top-up with crypto (USDT, BTC and others via NOWPayments) makes the account paid and first in the capacity queue
- reliability: at model capacity, requests are admitted paid accounts first, then free accounts; 429 model_concurrency when a model is full
- notes: one-time grant, no monthly reset
- evidence:
  - [1] 2026-11-04: a new account receives 100 million tokens at signup | capture: sha256:2b66300782144b6629e93fd49ef41abdcef8c97ddaa0208b061df6d172286635 | quote: - New account: 100 million tokens as a gift at signup — they go to the pool, not to the first key.
  - [1] 2026-11-04: extra keys add no free tokens | capture: sha256:2b66300782144b6629e93fd49ef41abdcef8c97ddaa0208b061df6d172286635 | quote: Creating extra keys does not grant more free tokens.
  - [3] 2026-11-04: accounts have no email | capture: sha256:adfcb711d814aa8d725a6a4c9424b6c92f195318d378cc23ba9839242b9d847b | quote: If you lose the fingerprint, create a new account. There is no email recovery by design.
  - [3] 2026-11-04: the account is a username plus a fingerprint | capture: sha256:adfcb711d814aa8d725a6a4c9424b6c92f195318d378cc23ba9839242b9d847b | quote: Username: 3–20 characters, letters, digits, underscore.
  - [2] 2026-11-04: free accounts queue behind paid at capacity | capture: sha256:30c66a27bb24a911a0406541c93c4134a7817f55343d2872e91bd118009190a2 | quote: When a model is at capacity, requests are admitted by account class: paid accounts first, then free accounts, then keys not linked to an account.
  - probe:https://inference.dahl.global/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:fd814a72cba6894c12f9e94198ae5bda6466286f0c0eed7f2c27e2c6ee4deb6a | quote: "status": 401
- sources:
  - [1] https://inference.dahl.global/docs/tokens/
  - [2] https://inference.dahl.global/docs/api/
  - [3] https://inference.dahl.global/docs/authentication/
