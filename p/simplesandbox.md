# SimpleSandbox

> simplesandbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simplesandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/simplesandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SimpleSandbox

- `compute/simplesandbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category container sandbox / code execution API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:35.593Z (live) | stale on 2026-12-05
- url https://www.simplesandbox.dev/
- free tier: Free $0: 1M credits a month, 3 concurrent sandboxes, no credit card required. 1M credits = USD 1, and the meter is billed per second at USD 0.0252 per vCPU-hour. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: a monthly credit allowance equal to USD 1 of CPU time
- per-object cap: not applicable: the unit is a sandbox, not an object; no memory or disk allocation is published per sandbox
- retention: The sandbox advertises 'No duration limits'. Persistent volumes are 1-100 GB, one per sandbox, single attachment, 'currently free only during beta' with future pricing unpublished. | source: [2]
- egress: No network fees: the pricing docs state billing is per-millisecond for compute and memory with no network fees; no traffic allowance is stated. | metered: no | source: [1]
- identity: email | detail: 'No credit card required' on the Free plan, with a free API key issued at app.simplesandbox.dev. Card types for paid plans and any authorisation hold are not stated on the page read.
- interface: rest, cli
- limits:
  - volume-quota (binding): 1M credits a month on the free tier (USD 1 of usage); 10M on the USD 10 plan; 50M on the USD 50 plan [1]
  - request-rate: 3 concurrent sandboxes on free, 10 on the USD 10 plan, 1,000+ on Pro [1]
- limits note: 'No duration limits' and '~1s cold start' are the advertised shape. Auto top-up adds 1M credits (USD 1) when the balance runs low, which quietly converts a free tier into a paid one.
- binding note: USD 1 of CPU credit is spent in about 39 vCPU-hours at the published rate, so an always-on 1 vCPU sandbox exhausts the free month in under two days.
- interface detail: TypeScript/Node SDK ('import { Sandbox } from '@simplesandbox/sdk')') and a REST API, with a free API key issued from the app.
- tooling: The vendor SDK; the sandboxes run on Fly.io infrastructure under the vendor's own isolation.
- composes with: A genuinely free, no-card code-execution endpoint with a USD 1 monthly credit is useful as a fallback executor but not as a machine: 1M credits buys about 39 vCPU-hours of CPU time and the memory meter is not published, so it cannot be sized as an always-on box.
- reliability: no reliability event observed; the platform is a thin layer over Fly.io Machines, so its availability follows a third party's.
- notes: Arithmetic from the published CPU rate alone: 1 vCPU × 730 h × USD 0.0252 = USD 18.396 a month of CPU time, before any memory charge, which the page does not publish. That number is deliberately not promoted to m24h_usd because a record cannot claim a 24/7 total from one of two meters. The free allowance is USD 1, which is 39.7 vCPU-hours. Region and egress are unverified.
- evidence note: The credit price, the CPU rate, the plan prices, the concurrency caps and the no-card claim are quoted from the vendor's homepage read. The memory meter and the disk rate are not published, so no 24/7 total for a shape is recorded: the vCPU figure alone would understate the bill. What would raise it: the docs' billing page, or an account that reads the meter.
- extras:
  - billing_model: hourly
  - term: monthly credit plans plus per-second metering
  - price_arithmetic: CPU only: USD 0.0252/vCPU-hour × 730 h = USD 18.396 a month for 1 vCPU of CPU time. The memory meter is not published, so no complete 24/7 total is computed or claimed.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.ports: not published
  - session_cap.restart_required: no
  - session_cap.note: 'No duration limits' advertised
  - aggregator_note: sandboxprices.com carries SimpleSandbox in the picker with no modelled total; its note says the complete CPU/RAM shape tariff is unresolved, which matches what the vendor homepage shows today.
- evidence:
  - [1] 2026-10-24: quoted: 'Start free, upgrade to $10/mo (10 concurrent) or $50/mo (1,000+ concurrent)' and 'Per-second billing at $0.0252/vCPU-hour'
  - [1] 2026-10-24: free tier: 'Free $0 - 1M credits/month - No credit card required' and '1M credits = $1. Pay only for what you use, billed per-second'
  - [1] 2026-10-24: quoted: '~1s cold start', 'No duration limits', '1,000+ concurrent sandboxes'
  - [3] 2026-11-04: the docs state no network fees are charged | capture: sha256:8873b13d44800730139826634730b941d0ce52870257380bde2085419d405a19 | quote: Understand per-millisecond billing for compute and memory. No network fees.
  - [3] 2026-11-04: the lifecycle is controlled through an SDK or CLI | capture: sha256:8873b13d44800730139826634730b941d0ce52870257380bde2085419d405a19 | quote: Create, execute, refresh, and retire environments through the SDK or CLI.
- sources:
  - [1] https://www.simplesandbox.dev/
  - [2] https://docs.simplesandbox.dev/persistence
  - [3] https://docs.simplesandbox.dev/
