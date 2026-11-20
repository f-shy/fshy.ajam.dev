# Echo

> tracerml.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tracerml/ | JSON https://fshy.ajam.dev/api/v1/entity/tracerml.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Echo

- `inference/echo` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://echo.tracerml.ai/docs/api
- free tier: No free inference allowance is stated. The consumption offer has a 5.5% top-up fee, a USD 20 minimum credit purchase and 12-month validity for new credit. Echo model output is billed at USD 50 per million tokens. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create a workspace and a workspace API key at /api, then add credits at /credits
- interface: rest
- limits:
  - volume-quota (binding): USD 20 minimum credit purchase, 5.5% top-up fee, 12-month validity [1]
- endpoint: https://echo.tracerml.ai/v1
- tooling: an OpenAI-compatible base URL with a workspace API key and the official OpenAI SDK
- composes with: the paid credit wallet is the scarce link; no free text tier is published
- reliability: a pending receipt must not be treated as a free request; requests are stateless and not deduplicated, and SDK retries can incur another charge
- notes: no standing free inference allowance is published; a paid workspace wallet with a minimum purchase is required
- evidence:
  - [1] 2026-11-18: credits carry a 5.5% top-up fee, a USD 20 minimum purchase and 12-month validity; no free inference allowance is stated | capture: sha256:16c3469118e1e7b44f333b064c3ddf4baa662e665f181d9dd8f4fd7bda26fbfc | quote: The current consumption offer has a 5.5% top-up fee, a $20 minimum credit purchase and 12-month validity for new credit.
- sources:
  - [1] https://echo.tracerml.ai/docs/api
