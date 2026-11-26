# VirNAT

> virnat.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/virnat/ | JSON https://fshy.ajam.dev/api/v1/entity/virnat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VirNAT

- `compute/virnat-us-256-kvm` | qualifies-with-caveat | evidence documented | binding volume-quota | category NAT VPS | tier US-256-KVM (DC1)
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T03:20:10.000Z (live) | stale on 2026-11-24
- url https://virnat.com/client/store?kategori=nat-vps
- price parsed USD 0.2333/mo
- free tier: No free tier. US-256-KVM (DC1) is USD 0.80 a quarter, or USD 2.80 a year, for 1 vCPU, 256 MB RAM, 2 GB SSD, 20 IPv4 NAT ports, one IPv6 /64 and 200 GB a month at 200 Mbps. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the server persists for the paid term; no deletion schedule is printed on the store or the configure page | source: [2]
- egress: 200 GB a month at 200 Mbps on the DC1 SKU, 50 GB at 300 Mbps on the SG-320 SKU; no overage price is printed | metered: yes | free allowance: 200 GB | source: [1]
- identity: email | detail: an account on the client area is required to order; the store and the configure page state no card hold and list no payment methods, so the rails are unverified.
- interface: ssh
- limits:
  - volume-quota (binding): 200 GB a month on US-256-KVM DC1 [1]
  - per-ip-shaping: 20 forwarded ports on a shared IPv4, of which the first is TCP SSH and the remaining 19 forward the same port number, TCP or UDP [3]
- binding note: 200 GB a month is the smallest traffic allowance in the band and the first thing a tunnel carrying real traffic exhausts.
- interface detail: KVM guest with root; the public port block is derived from the internal address 10.10.10.N as N01-N20, the first port being SSH
- tooling: any SSH client; the vendor runs a port calculator at port.virnat.com that returns the mapped ports from the internal IP
- composes with: the second-cheapest documented-UDP machine in the band at USD 0.23 a month on annual prepay, with 256 MB and 19 usable TCP/UDP ports
- reliability: no reliability event observed; the storefront and its port calculator are in Chinese while the store labels are in English, and no company, address or registration number appears on any page read
- notes: The best price-per-megabyte in the band after TierHive: USD 0.2333 a month on annual prepay for 256 MB, 2 GB of SSD, 200 GB of traffic, 20 NAT ports and a /64. The UDP statement is the cleanest found on any vendor page - the port calculator says in one sentence which port is SSH and that the other 19 carry TCP or UDP. What it does not have is a counterparty. The about page is a table with 'Registered name | VirNAT' and a dash in every other field: no address, no telephone, no tax number, no registration. The storefront is in Chinese and the brand has no history in documented records. That is the opposite of the dissolved-company problem: not a company that stopped trading, but no company at all that a reader could pursue. The 200 GB allowance is also the tightest in the band. Not established: who operates it, whether the annual SKU renews at USD 2.80, and whether DC1 is in stock.
- evidence note: price, term, shape, traffic and the port rule are quoted from the vendor's own store and port-calculator pages read; the legal entity could not be established at all
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.25
  - shape.disk_gib: 2
  - billing_model: quarterly or annual prepay
  - term: 3 months at USD 0.80, or 12 months at USD 2.80
  - m10h_usd: 0.2333
  - m24h_usd: 0.2333
  - price_arithmetic: USD 2.80 a year / 12 = USD 0.2333 a month on annual prepay; the quarterly cycle is USD 0.80 / 3 = USD 0.2667 a month. A VPS bills whether it runs or not, so the 24/7 and 10 h/day figures are the same.
  - out_of_pocket_usd: 2.8
  - renewal_usd: not published
  - renewal_note: the configure page prints two cycles and no strike-through, so no promotional rate is stated and no renewal price is given
  - port_mbps: 200
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 20 forwarded ports on a shared IPv4: 1 TCP SSH plus 19 that forward on the same port number, TCP or UDP; plus one IPv6 /64
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - udp: stated: the port calculator says the 19 non-SSH ports '按原端口转发，支持 TCP/UDP' (forward on the same port number, supporting TCP/UDP)
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not read
  - price_on_page: USD 0.80/quarter
  - price_in_cart: USD 0.80/quarter (USD 2.80/annum)
  - cart_works: yes
  - cart_url: https://virnat.com/client/store/configure/us-256-kvm
  - signup_url: https://virnat.com/client/register
  - cart_evidence: configure page titled 'Configure: US-256-KVM (DC1)' renders 'Billing Cycle ... $0.80 USD quarterly ... $2.80 USD annually' and an Order Summary reading 'Product US-256-KVM (DC1) ... Add to Cart'
  - needs_account_first: no
- evidence:
  - [1] 2026-10-24: quoted card: 'US-256-KVM (DC1) | $0.80 USD /quarterly | 1 vCPU 256MB RAM 2GB SSD 20 IPv4 NAT Ports 1 /64 IPv6 Address 200GB @200Mbps per month KVM Virtualization'
  - [2] 2026-10-24: quoted billing cycles: 'Billing Cycle $0.80 USD quarterly $2.80 USD annually'
  - [3] 2026-10-24: quoted: '内网 IP 为 10.10.10.N 时，对应公网端口组为 N01-N20（例如 N=11 → 1101-1120）。其中第 1 个端口用于 TCP SSH → :22，其余 19 个端口按原端口转发，支持 TCP/UDP。' - the first port is TCP SSH to 22, the other 19 forward on the same port number and support TCP/UDP
  - [4] 2026-10-24: quoted company-details table: 'Registered name | VirNAT', with 'Address | -', 'Telephone | -', 'Tax office | -', 'Tax number | -' - the entity fields are empty
- sources:
  - [1] https://virnat.com/client/store?kategori=nat-vps
  - [2] https://virnat.com/client/store/configure/us-256-kvm
  - [3] https://port.virnat.com/
  - [4] https://virnat.com/about
