# submodel

> submodel.gitbook.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/submodel/ | JSON https://fshy.ajam.dev/api/v1/entity/submodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## submodel

- `inference/submodel` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway (GPU cloud)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://submodel.gitbook.io/docs/getting-started/billing-information.md
- free tier: Capacity limits, free allowances and prices come from current configuration. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and a gateway key are needed; no card is stated for the free-quota models
- interface: rest
- limits:
  - volume-quota (binding): free allowances exist but the amount is not stated on the captured page [1]
- endpoint: https://llm.submodel.ai/v1
- composes with: The submodel.ai model list marks several models Ready with a Free Quota badge, but no quota number is published; the field is unverified.
- reliability: the docs warn that free allowances, minimums and promotions follow live configuration
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: SubModel documents free allowances whose size comes from current configuration, and shows a Free Quota badge on several models | capture: sha256:38876729f64a6c68491a5e3af5b5ed3e35db1fee8f774c39c92904acea0d4836 | quote: Capacity limits, free allowances and prices come from current configuration.
- sources:
  - [1] https://submodel.gitbook.io/docs/getting-started/billing-information.md
