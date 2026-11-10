# OakHost

> oakhost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oakhost/ | JSON https://fshy.ajam.dev/api/v1/entity/oakhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OakHost

- `compute/oakhost` | paid-only | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:31.490Z (live) | stale on 2026-11-22
- url https://www.oakhost.com/mac-mini-hosting
- free tier: no free tier: dedicated Mac mini hosting from €120 a month, with the device assigned after checkout | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): €120 to €340 a month for dedicated Apple hardware [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Mac mini hosting page was read on 2026-10-22 and prices four monthly tiers. There is no free tier or trial, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: dedicated Mac mini hardware; the page prices tiers rather than shapes
  - session_cap.restart_required: no
  - session_cap.note: a dedicated Mac; the machine can be rebooted, powered on and driven into Recovery Mode, so the state belongs to the account
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.price: dedicated storage in the device
  - ps.durability: dedicated disk, FileVault supported
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: managed firewall with filter rules from the control panel
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '€ 120 /mo.', '€ 130 /mo.', '€ 200 /mo.', '€ 340 /mo.' for dedicated Mac mini hosting, with 'assigned to your account within minutes after checkout', quoted
- sources:
  - [1] https://www.oakhost.com/mac-mini-hosting
