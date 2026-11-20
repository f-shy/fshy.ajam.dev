# Surfsky

> surfsky.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/surfsky/ | JSON https://fshy.ajam.dev/api/v1/entity/surfsky.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Surfsky

- `compute/surfsky` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:39.481Z (live) | stale on 2026-12-05
- url https://surfsky.io/pricing
- free tier: free credit at signup with no card, 10 concurrent browsers, and browser hours at $0.35 with premium proxy traffic at $10 a GB | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Paid plans include shared proxy traffic each month: 5 GB on Starter, 15 GB on Base, 50 GB on Advanced; premium proxy traffic is billed per GB from the usage credit. No shared-traffic allowance is stated for the free tier. | metered: no | source: [1]
- identity: email | detail: 'Get free credit when you sign up. No card needed.', quoted from surfsky.io/pricing read 2026-10-22
- interface: unknown
- limits:
  - request-rate (binding): 10 concurrent browsers on the free tier, 15 and 50 on the paid ones [1]
  - per-ip-shaping: premium proxy traffic is $10 a GB on the free tier, $9 and $8 on the paid ones [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the signup credit and the free tier's concurrency and rates. The credit's size is not published, so the record does not put a number on it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 10 concurrent browsers; the page states no session clock
  - free_tier_kind: allowance
  - burst_x: 1.0
  - ps.price: persistent profiles are a plan row
  - ps.durability: persistent profile
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the profile exists
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: $10 a GB of premium proxy on free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Get free credit when you sign up. No card needed.' and 'The monthly fee turns into usage credit' with the free tier's '10 concurrent browsers', '$0.35 / browser hour' and '$10 / GB premium proxy', against 'Up to 90 browser hours of credit' on the $29 tier, quoted
  - [1] 2026-11-03: paid plans carry 5, 15 and 50 GB of shared traffic a month | capture: sha256:5f29afc9d6e32c62433598dc8244111becc3bc85cbec94b357c95f1dfc0f0c35 | quote: Every paid plan includes shared traffic each month: 5 GB on Starter, 15 GB on Base, 50 GB on Advanced.
  - [1] 2026-11-03: egress terms re-read | capture: sha256:5f29afc9d6e32c62433598dc8244111becc3bc85cbec94b357c95f1dfc0f0c35 | quote: Every paid plan includes shared traffic each month: 5 GB on Starter, 15 GB on Base, 50 GB on Advanced.
- sources:
  - [1] https://surfsky.io/pricing
