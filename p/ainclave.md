# ainclave

> ainclave.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ainclave/ | JSON https://fshy.ajam.dev/api/v1/entity/ainclave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ainclave

- `compute/ainclave` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:06.316Z (live) | stale on 2026-11-22
- url https://www.ainclave.com/pricing
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: billing is the wall clock from a session becoming ready to its stopping; idle time inside a running session is billed as if busy [1]
  - write-gated (binding): there is no self-serve price: access is through a design-partner programme that issues a written rate card [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: No price is published at all: the vendor has not fixed its rates and sells through a design-partner programme. That is why the record is paid-only on an absence, and the absence is now a quoted sentence rather than an unread card.
- evidence note: the pricing page was read on 2026-10-22. It states that no rate card exists yet and describes the billing model precisely: wall-clock from ready to stop, with no busy-versus-idle…
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 'We do not bound how long a session may run'; the caps are user-set and can be switched off, and an idle timeout is the one automatic bound
  - free_tier_kind: none
  - reclassified_from: dead
  - net.out: no
  - net.in: yes
  - net.ports: deny by default on the host datapath
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Rates are not published yet. We have not fixed the numbers, so there are none on this page. Design partners get the rate card as it is set, in writing, before anything is billed.' and 'Billing tracks the wall-clock time between a session becoming ready and it stopping. We do not meter busy time against idle time inside a running session' and 'An idle timeout bounds that' and 'Deny-default egress on the host datapath', quoted
- sources:
  - [1] https://www.ainclave.com/pricing
