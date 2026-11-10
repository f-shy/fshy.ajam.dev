# Wiredoor

> wiredoor.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wiredoor/ | JSON https://fshy.ajam.dev/api/v1/entity/wiredoor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wiredoor

- `egress/wiredoor` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category self-hosted WireGuard ingress | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.wiredoor.net/
- price USD 0
- free tier: 'Expose HTTP, TCP, and UDP services from private networks through outbound WireGuard tunnels. Keep control of your public endpoint, routing, certificates, and access policies.' The software is self-hosted; no vendor plan and no vendor quota. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published because there is no vendor in the path: the server's NIC and its hosting bill are the limit.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: Self-hosted: the only account is the local admin the installer creates ('username: admin@example.com'). No vendor registration. | country: None
- interface: cli
- limits:
  - volume-quota (binding): the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider [1]
- binding note: the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider
- interface detail: 'wiredoor http first-app --domain app.example.com --port 3000'
- tooling: wiredoor CLI, Docker, the server dashboard
- composes with: runs on the same free-tier VPS as Pangolin or Wireport, so the three are alternatives rather than additions; the VPS egress is the shared ceiling
- reliability: the public endpoint is the operator's; its uptime, certificate renewal and firewall are all local work
- notes: The second half of the ingress chain is missing: Wiredoor Server must sit on a host with a public IP. It is software, not a service, so the free tier is the VPS, not Wiredoor. The FAQ page was read through the search index rather than a direct fetch, which is why its evidence row is weaker than the home page.
- evidence note: WireGuard tunnel proxy architecture and relay routing are documented in repository specifications.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: 'Remote nodes connect outward to Wiredoor Server, and forwarded traffic crosses the encrypted tunnel.' The wiredoor CLI or the dashboard token holds the tunnel; no .conf export is documented.
  - ingress: tcp+udp
  - volume_stated: No allowance is published because there is no vendor in the path: the server's NIC and its hosting bill are the limit.
  - bytes_transit: yes
  - transit_note: the server receives on its public port and forwards down the outbound WireGuard tunnel to the private node
- evidence:
  - [1] 2026-10-23: 'Expose HTTP, TCP, and UDP services from private networks through outbound WireGuard tunnels'; 'Route web applications by domain or path and TCP or UDP services by an approved public port'
  - [2] 2026-10-23: 'Wiredoor assign unused port automatically in the range defined by TCP_SERVICES_PORT_RANGE', via the search index snippet
- sources:
  - [1] https://www.wiredoor.net/
  - [2] https://www.wiredoor.net/documentation/faq
