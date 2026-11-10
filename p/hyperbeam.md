# Hyperbeam

> hyperbeam.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyperbeam/ | JSON https://fshy.ajam.dev/api/v1/entity/hyperbeam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hyperbeam

- `compute/hyperbeam` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.983Z (live) | stale on 2026-12-07
- url https://hyperbeam.com/
- free tier: 10,000 free minutes every month, then pay as you go; free participant-minutes are counted separately | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: an email address, or a GitHub or Google account: the dashboard sign-up offers 'Continue with Github', 'Continue with Google' or an email address. The API key is issued on request: 'Please contact us via Discord or email for an API key.' No credit card is required: 'No credit card required.' The phone requirement is not published on https://hyperbeam.com/dashboard/. Country: not published on https://hyperbeam.com/dashboard/.
- interface: rest
- limits:
  - request-rate (binding): 10,000 minutes a month on the free tier, renewed monthly [1]
- interface detail: REST API for server-side session management; client SDKs for JavaScript and Unity (WebGL and Desktop)
- tooling: REST API; JavaScript and Unity client SDKs
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a monthly recurring 10,000-minute allowance, which is a tier rather than a trial
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no per-session cap published; the monthly minute allowance is the bound
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Get 10,000 free minutes every month. Only pay for what you use afterwards.' with a 'Free participant-minutes' row, quoted
  - [1] 2026-11-03: pricing is per participant-minute; no egress allowance or overage price per TB is stated | capture: sha256:f259d6619400bda824512da0855b01b084b9fc31f94c6e7d61e1058fb0b14a6e | quote: Get 10,000 free minutes every month. Pay-as-you-go afterwards.
  - [2] 2026-11-03: a REST API creates and manages sessions | capture: sha256:ff4ad5eec64e20da63133656fe0d378aa5711ecf904563a90b347cdf8b74e33d | quote: Create and manage virtual computer sessions server-side.
  - [3] 2026-11-04: an API key is requested from the vendor by email or Discord, not issued by a self-serve console | capture: sha256:8d3edcb34f31f738a21311fb41bfd0bacae8f7bbe55b71172bf30008e6c4c640 | quote: Please contact us via Discord or email for an API key.
  - [1] 2026-11-04: the free allowance needs no credit card | capture: sha256:f259d6619400bda824512da0855b01b084b9fc31f94c6e7d61e1058fb0b14a6e | quote: Get 10,000 free minutes every month. No credit card required.
  - [4] 2026-11-06: the dashboard sign-up offers a GitHub or Google account or an email address | capture: sha256:5a51b7caa53708b9c8b8b1b5a8149c170d8437bc1fc7dafe0480e4018984e135 | quote: Sign Up or Log In ... Continue with Github ... Continue with Google ... Email
  - [1] 2026-11-06: the free allowance needs no credit card | capture: sha256:f259d6619400bda824512da0855b01b084b9fc31f94c6e7d61e1058fb0b14a6e | quote: Get 10,000 free minutes every month. No credit card required.
- sources:
  - [1] https://hyperbeam.com/
  - [2] https://docs.hyperbeam.com/
  - [3] https://docs.hyperbeam.com/rest-api/dispatch/dispatch-overview
  - [4] https://hyperbeam.com/dashboard/
