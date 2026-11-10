# PortPlay

> portplay.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/portplay/ | JSON https://fshy.ajam.dev/api/v1/entity/portplay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PortPlay

- `egress/portplay` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category game tunnel (UDP port forward) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://portplay.net/
- price EUR 0
- free tier: Free: EUR 0, free forever. Session 24h, Max players 10, Ports 1, Speed 10 Mbps, Latency Standard. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published, on the pricing table or in the FAQ. The free plan states Session 24h, Max players 10, Ports 1, Speed 10 Mbps.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An account, or Google sign-in: 'Create an account or continue with Google. Getting started is fast and free.' | country: None
- interface: unknown
- limits:
  - per-ip-shaping (binding): Speed 10 Mbps on Free, 50 Mbps on Pro, 100+ Mbps on Pro Max [1]
  - retention-clamped: Session 24h on Free, 6 months on Pro, Unlimited on Pro Max [1]
- binding note: Bandwidth is capped at 10 Mbps (capable of 3.2 TiB over 30 days). Free sessions terminate after 24 hours and servers are capped at 10 concurrent players.
- interface detail: A Windows tray app: sign in, pick a preset or a port, copy the address. No API or CLI is described.
- tooling: PortPlay Windows app only; no CLI and no Linux client is offered
- composes with: Needs a Windows host, so it composes with a Windows instance rather than a Linux one.
- reliability: One port and 10 players on Free. The app reconnects automatically when the link drops. No statement on end-of-session behaviour or on idle reclamation.
- notes: The free allowance is a speed and a session length, not a byte quota. Because the endpoint is a vendor hostname plus a port, PortPlay demultiplexes UDP by port on a shared edge instead of spending an IP per customer, which is the structural reason it can give UDP away. Windows 10/11 only. Nothing on the site says what happens at the end of the 24h session.
- evidence note: One free session would show whether the assigned UDP port survives a reconnect and whether 10 Mbps is enforced per tunnel, per account or per session.
- extras:
  - wg_path: inside-udp
  - wg_detail: No WireGuard mode of its own, but the free port forwards any UDP named, so a WireGuard datagram addressed to the assigned host and port would pass. That is a reading of 'Any TCP/UDP port', not a test.
  - ingress: tcp+udp
  - volume_stated: No byte allowance is published, on the pricing table or in the FAQ. The free plan states Session 24h, Max players 10, Ports 1, Speed 10 Mbps.
  - bytes_transit: yes
  - transit_note: The PortPlay relay carries the datagrams; the origin only makes an outbound connection.
- evidence:
  - [1] 2026-10-23: Free is EUR 0 with Session 24h, Max players 10, Ports 1, Speed 10 Mbps; Pro is EUR 1.49 with 3 ports and 50 Mbps; Pro Max is EUR 4.99 with 10 ports
  - [1] 2026-10-23: Arbitrary ports: 'Set the ports you need. Simple Voice Chat, Geyser, and other plugins that require an extra TCP or UDP port work too.'
  - [1] 2026-10-23: FAQ: 'Java usually uses TCP port 25565, Bedrock and Geyser use UDP port 19132, and Simple Voice Chat uses UDP port 24454 by default.'
  - [1] 2026-10-23: The sample address is play.portplay.net:25565, so a customer gets a shared hostname plus an assigned port, not an IP of their own
- sources:
  - [1] https://portplay.net/
