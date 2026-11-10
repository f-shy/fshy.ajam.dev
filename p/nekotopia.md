# Nekotopia nSolo

> nekotopia.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nekotopia/ | JSON https://fshy.ajam.dev/api/v1/entity/nekotopia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nekotopia nSolo

- `egress/nekotopia-nsolo` | qualifies-with-caveat | evidence documented | binding volume-quota | category community mesh with dedicated public IPv4 | tier basic
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://nekotopia.io/sponsor.html
- price USD 0 during early access
- free tier: Encrypted WireGuard Mesh: Yes on every tier. Dedicated Public IPv4 (nSolo): 'Included (2^0=1)' on Pro and 'Ask (2^0=1)' on Plus. Monthly Data Cap: '50 GB | 50 GB | 200 GB | 200 GB | 1 TB' across Basic, Basic+, Plus, Plus+ and Pro. | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Monthly Data Cap 50 GB on Basic and Basic+, 200 GB on Plus and Plus+, 1 TB on Pro; ingress: tcp+udp | metered: yes | free allowance: Monthly Data Cap 50 GB on Basic and Basic+, 200 GB on Plus and Plus+, 1 TB on Pro | source: [1]
- identity: email | detail: Basic is obtained by 'Verify your email'. The rungs above it are not bought: 'Plus and Pro are switched on after a chat with the maintainer.' | country: None
- interface: cli
- limits:
  - volume-quota (binding): 50 GB per month on the entry tier; 1 TB on Pro [1]
  - write-gated: nSolo, Pro and Plus switched on by hand after a conversation [2]
- binding note: A new account starts at 50 GB/month, which is 0.0455 TiB, so the volume quota fails 22 times over before anything else is reached. The 1 TB rung that would pass the test is behind a human decision, and nSolo, the thing that makes a service inbound, is behind the same decision.
- interface detail: WireGuard configuration download from a member dashboard; email verification to join
- tooling: any WireGuard client; the Torus configuration is downloaded from the dashboard
- composes with: nSolo puts a dedicated public IPv4 on one free VM, and the mesh reaches the rest of the account's machines without any of them having an address
- reliability: early access run by a single operator; every rung above Basic depends on that operator's availability; the wiki is the only operational documentation and the member pages require a session.
- notes: The free tier is mesh-only: Basic has no Internet Outbound Egress at all ('-' in that row), so a new account cannot serve anything inbound until a rung is granted. nSolo is bidirectional NAT on one machine from 193.143.16.0/23 BYOIP, London only. UDP is inferred, not stated: the vendor says 'run services reachable from the internet' with no protocol restriction, and a NAT'd public IPv4 forwards whatever the port mapping says. The 1 TiB figure appears only as 1 TB on Pro, which is 0.909 TiB. All member documentation is behind a login, so the port-publishing detail and the 1 TB terms could not be read.
- evidence note: The tier table is documented. Whether an nSolo address forwards UDP is not stated anywhere read, so a UDP probe would move that field from inferred to measured.
- extras:
  - wg_path: native-conf
  - wg_detail: 'Torus is our ring of hubs, linked by WireGuard' and 'Torus VPN configuration and downloads' on the member login. The configuration is downloaded from the dashboard, which is behind a login.
  - ingress: tcp+udp
  - volume_tib_month: 0.0455
  - volume_stated: Monthly Data Cap 50 GB on Basic and Basic+, 200 GB on Plus and Plus+, 1 TB on Pro
  - bytes_transit: yes
  - transit_note: Nekotopia's hub routers in London and Ohio carry the traffic and own the announcing AS
- evidence:
  - [1] 2026-10-23: the tier table: data caps, peak bandwidth, nSolo availability, and how each rung is obtained
  - [3] 2026-10-23: 'Nothing is reachable from the internet until you publish a port, take an nSolo address, or announce an nColo prefix.'
  - [2] 2026-10-23: 'A dedicated public IPv4 mapped straight to one machine via bidirectional NAT. Reachable from the internet', and 'Basic is on for everyone; Plus and Pro are switched on after a chat with the maintainer.'
  - [4] 2026-10-23: 'Nekotopia is in early access and free to use right now.' and the exposure ladder from private mesh to fully routed
- sources:
  - [1] https://nekotopia.io/sponsor.html
  - [2] https://nekotopia.io/funding-model.html
  - [3] https://nekotopia.io/
  - [4] https://wiki.nekotopia.io/
