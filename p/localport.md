# Localport

> localport.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localport/ | JSON https://fshy.ajam.dev/api/v1/entity/localport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Localport

- `egress/localport` | paid-only | evidence documented | binding volume-quota | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://localport.io/pricing
- price USD 5/month | parsed USD 5/mo
- free tier: Why is there no free plan? What a free tier would cost, we put into your plan. Every plan starts with a trial. Hobby starts at $5 a month, Pro at $20, with a 30-day and a 14-day trial. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bandwidth is metered per plan: Pro includes 150 GB, Business 1 TB. Nothing is free.; ingress: tcp | metered: yes | free allowance: Bandwidth is metered per plan: Pro includes 150 GB, Business 1 TB. Nothing is free. | source: [1]
- identity: email | detail: A paid team account is required after the trial; no card-free tier exists. The signup form was not read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 TB on Business; tunnels stop when the monthly bandwidth is used up [1]
- binding note: There is no free tier, so the first failure is the invoice, not a quota. At $20/month Pro the 150 GB cap is 0.136 TiB.
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
  - volume_stated: Bandwidth is metered per plan: Pro includes 150 GB, Business 1 TB. Nothing is free.
  - bytes_transit: yes
  - transit_note: Localport relays through its regional edge.
- evidence:
  - [1] 2026-10-23: No free plan by design; Pro is $20/month with 150 GB, Business 1 TB, and tunnels stop when the monthly bandwidth is used up.
  - [2] 2026-10-23: HTTP, TCP and TLS tunnels over port 443; no UDP listed.
- sources:
  - [1] https://localport.io/pricing
  - [2] https://localport.io/tunnels
