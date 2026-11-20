# Isorun

> boxyard.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxyard/ | JSON https://fshy.ajam.dev/api/v1/entity/boxyard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Isorun

- `compute/isorun` | paid-only | evidence reported | binding volume-quota | category container and VM sandbox | tier default sandbox, 1 vCPU / 1 GiB
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T02:11:00.000Z (live) | stale on 2026-11-08
- url https://boxyard.dev/providers/isorun
- price parsed USD 29.2/mo
- free tier: USD 50 credit for new accounts (aggregator); the vendor's own pricing page did not render for a text read. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit
- per-object cap: the ladder runs past 1 vCPU; the per-shape ceiling was not readable first party
- retention: not established first party; the vendor advertises hibernate/resume ('Pause to disk and restore exactly where you left off') | source: [2]
- egress: No egress price and no transfer allowance are published on the page read; metered is recorded as false because nothing is known to be charged per gigabyte, which is an absence of evidence, not a promise of free traffic. | metered: no | free allowance: not stated | source: [2]
- identity: card | detail: A USD 50 credit is advertised; the card, hold and debit terms were not readable because the vendor pricing page did not render for a text read. Unverified.
- interface: unknown
- limits:
  - volume-quota (binding): rate USD 0.025/vCPU-hour and USD 0.015/GiB-hour; no egress terms published on the pages read [1]
- binding note: The hourly rate is the wall: USD 0.04/hour for the smallest sandbox is USD 29.20 a month, six times the budget.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: 1 vCPU / 1 GiB = 0.025 + 0.015 = USD 0.040/hour, which is exactly the vendor's own headline 'billed per second at $0.04/hr', so the two sources agree arithmetically even though only one of them is first party. At 730 h: USD 29.20. What would raise the confidence: a rendered pricing page, which also carries the shape ladder and the session cap.
- evidence note: The rates come from a third-party aggregator (boxyard.dev) that cites the vendor's own docs URL, and are consistent with the vendor homepage's meta description ('billed per second at $0.04/hr'). The vendor's pricing page returned a JavaScript stub on three routes (docs.isorun.ai/getting-started/pricing, its .md variant, isorun.ai/pricing), so no first-party quote of the rate exists.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - session_cap.restart_required: no
  - session_cap.note: hibernate/resume advertised; no cap readable first party
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: HTTP(S) and WebSockets through a public URL per exposed port; raw TCP/UDP ingress not stated
  - network_out.static_ip: no
  - free_tier_kind: credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: not stated on this page
  - ps.durability: hibernation preserves the sandbox
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until destroyed
  - term: prepaid, no commitment
  - m10h_usd: 12.0
  - m24h_usd: 29.2
  - price_arithmetic: 1 x 0.025 + 1 x 0.015 = USD 0.04/hour x 730 = USD 29.20 at 24/7; x 300 (10 h/day) = USD 12.00.
- evidence:
  - [3] 2026-10-02: 
  - [3] 2026-10-22: 'Every new account gets $50 in free credit, about 1,250 hours of a default sandbox. No card required to start.' with 'vCPU $0.025/hour', 'RAM $0.015/GiB/hour' and 'Hibernated sandboxes: not billed for active runtime; you pay nothing while the sandbox is paused', quoted
  - [1] 2026-10-24: quoted: 'It costs $0.025 per vCPU-hour and $0.015 per GiB-hour, billed per second. New accounts get a $50 credit.' (aggregator relaying the vendor's docs)
  - [2] 2026-10-24: quoted: 'Each sandbox boots its own guest kernel, sharing nothing with its neighbours.' and, from the page's own description, 'billed per second at $0.04/hr'
- sources:
  - [1] https://boxyard.dev/providers/isorun
  - [2] https://isorun.ai/
  - [3] https://docs.isorun.ai/getting-started/pricing
