# Shiper

> shiper.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shiper/ | JSON https://fshy.ajam.dev/api/v1/entity/shiper.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shiper

- `compute/shiper` | qualifies-with-caveat | evidence documented | binding per-object-cap | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:47.492Z (live) | stale on 2026-12-26
- url https://shiper.app/
- free tier: ## Hobby ... Best for testing, learning, or tiny apps ... ## $0 ... /mo. ... - Automatic Builds and Deployments ... - Included SSL ... - 1 Concurrent Build ... - 1 Self-Hosted Instance ... Included Resources ... - 0.25 vCPU ... - 256 ... ## Builder ... ## $5 ... /mo. ... - Custom Domains ... - Up to 3 Self-Hosted Instances ... - 0.5 vCPU ... - 512 ... ## Scale ... ## $20 ... /mo. ... - 2 vCPU ... - 1500 ... Get the Builder Plan for just $1/month including Custom Domains, Unlimited Projects, and more. Simply join our Discord and share what you're building to claim the offer. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The free plan publishes no bandwidth allowance, so no egress term is recorded; that is a documented absence, not a zero. | metered: no | source: [1]
- identity: email
- interface: rest, git
- limits:
  - per-object-cap (binding): the free plan is one instance at 0.25 vCPU and 256 MB with no custom domains, so the single-instance ceiling binds before any traffic limit. [1]
- limits note: the free plan is one instance at 0.25 vCPU and 256 MB with no custom domains, so the single-instance ceiling binds before any traffic limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free 0.25 vCPU instance that deploys from git covers a small API, and the USD 1 Builder offer cuts the price of adding a custom domain to a third of the list price.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: dalisoft/awesome-hosting says 'Shiper | Builder (5 USD/m) | trial 1 USD | Free yes'. The vendor confirms the free plan, the USD 5 Builder price and the USD 1 promotional price, and adds the plan shapes the aggregator omits. The free plan publishes no bandwidth allowance, so no egress term is recorded; that is a documented absence, not a zero.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.25
  - facets.shape.ram_gib: 0.25
- evidence:
  - [1] 2026-10-22: Hobby plan: 'USD 0 /mo ... 1 Concurrent Build - 1 Self-Hosted Instance ... 0.25 vCPU - 256', quoted
  - [1] 2026-10-22: Builder 'USD 5 /mo ... Custom Domains ... Up to 3 Self-Hosted Instances ... 0.5 vCPU - 512' and Scale 'USD 20 /mo ... 2 vCPU - 1500', quoted
  - [1] 2026-10-22: 'Get the Builder Plan for just USD 1/month including Custom Domains, Unlimited Projects, and more. Simply join our Discord and share what you're building to claim the offer.', quoted
  - [1] 2026-11-25: the pricing section states the free Hobby plan with 0.25 vCPU and 256, the Builder and Scale prices and shapes, and a USD 1 Builder promotional route | capture: sha256:bd7ada40d27a230067c28a444e6e0661ea322092a76a5d1aa9db38b69982aa5f | quote: ## Hobby ... Best for testing, learning, or tiny apps ... ## $0 ... /mo. ... - Automatic Builds and Deployments ... - Included SSL ... - 1 Concurrent Build ... - 1 Self-Hosted Instance ... Included Resources ... - 0.25 vCPU ... - 256 ... ## Builder ... ## $5 ... /mo. ... - Custom Domains ... - Up to 3 Self-Hosted Instances ... - 0.5 vCPU ... - 512 ... ## Scale ... ## $20 ... /mo. ... - 2 vCPU ... - 1500 ... Get the Builder Plan for just $1/month including Custom Domains, Unlimited Projects, and more. Simply join our Discord and share what you're building to claim the offer.
  - [1] 2026-11-25: the pricing section still states the free Hobby plan with 0.25 vCPU and 256, the Builder and Scale prices and shapes, and a USD 1 Builder promotional route | capture: sha256:bd7ada40d27a230067c28a444e6e0661ea322092a76a5d1aa9db38b69982aa5f | quote: ## Hobby ... Best for testing, learning, or tiny apps ... ## $0 ... /mo. ... - Automatic Builds and Deployments ... - Included SSL ... - 1 Concurrent Build ... - 1 Self-Hosted Instance ... Included Resources ... - 0.25 vCPU ... - 256 ... ## Builder ... ## $5 ... /mo. ... - Custom Domains ... - Up to 3 Self-Hosted Instances ... - 0.5 vCPU ... - 512 ... ## Scale ... ## $20 ... /mo. ... - 2 vCPU ... - 1500 ... Get the Builder Plan for just $1/month including Custom Domains, Unlimited Projects, and more. Simply join our Discord and share what you're building to claim the offer.
- sources:
  - [1] https://shiper.app/
