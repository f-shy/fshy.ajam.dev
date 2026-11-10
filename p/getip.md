# GetIP.online

> getip.online | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getip/ | JSON https://fshy.ajam.dev/api/v1/entity/getip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetIP.online

- `egress/getip-online` | fails-quota | evidence documented | binding volume-quota | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://getip.online/
- price USD 0
- free tier: IPv6 WireGuard peer; 100 GB traffic per peer every month; all server locations; manual peer renewal; no logs, no tracking - USD 0 /month | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 100 GB traffic per peer every month; ingress: udp | metered: yes | free allowance: 100 GB traffic per peer every month | source: [1]
- identity: email | detail: 'No credit card required' on the free plan; the free service is 'without adding a credit card'. The registration page was not read, so the exact fields are unestablished. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 100 GB traffic per peer every month [1]
  - per-object-cap: without the USD 1/month Custom Firewall add-on, ports 80/443 accept Cloudflare traffic only and SMTP remains restricted [1]
- binding note: 100 GB per month is about 0.09 TiB, and the overage is sold at USD 3 per 1 TB rather than tolerated. The byte counter is therefore reached long before any other limit.
- interface detail: a WireGuard peer allocated from a web panel
- tooling: any WireGuard client; the panel issues a config
- composes with: could carry a small heartbeat or DNS service, not a data workload, because of the 100 GB meter.
- reliability: manual peer renewal is required under the current free policy, so an unrenewed peer stops working.
- notes: Included because it is the cleanest WireGuard-native peer found and because its quota is the reason it fails: 0.09 TiB/month. The port restriction means that even at 100 GB a web service on 80/443 is proxied through Cloudflare unless the USD 1/month firewall is bought.
- evidence note: documented from the vendor's own pricing block read. The quota is stated, not measured; measuring it would need a peer and 100 GB of traffic.
- extras:
  - wg_path: native-conf
  - wg_detail: the free product is itself a WireGuard peer, provisioned from a panel: 'IPv6 WireGuard peer'. The page also tells users to 'disconnect and reconnect WireGuard to connect to the correct server'.
  - ingress: udp
  - volume_tib_month: 0.0909
  - volume_stated: 100 GB traffic per peer every month
  - bytes_transit: yes
  - transit_note: GetIP.online carries the traffic; the page mentions a host change in Los Angeles in 2026.
- evidence:
  - [1] 2026-10-23: '100 GB traffic per peer every month' on the USD 0 free core service
  - [1] 2026-10-23: 'Additional Traffic', 'US$3 / 1 TB'
  - [1] 2026-10-23: 'Without this add-on, ports 80/443 accept Cloudflare traffic only and SMTP remains restricted.'
  - [1] 2026-10-23: 'No credit card required'
- sources:
  - [1] https://getip.online/
