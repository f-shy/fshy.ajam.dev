# InstaTunnel

> instatunnel.my | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instatunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/instatunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InstaTunnel

- `egress/instatunnel` | fails-egress | evidence documented | binding per-ip-shaping | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://instatunnel.my/pricing
- price USD 0 (Pro USD 5/month) | parsed USD 5/mo
- free tier: Simultaneous Tunnels 3 ... Session Duration 24h ... Price FREE | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published. The page compares itself to ngrok with '2x the free tier bandwidth' and gives no figure.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'Start Free' account; MCP endpoints need Pro. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): Bandwidth is unstated, so an unpublished tolerance is what a 1 TiB/month user meets. Before that, the session cap ends the tunnel every 24 hours, and the protocol is HTTPS only. [1]
  - request-rate: 3 simultaneous tunnels and 24-hour sessions on free [1]
- binding note: Bandwidth is unstated, so an unpublished tolerance is what a 1 TiB/month user meets. Before that, the session cap ends the tunnel every 24 hours, and the protocol is HTTPS only.
- interface detail: npm install -g instatunnel.
- tooling: npm CLI.
- composes with: Webhook ingress only.
- reliability: Tunnels expire every 24 hours on free and the URL changes.
- notes: The 24-hour session beats ngrok's 2 hours, which is the vendor's whole pitch. Still HTTP.
- evidence note: A published byte figure would sharpen the binding; a TCP or UDP tunnel type would change the verdict.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance is published. The page compares itself to ngrok with '2x the free tier bandwidth' and gives no figure.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: free column: 3 simultaneous tunnels, 24h sessions, FREE; no bandwidth figure
- sources:
  - [1] https://instatunnel.my/pricing
