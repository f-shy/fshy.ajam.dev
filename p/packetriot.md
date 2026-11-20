# Packetriot

> packetriot.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/packetriot/ | JSON https://fshy.ajam.dev/api/v1/entity/packetriot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Packetriot

- `egress/packetriot` | fails-quota | evidence documented | binding volume-quota | category tunnel (hosted, ports sold separately) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://packetriot.com/pricing
- price USD 0
- free tier: Free: 1 tunnel, 1 GB monthly bandwidth; Port allocations are no longer available on the free-tier. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB monthly bandwidth on the free tier; Basic at USD 5/month raises it to 1 TB; ingress: http-only | metered: yes | free allowance: 1 GB monthly bandwidth on the free tier; Basic at USD 5/month raises it to 1 TB | source: [1]
- identity: email | detail: an account; the free tier is one tunnel | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB monthly bandwidth [1]
  - write-gated: 'Port allocations are no longer available on the free-tier' [1]
- binding note: Both the 1 GB quota and the removal of port allocations fail on the first day.
- interface detail: pktriot tunnel http add
- tooling: pktriot CLI
- composes with: HTTP ingress only
- reliability: the free tier is an HTTP subdomain only
- evidence note: The interesting fact is the footnote: a provider that used to sell ports on the free tier removed them, which is the direction this whole class moves.
- extras:
  - wg_path: none
  - wg_detail: no port can be allocated on the free tier at all, so there is no UDP endpoint to point at
  - ingress: http-only
  - volume_tib_month: 0.000909
  - volume_stated: 1 GB monthly bandwidth on the free tier; Basic at USD 5/month raises it to 1 TB
  - bytes_transit: yes
  - transit_note: the Packetriot edge carries the traffic
- evidence:
  - [1] 2026-10-23: free tier: 1 tunnel, 1 GB monthly, and 'Port allocations are no longer available on the free-tier'; Basic USD 5/month gives 1 TB
- sources:
  - [1] https://packetriot.com/pricing
