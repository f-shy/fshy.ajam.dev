# Umans AI

> umans.ai | Inference, Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/umans/ | JSON https://fshy.ajam.dev/api/v1/entity/umans.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Umans AI

- `inference/umans-ai` | paid-only | evidence documented | binding volume-quota | category coding-agent inference, team/credit based
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://app.umans.ai/offers/code/docs/orgs
- free tier: no self-serve free tier: an organization is created only after emailing contact@umans.ai, and credits are bought by adding a card in the Wallet; each member gets a key and an optional monthly limit | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the organization is created by emailing contact@umans.ai and credits are bought by adding a card in Wallet; no self-serve free signup is documented
- interface: rest
- limits:
  - volume-quota (binding): optional per-member monthly limits; pay-per-token draws from a shared organization balance [1]
- binding note: no free allowance, so a card-funded balance binds first
- endpoint: https://api.code.umans.ai/v1
- tooling: the umans CLI (umans claude) and an OpenAI-compatible key at api.code.umans.ai/v1
- composes with: pairs with coding agents through a team key; the scarce link is the email-to-provision organization and a card-funded balance
- reliability: no reliability event recorded
- notes: org provisioning needs a human email exchange and a card; no free inference offer appears on the page.
- evidence:
  - [1] 2026-11-18: an organization is provisioned by emailing the vendor | capture: sha256:e27dbb318d79da5f44e6882bc0752c4b3e809dd409f57cb761c8964acf11bd0a | quote: Email [contact@umans.ai](mailto:contact@umans.ai) with the email of your first admin. We create the organization and invite them.
  - [1] 2026-11-18: credits are bought by adding a card in Wallet | capture: sha256:e27dbb318d79da5f44e6882bc0752c4b3e809dd409f57cb761c8964acf11bd0a | quote: In Wallet, add a card and buy credits. Every key of the organization draws from this one balance.
- sources:
  - [1] https://app.umans.ai/offers/code/docs/orgs

## Umans AI Coding Plan

- `coding-subs/umans-ai-coding-plan` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://app.umans.ai/offers/code/docs
- free tier: No free tier. The page says to add credit and pay only for what is used, pricing Kimi-K3.1-Pro at USD 2.00 per 1M input and USD 10.00 per 1M output tokens. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: usage is prepaid by adding credit before a key is issued
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit billed per token, USD 2.00 per 1M input and USD 10.00 per 1M output on the flagship model [1]
- endpoint: https://api.code.umans.ai/v1
- tooling: the umans CLI, which authenticates through a browser, plus an OpenAI-compatible key
- composes with: prepaid credit is the scarce link, since no allowance is granted at signup
- reliability: the CLI opens a browser on first run, so an unattended host needs the key path instead
- evidence:
  - [1] 2026-11-18: the plan is prepaid per token with Kimi-K3.1-Pro at USD 2.00 per 1M input and USD 10.00 per 1M output and no free allowance | capture: sha256:2a19cf671e98dadf33f693cf054de643373afbc0069c14c6769e079bd00cac78 | quote: Run Claude Code, Cursor, Zed, Copilot, OpenCode, Kilo Code, Pi, and more with one API key. Pay only for what you use. Add credit, create a key, and start coding. Currently serving DeepSeek V4.1 Flash, Kimi K3.1 Pro, and GLM 5.3.
  - [1] 2026-11-18: the flat-rate plans were retired and the current product is pay-per-token | capture: sha256:2a19cf671e98dadf33f693cf054de643373afbc0069c14c6769e079bd00cac78 | quote: Flat-rate subscription plans were retired on August 1, 2026
  - [1] 2026-11-18: the service is pay-per-token from a prepaid wallet | capture: sha256:2a19cf671e98dadf33f693cf054de643373afbc0069c14c6769e079bd00cac78 | quote: Umans Code is pay-per-token.
- sources:
  - [1] https://app.umans.ai/offers/code/docs
