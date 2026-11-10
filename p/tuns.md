# tuns.sh

> tuns.sh | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tuns/ | JSON https://fshy.ajam.dev/api/v1/entity/tuns.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tuns.sh

- `egress/tuns-sh` | paid-only | evidence documented | binding none | category ssh tunnel with a udp port forward, behind a paid membership | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tuns.sh/pricing
- price USD 2/month billed yearly | parsed USD 2/mo
- free tier: tuns.sh is a pico+ service ... [TIER: PICO+] $2 / month billed yearly ($24/yr) | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No transfer allowance is published. pico+ is sold with a 5GB storage quota 'across all services', which is disk, not bandwidth.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a pico account with pico+ membership at USD 2/month billed yearly; the free Starter tier does not include tuns. | country: None
- interface: ssh
- limits:
  - volume-quota: no transfer quota published; pico+ storage is 5GB across all services [2]
- binding note: Nothing countable is published, so no quota can be shown to fail first; the constraint that does bind is the subscription, because tuns appears only in the pico+ column. At 1 TiB/month the open question is an unpublished tolerance, not a number.
- interface detail: 'ssh tuns.sh help lists every command'.
- tooling: system ssh plus iproute2; no vendor binary.
- composes with: With a rented or free VM that allows tun, this is a WireGuard ingress for USD 2/month.
- reliability: UDP forwarding requires a tun interface and root privileges on the host system; unprivileged containers cannot create it.
- notes: The only entry that documents a raw public UDP port without WireGuard tooling, and it is behind USD 2/month. Two caveats from the same page: the client side needs root ('This needs to be done as root', 'sudo ssh -w 0:0'), and the hard mode uses a tap interface the vendor says it does not process ARP for.
- evidence note: The pico+ page lists tuns under 'EVERYTHING IN STARTER, PLUS:' with no free mention.
- extras:
  - wg_path: inside-udp
  - wg_detail: A public UDP port is mapped to a local UDP port over an SSH tun interface: 'sudo ssh -w 0:0 tuns.sh udp-forward=10000:local-ip:5553' then 'nc -u tuns.sh 10000'. A WireGuard listener on the local port is reachable at tuns.sh:10000, so this is a udp port forward rather than an overlay.
  - ingress: tcp+udp
  - volume_stated: No transfer allowance is published. pico+ is sold with a 5GB storage quota 'across all services', which is disk, not bandwidth.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: # UDP Tunneling section: 'ssh -w 0:0 tuns.sh udp-forward=10000:local-ip-of-machines-main-interface:5553' and 'nc -u tuns.sh 10000'; 'tuns.sh is a pico+ service'
  - [2] 2026-10-23: Starter is $0 free forever (prose, pages, pipe, pastes); tuns is listed only under pico+ at $2/month billed yearly
- sources:
  - [1] https://tuns.sh/pricing
  - [2] https://pico.sh/plus
