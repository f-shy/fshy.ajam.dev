# Aion Labs

> aionlabs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aionlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/aionlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aion Labs

- `inference/aion-labs` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API, free tier with a daily token cap
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://www.aionlabs.ai/docs/rate-limits/
- free tier: a Free tier at $0 with a daily credit allowance; the Free rate tier is 20,000 tokens per minute and a 20,000 daily token limit, no card | unit: tokens | metered on: unstated | read on: 2026-11-04 | source: [1] | note: whether the daily credit allowance of the pricing page and the 20,000 daily token limit of the rate-limit page are one cap is unverified
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the account page offers an email address field plus Continue with GitHub and Continue with Google; the pricing page says no card is required for the Free tier
- interface: rest
- limits:
  - request-rate: Free tier: 20,000 tokens per minute [1]
  - volume-quota (binding): Free tier: 20,000 daily token limit [1]
- binding note: the 20,000 daily token limit equals the per-minute limit and binds after one minute of use
- endpoint: https://api.aionlabs.ai/v1/chat/completions
- tooling: OpenAI-compatible client at https://api.aionlabs.ai/v1; GET /v1/models is public
- composes with: any credit top-up moves the account to Tier 1 at 1,000,000 tokens per minute with no daily cap
- reliability: not measured
- notes: the free daily cap is small: 20,000 tokens a day
- evidence:
  - [1] 2026-11-04: the Free tier allows 20,000 tokens per minute and 20,000 per day | capture: sha256:056430d232985ee34cd2ae9c7e69a5b26fbb803b9291a2992f37ae13acef38bb | quote: | Free | 20,000 | 20,000 |
  - [1] 2026-11-04: the Free tier is the default at sign-up | capture: sha256:056430d232985ee34cd2ae9c7e69a5b26fbb803b9291a2992f37ae13acef38bb | quote: | Free | Default on signup |
  - [2] 2026-11-04: the Free Tier is a daily credit allowance with no card | capture: sha256:94cb8b055ea0791223b33d1ae5861246224984e3f3922851342b82c47960f41b | quote: A daily credit allowance to try agent jobs, the API, and browser chat. No card required.
  - [3] 2026-11-04: the account page offers an email address field | capture: sha256:15ae9a9d6215dddebb58d46fe678570fdcf865cfcf613a90a8918810af4a1a61 | quote: placeholder="Email address"
  - probe:https://api.aionlabs.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:f02a4ee6fbd2d469e88ed44f8a7c537bf84f59a779ca339baddc0d35829e1305 | quote: "status": 401
- sources:
  - [1] https://www.aionlabs.ai/docs/rate-limits/
  - [2] https://www.aionlabs.ai/pricing
  - [3] https://www.aionlabs.ai/app/api-keys/
