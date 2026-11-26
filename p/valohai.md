# Valohai

> valohai.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/valohai/ | JSON https://fshy.ajam.dev/api/v1/entity/valohai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Valohai

- `compute/valohai` | paid-only | evidence documented | binding none | category notebook runtime | tier Pro and Enterprise only
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T10:24:24.851Z (live) | stale on 2026-12-04
- url https://valohai.com/pricing/
- free tier: no free tier: 'Valohai offers straightforward, predictable pricing ... you pay per user license, not the scale of work you do on the platform' | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: Two tiers, Pro and Enterprise, both per-seat. No free plan and no published price; a 14-day trial with access to all features is offered, and what the trial sign-up asks for is unverified: behind a sign-up.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not applicable: no free allowance | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a per-seat licence is required; the pricing page publishes no self-serve free plan
- interface: cli, rest, git
- limits:
  - volume-quota: 0 hours: no free tier [1]
- binding note: there is no free allowance to exhaust
- interface detail: a pipeline tool driven by valohai-cli and Git
- tooling: part of interface detail
- composes with: an MLOps pipeline runner sold per seat; no free lane
- reliability: no reliability event recorded
- notes: No price is published, which is itself the finding: this cannot be compared to anything without a sales call.
- evidence note: the per-seat model and the two tiers are quoted from the pricing page today. No price is stated, so none is recorded.
- extras:
  - billing_model: subscription
  - term: per seat
  - price_arithmetic: not published
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: not applicable
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: 'Valohai offers straightforward, predictable pricing to help you concentrate on innovation rather than expenses. With Valohai, you pay per user license, not the scale of work you do on the platform'
  - [1] 2026-10-24: quoted from the page description: 'Valohai is available at two pricing tiers: Pro and Enterprise.'
  - [1] 2026-11-03: pricing is a per-user licence and the page lists no free plan or GPU allowance | capture: sha256:e3ab208ebd40ff7824371d5bc7eafe908225cbdbb318b15de30b8c1d6911fa62 | quote: With Valohai, you pay per user license, not the scale of work you do on the platform
  - [1] 2026-11-03: a 14-day free trial exists; the FAQ answer adds that the trial has access to all features | capture: sha256:e3ab208ebd40ff7824371d5bc7eafe908225cbdbb318b15de30b8c1d6911fa62 | quote: Yes, you can try Valohai for free with our 14-day trial.
  - [1] 2026-11-03: the page's meta description names two pricing tiers, Pro and Enterprise | capture: sha256:36ff87d608471d52d8b4167ef66910374c2e79a1fe53eed42a48f1c95b316a3f | quote: Valohai is available at two pricing tiers: Pro and Enterprise.
  - [1] 2026-11-03: the 14-day trial gives access to all features | capture: sha256:e3ab208ebd40ff7824371d5bc7eafe908225cbdbb318b15de30b8c1d6911fa62 | quote: During the trial period, you will have access to all Valohai features and capabilities.
- sources:
  - [1] https://valohai.com/pricing/
