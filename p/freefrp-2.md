# Free FRP

> freefrp.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freefrp-2/ | JSON https://fshy.ajam.dev/api/v1/entity/freefrp-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Free FRP (freefrp.net)

- `egress/freefrp-net` | qualifies-with-caveat | evidence documented | binding request-rate | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:53.450Z (live) | stale on 2026-12-20
- url https://freefrp.net/
- price USD 0
- free tier: Connection port: 7000; password: freefrp.net; open ports: 80 / 443, 10001 to 50000; current version: 0.56.0. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No quota is published anywhere on the site.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account: a shared server password is printed on the home page. | country: None
- interface: cli
- limits:
  - volume-quota: none published [1]
  - request-rate (binding): remote port must be unique inside the shared open-port range 80/443 and 10001-50000 [1]
- binding note: The vendor home page publishes open ports 80/443 and 10001-50000; the binding limit is a unique remote port inside that shared 10001-50000 range, the nearest constraint kind. No byte quota or rate cap is published.
- interface detail: Standard frpc against a published server and password.
- tooling: any frpc
- composes with: A zero-identity UDP entry point, same role as freefrp.com with a narrower port range.
- reliability: No ban policy and no SLA are published; nothing governs whether the server stays up.
- notes: Anonymous and quota-free, but with no operator identity and no stated limit the risk is the service vanishing rather than a metered cut-off. A 1 TiB/month run on a volunteer server is the least likely thing it survives.
- evidence note: The endpoint and port range are on the vendor page today; the UDP statement is from the docs page read. Only a probe shows whether UDP is served.
- extras:
  - wg_path: inside-udp
  - wg_detail: The docs page documents TCP and UDP proxy types against this server; a WG datagram can be proxied on a port from 10001 to 50000.
  - ingress: udp
  - volume_stated: No quota is published anywhere on the site.
  - bytes_transit: yes
  - transit_note: One volunteer server carries the datagrams.
- evidence:
  - [1] 2026-10-23: shared server on port 7000, open ports 10001-50000
  - [2] 2026-10-23: TCP and UDP proxy types are documented for this server
  - [1] 2026-11-19: the vendor home page publishes the open-port range 80/443 and 10001-50000 with numbers and unit | capture: sha256:a0e36652029bbfa17ac4cfe724270d22dd3b10c6d559f417e50c7b6bd1878399 | quote: 开放端口 ：80 / 443 , 10001 - 50000
  - [1] 2026-11-19: the first-party port range with numbers and unit supports the request-rate binding | capture: sha256:a0e36652029bbfa17ac4cfe724270d22dd3b10c6d559f417e50c7b6bd1878399 | quote: 开放端口 ：80 / 443 , 10001 - 50000
  - [1] 2026-11-19: the binding is a unique remote port inside the first-party 80/443 and 10001-50000 open-port range | capture: sha256:a0e36652029bbfa17ac4cfe724270d22dd3b10c6d559f417e50c7b6bd1878399 | quote: 开放端口 ：80 / 443 , 10001 - 50000
- sources:
  - [1] https://freefrp.net/
  - [2] https://freefrp.net/docs
