# VPSLog

> vpslog.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpslog/ | JSON https://fshy.ajam.dev/api/v1/entity/vpslog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPSLog

- `egress/vpslog` | dead | evidence unverified | binding none | category free nat vps | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:52:57.446Z (live) | stale on 2026-11-19
- url https://distribute.vpslog.net
- price USD 0
- free tier: A free NAT IPv4 VPS obtained through a Telegram bot; the panel shows the IPv4 address, an SSH port, and a port list behind a SHOW button. [translated] | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No traffic figure is stated in published documentation.; ingress: udp | metered: no | free allowance: none published | source: [2]
- identity: any-phone | detail: A Telegram account is the only credential: log in through @vpslog_distribute_bot and receive a code. | country: None
- interface: ssh
- limits:
  - request-rate: a fixed list of assignable ports [1]
  - retention-clamped: renewal required; renewal interval not published [1]
- binding note: No byte cap is published, so nothing in the vocabulary fails at 1 TiB; the port list is the practical limit.
- interface detail: SSH to the shared IPv4 on the assigned port, plus a web panel.
- tooling: ssh, wg-quick
- composes with: none: the distribution host does not resolve, so no machine is issued and no endpoint exists.
- reliability: Shared IPv4 with a restricted port list; nothing about durability is documented.
- notes: Dead: the distribution host distribute.vpslog.net does not resolve (DNS failure), so the free NAT VPS is no longer issued. Kept as the archetype of the Telegram-only free NAT VPS, where only a listed subset of ports of a shared IPv4 is forwarded; the write-ups date from 2023.
- evidence note: The distribution host answers a DNS failure, so the offer is dead; the other sources are from 2023 and describe the offer while it was live.
- extras:
  - wg_path: native-conf
  - wg_detail: Root on a NAT VPS with a published port list; WG would bind a listed port. The port list is the open question: only a subset of ports is usable.
  - ingress: udp
  - volume_stated: No traffic figure is stated in the write-ups.
  - bytes_transit: yes
  - transit_note: Unverified.
  - death.on: 2026-11-04
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: Telegram-only signup, NAT IPv4 with a restricted port list, no traffic figure
  - [3] 2026-10-23: the free NAT machines were handed out through a Telegram bot in 2023
  - probe:distribute.vpslog.net 2026-11-04: the host distribute.vpslog.net does not resolve; a public DoH resolver answered NXDOMAIN for it and for vpslog.net | capture: sha256:293ea806d2e67139d4a4f6cdc2193eb853e9174773206cf65d10f1e03af4035b | quote: "error": "dns"
  - probe:distribute.vpslog.net 2026-11-04: the distribution host does not resolve | capture: sha256:fa819a7f5e09e92469c5ed6b7268a3348ac57fd29c66f07768a425db27f95452 | quote: "error": "dns"
- sources:
  - [1] https://v2cross.com/4198.html
  - [2] https://distribute.vpslog.net
  - [3] https://www.nodeseek.com/post-6248-1
