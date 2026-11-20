# 3VPC NAT

> Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/3vpc-nat/ | JSON https://fshy.ajam.dev/api/v1/entity/3vpc-nat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 3VPC NAT

- `egress/3vpc-nat` | trial-only | evidence reported | binding volume-quota | category free nat vps | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:52.013Z (live) | stale on 2026-12-04
- url https://www.nodeseek.com/post-967503-1
- price USD 0
- free tier: Product 1h1g 50G disk NAT Special VPS, Hong Kong zone 128, price USD 0.00, 7-day billing cycle. [translated from a review post] | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No traffic figure is given in the review; the limit named is 20 Mbps bandwidth.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Account registration. Published documentation does not describe identity verification requirements. | country: None
- interface: ssh
- limits:
  - per-ip-shaping: 20 Mbps [1]
  - retention-clamped: 7-day billing cycle [1]
  - volume-quota (binding): 500 GB/mo [2]
- binding note: The vendor's NAT product page states a 500 GB/mo traffic allowance; that volume quota is the first constraint a larger monthly volume reaches.
- interface detail: SSH key login out of the box on Ubuntu 24.04.
- tooling: ssh, wg-quick
- composes with: A throwaway WG endpoint for a week at a time, in Hong Kong.
- reliability: NAT only, no dedicated public IPv4. Bandwidth is 20 Mbps, which constrains high-throughput workloads.
- notes: A 7-day free window rather than a durable free tier. Useful as a test box, not as an ingress endpoint. The review is three weeks old at the time of writing.
- evidence note: One reviewer's post from 2026-10-06; no vendor page was read. The vendor's own page would raise the rung.
- extras:
  - wg_path: native-conf
  - wg_detail: NAT VPS with port mapping; WireGuard runs on the box; whether a UDP port is among the mapped ports is not stated.
  - ingress: udp
  - volume_stated: No traffic figure is given in the review; the limit named is 20 Mbps bandwidth.
  - bytes_transit: yes
  - transit_note: Hong Kong host carries the traffic.
- evidence:
  - [1] 2026-10-23: USD 0.00, 7-day cycle, 20 Mbps, 50 GB disk, port mapping works, no dedicated IPv4
  - [2] 2026-11-19: the vendor's ZONE 128 NAT product line has a 500 GB per month traffic allowance | capture: sha256:e0bcf052d63fea0c66793826cdc4b12c69ff680417d39f39ec9cb69f04895f45 | quote: Traffic 500 GB/mo
  - [2] 2026-11-19: a 500 GB per month traffic allowance with number and unit from the vendor's own product page | capture: sha256:e0bcf052d63fea0c66793826cdc4b12c69ff680417d39f39ec9cb69f04895f45 | quote: Traffic 500 GB/mo
  - [2] 2026-11-19: a first-party monthly traffic allowance binds before larger volumes | capture: sha256:e0bcf052d63fea0c66793826cdc4b12c69ff680417d39f39ec9cb69f04895f45 | quote: Traffic 500 GB/mo
  - [1] 2026-11-19: the review of the free seven-day trial reports the panel showing a 20 Mbps speed limit and a 500 GiB monthly traffic allowance | capture: sha256:4fddb28ffb116d05968fa0ac1493cfc2720ec41ae93e19a093bd18d2bcc76ced | quote: 面板标注 | 限速 20 Mbps，月流量 500 GiB（已用 81 MiB）
  - [2] 2026-11-19: the binding is a 500 GB/mo volume quota | capture: sha256:e0bcf052d63fea0c66793826cdc4b12c69ff680417d39f39ec9cb69f04895f45 | quote: Traffic 500 GB/mo
- sources:
  - [1] https://www.nodeseek.com/post-967503-1
  - [2] https://3vpc.com/products/hongkong-zone-128-nat
