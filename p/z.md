# Z.ai GLM

> z.ai | Compute, Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/z/ | JSON https://fshy.ajam.dev/api/v1/entity/z.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Z.ai GLM Flash

- `compute/z-ai-glm-flash` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-03T14:55:03.467Z (live) | stale on 2026-12-04
- url https://docs.z.ai/guides/overview/pricing
- free tier: Three models are priced Free on every column of the official pricing table, with no time limit stated: GLM-4.7-Flash and GLM-4.5-Flash (text) and GLM-4.6V-Flash (vision), each 'Free | Free | Free | Free' for input, cached input, cached input storage and output. Most paid rows carry 'Limited-time Free' in the cached input storage column; these three carry plain 'Free'. The paid GLM-5.3-Flash sits beside them at USD 0.15 input and USD 0.50 output per 1M tokens, which is the rate to price the free lane against. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-free-model
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account on the Z.AI Open Platform ('Register or Login'); the quick start names a billing top-up only 'if needed'. The Z.ai international sign-in page (chat.z.ai/auth) offers Continue with Google, Continue with Email and Continue with GitHub and shows no phone field; unverified: whether the API console at z.ai uses the same sign-in, and whether a phone step follows: behind a sign-up
- interface: rest
- limits:
  - request-rate (binding): no quota is published at all: the FAQ points rate limits at z.ai/manage-apikey/rate-limits, which is behind a login, so the concurrency ceiling is unknown until an account exists and it is the first thing to measure. [1]
- limits note: no quota is published at all: the FAQ points rate limits at z.ai/manage-apikey/rate-limits, which is behind a login, so the concurrency ceiling is unknown until an account exists and it is the first thing to measure.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free model with an OpenAI-compatible endpoint is the cheap first pass in a two-stage pipeline: GLM-4.7-Flash classifies or filters, and only the survivors go to a metered model.
- reliability: no reliability event recorded
- notes: The rate limit is not public: the pricing doc prints no limits, the FAQ points at z.ai/manage-apikey/rate-limits, and docs.z.ai/api-reference/rate-limit.md, the Rate Limits entry of the docs index, redirects there, where a reader who is not signed in gets a marketing page and no limits table, also when the page is rendered in a browser. The docs are served in English; the quick start lists register or login, a billing top-up only if needed, and an API key, and the FAQ says card recharge does not support 3DS verification. The console figure is unverified: behind a sign-up.
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: recurring-free-model
- evidence:
  - [1] 2026-10-22: '| GLM-4.7-Flash | Free | Free | Free | Free |' and '| GLM-4.5-Flash | Free | Free | Free | Free |' in the text models table, quoted
  - [1] 2026-10-22: GLM-5.3-Flash priced USD 0.15 input and USD 0.50 output per 1M tokens, which is the paid comparator for the free Flash lane, quoted
  - [2] 2026-10-22: 'How can I check the rate limits? You can check the rate limits from here: https://z.ai/manage-apikey/rate-limits', quoted; the page requires a login
  - [1] 2026-10-28: GLM-4.6V-Flash is priced Free on every column; GLM-4.7-Flash and GLM-4.5-Flash carry the same four Free cells | capture: sha256:33a372c40dc41ea671512a575590cdd218e648897e4b4dce9caa49fc7dc0e205 | quote: | GLM-4.6V-Flash | Free | Free | Free | Free |
  - [1] 2026-10-28: GLM-5.3-Flash is priced $0.15 input and $0.50 output per 1M tokens, the paid comparator for the Free Flash rows | capture: sha256:33a372c40dc41ea671512a575590cdd218e648897e4b4dce9caa49fc7dc0e205 | quote: | GLM-5.3-Flash | \$0.15 | \$0.03 | Limited-time Free | \$0.50 |
  - [3] 2026-10-28: the quick start tells a new user to register on the Z.AI Open Platform and mentions a billing top-up only if needed | capture: sha256:ee725fe9fb78d0f58c81ff887a932f48b7a23f701476e905389ca057376135cd | quote: * Access [Z.AI Open Platform](https://z.ai/model-api), Register or Login.
  - [2] 2026-10-31: the FAQ sends rate limits to the console page z.ai/manage-apikey/rate-limits and prints no figure | capture: sha256:f3989c87449e0bd5cea15b9d15f93995dbf394d5d626f2b14042ff3689e3972b | quote: You can check the rate limits from here: [https://z.ai/manage-apikey/rate-limits](https://z.ai/manage-apikey/rate-limits)
  - [4] 2026-10-31: the Rate Limits doc URL is served by the console route manage-apikey/rate-limits, not by a docs page | capture: sha256:90c8df3ca290ddaf0e2948e0981b6254ff18886e2c0ef8e63cfff681c1ad1cc4 | quote: x-middleware-rewrite: /en/manage-apikey/rate-limits
  - [4] 2026-10-31: read without a sign-in, the Rate Limits doc URL ends at z.ai/manage-apikey/rate-limits and serves a marketing banner with no limits table | capture: sha256:b618b9803b9cdd5a6b7433170ff164cb454575d4ecbc3c8434445c5a89406dc3 | quote: From only $18/mo, enjoy high quotas
  - [5] 2026-10-31: rendered in a browser without a sign-in, the console rate-limits page shows a marketing banner and no limits table | capture: sha256:2f4a0e985d8e7957f535ff8f838089faffcacb38ca2bee9997398f098c475b45 | quote: From only $18/mo, enjoy high quotas
  - [6] 2026-10-31: the docs index names api-reference/rate-limit.md as its Rate Limits page | capture: sha256:9e19db422d2dd97c4448ced0eaf5684421411f27fc2cd5150153dd04cbb31e3c | quote: - [Rate Limits](https://docs.z.ai/api-reference/rate-limit.md)
  - [2] 2026-10-31: a card recharge needs a card that does not go through 3DS verification | capture: sha256:f3989c87449e0bd5cea15b9d15f93995dbf394d5d626f2b14042ff3689e3972b | quote: 3DS verification is not supported in our platform at this moment.
  - [3] 2026-10-31: the quick start names a billing top-up only if needed between registering and creating a key | capture: sha256:65f28d8ef0ff9259d9d83742c66e1e3cd1605459af539d51012cf097bfbcdfa2 | quote: * Access [Billing Page](https://z.ai/manage-apikey/billing) to top up if needed.
  - [1] 2026-10-31: GLM-4.7-Flash is still Free on every column of the pricing table, which prints no rate limit | capture: sha256:4ee3a3e9eab6eab9d8a06309fe6984d82db7351586786bb8422deee1f16f78bf | quote: | GLM-4.7-Flash | Free | Free | Free | Free |
  - [7] 2026-11-03: the Z.ai international sign-in page offers email, GitHub and Google sign-in | capture: sha256:698852f8ed7634b302b495ccb20a6f5758e104745c493fa99df4d0ef5ae7ce4d | quote: ContinuewithEmailContinuewithGithubSkip for now
  - [7] 2026-11-03: the Z.ai international sign-in page offers Continue with Google | capture: sha256:698852f8ed7634b302b495ccb20a6f5758e104745c493fa99df4d0ef5ae7ce4d | quote: ContinuewithGoogle
  - [8] 2026-11-03:  | capture: sha256:c74f07e6ee2970daf741d1e58ed858c93f263065d6a843dbef92072812c8aedd | quote: Account information.** We collect information that you provide when you set up an account, such as your date of birth (where applicable), username (where applicable), email address, and password.
  - [9] 2026-11-03: the Core Parameters page says concurrency quotas differ by user and plan and prints no per-model figure | capture: sha256:2b849c494d4ed9f3cf289c8fb296016e16e493ed75b392eb9384c13f4ff3ccfd | quote: * Limits: Different users or subscription plans may have different concurrency quotas.
  - [10] 2026-11-03: the docs path docs.z.ai/guides/overview/concurrency-limit answers Page Not Found, so no separate concurrency table is published | capture: sha256:8917a3858798b17cf274978889c03b93743f1ff3ed39fa0c6d360444c7b9b854 | quote: The requested page could not be found.
  - [1] 2026-11-03: GLM-4.5-Flash is priced Free on every column of the pricing table | capture: sha256:4ee3a3e9eab6eab9d8a06309fe6984d82db7351586786bb8422deee1f16f78bf | quote: | GLM-4.5-Flash | Free | Free | Free | Free |
  - [11] 2026-11-03: a third-party index reports a free-tier limit of 1 concurrent request for GLM-4.7-Flash; the first-party console figure is behind a sign-up | capture: sha256:389d5fbc5bdf558607ba63e0cc39d41c2cefbe0058b8fb7a75318ce08d039f0a | quote: Rate limit 1 concurrent request provider policy
  - [12] 2026-11-03: a third-party index reports a free-tier limit of 1 concurrent request for GLM-4.5-Flash; the first-party console figure is behind a sign-up | capture: sha256:fd68416c66a5571fc32f8f172c9cc5753e9282e56490d058da84ac861eb07940 | quote: Rate limit 1 concurrent request provider policy
  - [13] 2026-11-03: a third-party proxy log on a coding plan lists GLM-4.5-Flash at 1 observed and 2 configured concurrent requests, not stress-tested, which disagrees with the 1 of the index | capture: sha256:86fcb58decaa0058f670585131da822e8fd02f514e0adabd2a7f1dad7339e6e7 | quote: | `glm-4.5-flash` | OK | 1 (not stress-tested) | - | - | 2 |
  - [14] 2026-11-03: a third-party index reports phone verification for Z.ai, which the first-party sign-in page does not show | capture: sha256:ee07c0ed87256274bd2c8565c872b066b0b7a49d4f455a0e24581526b986be5a | quote: Phone Verification Required
  - [1] 2026-11-03: GLM-4.7-Flash is still priced Free on every column | capture: sha256:4ee3a3e9eab6eab9d8a06309fe6984d82db7351586786bb8422deee1f16f78bf | quote: | GLM-4.7-Flash | Free | Free | Free | Free |
- sources:
  - [1] https://docs.z.ai/guides/overview/pricing
  - [2] https://docs.z.ai/help/faq
  - [3] https://docs.z.ai/guides/overview/quick-start
  - [4] https://docs.z.ai/api-reference/rate-limit.md
  - [5] https://z.ai/manage-apikey/rate-limits
  - [6] https://docs.z.ai/llms.txt
  - [7] https://chat.z.ai/auth
  - [8] https://docs.z.ai/legal-agreement/privacy-policy
  - [9] https://docs.z.ai/guides/overview/concept-param
  - [10] https://docs.z.ai/guides/overview/concurrency-limit
  - [11] https://freellm.net/models/z-ai-zhipu-ai/glm-4-7-flash
  - [12] https://freellm.net/models/z-ai-zhipu-ai/glm-4-5-flash
  - [13] https://richertunes.github.io/ai-proxy/model-concurrency-findings/
  - [14] https://freellm.net/providers/z-ai-zhipu-ai

## Z.ai GLM Coding Plan

- `coding-subs/zai-glm-coding-plan` | paid-only | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T01:56:01.012Z (live) | stale on 2026-12-11
- url https://docs.z.ai/devpack/overview
- price parsed USD 18/mo
- free tier: no free tier; Lite from USD 18 a month | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: usage is metered in credits, and the credit formula is published
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: a paid subscription
- interface: rest, cli
- limits:
  - request-rate (binding): Lite 2,000 five-hour credits and 10,000 weekly; Pro 12,000 and 60,000; Max 28,000 and 140,000 [1]
  - request-rate (binding): credit cost = (input tokens x input multiplier + cached input x cached multiplier + output x output multiplier) / 10,000; GLM-5.3 multipliers are 6.9, 1.7 and 24 [1]
- interface detail: supported in Claude Code, Codex, OpenCode, Cline, ZCode and others
- tooling: any Claude-Code-compatible client, plus the named supported tools
- composes with: the credit formula lets a token budget be converted to a plan, which almost no other plan in this topic allows
- reliability: no reliability event recorded
- notes: Prior reports cited Pro at USD 72 and Max at USD 160, or USD 80 and USD 168. The subscribe page renders tier names without prices. Consequently, specific prices for those tiers are unverified and unlisted.
- evidence note: the credit allowances and the per-model multipliers are quoted from the vendor documents today. Lite is USD 18; the Pro and Max prices were not readable.
- extras:
  - monthly_usd: 18
- evidence:
  - [1] 2026-10-22: Lite from USD 18 a month; 5-hour and weekly credit allowances of 2,000 and 10,000 on Lite, 12,000 and 60,000 on Pro, 28,000 and 140,000 on Max; credit formula with per-model multipliers; 5-hour credits reset five hours after consumption and weekly credits every seven days
  - [2] 2026-10-22: Lite, Pro and Max tiers exist and Pro carries six times Lite usage; the price values did not render in any extraction route
  - [1] 2026-11-10: the page states the plan page states plans from USD 18 a month | capture: sha256:a6ded9e6ec5cf3b95a9fbebc098351ff4a88b2b1274799ef72dae00c646852d8 | quote: Plans from $18/month
- sources:
  - [1] https://docs.z.ai/devpack/overview
  - [2] https://z.ai/subscribe
