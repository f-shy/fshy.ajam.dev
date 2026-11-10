# RentaMac

> rentamac.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rentamac/ | JSON https://fshy.ajam.dev/api/v1/entity/rentamac.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RentaMac (rentamac.io)

- `compute/rentamac` | paid-only | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:47.525Z (live) | stale on 2026-11-22
- url https://rentamac.io/pricing
- free tier: no free tier: continuous 24/7 Mac access billed monthly, starting immediately after payment and auto-renewing | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: a monthly term with continuous 24/7 access; no hourly rate and no free tier [1]
  - write-gated (binding): access starts only after payment and auto-renews, so a card is the gate [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states continuous 24/7 access on a monthly term. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: a rented Mac; the page prices the term rather than the shape
  - session_cap.restart_required: no
  - session_cap.note: continuous access with no hour cap and no resource to reap
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.price: included in the monthly term
  - ps.durability: the rented device
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '1 month access. Continuous 24/7 access - not working days or limited hours. Your access starts immediately after payment and auto-renews unless you cancel from the User Portal.' and 'Billed monthly', quoted
- sources:
  - [1] https://rentamac.io/pricing
