# Trae

> trae.ai | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trae/ | JSON https://fshy.ajam.dev/api/v1/entity/trae.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trae

- `coding-subs/trae` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:28:03.755Z (live) | stale on 2026-12-05
- url https://www.trae.ai/pricing
- free tier: Free: USD 0, auto mode only, limited usage, limited autocomplete | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the Free tier restricts model choice to auto routing, so the model is chosen for you
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: an account; no card is stated for the Free tier
- interface: cli
- limits:
  - request-rate (binding): usage denominated in USD per month: 0 on Free, USD 20 on Pro, USD 60 on Pro+, USD 200 on Ultra [1]
- interface detail: the Trae IDE; a cloud task surface is counted in concurrent tasks per plan
- tooling: Trae IDE on desktop
- composes with: no documented programmatic API key; the quota is bound to the editor
- reliability: no reliability event recorded
- notes: Pro was USD 20 on 2026-09-20. The pricing page read on 2026-10-22 has no Pro at USD 10 and no 'Lite' tier at USD 3.
- evidence note: the Free plan was re-read on the vendor pricing page on 2026-11-04 (auto mode only), which is the evidence row of that date; the full ladder was read on 2026-10-22. verified_at is the instant of the 2026-11-04 fetch, read from the fetch log, not typed.
- evidence:
  - [1] 2026-10-22: Free USD 0, Pro USD 20, Pro+ USD 60, Ultra USD 200, each with a monthly usage allowance equal to its price; there is no Lite tier and no USD 3 or USD 10 row
  - [1] 2026-11-04: the Free plan still offers auto mode only, limited usage and limited autocomplete | capture: sha256:eed10a453d4cb98ccd8c2776fbf3764d11d49fca5a13ca1adf45fe0a63bb04b5 | quote: Auto mode only
  - [1] 2026-11-04: the Free plan still offers auto mode only on the pricing page read on 2026-11-04 | capture: sha256:eed10a453d4cb98ccd8c2776fbf3764d11d49fca5a13ca1adf45fe0a63bb04b5 | quote: Auto mode only
- sources:
  - [1] https://www.trae.ai/pricing
