# LusoVPS IPv6 free

> lusovps.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lusovps/ | JSON https://fshy.ajam.dev/api/v1/entity/lusovps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LusoVPS IPv6 free

- `egress/lusovps-ipv6-free` | trial-only | evidence documented | binding volume-quota | category origin VM (free trial) | tier trial
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:54.167Z (live) | stale on 2026-12-20
- url https://www.lusovps.com/products/vps-starter-ipv6
- price USD 0 for 15 days, then EUR 3.50 a month | parsed USD 3.94/mo
- free tier: VPS Linux IPv6 Only Free ... 64MB RAM ... 10GB Traffic @ 100Mbps ... 5 IPv6 Addresses ... Price: FREE for 15 days | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10GB Traffic @ 100Mbps; ingress: udp | metered: yes | free allowance: 10GB Traffic @ 100Mbps | source: [1]
- identity: email | detail: the order goes through a cart at cart.lusovps.com with no card term stated on the product page; the checkout flow was not read | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 10GB Traffic @ 100Mbps [1]
  - per-object-cap: 64 MB of RAM, 2 GB of disk [1]
- binding note: The first-party product page states 10GB Traffic @ 100Mbps for the free VPS; this volume quota is the first constraint a larger monthly volume reaches, and the 15-day term ends the server.
- interface detail: SolusVM panel plus SSH over one of five IPv6 addresses
- tooling: wg-quick over IPv6, RAM permitting
- composes with: does not compose; recorded to close the IPv6-free-VPS question
- reliability: the free term is 15 days and the server is then deleted or converted to the EUR 3.50 a month plan
- notes: Provides an IPv6-only virtual machine with 10 GB of bandwidth on a 15-day promotional trial. Standard paid IPv6 plans are priced at EUR 3.50 monthly.
- evidence note: the specification table and the 'FREE for 15 days' price line are on the product page read; no probe was run
- extras:
  - wg_path: native-conf
  - wg_detail: a Xen VPS with five IPv6 addresses and a SolusVM panel, so wg-quick is native over IPv6; 64 MB of RAM is the practical constraint, since the kernel module plus sshd plus wg-quick is a tight fit and a userspace fallback would not fit at all
  - ingress: udp
  - volume_tib_month: 0.0091
  - volume_stated: 10GB Traffic @ 100Mbps
  - bytes_transit: yes
  - transit_note: bytes leave over IPv6 at up to 100 Mbps
- evidence:
  - [1] 2026-10-23: the free plan reads '64MB RAM', '2GB Hard Drive', '10GB Traffic @ 100Mbps', '5 IPv6 Addresses' and 'Price: FREE for 15 days'
  - [1] 2026-10-23: the paid twin of the same shape is 'EUR 3.50EUR monthly', so the free 15 days is a trial of a paid product
  - [1] 2026-11-19: the first-party product page states a 10GB traffic allowance at 100Mbps | capture: sha256:83cfcfe7c5a445c194fc5a484464f18a67494dee119586e9c4b1acb76854ed54 | quote: 10GB Traffic @ 100Mbps
  - [1] 2026-11-19: the first-party product page states 10GB Traffic @ 100Mbps and a 15-day free term on the same page | capture: sha256:83cfcfe7c5a445c194fc5a484464f18a67494dee119586e9c4b1acb76854ed54 | quote: 10GB Traffic @ 100Mbps
  - [1] 2026-11-19: the binding is a first-party 10GB Traffic @ 100Mbps volume quota | capture: sha256:83cfcfe7c5a445c194fc5a484464f18a67494dee119586e9c4b1acb76854ed54 | quote: 10GB Traffic @ 100Mbps
- sources:
  - [1] https://www.lusovps.com/products/vps-starter-ipv6
