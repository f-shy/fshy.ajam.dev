# Sail Research

> sailresearch.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sailresearch/ | JSON https://fshy.ajam.dev/api/v1/entity/sailresearch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sail Research (Sailboxes)

- `compute/sail` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:51.763Z (live) | stale on 2026-11-22
- url https://docs.sailresearch.com/pricing
- free tier: no free compute tier: the page prices model inference per million tokens in three service tiers, ASAP, Balanced and Flex, from $0.05 an input MTok | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: per million input and output tokens, from $0.05 an input MTok on the cheapest tier [1]
  - per-ip-shaping: the three tiers trade latency for price: ASAP at $2.50, Balanced at $2.00 and Flex at $1.25 on the same model [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The USD 250 a month is a surcharge floor, not a minimum bill; the metered bill is a separate, lower figure.
- evidence note: the pricing documentation was read on 2026-10-22 and carries per-token model rates in three latency tiers. There is no machine and no free compute allowance on it, so the record's USD 5 credit is not established and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an inference API answers tokens; there is no machine and no session
  - price_note: The USD 250 is a plan floor that this workload never reaches
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - burst_x: 1.4604
  - burst_bill: $0.01 per start
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and is a per-million-token model ladder with three service tiers: 'Kimi K3 Default (ASAP) $2.50 / $0.25 / $12.50', 'Balanced $2.00', 'Flex $1.25', and 'GLM-5.3-Flash from $0.05 to $0.11'
- sources:
  - [1] https://docs.sailresearch.com/pricing
