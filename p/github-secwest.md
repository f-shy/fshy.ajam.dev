# WGTCP

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-secwest/ | JSON https://fshy.ajam.dev/api/v1/entity/github-secwest.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WGTCP

- `egress/wgtcp` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/secwest/WGTCP
- price USD 0
- free tier: no service and no account; a patch to the Linux kernel WireGuard module with Ubuntu 24.04 binaries | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: both peers must run the patched kernel module, which means two hosts with module build or install rights; that is outside the vocabulary
- interface detail: wg and wg-quick unchanged
- tooling: Ubuntu 24.04 amd64 and arm64 archives, or build from source
- composes with: composes only with hosts where the operator controls the kernel, so a free-tier VM works and a managed tunnel does not.
- reliability: out-of-tree kernel patch for a specific kernel and distro; both peers must match
- notes: Kernel-level WireGuard implementation supporting TCP encapsulation directly within the kernel module. Requires running matching patched kernel modules on both endpoints.
- evidence note: a measured A/B against UDP WireGuard on a named path would raise it; the repository publishes its own comparison numbers, which are reported rather than reproduced here
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: "Keep the usual keys, peers, AllowedIPs, preshared keys, keepalives, wg, and wg-quick workflow" - the standard configuration drives it, with the transport swapped underneath
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: directly between the two patched peers, with no intermediary process
  - hosting_requirement: two hosts that can install the patched kernel module, one of them publicly reachable
  - last_release: no GitHub releases; last push 2026-08-04
  - stars: 27
- evidence:
  - [1] 2026-10-23: "adds a high-performance TCP transport patch to the Linux WireGuard kernel module" and the wg / wg-quick compatibility claim
  - [1] 2026-10-23: "It has not been approved, endorsed, or adopted by the WireGuard project"
  - [1] 2026-10-23: no GitHub releases, last push 2026-08-04, 27 stars
  - [1] 2026-10-23: the author reports 512 comparison cells and CPU reductions of 6.7-10.9 percent for clean-LAN bulk transfer; reported, not measured here
- sources:
  - [1] https://github.com/secwest/WGTCP
