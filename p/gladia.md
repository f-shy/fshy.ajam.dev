# Gladia

> gladia.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gladia/ | JSON https://fshy.ajam.dev/api/v1/entity/gladia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gladia

- `compute/gladia` | qualifies-with-caveat | evidence documented | binding retention-clamped | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:28.068Z (live) | stale on 2026-12-05
- url https://www.gladia.io/pricing
- free tier: 'New accounts get EUR 50 in free credits, valid for one year. That's roughly 312 hours of async transcription on solaria-3, 185 hours on solaria-1, or 73 hours of real-time.' The amount is printed with a euro sign on the vendor page and is written here as EUR 50. The price card is 'Starts at EUR 0.16/hour', with async tiers from EUR 0.27 an hour at 0 to 100 hours down to EUR 0.21 at 10,000+ hours, and real-time from EUR 0.16 to EUR 0.12. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: the wallet is one year: unused credit is lost 12 months after signup, so a 312-hour allowance is a 12-month budget and not a reserve; a project that starts in month 11 gets one month of transcription. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - retention-clamped (binding): the wallet is one year: unused credit is lost 12 months after signup, so a 312-hour allowance is a 12-month budget and not a reserve; a project that starts in month 11 gets one month of transcription. [1]
- limits note: the wallet is one year: unused credit is lost 12 months after signup, so a 312-hour allowance is a 12-month budget and not a reserve; a project that starts in month 11 gets one month of transcription.
- binding note: the same as limits note
- interface detail: REST API at api.gladia.io (POST /v2/pre-recorded starts a job), plus WebSockets for live transcription and the official SDKs, documented.
- tooling: Official SDKs: JavaScript/TypeScript (npm @gladiaio/sdk) and Python (pip gladiaio-sdk); the REST API is used directly otherwise; live transcription uses WebSockets.
- composes with: 312 hours of async transcription for free is the cheapest per-hour speech-to-text lane found among evaluated offerings, and it composes with a free object store for the audio and a free runner for the upload loop. What breaks: the one-year clock, and the 73-hour real-time figure, which is a quarter of the async allowance because real-time bills the connection rather than the audio.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. This is a French vendor billing in EUR, so the figure is EUR 50 and not a converted USD number. Not established: whether signup demands a card; the page offers 'Start with EUR 50 free credits' with a direct app link and states no card requirement, but the form was not opened. Model training is 'Opt-in by default (free opt-out anytime)' on the standard tier and 'Opted out by default' on the enterprise column, which changes what the same 50 EUR buys in privacy terms rather than in hours.
- extras:
  - facets.class: credit-large-enough-for-real-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'New accounts get EUR 50 in free credits, valid for one year. That's roughly 312 hours of async transcription on solaria-3, 185 hours on solaria-1, or 73 hours of real-time', quoted from the FAQ, euro sign written as EUR
  - [1] 2026-10-22: the page header prints 'Credit-based speech-to-text API pricing with no subscription ... Start with EUR 50 free', and the price block 'Starts at EUR 0.16/hour', quoted with the euro sign written as EUR
  - [1] 2026-10-22: the async tier table prints '0 - 100 hours EUR 0.27/hr' for the standard column and 'EUR 0.16/hr' for the volume column, quoted with the euro sign written as EUR; top-up credits above EUR 1,000 'never expire'
  - [2] 2026-11-04: official SDKs exist; jobs and live WebSockets are offered | capture: sha256:f8bc527c04b75e094a31537cc057d3edcc5ff3d2d8b77a59ef9491ab3380da46 | quote: The official SDKs handle upload, jobs, live WebSockets, and retries so you write product code, not plumbing.
  - [3] 2026-11-04: the OpenAPI definition of the pre-recorded endpoint is served from api.gladia.io | capture: sha256:511489fd49d291d33e9f9095fbc99a4c42411e9126fc25072ac866e400b96309 | quote: - url: https://api.gladia.io/
- sources:
  - [1] https://www.gladia.io/pricing
  - [2] https://docs.gladia.io/chapters/how-to-use-gladia/sdk.md
  - [3] https://docs.gladia.io/api-reference/v2/pre-recorded/init
