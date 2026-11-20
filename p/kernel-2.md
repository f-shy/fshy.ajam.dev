# Kernel

> kernel.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kernel-2/ | JSON https://fshy.ajam.dev/api/v1/entity/kernel-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kernel

- `compute/kernel` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.kernel.sh/pricing
- price parsed USD 30/mo
- free tier: free: USD 0 a month plus usage, USD 5 of free credits a month, 5 concurrent browsers, unmarked mode, 3 managed auth connections | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: 'You can sign up without a credit card' is stated in the page FAQ
- per-object cap: not applicable
- retention: session replays are kept 1 day on free, 7 days on hobbyist and 30 days on start-up | days: 1
- egress: usage is USD 0.0000166667 per GB-second with no charge for idle time or proxies | metered: yes | free allowance: within USD 5 of credit | source: [1]
- identity: email | detail: 'You can sign up without a credit card and get started right away', quoted
- interface: rest, cli
- limits:
  - per-object-cap: USD 5 of credit a month on free; 5 concurrent browsers [1]
  - retention-clamped: session replays kept 1 day on free [1]
- limits note: hobbyist is USD 30 a month with USD 10 of credit and unlimited proxy use
- binding note: USD 5 of monthly credit at a GB-second rate is spent by page weight, so the credit is the allowance and page size decides how fast
- interface detail: REST API and SDKs; a browser session with live view
- tooling: Kernel SDK and REST; Playwright over CDP; live view of a session
- composes with: GB-second billing with no idle charge makes a held session cheap when it is doing nothing
- reliability: no reliability event recorded
- notes: USD 5 a month recurring, no card, and unmarked mode included on the free plan. The GB-second unit makes the cost depend on page weight rather than time, which is unusual in this class.
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: no idle charge
  - keep_rate.value: 0.0
  - keep_rate.basis: no charges for idle time
  - keep_rate.source: https://www.kernel.sh/pricing
  - persistent_storage.durability: replays kept 1 day
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 1 day
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP
  - free_tier_kind: recurring-credit
  - m10h_usd: 30.0
  - m24h_usd: 30.0
  - price_note: Hobbyist at USD 30 a month includes USD 10 of credit and unlimited proxy; usage is USD 0.0000166667 per GB-second, so a 300-hour run depends on page weight and not on time.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: free: USD 5 of credits a month, 5 concurrent browsers, session replays 1 day, 3 managed auth connections
  - [1] 2026-10-22: usage is USD 0.0000166667 per GB-second with no charges for idle time or proxies
- sources:
  - [1] https://www.kernel.sh/pricing
