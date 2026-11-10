# freefrp.com public server

> freefrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freefrp/ | JSON https://fshy.ajam.dev/api/v1/entity/freefrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freefrp.com public server

- `egress/freefrp-com` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.freefrp.com/
- price USD 0
- free tier: Open protocols: TCP / UDP / HTTP / HTTPS; open ports: 10000 to 60000; auth token: public.freefrp.com. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte quota is published. The page warns that sustained bandwidth at or above 30 Mbps will get the /24 banned.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account: the page publishes the server address, port, version and a shared auth token. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): sustained 30 Mbps triggers a /24 ban [1]
  - volume-quota: none published [1]
- binding note: No byte cap exists, so the 30 Mbps sustained threshold is the first thing that fails: it is a rate, and 1 TiB/month needs only 3.24 Mbps, so the quota test can pass while a burst still gets the address banned.
- interface detail: Standard frpc against a published server and token.
- tooling: any frpc
- composes with: A no-identity UDP entry point that can front a WG listener, at the cost of an address that may move.
- reliability: The operator warns the IP may change at any time and that sustained 30 Mbps gets the whole /24 blocked.
- notes: The most permissive free endpoint in the sweep: no account, no quota, UDP in the port range. Unlimited here means the operator publishes no byte cap, not that it promises unmetered capacity. It is a single volunteer server with an explicit no-SLA warning, so the binding is reliability, not volume. The /24 ban means a shared address takes neighbours with it.
- evidence note: Public FRP server parameters, port ranges, supported protocols and rate limits are published on the vendor status page.
- extras:
  - wg_path: inside-udp
  - wg_detail: A raw frps endpoint with a shared token and a 10000-60000 port range; a WG datagram can be proxied on any port in that range, subject to frp's UDP session handling.
  - ingress: udp
  - volume_stated: No byte quota is published. The page warns that sustained bandwidth at or above 30 Mbps will get the /24 banned.
  - bytes_transit: yes
  - transit_note: One volunteer server carries the datagrams.
- evidence:
  - [1] 2026-10-23: TCP/UDP/HTTP/HTTPS on ports 10000-60000, shared token, 30 Mbps sustained triggers a ban, IP may change without notice
- sources:
  - [1] https://www.freefrp.com/
