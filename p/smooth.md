# Smooth

> smooth.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smooth/ | JSON https://fshy.ajam.dev/api/v1/entity/smooth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Smooth

- `compute/smooth` | qualifies-with-caveat | evidence documented | binding write-gated | category browser host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.984Z (live) | stale on 2026-12-07
- url https://www.smooth.sh/pricing
- free tier: a free tier with basic features and limited usage; the first paid tier includes $50 of credits and 10 concurrent browsers, so the page does not price the free tier's own allowance | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: an email address, or a Google or GitHub account: the dashboard sign-in lists an email provider beside Google and GitHub. The free key needs no card: 'sign up to get a free key, no credit card required', and the docs state 'Unlock your free welcome credits. No credit card required.' The phone requirement is not published on https://app.smooth.sh/api/auth/providers. Country: not published on https://app.smooth.sh/api/auth/providers.
- interface: rest, cli
- limits:
  - write-gated (binding): the free tier's allowance is stated only as 'limited usage'; the first priced tier carries $50 of credits and 10 concurrent browsers [1]
- interface detail: REST API with an API reference and an OpenAPI spec, Python and TypeScript SDKs, and a Smooth CLI, per the vendor docs
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and its table prices the paid tiers while describing the free one as 'basic features, limited usage'. The USD 5 the record carried is not on the page, so no figure is asserted
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: persistent sessions are offered on every tier; the page states no cap
  - free_tier_kind: allowance
  - ps.price: not stated
  - ps.durability: persistent session
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: not stated
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| credits included | $50 | $500 | unlimited |' with '| concurrent browsers | 10 | 50 | unlimited |', '| persistent sessions | ✓ | ✓ | ✓ |', and a free tier described as 'basic features, limited usage', quoted
  - [2] 2026-11-04: the docs describe a REST API | capture: sha256:6e5dac70d18032fc7196f038d14ea326a49ac4093a6e6424e5d249ed5eba4467 | quote: Complete guide to the Smooth REST API
  - [3] 2026-11-04: the docs index lists a Smooth CLI | capture: sha256:042f50eb254e2011760f28de84e63a3f01fa0ad6b233c5bc2ba8d4f119d63a79 | quote: Setup Smooth CLI for any agent
  - [4] 2026-11-04: the docs name Python and TypeScript SDKs | capture: sha256:07ad39112a3109fb8a9750572e56ca99038383f5e2568d860831af72ef0f852f | quote: Smooth has both a Python and a Typescript SDK.
  - [5] 2026-11-04: a free API key for an account needs no credit card | capture: sha256:07ad39112a3109fb8a9750572e56ca99038383f5e2568d860831af72ef0f852f | quote: Unlock your free welcome credits. No credit card required.
  - [6] 2026-11-06: the dashboard sign-in offers an email provider beside Google and GitHub | capture: sha256:2ae423831ea8b8bc05c4995ded7f2a0a064d61b393bce1129558d72fa77558d8 | quote: {"email":{"id":"email","name":"Email","type":"email","signinUrl":"https://app.smooth.sh/api/auth/signin/email"
  - [7] 2026-11-06: a free key needs no credit card | capture: sha256:2c6224ccaec03359e3b0276f95e9abc8d9cae1d08fceb330c145fd53dda921f0 | quote: sign up to get a free key, no credit card required
- sources:
  - [1] https://www.smooth.sh/pricing
  - [2] https://docs.smooth.sh/api-reference/introduction.md
  - [3] https://docs.smooth.sh/llms.txt
  - [4] https://docs.smooth.sh/quickstart.md
  - [5] https://docs.smooth.sh/quickstart
  - [6] https://app.smooth.sh/api/auth/providers
  - [7] https://www.smooth.sh/
