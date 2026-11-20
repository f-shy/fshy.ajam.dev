# Tencent EdgeOne L4 Proxy

> edgeone.ai | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/edgeone/ | JSON https://fshy.ajam.dev/api/v1/entity/edgeone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tencent EdgeOne L4 Proxy

- `egress/tencent-edgeone-l4-proxy` | paid-only | evidence documented | binding write-gated | category L4 anycast proxy (TCP/UDP) | tier enterprise
- needs card no, phone no, ID no, institution yes | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://edgeone.ai/pricing
- price unpublished (Enterprise Edition)
- free tier: Free Plan $0 / month, No Credit Card, Unmetered Security Traffic | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The free plan carries 50 GB of traffic per month and the L4 Proxy row is 'Paid Value-Added'. The L4 proxy itself is 'only available with the Enterprise Edition package'.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: An Enterprise Edition package or a prepaid plan for the L4 proxy; the free plan is 'No Credit Card' but carries no L4 proxy at all. | country: None
- interface: rest, cli
- limits:
  - write-gated (binding): The L4 proxy is only available with the Enterprise Edition package [2]
  - volume-quota: free plan 50 GB traffic per month, paid plans 500 GB and 3 TB [1]
- binding note: At 1 TiB/month the byte count is irrelevant: the Enterprise Edition package is what stands between an account and an L4 rule. On the free plan the available volume for UDP is zero.
- interface detail: L4 proxy instances are created in the console with forwarding rules, up to 2,000 rules per instance
- tooling: EdgeOne console or API; no client-side daemon
- composes with: an origin on any VM by IP or domain name, so a free VM works as the origin; only the package price blocks it
- reliability: the L4 forwarding rules cannot pass the client IP over TOA or Proxy Protocol V1 on UDP; only Proxy Protocol V2 carries it for UDP
- notes: The free plan's 'Unmetered Security Traffic' is attack-side language, not clean-traffic allowance: the same page's traffic row is 50 GB and the L4 row is paid. The L4 row could mean a paid add-on available on any plan, Enterprise only, or a mis-extracted table. The L4 overview note settles it as Enterprise only.
- evidence note: The Enterprise-only note, the TCP/UDP forwarding rule fields and the free-plan allowance are each quoted from pages read. The Enterprise price is not published.
- extras:
  - wg_path: inside-udp
  - wg_detail: L4 proxy forwarding rules accept 'Valid values: TCP and UDP', so a WireGuard datagram is forwarded to the origin; the free plan cannot create one.
  - ingress: tcp+udp
  - volume_stated: The free plan carries 50 GB of traffic per month and the L4 Proxy row is 'Paid Value-Added'. The L4 proxy itself is 'only available with the Enterprise Edition package'.
  - bytes_transit: yes
  - transit_note: EdgeOne's layer-4 proxy nodes carry the bytes to the origin
- evidence:
  - [2] 2026-10-23: Note: The L4 proxy is only available with the Enterprise Edition package.
  - [3] 2026-10-23: Forwarding protocol of L4 proxy. Valid values: TCP and UDP; Single origin lets you enter the IP address or domain name of a single origin
  - [1] 2026-10-23: Free Plan $0 / month, No Credit Card, Unmetered Security Traffic, traffic column 50 GB / 500 GB / 3 TB, and an L4 Proxy line marked Paid Value-Added
- sources:
  - [1] https://edgeone.ai/pricing
  - [2] https://edgeone.ai/document/54506
  - [3] https://edgeone.ai/document/54507
