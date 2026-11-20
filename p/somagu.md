# Somagu VPS

> somagu.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/somagu/ | JSON https://fshy.ajam.dev/api/v1/entity/somagu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Somagu VPS

- `egress/somagu-vps` | paid-only | evidence documented | binding none | category vps (hosted, South Korea, NAT) | tier paid
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://somagu.com/
- price USD 0.54 per month plus pay-per-traffic | parsed USD 0.54/mo
- free tier: [translated] 'VPS Plan v20: $0.54 USD per month. vCPU 1 core, memory 512 MB, disk 20 GB, traffic: pay per traffic, network: NAT, location: South Korea.' No free tier appears on the page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] 'Traffic: pay per traffic', priced from the vendor's pricing document. No monthly allowance is included; data is billed as used.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The page's 'Create' links land on somagu.com/vps/create/...; no signup requirements are stated on the page read, so email-or-card is not established either way. | country: None
- interface: ssh, cli
- binding note: Nothing free binds. Traffic is billed per byte on a NAT guest, so the first failure at 1 TiB/month is the invoice, not a quota.
- interface detail: [translated] 'Create your WireGuard server by oneclick', 'Access your shadowsocks server by oneclick' - the panel builds the server image.
- tooling: one-click Shadowsocks, WireGuard and OpenVPN images plus a custom VPS; SSH on a NAT-forwarded port
- composes with: At USD 0.54 per month for a Korean guest it is the cheap fallback for a Korean endpoint if a free one never appears.
- reliability: Contention on NAT guest and pay-per-traffic billing. Community forum carries a 2023 end-of-service announcement, conflicting with the current pricing page.
- notes: This is the cheapest Korean address found and the only one that builds a WireGuard server in one click, but it is paid and the network is NAT with no stated port mapping. History worth knowing: Somagu ran a free 512 MB NAT VPS in 2017 (announced by the same operator who runs Mudfish), and search results quote a forum post announcing the service would end on 2023-08-31. The live pricing page on 2026-10-23 sells plans, so the shutdown notice is either reversed or refers to the free tier. The forum page itself did not render that text to this reader, so the quote is a search snippet and is not trusted. Country: South Korea.
- evidence note: The price, the NAT network and the one-click WireGuard product are vendor sentences with a date. Whether the NAT address accepts an inbound UDP handshake is not stated and would need a probe; the record cannot be raised without one.
- extras:
  - wg_path: registration-api
  - wg_detail: [translated] The vendor builds the endpoint for you: 'WireGuard $0.54 USD/m - VPS Plan v20 (1 vCPU + 512 MB) - WireGuard Server - Create your WireGuard server by oneclick.' The network is NAT, and no public port or port-forward count is stated for this plan.
  - ingress: udp
  - volume_stated: [translated] 'Traffic: pay per traffic', priced from the vendor's pricing document. No monthly allowance is included; data is billed as used.
  - bytes_transit: yes
  - transit_note: A NAT guest behind the operator's Korean address; the shared address carries the bytes.
- evidence:
  - [1] 2026-10-23: [translated] 'VPS Plan v20: $0.54 USD per month', 'Traffic: pay per traffic', 'Network: NAT', 'Location: South Korea'.
  - [1] 2026-10-23: [translated] 'WireGuard $0.54 USD/m - VPS Plan v20 (1 vCPU + 512 MB) - WireGuard Server - Create your WireGuard server by oneclick.'
- sources:
  - [1] https://somagu.com/
