# AI Power Grid

> aipowergrid.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aipowergrid/ | JSON https://fshy.ajam.dev/api/v1/entity/aipowergrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Power Grid

- `inference/aipg` | paid-only | evidence documented | binding volume-quota | category inference endpoint, keyed paid credits
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://aipowergrid.io/docs/integrations
- free tier: no standing free tier: accounts need spendable credit and a request returns HTTP 402 when credit is low; a manually reviewed builder-credit pilot grants USD 5 to USD 20 that expires 60 days after issuance | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a scoped API key with inference.submit (and account.read for quotes) is created in the console; no card field is shown on the docs pages, but credit must be added before a request succeeds
- interface: rest
- limits:
  - volume-quota (binding): requests need spendable USD credit; HTTP 402 when the account lacks enough credit for the quoted request [1]
- binding note: there is no free allowance, so the need for credit binds before any rate
- endpoint: https://api.aipowergrid.io/v1
- tooling: any OpenAI-compatible client (OpenAI SDK, LiteLLM, LangChain, Vercel AI SDK) with a scoped Grid key
- composes with: pairs with an OpenAI-compatible agent, but every request spends USD-denominated service credit; the scarce link is a funded account
- reliability: workers are community-operated and model availability follows connected workers; a discovered model is not an uptime guarantee
- notes: builder credits are a reviewed pilot capped at USD 5-20 and expiring after 60 days, not a standing free tier.
- evidence note: the verdict rests on the cited first-party evidence; confidence is documented
- evidence:
  - [1] 2026-11-18: an HTTP 402 means the account needs more spendable credit | capture: sha256:c1b96415f97ddf6395d18f25181ab328e0a4b71ceb25b6c65cf27f34a907b081 | quote: An HTTP `402` means the account needs more currently spendable credit; it does not mean the key or client configuration is invalid.
  - [2] 2026-11-18: builder credits are USD 5-20 and expire 60 days after issuance | capture: sha256:3badf5ca404a37fc1fc98192ebd4baaf81d0958c47a00ffd54ada143b93cb688 | quote: Grants expire 60 days after issuance and are issued only while the finite campaign budget and promotional-credit rail are active.
- sources:
  - [1] https://aipowergrid.io/docs/integrations
  - [2] https://aipowergrid.io/docs/builder-credits
