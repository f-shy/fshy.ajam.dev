# Nekotopia nSolo

> nekotopia.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nekotopia/ | JSON https://fshy.ajam.dev/api/v1/entity/nekotopia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nekotopia nSolo

- `egress/nekotopia-nsolo` | qualifies-with-caveat | evidence documented | binding volume-quota | category community mesh with dedicated public IPv4 | tier basic
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:54.548Z (live) | stale on 2026-12-20
- url https://nekotopia.io/sponsor.html
- price USD 0 during early access
- free tier: Encrypted WireGuard Mesh: Yes on every tier. Dedicated Public IPv4 (nSolo): 'Included (2^0=1)' on Pro and 'Ask (2^0=1)' on Plus. Monthly Data Cap: '50 GB | 50 GB | 200 GB | 200 GB | 1 TB' across Basic, Basic+, Plus, Plus+ and Pro. | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Monthly Data Cap 50 GB on Basic and Basic+, 200 GB on Plus and Plus+, 1 TB on Pro; ingress: tcp+udp | metered: yes | free allowance: Monthly Data Cap 50 GB on Basic and Basic+, 200 GB on Plus and Plus+, 1 TB on Pro | source: [1]
- identity: email | detail: Basic is obtained by 'Verify your email'. The rungs above it are not bought: 'Plus and Pro are switched on after a chat with the maintainer.' | country: None
- interface: cli
- limits:
  - volume-quota (binding): 50 GB per month on Basic, 200 GB on Plus, 1 TB on Pro; after the allowance the connection is throttled to 256 kbps on Basic/Plus or 1 Mbps on Pro [2]
  - write-gated: nSolo, Pro and Plus switched on by hand after a conversation [3]
- binding note: The first-party terms state a monthly data allowance of 50 GB on Basic, 200 GB on Plus and 1 TB on Pro, with a throttle to 256 kbps on Basic/Plus and 1 Mbps on Pro after the allowance; the volume quota binds before any other limit.
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
  - [4] 2026-10-23: 'Nothing is reachable from the internet until you publish a port, take an nSolo address, or announce an nColo prefix.'
  - [3] 2026-10-23: 'A dedicated public IPv4 mapped straight to one machine via bidirectional NAT. Reachable from the internet', and 'Basic is on for everyone; Plus and Pro are switched on after a chat with the maintainer.'
  - [5] 2026-10-23: 'Nekotopia is in early access and free to use right now.' and the exposure ladder from private mesh to fully routed
  - [2] 2026-11-19: the first-party terms state the post-allowance throttle rates of 256 kbps and 1 Mbps with numbers and units | capture: sha256:0097d450bcde18f5570cd271f94d5663dbc24a485359cdc0f8abb255457aafe2 | quote: Once you exceed it in a calendar month, your connection is throttled (to 256 kbps on Basic/Plus, 1 Mbps on Pro) until the allowance resets at the start of the next month.
  - [2] 2026-11-19: the first-party terms give the numbered monthly data allowances that make the volume quota binding | capture: sha256:0097d450bcde18f5570cd271f94d5663dbc24a485359cdc0f8abb255457aafe2 | quote: Each tier runs at a fast peak speed with a monthly data allowance: Basic 10 Mbps / 50 GB, Plus 25 Mbps / 200 GB, Pro 100 Mbps / 1 TB.
  - [2] 2026-11-19: the first-party terms still state the monthly data allowance that binds egress by volume | capture: sha256:0097d450bcde18f5570cd271f94d5663dbc24a485359cdc0f8abb255457aafe2 | quote: Each tier runs at a fast peak speed with a monthly data allowance: Basic 10 Mbps / 50 GB, Plus 25 Mbps / 200 GB, Pro 100 Mbps / 1 TB.
- sources:
  - [1] https://nekotopia.io/sponsor.html
  - [2] https://nekotopia.io/terms.html
  - [3] https://nekotopia.io/funding-model.html
  - [4] https://nekotopia.io/
  - [5] https://wiki.nekotopia.io/
