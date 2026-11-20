# CoralBricks

> coralbricks.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coralbricks/ | JSON https://fshy.ajam.dev/api/v1/entity/coralbricks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoralBricks

- `inference/coralbricks` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://www.coralbricks.ai/docs
- free tier: No free allowance is stated. Access is self-serve with no waitlist or allowlist, and requests are paid per token from a prepaid credit balance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up and create an API key; no waitlist or allowlist
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit balance billed per token [1]
- endpoint: https://inference.coralbricks.ai/v1
- tooling: an OpenAI-compatible base URL with Chat Completions, Responses and background Responses surfaces
- composes with: the prepaid credit balance is the scarce link; no free text tier is published
- reliability: per-organization concurrency limits apply; with Zero Data Retention on, background Responses mode is unavailable
- notes: no standing free inference allowance is published; usage is prepaid per token
- evidence:
  - [1] 2026-11-18: access is self-serve with no waitlist, and inference is paid per token from a prepaid credit balance; no free allowance is stated | capture: sha256:8b09659c158fa9045770a1e19a6b8664b3fd4d140d358916a6135cafdd3ecbed | quote: Access is self-serve: [sign up](https://www.coralbricks.ai/register), create a key at [/api-keys](https://www.coralbricks.ai/api-keys), and pay per token from a prepaid credit balance, with no waitlist or allowlist.
- sources:
  - [1] https://www.coralbricks.ai/docs
