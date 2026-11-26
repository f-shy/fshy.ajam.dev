# RunInfra

> runinfra.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runinfra/ | JSON https://fshy.ajam.dev/api/v1/entity/runinfra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunInfra

- `compute/runinfra` | trial-only | evidence documented | binding volume-quota | category inference API | tier Pay-as-you-go credits (USD 1 free on signup)
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:15.041Z (live) | stale on 2026-12-25
- url https://runinfra.ai/pricing
- free tier: $1 free for a new account. A workspace has one balance, and one credit is USD 1. Two things add to it: the free signup credit of USD 1, once per account, which never expires, and top-ups from USD 5, which last one year from purchase. At zero balance, calls answer 402 and are not billed. | unit: credits | metered on: none | read on: 2026-11-24 | source: [1] | note: one-time signup credit, not recurring: at the listed DeepSeek V4.1 Flash input price of USD 0.15 per 1M tokens, USD 1 buys about 6.7M input tokens if spent on input alone
- per-object cap: not applicable: the unit is API tokens and prepaid credits, not stored objects. | source: [1] | note: machine/API record; no per-object cap published
- retention: Zero data retention by default. Request and response content is never used for training. | days: 0 | source: [1] | note: the gateway keeps usage metadata for billing, not prompt text
- egress: not published: the pricing and account pages state zero data retention and prompt caching but no egress allowance, quota or per-TB price. | metered: no | source: [1]
- identity: email | detail: Sign in with Google, GitHub or an email link, at the email address you already use. If you have no account yet, the first sign-in creates one, with no card required and USD 1 in credit. SAML or OIDC single sign-on is not available today. A card is asked only for a top-up from USD 5, not for the free credit.
- interface: rest, cli
- limits:
  - request-rate: 10,000 requests per minute per key before the first purchase; 50,000 after a purchase from USD 5; 200,000 at USD 200 in total purchases. The signup credit does not raise the limit. [2]
  - volume-quota (binding): USD 1 in credit once on signup, never expiring; top-ups from USD 5. At zero balance, calls answer 402 and are not billed. [1]
- limits note: Tokens per minute are each model's own default before USD 50 in purchases, then at least 20,000,000 per minute at USD 50 and no practical limit at USD 200. Concurrent requests are about a quarter of each model before the first purchase.
- binding note: The one-time USD 1 balance is spent before 10,000 requests a minute is reached at ordinary model prices; after a top-up the request-rate limit becomes the next constraint.
- interface detail: OpenAI-compatible Chat Completions at /v1/chat/completions and Anthropic-compatible Messages at /v1/messages through one workspace key, plus the runinfra command-line tool for setting up coding agents.
- endpoint: https://api.runinfra.ai/v1
- tooling: the user installs an OpenAI- or Anthropic-compatible SDK or the runinfra CLI and connects to the hosted API; no server binary is run by the user and no hardware is owned.
- composes with: One key reaches the OpenAI-compatible and Anthropic-compatible routes, so an existing agent loop can be pointed at RunInfra; the free credit is spendable on both, but the 10,000-requests-per-minute key limit and the one-time USD 1 balance bind first.
- reliability: Requests return 402 at zero balance, and a rate-limited request returns 429 with Retry-After; shared-model congestion errors are not cleared by purchases.
- notes: The free offer is a one-time USD 1 credit, not a recurring allowance, and the service is a paid-per-token hosted inference API. Token prices range from USD 0.05 per 1M input tokens on Nemotron 3.5 Lightning 30B to USD 1.60 on Kimi K3.1 Pro; cached input is cheaper. The API list needs a key (HTTP 401), so no endpoint was probed beyond reachability. A separate startups program offers up to USD 2,700 in credits after approval and is not the published free tier.
- evidence note: The free credit, token rates, key rate limits, sign-in methods and egress silence are quoted from the vendor's own pricing, docs and account pages read on 2026-11-24; the API base URL was probed and answered 401 without a key.
- extras:
  - shape.gpu_class: hosted open models, GPUs not exposed
  - billing_model: prepaid USD 1 signup credit then per-token payment or a monthly coding plan
  - free_tier_kind: one-time-credit
  - term: one-time credit never expires; top-ups last one year
  - status: published on the current pricing page
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: 10,000 requests a minute per key initially; limits rise with lifetime purchases
- evidence:
  - [1] 2026-11-24: a new account receives USD 1 in free credit | capture: sha256:003ad852766243158d6351755c1a9448740d02b2a88b549c088eb2cc55125457 | quote: $1 free for a new account
  - [1] 2026-11-24: the starting request-rate ceiling is 10,000 requests a minute per key, rising with purchases | capture: sha256:003ad852766243158d6351755c1a9448740d02b2a88b549c088eb2cc55125457 | quote: 10,000 requests a minute per key to start, 50,000 after your first purchase, 200,000 once your purchases reach USD 200.
  - [1] 2026-11-24: the vendor states zero data retention by default and no training on content | capture: sha256:003ad852766243158d6351755c1a9448740d02b2a88b549c088eb2cc55125457 | quote: Zero data retention by default
  - [3] 2026-11-24: the free signup credit is USD 1 once per account and never expires, top-ups start at USD 5, and a card or USDC pays them | capture: sha256:ffa1be0e89f8f525d95d100edae35bcb481d4a70d0caba03b7d918fe0e0277e3 | quote: Free on signup | USD 1, once per account, never expires
  - [3] 2026-11-24: top-ups are paid by card or USDC, so a card is not needed for the free credit | capture: sha256:ffa1be0e89f8f525d95d100edae35bcb481d4a70d0caba03b7d918fe0e0277e3 | quote: How you pay | Card, or USDC for one-time top-ups up to USD 10,000
  - [2] 2026-11-24: the USD 0 tier is 10,000 requests a minute per key and the signup credit does not raise limits | capture: sha256:2b61526f913d37fa32db9c4f50fd7b6bc14a46ac23fe14f64fcd61b19cf4bc73 | quote: USD 0 | 10,000 | The model's own limit | About a quarter of the model
  - [4] 2026-11-24: sign-in uses Google, GitHub or an email link, creates an account with no card and USD 1 in credit | capture: sha256:30f7ae9140a7ddeb3625b542e79ef5b2ca9abd525d2c89aa225a856154c48859 | quote: Sign in with Google, GitHub or an email link, at the email address you already use. If you have no account yet, the first sign-in creates one, with no card required and USD 1 in credit. An expired link says so with a resend option.
  - [4] 2026-11-24: no SAML or OIDC single sign-on is offered today | capture: sha256:30f7ae9140a7ddeb3625b542e79ef5b2ca9abd525d2c89aa225a856154c48859 | quote: Sign-in today is Google, GitHub or an email link. SAML or OIDC single sign-on is not available today. If your company needs it, write to [support](https://www.rightnowai.co/docs/open-models/support).
  - [5] 2026-11-24: the API base URL used by the provider is https://api.runinfra.ai/v1 | capture: sha256:65ea24cb9f0189115445a95762e9e1c60c785d4b65e7ae9493d33adc7f81527b | quote: https://api.runinfra.ai/v1
  - probe:https://api.runinfra.ai/v1/models 2026-11-24: the model list endpoint answered 401 without a key | capture: sha256:14bed25b6860535193bd5b5077688e9b16cce72eb859839bf0834165c4ff4a9a | quote: "status": 401
- sources:
  - [1] https://runinfra.ai/pricing
  - [2] https://www.rightnowai.co/docs/open-models/rate-limits
  - [3] https://runinfra.ai/docs/introduction/plans
  - [4] https://runinfra.ai/docs/faq/account
  - [5] https://models.dev/providers/runinfra
