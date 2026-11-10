# microLXC

> microlxc.net | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/microlxc/ | JSON https://fshy.ajam.dev/api/v1/entity/microlxc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## microLXC, tiny (free LXC container)

- `compute/microlxc-tiny` | qualifies-with-caveat | evidence documented | binding volume-quota | category NAT VPS | tier tiny (free LXC container)
- needs card no, phone no, ID no, institution yes | verified 2026-11-02T02:17:27.462Z (live) | stale on 2026-12-03
- url https://microlxc.net/
- free tier: 'Get a free LXC container with instant* deployment.' The tiny shape is 1 core, 256 MB, 2.56 GB SSD, 200 GB traffic | unit: unlimited | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: the unit is a container, not an object
- retention: no retention term is stated on the page; what happens to an idle container was not established | source: [1]
- egress: 200 GB of traffic on the tiny shape; metering unit not stated | metered: yes | free allowance: 200 GB | source: [1]
- identity: institution | detail: no card and no phone number: the gate is a forum account, quoted 'You need to have an active Hostballs, Lowendspirit, or Lowendtalk account with the following:', with '3 Months old account', 'At least 50 Posts (shitposts do not count)' and 'At least 50 Likes on your posts in total'. An activity rule follows: 'Yes, you have to log in to the Portal every 60 days.' No country limit is stated on the about page or the home page. The portal's own registration form was not reached, so whether it asks for an email address or a phone number is unverified. | country: Hostballs, Lowendspirit or Lowendtalk membership
- interface: ssh
- limits:
  - volume-quota (binding): 200 GB of traffic [1]
  - per-ip-shaping: 20 forwarded IPv4 ports on a shared address [1]
  - per-object-cap: 2.56 GB of SSD [1]
- binding note: 200 GB of traffic is small even for a personal tunnel, and it is the first thing a WireGuard node carrying real traffic exhausts.
- interface detail: SSH into an LXC container reachable on a NAT IPv4 port and over IPv6
- tooling: any SSH client; HAProxy support is listed as a feature
- composes with: the only zero-cost machine found among evaluated providers with a NAT IPv4 and 20 forwarded ports, if it has stock and if those ports carry UDP.
- reliability: the deploy page reported 'Out of Stock' for Melbourne, Auckland, Tokyo and Singapore at the time of reading
- notes: Two things decide whether this is the answer and neither was established: whether the 20 forwarded IPv4 ports carry UDP (the page says only '20 IPv4 Ports', unlike NATKVM which states UDP explicitly), and whether any location has stock. WireGuard needs both. The identity cost could not be read because the deploy page showed stock status instead of a form. A 2026-10-24 re-read found the plan orderable: six of sixteen locations carry an 'Out of Stock' badge (Melbourne, Auckland, Tokyo jp1, Singapore, Ho Chi Minh, Johannesburg) and the other ten are flagged stock-available. UDP appears nowhere on the homepage, the deploy page or the raw HTML, so a UDP forward is unverified rather than absent. The word 'instant' carries an asterisk with no footnote found. The free container is 64 MiB today, not the 256 MiB the home page advertises; the home page and the deploy page disagree.
- evidence note: the free offer, the shape, the port count and the traffic figure are quoted from the home page read; whether the 20 ports carry UDP is not stated, and stock is a moving condition
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.0625
  - shape.disk_gib: 2.56
  - billing_model: free
  - term: no term stated
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: USD 0: stated free
  - free_tier_kind: free container
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 20 forwarded ports on a shared IPv4; UDP support not stated
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none stated
  - ipv6_prefix: /64 or /70, per the features list
  - renewal_usd: USD 0
  - renewal_note: free container; no renewal step is stated
  - payment_rails: not read
- evidence:
  - [1] 2026-10-24: quoted: 'Get a free LXC container with instant* deployment.' and features 'NAT IPv4 + IPv6', '/64 or /70 IPv6', '20 IPv4 Ports'
  - [1] 2026-10-24: quoted tiny shape: '1 Core, 256 MB, 2.56GB SSD, 200GB Traffic'
  - [2] 2026-10-24: quoted: the deploy page listed 'Out of Stock' against Melbourne, Auckland, Tokyo and Singapore
  - [3] 2026-11-02: the gate is membership of one of three hosting forums, not an email address | capture: sha256:bc53fbf04629302a1cedc1b234112ee4f9735cfd9079ba7eff46e1c57cb9f671 | quote: You need to have an active Hostballs, Lowendspirit, or Lowendtalk account with the following:
  - [3] 2026-11-02: the forum account must be three months old, with fifty posts and fifty likes, and the portal login every sixty days | capture: sha256:bc53fbf04629302a1cedc1b234112ee4f9735cfd9079ba7eff46e1c57cb9f671 | quote: 3 Months old account
  - [3] 2026-11-02: the answer that follows gives the forum-membership requirement, and names no country | capture: sha256:bc53fbf04629302a1cedc1b234112ee4f9735cfd9079ba7eff46e1c57cb9f671 | quote: #### How do I get a free lxc container?
  - [3] 2026-11-02: the account gate is a forum membership with an age, post and like threshold | capture: sha256:bc53fbf04629302a1cedc1b234112ee4f9735cfd9079ba7eff46e1c57cb9f671 | quote: You need to have an active Hostballs, Lowendspirit, or Lowendtalk account with the following:
  - [2] 2026-11-02: the deploy page still marks four of its locations out of stock, so stock is a moving condition | capture: sha256:b72e0d4e43936e8fdbf3805ab08fe594317eeccaeb689df6c6180b2a17920afe | quote: Out of Stock
- sources:
  - [1] https://microlxc.net/
  - [2] https://microlxc.net/index.php?p=deploy
  - [3] https://microlxc.net/index.php?p=about

## microLXC (tiny)

- `egress/microlxc-tiny` | qualifies-with-caveat | evidence documented | binding volume-quota | category free nat vps | tier tiny
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:42.014Z (live) | stale on 2026-12-04
- url https://microlxc.net/
- free tier: Free LXC container, tiny shape: 1 Core, 256 MB, 2.56GB SSD, 200GB Traffic; NAT IPv4 + IPv6, HAProxy support, a /64 or /70 IPv6, 20 IPv4 ports. | unit: GB | metered on: unstated | read on: 2026-11-03 | source: [1] | note: No period is stated for the 200GB.
- per-object cap: not applicable: a NAT VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 200GB traffic, no period or overage rule stated on the page read. | metered: yes | free allowance: 200GB, period not stated | source: [1]
- identity: email | detail: unverified: behind a sign-up. The deploy page lists locations and stock only; the fields of the launch flow are not shown.
- interface: ssh
- limits:
  - volume-quota (binding): 200GB traffic, period not stated [1]
  - per-ip-shaping: NAT IPv4 with 20 ports [1]
- binding note: 200GB is the first number reached; stock at the deploy page is the practical gate.
- interface detail: LXC container; the access method is not stated on the pages read.
- tooling: unverified: the pages read do not name a client tool; the container is reached over NAT IPv4 or IPv6.
- composes with: A free 200GB NAT box with a /64 or /70 IPv6 and HAProxy support; IPv4 inbound is limited to 20 ports and UDP forwarding is not stated.
- reliability: The deploy page marks several locations 'Out of Stock' and one 'Low Stock' on the date read.
- notes: Free tier with a stock gate; the deploy page lists many locations and shapes.
- evidence note: Shape and allowance are quoted from the vendor's front page; identity is behind a launch flow.
- extras:
  - nat_ports: 20
  - ipv6: /64 or /70
  - udp_forwarding: unverified: not stated
  - routed_ipv6_prefix: yes
  - inbound_ipv4_ports: 20
  - virtualization: LXC container on a shared NAT IPv4.
- evidence:
  - [1] 2026-11-03: microLXC offers a free LXC container | capture: sha256:5e6fe7fb336960321c26e8e93899e86afaa904e38b20af94d0fbd56a5faccae5 | quote: Get a free LXC container with instant* deployment.
  - [1] 2026-11-03: the containers have a NAT IPv4 and an IPv6 | capture: sha256:5e6fe7fb336960321c26e8e93899e86afaa904e38b20af94d0fbd56a5faccae5 | quote: NAT IPv4 + IPv6
  - [1] 2026-11-03: 20 IPv4 ports | capture: sha256:5e6fe7fb336960321c26e8e93899e86afaa904e38b20af94d0fbd56a5faccae5 | quote: 20 IPv4 Ports
  - [1] 2026-11-03: the IPv6 block is a /64 or a /70 | capture: sha256:5e6fe7fb336960321c26e8e93899e86afaa904e38b20af94d0fbd56a5faccae5 | quote: /64 or /70 IPv6
  - [1] 2026-11-03: the tiny shape carries 200GB traffic | capture: sha256:5e6fe7fb336960321c26e8e93899e86afaa904e38b20af94d0fbd56a5faccae5 | quote: 200GB Traffic
  - [2] 2026-11-03: the deploy page marks locations out of stock | capture: sha256:693f31887db50bc97fab3c53824d3327139cf98aa6b43ad727c29e4574d4d86e | quote: Out of Stock
  - [2] 2026-11-03: the deploy page marks a location low on stock | capture: sha256:693f31887db50bc97fab3c53824d3327139cf98aa6b43ad727c29e4574d4d86e | quote: Low Stock
  - [3] 2026-11-03: serverdeals lists MicroLXC at USD 0.0 per year with 200 GB and a /64 IPv6 | quote: ###### MicroLXC
- sources:
  - [1] https://microlxc.net/
  - [2] https://microlxc.net/index.php?p=deploy
  - [3] https://serverdeals.cc/
