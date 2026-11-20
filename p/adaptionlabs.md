# Adaption

> adaptionlabs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adaptionlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/adaptionlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Adaption

- `inference/adaption` | paid-only | evidence documented | binding write-gated | category data-optimization and training API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://docs.adaptionlabs.ai
- free tier: No self-serve inference free tier or public model-API price is stated. The API documents Adaptive Data and AutoScientist product APIs reached with a key. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in at adaptionlabs.ai and create an API key in Settings; no self-serve inference free tier is published
- interface: rest
- limits:
  - write-gated (binding): sign-in and an API key are required; no public inference allowance is stated [1]
- endpoint: https://api.prod.adaptionlabs.ai/api/v1
- tooling: the Adaption Python SDK and an API key; the operator markets data-optimization and custom-model training, not a text inference endpoint
- composes with: the absence of a published inference offer is the scarce link; the API sells data adaptation and model training
- reliability: no public inference free tier, price, or quota is documented, so the inference offer is unverified
- notes: the first-party docs describe a data-optimization and training platform with a key-gated API; no model-inference free tier or price is published
- evidence:
  - [1] 2026-11-18: the API exposes Adaptive Data and AutoScientist; no inference free tier, price, or self-serve inference allowance is stated | capture: sha256:12c10a57d3417ee986cf561eb8614e17e2d6529d3b030174e5e024a25c622d54 | quote: Both Adaptive Data and AutoScientist are accessible through our API today.
- sources:
  - [1] https://docs.adaptionlabs.ai
