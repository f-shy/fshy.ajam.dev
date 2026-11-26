# Hostinger VPS

> hostinger.com | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostinger/ | JSON https://fshy.ajam.dev/api/v1/entity/hostinger.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostinger Router

- `inference/hostinger-router` | paid-only | evidence documented | binding write-gated | category inference gateway, credit-based
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://www.hostinger.com/ai-router
- free tier: No free allowance: AI Router starts at USD 5.99 for 5 credits, and credits are metered per request / charged per token. | unit: credits | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a Hostinger account and a purchase of credits; the page offers no free credit grant
- interface: rest
- limits:
  - write-gated (binding): USD 5.99 for 5 credits; usage billed from a purchased credit balance [1]
- endpoint: https://router.hostinger.com/v1
- tooling: OpenAI-compatible and Anthropic-compatible clients; one API key for all models
- composes with: the paid credit balance is the scarce link, with no free tier to bridge a workload
- reliability: credits are consumed per request and per token; no free allowance is stated
- notes: Pricing explicitly starts at USD 5.99 for 5 credits; no free-credit grant is offered.
- evidence:
  - [1] 2026-11-18: the router starts at USD 5.99 for 5 credits | capture: sha256:4b3fbe34a8e6bd04e01d80f12cba3d04e55501c4663457004ccc9841616dba24 | quote: Starting at $5.99 • 5 credits
  - [1] 2026-11-18: billing is metered per request / pay only for what you use | capture: sha256:4b3fbe34a8e6bd04e01d80f12cba3d04e55501c4663457004ccc9841616dba24 | quote: Pay only for what you use
- sources:
  - [1] https://www.hostinger.com/ai-router

## Hostinger VPS

- `compute/hostinger-vps` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:50.406Z (live) | stale on 2026-12-26
- url https://www.hostinger.com/vps-hosting
- price parsed USD 14.99/mo
- free tier: Today you pay $155.76 for 24 months. Renews at $11.99/mo for the same term. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $6.49 a month on a two-year term, renewing at $11.99; the entry shape is 1 vCPU and 50 GB of NVMe [1]
  - per-ip-shaping: 4 TB of bandwidth on the entry plan [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: KVM 1: 1 vCPU core, 4 GB RAM, 50 GB NVMe disk space, 4 TB bandwidth, $6.49/mo after the Black Friday discount from $19.49/mo; 30-day money-back guarantee. No free VPS plan appears on the page.
- evidence note: the VPS page was read on 2026-10-22 and prices the ladder with its renewal rates. There is no free tier and no trial credit, only a 30-day money-back guarantee
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - shape.vcpu: 1
  - shape.disk: 50
  - shape.note: the entry plan: 1 vCPU, 50 GB of NVMe, 4 TB of bandwidth
  - session_cap.restart_required: no
  - session_cap.note: a monthly VPS with root access; no session clock
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 10.06
  - m24h_usd: 14.99
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - granularity.min_billed_s: 3600
  - burst_x: 1.0
  - burst_bill: min 1 h
  - ps.gib: 50
  - ps.price: included in the monthly price
  - ps.durability: NVMe
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.ipv6: yes
  - net.allowance: 4 TB a month on the entry plan
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'From $6.49/mo' with 'Renews at $11.99/mo for 2 years', '1 vCPU core', '50 GB NVMe disk space', '4 TB bandwidth', and '30-day money-back guarantee', quoted
  - [1] 2026-11-25: the entry KVM 1 plan states its upfront 24-month payment and renewal rate | capture: sha256:e838568e9d0fb80e81fd277ccbac5e661bf00d2a0cf5bc2ad1bd915e3cd1bd49 | quote: Today you pay $155.76 for 24 months. Renews at $11.99/mo for the same term.
  - [1] 2026-11-25: the page was read on 2026-11-25 and still states this VPS price | capture: sha256:e838568e9d0fb80e81fd277ccbac5e661bf00d2a0cf5bc2ad1bd915e3cd1bd49 | quote: Today you pay $155.76 for 24 months. Renews at $11.99/mo for the same term.
  - [1] 2026-11-25: the reading of the entry plan price on 2026-11-25 | capture: sha256:e838568e9d0fb80e81fd277ccbac5e661bf00d2a0cf5bc2ad1bd915e3cd1bd49 | quote: Today you pay $155.76 for 24 months. Renews at $11.99/mo for the same term.
- sources:
  - [1] https://www.hostinger.com/vps-hosting
