# Pangolin

> pangolin.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pangolin/ | JSON https://fshy.ajam.dev/api/v1/entity/pangolin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pangolin

- `egress/pangolin` | paid-only | evidence documented | binding volume-quota | category zero trust overlay with public TCP/UDP ingress | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://pangolin.net/pricing
- price USD 0
- free tier: Basic Free: 'Up to 5 users', 'Custom domains', 'All resource types', 'No credit card required.' The limits row reads Users 5, Sites 5, Domains 5, Organizations 1, Public resources 15, Private resources 15, Machine clients 5. | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published on any plan. The free tier is metered on users, sites, resources and machine clients, not bytes.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'No credit card required.' The Cloud account is an email signup; the self-hosted Community Edition needs no vendor account at all. | country: None
- interface: cli
- limits:
  - volume-quota (binding): the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider [1]
- binding note: the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider
- interface detail: the dashboard creates the resource and the newt connector joins the site to it
- tooling: newt site connector, browser dashboard, Docker
- composes with: Community Edition on a virtual machine provides public TCP/UDP ingress; host network transfer allowances remain binding.
- reliability: TCP and UDP resources 'do not enforce Pangolin authentication or access rules', so the listener is unauthenticated at the proxy layer.
- notes: The count caps have no kind in the seven-value vocabulary, so limits[] is empty and the numbers are in free_stated: 15 public resources is what a reader hits first if they need many services. Three candidate readings of the Cloud/free conflict were tested: (1) the free tier ships raw resources, (2) raw resources are self-hosted only, (3) the docs are stale. The raw-resources page and the Cloud-vs-self-hosted page agree with each other and are dated after the pricing page, so (2) holds and 'All resource types' on the pricing page means the HTTP, SSH, RDP, VNC and AI Gateway families on Cloud.
- evidence note: Software functionality and deployment architecture are documented in official repository guides.
- extras:
  - wg_path: none
  - wg_detail: The site connector (newt) holds the WireGuard tunnel and no page read documents a .conf export, so only the vendor connector joins. The public listener is a port bound on the server host: 'Clients connect to <pangolin-server>:<port> and traffic is forwarded to the downstream service through a site connector.'
  - ingress: tcp+udp
  - volume_stated: No byte allowance is published on any plan. The free tier is metered on users, sites, resources and machine clients, not bytes.
  - bytes_transit: yes
  - transit_note: traffic enters the Pangolin server's public port, crosses the WireGuard tunnel to the site, and leaves from the site's own NIC
- evidence:
  - [1] 2026-10-23: 'Basic' is 'Free' with 'Up to 5 users', 'All resource types' and 'No credit card required.'; the limits table gives Public resources 15
  - [2] 2026-10-23: 'TCP and UDP public resources are protocol-agnostic proxies'; 'each resource binds to a port on the Pangolin server host'; 'This feature is only available in self-hosted Pangolin instances. If you're using Pangolin Cloud, you will need to deploy a remote node.'
  - [3] 2026-10-23: 'Public TCP/UDP listeners that bind a port on the Pangolin host are a self-hosted-server feature. On Cloud, deploy a remote node for that.'
- sources:
  - [1] https://pangolin.net/pricing
  - [2] https://docs.pangolin.net/manage/resources/public/raw-resources.md
  - [3] https://docs.pangolin.net/about/pangolin-cloud-vs-self-hosted.md
