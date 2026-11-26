# Localport

> localport.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localport/ | JSON https://fshy.ajam.dev/api/v1/entity/localport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Localport

- `egress/localport` | paid-only | evidence documented | binding volume-quota | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T17:26:44.695Z (live) | stale on 2026-12-26
- url https://localport.io/pricing
- price USD 5/month | parsed USD 5/mo
- free tier: Why is there no free plan? What a free tier would cost, we put into your plan. Every plan starts with a trial. Hobby starts at $5 a month, Pro at $20, with a 30-day and a 14-day trial. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bandwidth is metered per plan: Hobby 100 GB, Pro 500 GB and Business 2.5 TB a month. | metered: yes | free allowance: Bandwidth is metered per plan: Hobby 100 GB, Pro 500 GB and Business 2.5 TB a month. | source: [1]
- identity: email | detail: an email address: 'Enter your email to get started' | country: None
- interface: cli
- limits:
  - volume-quota (binding): Hobby 100 GB, Pro 500 GB and Business 2.5 TB a month [1]
- binding note: An overage is never invoiced: when the monthly bandwidth is used up, tunnels stop until the next cycle or until you upgrade.
- interface detail: Agent makes outbound connections on port 443; no CLI syntax published on the pages read.
- tooling: Vendor agent; outbound on port 443 only.
- composes with: Not usable without a subscription; no role in a zero-budget stack.
- reliability: Hard stop at the monthly bandwidth cap rather than a throttle.
- notes: Recorded to close the question: a 2026 entrant that deliberately has no free tier. Nothing here is reachable at zero cost, and it does not carry UDP.
- evidence note: The pricing page is explicit; a trial would only confirm the tunnel works.
- extras:
  - wg_path: none
  - wg_detail: The tunnel page offers HTTP, TCP and TLS. No UDP protocol is listed, and the pricing page counts bandwidth rather than ports.
  - ingress: tcp
  - volume_tib_month: 0.0
  - volume_stated: Bandwidth is metered per plan: Hobby 100 GB, Pro 500 GB and Business 2.5 TB a month.
  - bytes_transit: yes
  - transit_note: Localport relays through its regional edge.
- evidence:
  - [1] 2026-10-23: No free plan by design; Pro is $20/month with 150 GB, Business 1 TB, and tunnels stop when the monthly bandwidth is used up.
  - [2] 2026-10-23: HTTP, TCP and TLS tunnels over port 443; no UDP listed.
  - [1] 2026-11-25: the monthly bandwidth allowance of each plan | capture: sha256:6feac1041579a96be5d3e173541928b2720bc3dd132c0f2248a787e746269dc0 | quote: | Bandwidth a month | 100 GB | 500 GB | 2.5 TB | Custom |
  - [1] 2026-11-25: the cap stops the tunnels instead of billing an overage | capture: sha256:6feac1041579a96be5d3e173541928b2720bc3dd132c0f2248a787e746269dc0 | quote: Nothing extra is billed. When the monthly bandwidth is used up, tunnels stop until the next cycle or until you upgrade.
  - [3] 2026-11-25: the dashboard login asks for an email address | capture: sha256:6f4807347b6e993758708e17549c62fe8c7d61628de294a00758b64a58308bfd | quote: Enter your email to get started
  - [1] 2026-11-25: TCP is offered on every plan | capture: sha256:6feac1041579a96be5d3e173541928b2720bc3dd132c0f2248a787e746269dc0 | quote: HTTP, TCP and TLS Every protocol on every plan
- sources:
  - [1] https://localport.io/pricing
  - [2] https://localport.io/tunnels
  - [3] https://dashboard.localport.io/auth/login?plan=hobby&cycle=yearly
