# Horizon Tunnel

> hrzn.run | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hrzn/ | JSON https://fshy.ajam.dev/api/v1/entity/hrzn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Horizon Tunnel

- `egress/horizon-tunnel` | fails-egress | evidence documented | binding per-ip-shaping | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://hrzn.run/pricing
- price USD 0 (reserved names paid)
- free tier: Tunnels on a random subdomain are free, with HTTPS, WebSockets and the request log. No card is needed. The Free plan has no time limit. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited tunnels on a random subdomain; no byte allowance is published in either direction.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'No card is needed'; a login is required to start a tunnel. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): No quota is published, so at 1 TiB/month the thing that fails is an unpublished per-caller tolerance. Protocol fails first in practice: HTTPS and WebSockets only, with no TCP or UDP port. [1]
- binding note: No quota is published, so at 1 TiB/month the thing that fails is an unpublished per-caller tolerance. Protocol fails first in practice: HTTPS and WebSockets only, with no TCP or UDP port.
- interface detail: CLI plus request log in the dashboard.
- tooling: vendor CLI.
- composes with: Webhook and demo ingress only.
- reliability: Random subdomain on free; reserved names are the paid feature.
- notes: Free is genuinely unmetered in count and time, which is rare; the disqualifier is the protocol.
- evidence note: A TCP or UDP tunnel type on any plan would change this; the pricing page lists only HTTP-shaped features.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: Unlimited tunnels on a random subdomain; no byte allowance is published in either direction.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'Tunnels on a random subdomain are free, with HTTPS, WebSockets and the request log'; 'The Free plan has no time limit'
- sources:
  - [1] https://hrzn.run/pricing
