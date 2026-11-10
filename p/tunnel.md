# Tunnel.to

> tunnel.to | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnel.to

- `egress/tunnel-to` | fails-quota | evidence documented | binding volume-quota | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnel.to/pricing
- price USD 0
- free tier: Anonymous forever $0 - No account required - Random ephemeral hostname - 1 active tunnel - 512 MiB per tunnel. Registered Free forever - 1 reserved hostname - 3 API tokens - 2 active tunnels - 5 GB bandwidth / month. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 GB bandwidth / month on Registered Free; 512 MiB per tunnel on Anonymous.; ingress: http-only | metered: yes | free allowance: 5 GB bandwidth / month on Registered Free; 512 MiB per tunnel on Anonymous. | source: [1]
- identity: anonymous | detail: No account required for basic usage. The vendor writes: no account required, random ephemeral hostname. Reserving a hostname is free but needs a login. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 5 GB bandwidth / month [1]
  - per-object-cap: 512 MiB per tunnel on Anonymous [1]
- binding note: At 1 TiB/month the 5 GB monthly allowance is exhausted in under two days (0.0045 TiB), and the free allowance is a hard stop, not a throttle.
- interface detail: brew install tunnel-to/tunnelto/tunnelto; tunnelto 3000.
- tooling: brew install tunnel-to/tunnelto/tunnelto, then tunnelto 3000.
- composes with: Sits in front of a free VM as a webhook or demo endpoint; no transport for WireGuard.
- reliability: Anonymous hostnames are ephemeral and change per run; the free tier is metered and stops at the allowance.
- notes: Launched 2026-05-28 on Hacker News and listed on Product Hunt. HTTP-only by construction, so it cannot pass the UDP ingress test regardless of quota.
- evidence note: A measured run would confirm whether the 5 GB counts ingress, egress or both; the page does not say.
- extras:
  - wg_path: none
  - wg_detail: The relay speaks HTTPS, SSE and WebSocket only. The homepage describes outbound connections with no firewall ports, and no UDP or raw TCP listener is offered.
  - ingress: http-only
  - volume_tib_month: 0.0045
  - volume_stated: 5 GB bandwidth / month on Registered Free; 512 MiB per tunnel on Anonymous.
  - bytes_transit: yes
  - transit_note: The vendor relay carries the bytes over wss://tor1.tunnel.to.
- evidence:
  - [1] 2026-10-23: Anonymous tier is $0 with 512 MiB per tunnel and no account; Registered Free is 5 GB bandwidth per month with 2 active tunnels; the paid tier is $36/year for 50 GB.
  - [2] 2026-05-28: Launch post: lightweight relay-based tunnel service, CLI-first, public relay nodes in North America and Europe, no account required for basic usage.
- sources:
  - [1] https://tunnel.to/pricing
  - [2] https://news.ycombinator.com/item?id=48309288
