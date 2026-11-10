# Portwarp

> portwarp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/portwarp/ | JSON https://fshy.ajam.dev/api/v1/entity/portwarp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Portwarp

- `egress/portwarp` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category udp port forward (game tunnel, hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://portwarp.com/pricing
- price USD 0
- free tier: 1 active tunnel, 2 extra ports per tunnel, TCP and UDP support, Unlimited bandwidth | unit: unlimited | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited bandwidth, stated for every plan: 'Every plan includes TCP, UDP, encrypted tunnels, and unlimited bandwidth.' No rate, meter or tolerated tolerance is published.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a free account with browser device-code approval: 'Create an account in 30 seconds. No credit card.' https://portwarp.com/ ; 'The CLI opens a browser approval flow and displays a short code.' https://portwarp.com/docs/cli/quickstart | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): no number published; 'unlimited bandwidth' is the whole of the stated allowance [1]
- binding note: Free plan provides one active tunnel with unstated bandwidth limits. Dropped free tunnels require manual restart.
- interface detail: pwrp login, pwrp tunnels, pwrp connect
- tooling: pwrp CLI, Portwarp Desktop, Docker
- composes with: one free UDP port is exactly one WireGuard endpoint: run wg-quick on the origin, point a free VM or a second tunnel at it, and the relay carries the datagrams
- reliability: Auto-reconnect requires a PRO subscription; dropped free tunnels require manual client restart. Bandwidth rate limits are unpublished.
- notes: The strongest free-tier UDP candidate found that is not a game-preset tunnel: UDP is in the base plan, the port is configured rather than allocated, and the allowance is stated as unlimited. Not measured. The free tier's one-tunnel cap is a plan limit outside the constraint vocabulary and lives in binding_note. Re-read 2026-10-23: PRO adds 90-day traffic history and connection insights, so the edge counts bytes even though every plan is sold as unlimited.
- evidence note: Raise to measured by running the CLI on a free account, holding a UDP port, reconnecting, and confirming the public port is unchanged after a restart; then pushing a counted byte volume through it for an hour and reading the transfer counter.
- extras:
  - wg_path: inside-udp
  - wg_detail: UDP is a native free-tier protocol and the public port is a property of the tunnel configured in the dashboard, not an allocation made at connect time: 'The list shows a number, name, protocol, local port, public port, and current state for each tunnel.' https://portwarp.com/docs/cli/quickstart
  - ingress: udp
  - volume_stated: Unlimited bandwidth, stated for every plan: 'Every plan includes TCP, UDP, encrypted tunnels, and unlimited bandwidth.' No rate, meter or tolerated tolerance is published.
  - bytes_transit: yes
  - transit_note: the anycast edge carries the datagrams; the operator's POP is the single point of failure
- evidence:
  - [1] 2026-10-23: free plan is 1 active tunnel with TCP and UDP support and unlimited bandwidth; PRO is USD 2.99/month with 32 tunnels
  - [2] 2026-10-23: the tunnel's public port is listed as a stored property of the tunnel, not a per-session allocation; login is a browser device-code flow
  - [3] 2026-10-23: 'The CLI supports TCP, UDP, and tunnels that use both protocols. It only makes outbound connections'
  - [4] 2026-10-23: 'Native UDP & TCP Tunneling' and a LOCAL PORT 27015 to TUNNEL PORT 27015 mapping, plus 'No credit card'
  - probe:https://portwarp.com/ tcp:443 2026-10-23: portwarp.com:443 accepts a TCP connection from this host and the pricing page returns HTTP 200
- sources:
  - [1] https://portwarp.com/pricing
  - [2] https://portwarp.com/docs/cli/quickstart
  - [3] https://portwarp.com/docs/cli
  - [4] https://portwarp.com/
