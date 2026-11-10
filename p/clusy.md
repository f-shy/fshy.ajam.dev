# Clusy

> clusy.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clusy/ | JSON https://fshy.ajam.dev/api/v1/entity/clusy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clusy

- `compute/clusy` | qualifies-with-caveat | evidence documented | binding request-rate | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:14.689Z (live) | stale on 2026-12-05
- url https://www.clusy.io/pricing
- free tier: $0/mo tier with 1 concurrent sandbox; Plus is $12/mo for 3 concurrent sandboxes and Pro $30/mo for 8 | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page limits table lists checkpoint storage, retention, sandbox RAM, GPUs and concurrent sandboxes, and no egress or bandwidth row | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): 1 concurrent sandbox on Free, 3 on Plus, 8 on Pro, 12 and 24 on the Max levels [1]
- interface detail: a web notebook IDE (console only); .ipynb import and export, and publish to Hugging Face, Kaggle or GitHub; no REST API, CLI or SSH on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the limits table was read on 2026-10-22. The free tier is defined by concurrency, not by a credit or an hour allowance, so the unit is none and the limit is the concurrency row
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page publishes no session cap; concurrency is what bounds a free account
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| Price | $0/mo | $12/mo | $30/mo | $90/mo | $200/mo |' against '| Concurrent sandboxes | 1 | 3 | 8 | 12 | 24 |', quoted
  - [1] 2026-11-03: the limits table lists sandbox, storage, RAM and GPU rows and no egress row | capture: sha256:83db0fc93b898d869ab77cd1912bd49fc65097f3aadf89e4e547a4daa67e8d97 | quote: | Concurrent sandboxes | 1 | 3 | 8 | 12 | 24 |
  - [2] 2026-11-03: the product is a browser notebook IDE; no API, CLI or SSH is described | capture: sha256:9bbe7bd51a17be33ea97a5eb29d48af4ddb3b64a6b1245a740564edc134241a0 | quote: Clusy is an AI IDE for Jupyter notebooks.
- sources:
  - [1] https://www.clusy.io/pricing
  - [2] https://www.clusy.io/notebook
