# Isorun

> isorun.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/isorun/ | JSON https://fshy.ajam.dev/api/v1/entity/isorun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Isorun

- `compute/isorun` | trial-only | evidence documented | binding volume-quota | category container and VM sandbox | tier default sandbox, 1 vCPU / 1 GiB
- needs card unknown, phone no, ID no, institution no | verified 2026-11-25T15:03:54.716Z (live) | stale on 2026-12-26
- url https://docs.isorun.ai/getting-started/pricing
- price parsed USD 29.2/mo
- free tier: Every new account gets $50 in free credit, about 1,250 hours of a default sandbox. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit
- per-object cap: the ladder runs past 1 vCPU; the per-shape ceiling was not readable first party
- retention: not established first party; the vendor advertises hibernate/resume ('Pause to disk and restore exactly where you left off') | source: [2]
- egress: No egress price and no transfer allowance are published on the page read; metered is recorded as false because nothing is known to be charged per gigabyte, which is an absence of evidence, not a promise of free traffic. | metered: no | free allowance: not stated | source: [2]
- identity: email | detail: An account is created at the dashboard https://app.isorun.ai and creates an organization in the US or EU region; an API key is bound to that organization. "No card required to start." unverified: the signup form's exact fields could not be read on 2026-11-24.
- interface: unknown
- limits:
  - volume-quota (binding): USD 0.025 per vCPU-hour and USD 0.015 per GiB-hour, billed per second, with no minimum; USD 0.040/hour for 1 vCPU and 1 GiB [1]
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
  - [3] 2026-11-25: the vendor's pricing page states a USD 50 credit for new accounts and its hour estimate | capture: sha256:57cbec95b2abb99fc1f7f52bee124a6e779f57c47c5740e5747e04afa67f9bd0 | quote: Every new account gets $50 in free credit, about 1,250 hours of a default sandbox.
  - [3] 2026-11-24: the vendor's pricing page states the credit, its hour estimate and that no card is required | capture: sha256:57cbec95b2abb99fc1f7f52bee124a6e779f57c47c5740e5747e04afa67f9bd0 | quote: Every new account gets $50 in free credit, about 1,250 hours of a default sandbox. No card required to start.
  - [3] 2026-11-24: the vendor publishes a USD 0.040/hour rate for the default shape | capture: sha256:57cbec95b2abb99fc1f7f52bee124a6e779f57c47c5740e5747e04afa67f9bd0 | quote: So a 1 vCPU + 1 GiB sandbox is $0.040 / hour, which rounds to four cents.
  - [3] 2026-11-24: the rate is now quoted from the vendor's own page | capture: sha256:57cbec95b2abb99fc1f7f52bee124a6e779f57c47c5740e5747e04afa67f9bd0 | quote: | vCPU | $0.025 / hour |
  - [4] 2026-11-24: a default 300-second auto-destroy timer applies and is configurable with timeoutSec | capture: sha256:67f4da00e8fc2d88123ac74104f75b1e9f2a78576e357aabf2ce8de98a04f8d9 | quote: Every sandbox has an idle timeout (default 300 seconds, configurable per-create via `timeoutSec`). When the timer fires, the sandbox is destroyed.
  - [1] 2026-11-24: the third-party aggregator agrees with the vendor rate and credit | capture: sha256:d7cca9df62e7fe6c1f1022b357d040ae738832e47bab617fb2fb44ffef8fa2e4 | quote: It costs $0.025 per vCPU-hour and $0.015 per GiB-hour, billed per second. New accounts get a $50 credit.
  - [5] 2026-11-24: a REST streaming endpoint is documented | capture: sha256:0183fc67db7a87c139bcaca9b650b6525a520a5726b37d33cc90ac5d71b51ee3 | quote: POST /v1/runs/{id}/exec/stream
  - [2] 2026-11-24: a public HTTPS URL per exposed port is documented | capture: sha256:8ab3c832ed521ee0ab3f19014418a4123a0b67df65e31875592591efb5326c92 | quote: Call `sb.url(port)` for a signed HTTPS URL to whatever you
  - [6] 2026-11-24: an account gate creates an organization in a chosen region; the pricing page states no card is required | capture: sha256:a1b866660ed37f356805f8886d05826b6a5446b3e34cdc56711a866235402d76 | quote: When you sign up you create an organization, and the organization is scoped to a region (US or EU).
  - [6] 2026-11-24: the account is created in the dashboard and keys are bound to an organization and region | capture: sha256:a1b866660ed37f356805f8886d05826b6a5446b3e34cdc56711a866235402d76 | quote: Create one in the [dashboard](https://app.isorun.ai/). A key is bound to your organization and its region.
- sources:
  - [1] https://boxyard.dev/providers/isorun
  - [2] https://isorun.ai/
  - [3] https://docs.isorun.ai/getting-started/pricing
  - [4] https://docs.isorun.ai/sandboxes/lifecycle
  - [5] https://docs.isorun.ai/sandboxes/create-and-execute
  - [6] https://docs.isorun.ai/getting-started/authentication
