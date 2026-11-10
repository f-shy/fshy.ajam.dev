# OpenAI ChatGPT

> chatgpt.com | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chatgpt/ | JSON https://fshy.ajam.dev/api/v1/entity/chatgpt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenAI ChatGPT

- `coding-subs/chatgpt-plans` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:15:03.728Z (live) | stale on 2026-12-05
- url https://chatgpt.com/pricing
- free tier: Free: USD 0; Codex is 'Limited' (GPT-6 Luna at Standard speed in the desktop app, subject to rollout) with no number and no window; unlimited text chats subject to abuse guardrails | unit: mixed | metered on: unstated | read on: 2026-10-22 | source: [1] | note: chatgpt.com/pricing serves the tier names without prices; the Codex pricing page prices the same ladder at USD 0 Free, USD 8 Go, USD 20 Plus and USD 100, 200 or 500 Pro a month
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: an OpenAI account
- interface: cli, rest
- limits:
  - request-rate (binding): Codex is 'Limited' on Free and Go with no number or window (desktop app); 'Yes' on Plus; 'Expanded' on Pro [1]
- limits note: no numeric limit is published on the plan page for any tier no vendor quota binds: the vendor does not serve the usage this record prices
- binding note: the unnumbered Codex allowance on Free and Go binds before anything else; Plus and Pro are 'Yes' and 'Expanded' with no number either
- interface detail: Codex on Free and Go is GPT-6 Luna at Standard speed in the desktop app, subject to rollout; the web, the CLI, the IDE extension and iOS are listed from Plus; an API key runs Codex in the CLI, SDK or IDE extension at API prices
- tooling: ChatGPT web and apps; Codex CLI separately
- composes with: a ChatGPT subscription and Codex quota are separate products on one account
- reliability: no reliability event recorded
- notes: The Codex pricing page prices the plans at USD 0 Free, USD 8 Go, USD 20 Plus and USD 100, 200 or 500 Pro a month; chatgpt.com/pricing lists the tiers without prices. Free carries unlimited text chats subject to abuse guardrails, and Codex is Limited on Free and Go, Yes on Plus and Expanded on Pro, with no number published for any tier. The Codex pricing page gives local-message estimates per five hours for Plus, labelled estimates, not fixed limits.
- evidence note: chatgpt.com/pricing still serves plan names and a feature table without prices; the prices (USD 0, 8, 20, 100, 200, 500) are quoted from the Codex pricing page. That page also publishes per-model local-message estimates per five hours for Plus (GPT-6 Luna 350-3,000, GPT-6 Astra 5-45), labelled estimates, not fixed limits; Free and Go carry a tier label only, with no number.
- evidence:
  - [1] 2026-10-22: Free, Go, Plus and Pro tiers exist as named products; Free is 'unlimited text chats subject to abuse guardrails', which is to say unlimited subject to limits on excess use; no price appears in the served document
  - [1] 2026-10-22: the escalation route returned a challenge page from an automated-traffic filter, so no price could be read
  - [2] 2026-10-30: the Free and Go cards of the Codex pricing page grant Codex in the desktop app only, with one model, subject to rollout | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: GPT-6 Luna at Standard speed in the desktop app, subject to rollout
  - [2] 2026-10-30: the Codex pricing page prices Free at $0, Go at $8, Plus at $20 and Pro at $100, $200 or $500 a month | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: Plans at $100, $200, or $500 USD per month
  - [1] 2026-10-30: the Free tier is still unlimited text chats subject to abuse guardrails | capture: sha256:1072808d6530c5bf4ab627a9a81139689efc1ba16859c4d1020f4c0113c0bcb8 | quote: Unlimited text chats subject to abuse guardrails.
  - [1] 2026-10-30: the ChatGPT plan table lists Codex on Free as Limited | capture: sha256:1072808d6530c5bf4ab627a9a81139689efc1ba16859c4d1020f4c0113c0bcb8 | quote: Plan: Free, Feature: Codex, Limited
  - [2] 2026-10-30: the Plus card of the Codex pricing page lists Codex on the web, in the CLI, in the IDE extension and on iOS; the Pro card adds to everything in Plus | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: Codex on the web, in the CLI, in the IDE extension, and on iOS
  - [2] 2026-10-30: the API Key card of the Codex pricing page runs Codex in the CLI, SDK or IDE extension, paid at API pricing ('Pay for Codex usage based on API pricing') | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: Codex in the CLI, SDK, or IDE extension
  - [1] 2026-10-30: the ChatGPT plan table places Codex on Free on the desktop and lists GPT-5.6 Terra there as limited access, beside GPT-6 Luna (Yes on Free) | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: GPT-5.6 Terra, Limited access in Work and Codex on desktop
  - [1] 2026-11-03: the ChatGPT plan table lists Codex on Free as Limited, with no number | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: Codex, Limited
  - [1] 2026-11-03: Codex on Free is limited, so the unit is not unlimited for coding | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: Codex, Limited
  - [1] 2026-11-03: Codex on Free is Limited with no numeric allowance | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: Codex, Limited
  - [1] 2026-11-03: the Free Codex allowance is limited | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: Codex, Limited
  - [1] 2026-11-03: Codex on Free is Limited | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Plan: Free, Feature: Codex, Limited
  - [2] 2026-11-03: the Codex pricing page prices Free at USD 0; the ChatGPT plan table lists Codex limits by tier | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: $0/month
  - [2] 2026-11-03: the Codex pricing page prices Pro at USD 100, 200 or 500 a month | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: Plans at $100, $200, or $500 USD per month
  - [1] 2026-11-03: the Free card still says unlimited text chats subject to abuse guardrails, beside Codex Limited | capture: sha256:6ba3bb0c1646f193c8e346901a5de938045b0427523c7050e366b95d6134cfad | quote: Unlimited text chats subject to abuse guardrails.
  - [2] 2026-11-04: the Codex pricing page publishes per-model local-message estimates per five hours for Plus, labelled estimates | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: The estimates below show local messages per five-hour period for Plus and Standard Business.
  - [2] 2026-11-04: the Free and Go cards still grant Codex in the desktop app with one model, subject to rollout | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: GPT-6 Luna at Standard speed in the desktop app, subject to rollout
  - [2] 2026-11-04: the Codex pricing page publishes prices for the plan ladder | capture: sha256:d48ce3db646a387bd683d1ba972003bd0e2c67c04fe11d8f00397cce79f527d4 | quote: Plans at $100, $200, or $500 USD per month
- sources:
  - [1] https://chatgpt.com/pricing
  - [2] https://developers.openai.com/codex/pricing
