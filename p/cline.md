# Cline

> cline.bot | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cline/ | JSON https://fshy.ajam.dev/api/v1/entity/cline.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cline

- `coding-subs/cline` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category BYOK coding agent
- needs card no, phone no, ID no, institution no | verified 2026-11-03T17:29:12.673Z (live) | stale on 2026-12-04
- url https://cline.bot/pricing
- free tier: free for individual developers; bring your own API key or use managed infrastructure | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: the product costs nothing; the inference it calls is the bill
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: a GitHub account for the extension marketplace
- interface: cli
- limits note: no vendor-imposed usage cap, because the vendor does not serve the inference no vendor quota binds: the vendor does not serve the usage this record prices
- interface detail: a VS Code extension; any OpenAI-compatible or Anthropic-compatible endpoint
- tooling: VS Code extension; accepts an arbitrary base URL and key
- reliability: no reliability event recorded
- notes: Its cost is entirely the upstream endpoint.
- evidence note: the price model is quoted from the vendor page. Nothing about capacity can be measured here because capacity belongs to the endpoint chosen.
- self hosted: yes
- evidence:
  - [1] 2026-10-22: individual use is free, and the product is described as BYO API key or managed infrastructure, with an Enterprise tier for organisations
  - [1] 2026-10-30: the product stays free for individual developers; inference is billed on usage or brought as an own key | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: Cline is free for individual developers.
  - [1] 2026-11-03: the individual plan is still free; there is no vendor quota | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: Cline is free for individual developers.
  - [1] 2026-11-03: the Free card lists model inference at cost or with the user's own key, so the inference is the cost and no vendor quota binds | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: - Purchase and Model Inference at Cost or BYOK
- sources:
  - [1] https://cline.bot/pricing
