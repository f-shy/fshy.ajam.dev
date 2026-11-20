# Tailscale Funnel

> tailscale.com | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tailscale/ | JSON https://fshy.ajam.dev/api/v1/entity/tailscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tailscale Personal

- `egress/tailscale-personal` | qualifies | evidence measured | binding request-rate | category mesh network
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-12-22
- url https://tailscale.com/pricing
- free tier: 6 users, unlimited user devices, 3 ACL groups, 50 tagged resources | unit: users | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: signalling; direct WireGuard paths, DERP relay only when a direct path fails | metered: no | source: [1]
- identity: email | detail: a Tailscale account
- interface: cli
- limits note: counts of things, not rates, so no vocabulary kind names them: 6 users, unlimited user devices, 50 tagged resources; 1,000 ephemeral node-minutes per month
- interface detail: tailscale up
- tooling: part of interface detail
- composes with: signalling only, which is why its free tier is genuinely unlimited in bytes. It composes with a private mesh and not with a public serving tier.
- reliability: DERP relays transit bytes when hole-punching fails and were not measured
- notes: Funnel, the product that puts bytes on Tailscale's relays, is capped and recorded separately.
- evidence note: this host runs Tailscale client 1.102.4 on a live tailnet: `tailscale ping` to a peer returned via a LAN address on port 41641, a direct WireGuard path and not DERP, and `netcheck` reported UDP true with the nearest DERP at Bengaluru 56.2 ms. Signalling is measured; no byte throughput was run over the mesh
- extras:
  - stale_after_days: 180
  - bytes_transit: conditional
  - transit_note: peers negotiate a direct WireGuard path and DERP carries bytes only when hole-punching fails
- evidence:
  - [1] 2026-10-22: 6 users, unlimited user devices and 50 tagged resources
  - probe:tailscale://peer/ping 2026-10-22: tailscale 1.102.4 on a live tailnet: `tailscale ping` replied 'pong from a peer (its tailnet address) via a LAN address on port 41641 in 100ms', a direct path; `netcheck` reported UDP true, both address families present, and the nearest DERP at Bengaluru 56.2 ms
- sources:
  - [1] https://tailscale.com/pricing

## Tailscale Funnel

- `egress/tailscale-funnel` | fails-quota | evidence documented | binding per-ip-shaping | category tunnel (hosted, mesh front door)
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tailscale.com/kb/1223/funnel
- free tier: public HTTPS on a *.ts.net name, available on every plan | unit: unlimited | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: not applicable | source: [1]
- egress: subject to non-configurable bandwidth limits whose value is not published | metered: no | source: [1]
- identity: email | detail: a Tailscale account
- interface: cli
- limits:
  - per-ip-shaping (binding): non-configurable and unpublished [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: ports 443, 8443 and 10000 only
- binding note: a discretionary throttle with no number is worse than a quota: there is no threshold to design against.
- interface detail: tailscale funnel; ports 443, 8443 and 10000 only
- tooling: part of interface detail
- composes with: gives a tailnet device a public HTTPS name with no domain and no port, which is the cheapest stable-address chain. The unpublished throttle is what stops it being a serving tier.
- reliability: Funnel is in beta
- notes: Re-read 2026-10-23: Funnel is a TCP proxy with TLS termination ('Tailscale does this using a TCP proxy and Funnel relay servers', 'Funnel only works over TLS-encrypted connections'), so it carries no UDP at all. That is a second, independent reason it cannot serve a WireGuard or game or DNS workload, alongside the unpublished bandwidth limit.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: Funnel is the product that puts bytes on Tailscale's relays, which is why the throttle returns with it
- evidence:
  - [1] 2026-10-22: 'Traffic sent over a Funnel is subject to non-configurable bandwidth limits', and the port restriction
  - [1] 2026-10-23: 'Funnel can only listen on ports 443, 8443, and 10000'; 'Funnel only works over TLS-encrypted connections'; 'Traffic sent over a Funnel is subject to non-configurable bandwidth limits.'
  - [2] 2026-10-23: '--tcp=<port>' and '--tls-terminated-tcp=<port>' are listed under 'Serve command flags', not funnel flags
- sources:
  - [1] https://tailscale.com/kb/1223/funnel
  - [2] https://tailscale.com/kb/1242/tailscale-funnel
