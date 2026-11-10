# Comfy Deploy

> comfydeploy.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/comfydeploy/ | JSON https://fshy.ajam.dev/api/v1/entity/comfydeploy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Comfy Deploy

- `compute/comfy-deploy` | qualifies-with-caveat | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-02T02:17:25.932Z (live) | stale on 2026-12-03
- url https://app.comfydeploy.com/pricing
- free tier: a free starting tier priced as credits; GPU time bills per second from $0.6480 an hour for a T4 to $1.2132 an hour for an A10G | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: any-phone | detail: The signup form asks for a first name, a last name, an optional username, an email address and a phone number with a country selector, or Google sign-in. Only the username is marked Optional; the phone is not, so a phone number is required. No card field is on the form, and no country limit is stated beyond the country selector.
- interface: unknown
- limits:
  - request-rate (binding): GPU time bills per second from $0.6480 an hour for a T4 to $6.1488 an hour for an A100 80 GB [1]
  - request-rate (binding): GPU concurrency is the plan's limit; the page lists it as a plan row [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the full GPU ladder at per-second billing. It states no free credit amount, so the record's free tier is recorded as a free starting tier without a published size
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: T4
  - shape.gpu_count: 1
  - shape.note: the ladder runs T4, L4, A10G, L40S, A100 and A100 80GB
  - session_cap.restart_required: no
  - session_cap.note: per-second GPU billing; the page states no session clock
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free, scale as you grow' with per-second and per-hour GPU rates: 'T4 $0.6480/hour', 'L4 $1.1520/hour', 'A10G $1.2132/hour', quoted
  - [1] 2026-10-22: 'Transparent, usage-based pricing for all GPU types' with T4 at $0.6480 an hour, L4 at $1.1520, A10G at $1.2132, L40S at $2.1456, A100 at $4.1040 and A100 80GB at $6.1488, quoted
  - [2] 2026-11-02: the signup form has a Phone number field with a country selector, and only the username is marked optional | capture: sha256:a209ab0ad68f016bfe948d1773517aef057343e093fb111711f7f6cb3fd59a57 | quote: First name First name Last name Last name Username Optional Email address Enter your email address Phone number [country code selector, redacted] Continue
  - [2] 2026-11-02: the form's fields are first and last name, an optional username, an email address and a phone number, with no card field | capture: sha256:a209ab0ad68f016bfe948d1773517aef057343e093fb111711f7f6cb3fd59a57 | quote: First name First name Last name Last name Username Optional Email address Enter your email address Phone number [country code selector, redacted] Continue
  - probe:https://app.comfydeploy.com/signup 2026-11-02: the served HTML of the signup route is a 708-byte app shell, so the form itself is rendered client-side | capture: sha256:01dd29fbb468a89d7c75aa9c33a51b1a6d4a864279256debebdf0a2a6c6cf73e | quote: "status": 200
  - [2] 2026-11-02: the signup form carries a phone number field that is not marked optional | capture: sha256:a209ab0ad68f016bfe948d1773517aef057343e093fb111711f7f6cb3fd59a57 | quote: Phone number
- sources:
  - [1] https://app.comfydeploy.com/pricing
  - [2] https://app.comfydeploy.com/auth/sign-up
