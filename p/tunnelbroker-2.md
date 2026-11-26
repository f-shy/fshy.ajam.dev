# Hurricane Electric tunnelbroker

> tunnelbroker.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelbroker-2/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelbroker-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hurricane Electric tunnelbroker

- `egress/he-tunnelbroker` | qualifies-with-caveat | evidence documented | binding none | category IPv6 tunnel (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:29.663Z (live) | stale on 2026-12-26
- url https://tunnelbroker.net/
- free tier: Our free tunnel broker service enables you to reach the IPv6 Internet by tunneling over existing IPv4 connections from your IPv6 enabled host or router to one of our IPv6 routers. Ability to get your own /48 prefix once your tunnel is up | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a routed prefix
- retention: not applicable | source: [1]
- egress: not metered | metered: no | source: [1]
- identity: email | detail: a tunnelbroker account
- interface: cli
- limits note: the endpoint must answer ICMP and accept protocol 41. That is not write-gated in the vocabulary's sense, because no curator or review stands between the caller and the write; it is a capability the local ISP either passes or does not, and none of the six kinds names it
- binding note: nothing in the vocabulary binds: the protocol-41 requirement is a network capability the local ISP passes or blocks, not a queue with a person in it, and the /48 itself has no volume limit
- interface detail: a 6in4 tunnel to a Hurricane Electric endpoint
- tooling: iproute2, netplan
- composes with: the free answer to a static address rather than to capacity: it composes with a dual-stack front and only with clients that have IPv6.
- reliability: the site served an incomplete TLS chain on 2026-10-22
- notes: Re-read 2026-10-23 and unchanged: still a free tunnel over an existing IPv4 connection with a /48 once the tunnel is up, still protocol 41 or GRE, and WireGuard is not offered. A WireGuard client therefore cannot use it directly and would need a second host to terminate the tunnel.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the 6in4 tunnel carries the endpoint's IPv6 traffic over Hurricane Electric's network
  - extras.wg_path: none
  - extras.wg_test: fails: no WireGuard transport is offered, so no .conf can be obtained and no WG datagram is carried except inside a 6in4 or GRE outer packet the client builds itself
- evidence:
  - [1] 2026-10-22: a free tunnel plus a routed /48
  - probe:https://tunnelbroker.net/ 2026-10-22: the served TLS chain names only CN=tunnelbroker.net and openssl reports an incomplete chain; curl exits 35 CRYPT_E_REVOKED without -k and returns 200 with it
  - [1] 2026-10-23: 'Our free tunnel broker service enables you to reach the IPv6 Internet by tunneling over existing IPv4 connections' and 'Ability to get your own /48 prefix once your tunnel is up'
  - [1] 2026-11-25: the free tunnel broker and the /48 prefix are still offered | capture: sha256:dd76e6f776ab5f78ae56d90cc5643a19190a822628d59bb9ed14b5e52141be5a | quote: Our free tunnel broker service enables you to reach the IPv6 Internet by tunneling over existing IPv4 connections from your IPv6 enabled host or router to one of our IPv6 routers. ... Ability to get your own /48 prefix once your tunnel is up
  - [2] 2026-11-25: the tunnel is 6in4 over IPv4 and only the routed /64 or /48 is delegated reverse DNS | capture: sha256:9ab33db698480da1f60842d521213b77e30b2d6887d73196d193c164b9adf0ec | quote: In order to create a 6in4 tunnel, your IPv4 endpoint must be reachable. ... We delegate only to the routed /64 or /48s.
  - [1] 2026-11-25: registration is still a plain signup whose password is mailed | capture: sha256:dd76e6f776ab5f78ae56d90cc5643a19190a822628d59bb9ed14b5e52141be5a | quote: If you are a new user please register by clicking on Register below. After registering your password will be mailed to you and you can return here to activate your tunnel.
- sources:
  - [1] https://tunnelbroker.net/
  - [2] https://ipv6.he.net/certification/faq.php
