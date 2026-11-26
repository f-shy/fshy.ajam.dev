# Reflex

> reflex.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reflex/ | JSON https://fshy.ajam.dev/api/v1/entity/reflex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Reflex

- `compute/reflex` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-18T04:58:12.815Z (live) | stale on 2026-12-19
- url https://reflex.dev/pricing/
- free tier: a Free plan at $0 with limited usage for AI generation and hosting that refills periodically; paid tiers from $25 to $200 a month carry an allowance equal to the price | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): limited usage on Free, refilling periodically; the paid tiers carry a dollar allowance equal to their price [1]
  - request-rate (binding): Pro and Enterprise have no session limits; the monthly allowance still applies [1]
- interface detail: Reflex Cloud deploys from the reflex CLI: the dashboard supplies a project-specific `reflex deploy --project...` command, run from the project directory
- tooling: the reflex CLI (`reflex deploy`)
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a Free plan whose usage refills periodically. That is a tier rather than a trial, and the amount is stated only as 'limited'
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session limit on the paid tiers; the free tier's bound is its periodic refill
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| Free | $0 | Limited free usage; refills periodically |' and 'Pro includes a monthly dollar allowance shared by AI generation and app hosting, equal to the selected plan price. Pro and Enterprise have no session limits', quoted
  - [1] 2026-11-04: the pricing URL serves a book-a-demo page with no egress allowance or price | capture: sha256:d72e753c503d105517361e82e4da973e49b83ef0743aa9adc485a36df8b16911 | quote: ## Book a Demo
  - [2] 2026-11-04: Reflex Cloud deploys from a CLI | capture: sha256:cf1b0e63f084e4a4bb7b3ffc8edee0bb0e0f7e808d3d55bcb913e6f56fae4317 | quote: For the CLI workflow, copy the project-specific `reflex deploy --project ...` command.
  - [2] 2026-11-04: Reflex Cloud deploys with the reflex CLI | capture: sha256:cf1b0e63f084e4a4bb7b3ffc8edee0bb0e0f7e808d3d55bcb913e6f56fae4317 | quote: For the CLI workflow, copy the project-specific `reflex deploy --project ...` command.
  - [1] 2026-11-18: not stated | capture: sha256:b93e8314a92c64409ae7bc250999d04b90c46c7f6f650595d75427934c7d753a | quote: # Bring us a problem. Leave with a solution for it.
- sources:
  - [1] https://reflex.dev/pricing/
  - [2] https://reflex.dev/docs/hosting/deploy-quick-start/
