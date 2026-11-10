# UlziX Hong Kong free NAT

> nodeloc.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodeloc/ | JSON https://fshy.ajam.dev/api/v1/entity/nodeloc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UlziX Hong Kong free NAT

- `egress/ulzix-hk-nat` | qualifies-with-caveat | evidence reported | binding write-gated | category free nat vps (hosted, Hong Kong) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.nodeloc.com/t/topic/101622
- price CNY 0 on the free waves; the sibling 19-district public-benefit NAT is CNY 0.60 per month | parsed USD 0.09/mo
- free tier: [translated] 'To celebrate UlziX's half-year anniversary we are launching a pre-sale event for a permanently free Hong Kong NAT VPS. Datacenter: Hong Kong district 11, China Telecom CN2 with direct connections for the others. Configuration: 1 CPU core, 128 MB memory, 128 MB disk. Type: NAT virtual machine. Commitment: permanently free, no charge, no points deducted.' | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] No byte allowance is published for the free machine. The offer states 'the resource pool is contention-based and stability is not guaranteed; do not run CPU or bandwidth full for long periods or the machine will be rebuilt'. The sibling 19-district NAT product on the same order page caps at 10 Mbit in and 10 Mbit out.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: No national ID or local phone is required by the text read. | country: None
- interface: ssh, cli
- limits:
  - write-gated (binding): [translated] 'Everyone: renew manually once a month, permanently free.' [1]
  - per-ip-shaping: [translated] 'inbound bandwidth 10 Mbit, outbound bandwidth 10 Mbit' and 'IPv4 port mapping: 10' for the 19-district public-benefit NAT on the same order page [2]
- binding note: 10 Mbit carries 1 TiB/month at 3.39 Mbit/s sustained (1099511627776 bytes over 30 days), so the shaping does not bind.
- interface detail: [translated] The order page lists per-district NAT products at idc-new.ulzix.com/order; the review shows panel-set port mapping and an Alpine or Debian image.
- tooling: root on a KVM guest, so wg-quick, SSH and any port-forwarding rule the panel exposes; images are Ubuntu 22.04 or Debian 12 per the review
- composes with: A Hong Kong root guest with ten forwarded ports is the endpoint a free Japanese or Korean tunnel could not provide, and it composes with any WireGuard client already running.
- reliability: Contended resource pool with rebuilds for long saturation; multi-account buying is detected and all machines on the account are deleted; a missed monthly renewal ends the machine; the public-benefit district is explicitly 'no after-sales support'.
- notes: The strongest Hong Kong lead and the only free NAT host in it with a stated port-mapping count: a real KVM guest with root, ten forwarded IPv4 ports, Hong Kong district 11 on CN2, permanently free with monthly renewal. Its cost is supply: 30 machines per wave, six waves so far, each gone in minutes, and the operator explicitly rebuilds machines that saturate the pool. The free wave and the 0.60 CNY public-benefit product are different products on the same order page; only the port count and 10 Mbit shaping come from the paid card and that transfer is marked reported, not measured. Country: Hong Kong.
- evidence note: Port-mapping count and bandwidth are quoted from the paid sibling product, which may not match the free machine. Registering an account and reading the panel would raise it to documented.
- extras:
  - wg_path: native-conf
  - wg_detail: [translated] 'Type: NAT virtual machine' with root on a KVM guest, so WireGuard is installed and wg-quick writes the .conf. The sibling product on the same order page states 'IPv4 port mapping: 10' and 'inbound bandwidth 10 Mbit, outbound bandwidth 10 Mbit'.
  - ingress: tcp+udp
  - volume_stated: [translated] No byte allowance is published for the free machine. The offer states 'the resource pool is contention-based and stability is not guaranteed; do not run CPU or bandwidth full for long periods or the machine will be rebuilt'. The sibling 19-district NAT product on the same order page caps at 10 Mbit in and 10 Mbit out.
  - bytes_transit: yes
  - transit_note: The guest sits behind a shared Hong Kong IPv4 with ten mapped ports.
- evidence:
  - [1] 2026-10-23: [translated] 'permanently free, no charge, no points deducted'; '1 CPU core, 128 MB memory, 128 MB disk'; 'Type: NAT virtual machine'; 'Hong Kong district 11, China Telecom CN2'.
  - [1] 2026-10-23: [translated] 'Everyone: renew manually once a month, permanently free', and 'the resource pool is contention-based, stability is not guaranteed, do not run CPU or bandwidth full for long periods or the machine will be rebuilt'.
  - [2] 2026-10-23: [translated] The Hong Kong public-benefit NAT product card: 'inbound bandwidth 10 Mbit', 'outbound bandwidth 10 Mbit', 'IPv4 port mapping: 10', at 0.60 CNY per month for the 1H128M tier.
  - [3] 2026-10-23: [translated] A third-party review of the free machine: 'a permanently free Hong Kong NAT VPS', '1 core, 128 MB, 128 MB, NAT virtual machine, shared bandwidth (contended resource pool)'.
- sources:
  - [1] https://www.nodeloc.com/t/topic/101622
  - [2] https://idc-new.ulzix.com/order
  - [3] https://www.nodeloc.com/t/topic/101672
