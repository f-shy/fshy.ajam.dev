# ShubhamTun

> shubham-dev.in | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shubham-dev/ | JSON https://fshy.ajam.dev/api/v1/entity/shubham-dev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ShubhamTun

- `egress/shubhamtun` | fails-egress | evidence documented | binding write-gated | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tun.shubham-dev.in/
- price USD 0
- free tier: Free - 3 active tunnels - Any subdomain - 1 reserved subdomain - 0 custom domains - 1 access key - HTTP Inspector - UDP requires a paid plan. All plans include: No request or bandwidth limits - No session timeout - HTTP and TCP tunnels (UDP on paid plans). | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No request or bandwidth limits on any plan, and no session timeout.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Sign in with GitHub or Google, then generate an API token: shubhamtun login --token sk_xxxxx. No card is mentioned for the free plan. | country: None
- interface: cli
- limits:
  - write-gated (binding): UDP requires a paid plan, cheapest listed at $80/month (Base) [1]
  - per-object-cap: 3 active tunnels and 1 access key on Free [1]
- binding note: The free tier has no UDP listener at all; the first UDP packet requires the $80/month Base plan, so volume is irrelevant to this workload.
- interface detail: shubhamtun http 3000 --domain myapp, shubhamtun tcp 22, shubhamtun udp 25565.
- tooling: curl -fsSL https://tun.shubham-dev.in/install.sh | sh; CLI and desktop app.
- composes with: Free TCP tunnel with no byte cap could front a WireGuard-over-TCP wrapper, but not native WireGuard.
- reliability: No session timeout claimed on any plan; the service is small and its pricing jumped from a $2.50/mo entry to $80/mo for UDP, which suggests repricing risk.
- notes: A single-developer service with a $80/month Base plan, which is expensive for the category. Free TCP with no bandwidth limit is the interesting part; UDP is not reachable at zero cost.
- evidence note: The pricing block rendered only in the search-index copy of the vendor page, not in the extracted body; a rendered read or a signup walk would confirm it at the same rung.
- extras:
  - wg_path: inside-udp
  - wg_detail: UDP is a paid-plan protocol: the free plan carries HTTP and TCP only, and the UDP command (shubhamtun udp 25565) is gated behind Base at $80/month.
  - ingress: tcp
  - volume_stated: No request or bandwidth limits on any plan, and no session timeout.
  - bytes_transit: yes
  - transit_note: The vendor relay terminates TLS and forwards to the local agent.
- evidence:
  - [1] 2026-10-23: Free: 3 active tunnels, any subdomain, 1 reserved subdomain, 1 access key, UDP requires a paid plan; no request or bandwidth limits; TCP on free, UDP on paid.
- sources:
  - [1] https://tun.shubham-dev.in/
