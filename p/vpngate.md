# VPN Gate

> vpngate.net | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpngate/ | JSON https://fshy.ajam.dev/api/v1/entity/vpngate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPN Gate

- `ip-proxy/vpn-gate-sstp` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category volunteer VPN relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:16.544Z (live) | stale on 2026-12-20
- page https://fshy.ajam.dev/p/vpngate.md
- price USD 0: free, no registration, no allowance published
- free tier: Free with no registration: the relay nodes are volunteered by their operators, and a relay is reachable from a published list without creating an account. | unit: unlimited | metered on: unstated | read on: 2026-10-24 | source: [1] | note: No byte allowance is published on the front page, so unlimited here records that no quota is stated, not that none exists. The measurement puts the ceiling on throughput per client rather than on a byte count.
- per-object cap: not applicable: a tunnel and an exit address, not an object | source: [1]
- retention: not applicable | source: [1]
- egress: No traffic allowance in either direction is published. The offer is free with no registration, and the far end is a volunteer's own machine. The measured position is a rate rather than a cap: 16 MiB crossed in 918 s. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No registration: the node list is public and a relay is reachable directly, so no email, phone, card or account is collected at any point.
- interface: cli
- limits:
  - per-ip-shaping (binding): 16 MiB in 918 s, about 17.8 KiB/s (about 146 kbit/s) for one client against one relay; the slowest path measured on the dash.vpn slate
  - volume-quota: none published: free with no registration, and no byte allowance stated on the front page [1]
- limits note: The ceiling that was measured is a rate, not a byte cap, so it is filed under per-ip-shaping. The volume-quota entry records that no allowance was found, not that a generous one exists.
- binding note: At the measured rate the 45 GB month occupies about 28.5 days counted as 45 GB decimal and about 30.6 days counted as 45 GiB, so the shaped throughput saturates a month of continuous use before any quota, request count or object cap can be reached; the roughly 599,000 requests are small and are never the binding quantity.
- interface detail: SSTP carries the tunnel inside TLS. The relay's address is taken from the published node list and the connection is made with an SSTP client; this record measures the SSTP path only.
- tooling: An SSTP client inside a free or rented host with a full TCP stack, driven by hand from the published node list, plus a way to pick and re-pick a node as volunteers drop out. No rclone backend covers SSTP, so a wrapper would have to be written; that is a tooling note, not a verdict.
- composes with: A free outbound exit for fetches the gateway would otherwise make from a datacentre address, held as a fallback rather than a primary path because 16 MiB took 918 s.
- reliability: The transit TLS terminates at a volunteer's own machine rather than at an audited endpoint, and a volunteer's node can disappear or change its exit address at any time; the measured path was the slowest on the dash.vpn slate.
- notes: Performance and network classification for VPN Gate volunteer SSTP relays. The vendor publishes no data transfer allowance or byte limits, so limits reflect measured connection throughput rather than quota caps. Measured throughput: a 16 MiB payload transferred in 918 seconds (16,777,216 bytes over 918 s, approximately 18,275 bytes per second or 17.8 KiB/s). Network diversity: sweep measurements identified 35 distinct exit autonomous systems across active relays, predominantly residential and carrier networks led by Korea Telecom, SoftBank, KDDI, and LG Powercomm. The measured test transfer exited via AS8369 (INTERSVYAZ).
- evidence note: Throughput, exit ASN, and network diversity counts across 35 autonomous systems were measured on 2026-10-24. Free access without registration is documented from the vendor homepage read on 2026-10-24.
- extras:
  - rung: 5
  - rung_note: The exit identity is characterised at the registration class of the carrier ASNs behind the relays, not at one address: lane 4 counted 35 distinct exit ASNs led by consumer carriers, and the measured transfer exited one of them.
  - measured_exit_asn: AS8369
  - measured_exit_asn_name: INTERSVYAZ-AS
  - payload_mib: 16
  - elapsed_seconds: 918
  - derived_throughput: 16 MiB / 918 s = about 17.8 KiB/s, about 146 kbit/s
  - distinct_exit_asns: 35
  - leading_asns: Korea Telecom; SoftBank; KDDI; LG Powercomm
  - slowest_on_slate: dash.vpn
  - transport_tls_terminates_at: the volunteer relay operator
  - measured_exit_asn_registration: RIPE aut-num AS8369, as-name INTERSVYAZ-AS, status active, registrant organisation Intersvyaz-2 JSC (ORG-IJ7-RIPE), Russian Federation. RIPE carries no IP-type field, so the carrier class is read from the holder, not from a registry class.
  - registry_lookup_kornet: APNIC RDAP: 121.186.118.191 is in KORNET-KR, 121.160.0.0-121.191.255.255, type ALLOCATED PORTABLE (source KRNIC)
  - registry_lookup_bbtec: APNIC RDAP: 126.12.172.212 is in BBTEC, 126.0.0.0-126.31.255.255, type ALLOCATED PORTABLE
  - registry_lookup_lg_hellovision: APNIC RDAP: 59.86.200.244 is in LG-HELLOVISION-KR, 59.86.192.0-59.86.255.255, type ALLOCATED PORTABLE (source KRNIC)
  - registry_lookup_kddi_net: APNIC RDAP: 114.16.18.46 is in KDDI-NET, 114.16.18.0-114.16.18.255 (source JPNIC); the object carries no type field
  - registry_lookup_softether: APNIC RDAP: 219.100.37.212 is in SoftEther-CIDR-BLK-JP, 219.100.36.0-219.100.39.255 (source JPNIC); the object carries no type field
  - rdap_allocation.address: 121.186.118.191
  - rdap_allocation.netname: KORNET-KR
  - rdap_allocation.type: ALLOCATED PORTABLE
  - rdap_allocation.source: https://rdap.arin.net/registry/ip/121.186.118.191
  - rdap_allocation.handle: 121.160.0.0 - 121.191.255.255
  - rdap_allocation.range: 121.160.0.0-121.191.255.255
  - rdap_allocation.country: KR
  - rdap_allocation.class: consumer-isp
  - rdap_allocation.result: passes
  - rdap_allocation.remark: remark 'Korea Telecom'; a consumer carrier, not a hosting network
- evidence:
  - withheld 2026-10-10: A 16 MiB payload crossed the SSTP relay in 918 s and exited at AS8369 INTERSVYAZ; this is the slowest path measured on the dash.vpn slate.
  - [1] 2026-10-24: The relay is free and needs no registration, and its nodes are volunteered by their operators rather than run by the site.
  - probe:vpngate-exit-asn-sweep 2026-10-24: Lane 4 counted 35 distinct exit ASNs across the relays, led by Korea Telecom, SoftBank, KDDI and LG Powercomm. The sweep's own run date was not carried in the handoff, so this row is dated to the record rather than to the run.
  - probe:rdap.db.ripe.net/autnum/8369 2026-11-03: The registrant organisation ORG-IJ7-RIPE of RIPE aut-num AS8369 (as-name INTERSVYAZ-AS) is Intersvyaz-2 JSC. | capture: sha256:990e232b8c3cb7136e830470a8d65ecd68d889709b6d92453cb7b78d56a38d87 | quote: "fn", { }, "text", "Intersvyaz-2 JSC"
  - probe:rdap.db.ripe.net/autnum/8369 2026-11-03: RIPE aut-num AS8369 has as-name INTERSVYAZ-AS. | capture: sha256:990e232b8c3cb7136e830470a8d65ecd68d889709b6d92453cb7b78d56a38d87 | quote: "name" : "INTERSVYAZ-AS",
  - probe:rdap.arin.net/registry/ip/121.186.118.191 2026-11-03: 121.186.118.191 lies in KORNET-KR, 121.160.0.0-121.191.255.255, type ALLOCATED PORTABLE, source KRNIC. | capture: sha256:38132593c51dd5fb1c3b5ee22ec963bc90b196dc80b9322450ad74bb6d953fc3 | quote: "name":"KORNET-KR","type":"ALLOCATED PORTABLE"
  - probe:rdap.arin.net/registry/ip/126.12.172.212 2026-11-03: 126.12.172.212 lies in BBTEC, 126.0.0.0-126.31.255.255, type ALLOCATED PORTABLE, source APNIC. | capture: sha256:93e5a3eb67ca004fcf068d034f7124ee65b56ef63bceaf73d0cc7d258219bd01 | quote: "name":"BBTEC","type":"ALLOCATED PORTABLE"
  - probe:rdap.arin.net/registry/ip/59.86.200.244 2026-11-03: 59.86.200.244 lies in LG-HELLOVISION-KR, 59.86.192.0-59.86.255.255, type ALLOCATED PORTABLE, source KRNIC. | capture: sha256:56b490122b9dbc34f08ee80b7c99336def84100c838d8eda2e134e52cdc5f5a0 | quote: "name":"LG-HELLOVISION-KR","type":"ALLOCATED PORTABLE"
  - probe:rdap.arin.net/registry/ip/114.16.18.46 2026-11-03: 114.16.18.46 lies in KDDI-NET, 114.16.18.0-114.16.18.255, source JPNIC; the object carries no type field. | capture: sha256:cd66d71e7147f2c6b1c9eec04047ece6432567d5f18103157d27d1801552d925 | quote: "name":"KDDI-NET"
  - probe:rdap.arin.net/registry/ip/219.100.37.212 2026-11-03: 219.100.37.212 lies in SoftEther-CIDR-BLK-JP, 219.100.36.0-219.100.39.255, source JPNIC; the object carries no type field. | capture: sha256:355fe714da3c40b82ee4f1f98ffa10f9c3220b1eee75c8900143f7f0348e5868 | quote: "name":"SoftEther-CIDR-BLK-JP"
  - probe:rdap.db.ripe.net/autnum/8369 2026-11-03: RIPE aut-num AS8369 has as-name INTERSVYAZ-AS | capture: sha256:990e232b8c3cb7136e830470a8d65ecd68d889709b6d92453cb7b78d56a38d87 | quote: "name" : "INTERSVYAZ-AS",
  - probe:https://rdap.arin.net/registry/ip/121.186.118.191 2026-11-19: RDAP for the published 121.186.118.191 names KORNET-KR (remark Korea Telecom), range 121.160.0.0-121.191.255.255, type ALLOCATED PORTABLE, source KRNIC. | capture: sha256:a08839f772e8b8478ee550e7c9837db580e5dd6054a8558c11df9066ca4c1f52 | quote: "handle":"121.160.0.0 - 121.191.255.255","type":"ALLOCATED PORTABLE","startAddress":"121.160.0.0","endAddress":"121.191.255.255"
  - probe:https://rdap.arin.net/registry/ip/121.186.118.191 2026-11-19: RDAP confirms the published address is a consumer-carrier allocation (KORNET-KR, Korea Telecom). | capture: sha256:a08839f772e8b8478ee550e7c9837db580e5dd6054a8558c11df9066ca4c1f52 | quote: "handle":"121.160.0.0 - 121.191.255.255","type":"ALLOCATED PORTABLE","startAddress":"121.160.0.0","endAddress":"121.191.255.255"
  - probe:https://rdap.arin.net/registry/ip/126.12.172.212 2026-11-19: RDAP for published 126.12.172.212 names BBTEC (remark Japan Nation-wide Network of Softbank Corp.), source APNIC, a consumer carrier. | capture: sha256:8ee79b70ad502fdd8c656ca0a35bf00bc4b3dac3bae45c918a637ae8b5355d62 | quote: "handle":"126.0.0.0 - 126.31.255.255","type":"ALLOCATED PORTABLE","startAddress":"126.0.0.0","endAddress":"126.31.255.255"
  - probe:https://rdap.arin.net/registry/ip/59.86.200.244 2026-11-19: RDAP for published 59.86.200.244 names LG-HELLOVISION-KR (remark LG HelloVision Corp.), source KRNIC, a consumer ISP. | capture: sha256:f17fc4d43391a1592a22ca2db66300f04e62ee04c448a4abc8cf1530357ca6ed | quote: "handle":"59.86.192.0 - 59.86.255.255","type":"ALLOCATED PORTABLE","startAddress":"59.86.192.0","endAddress":"59.86.255.255"
  - probe:https://rdap.arin.net/registry/ip/114.16.18.46 2026-11-19: RDAP for published 114.16.18.46 names KDDI-NET (remark DION, KDDI CORPORATION), source JPNIC; the object carries no type field. | capture: sha256:ad8fe2945b6f3d917014e712847ad4b1b9601cc09e9b74803e33e5efcb019f63 | quote: "handle":"114.16.18.0 - 114.16.18.255","type":null,"startAddress":"114.16.18.0","endAddress":"114.16.18.255"
  - probe:https://rdap.arin.net/registry/ip/219.100.37.212 2026-11-19: RDAP for published 219.100.37.212 names SoftEther-CIDR-BLK-JP (remark SoftEther Corporation), source JPNIC; the object carries no type field. | capture: sha256:c80945347f386b618f9b7cce8ada23725a8c152d5479f856b692bfd2f6ae194e | quote: "handle":"219.100.36.0 - 219.100.39.255","type":null,"startAddress":"219.100.36.0","endAddress":"219.100.39.255"
- sources:
  - [1] https://www.vpngate.net/
