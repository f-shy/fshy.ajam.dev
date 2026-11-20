# hsync

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-monteslu/ | JSON https://fshy.ajam.dev/api/v1/entity/github-monteslu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hsync

- `egress/hsync` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.939Z (live) | stale on 2026-12-20
- url https://github.com/monteslu/hsync
- price USD 0
- free tier: Works in Node.js and browsers. Any two instances can easily pair and make a peer-to-peer WebRTC connection to forward TCP/UDP ports (even in browser). No additional signaling server needed. Written in JavaScript. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: A default hosted hsync.tech server exists but publishes no byte allowance and limits a connection to 4 hours; no free hosted allowance reaches the volume bar. Forwards TCP/UDP ports between two hsync instances, and a user can also run a private hsync-server.
- interface detail: not established
- tooling: The user installs and runs the hsync software (npm i -g hsync, npx hsync, or a browser script); a default hosted hsync.tech server exists and a user can point the software at a self-hosted hsync-server.
- reliability: The default hosted hsync.tech server answered HTTP 502 on 2026-11-19.
- notes: Forwards TCP/UDP ports between two hsync instances. The first-party README was read on 2026-11-19; it names a default hosted hsync.tech server with a 4-hour connection limit and no published byte allowance, and allows a self-hosted hsync-server.
- evidence note: First-party project README read on 2026-11-19; it names a hosted default server with a 4-hour connection limit, no published byte allowance and a self-host option. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Works in Node.js and browsers. Any two instances can easily pair and make a peer-to-peer WebRTC connection to forward TCP/UDP ports (even in browser). No additi
  - [2] 2026-11-19: the first-party README names a default hosted server with a 4-hour connection limit and no published byte allowance | capture: sha256:466dcd59344de357a1c87d79c1d23fe9004125869bf1e25ef94bdebd3623556d | quote: by default hsync will connect to the default hsync.tech server and allow a connection for up to 4 hours.
  - [2] 2026-11-19: the first-party README describes a user-installed client that connects to an hsync-server, with a hosted default and a self-hostable option | capture: sha256:466dcd59344de357a1c87d79c1d23fe9004125869bf1e25ef94bdebd3623556d | quote: hsync is a [reverse-proxy](https://en.wikipedia.org/wiki/Reverse_proxy) client for node.js and browsers that connects to an [hsync-server](https://github.com/monteslu/hsync-server).
  - [2] 2026-11-19: the hosted default has a 4-hour limit and no published byte allowance | capture: sha256:466dcd59344de357a1c87d79c1d23fe9004125869bf1e25ef94bdebd3623556d | quote: by default hsync will connect to the default hsync.tech server and allow a connection for up to 4 hours.
  - [2] 2026-11-19: the first-party README establishes the hosted default and its limit | capture: sha256:466dcd59344de357a1c87d79c1d23fe9004125869bf1e25ef94bdebd3623556d | quote: by default hsync will connect to the default hsync.tech server and allow a connection for up to 4 hours.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis | capture: sha256:466dcd59344de357a1c87d79c1d23fe9004125869bf1e25ef94bdebd3623556d | quote: by default hsync will connect to the default hsync.tech server and allow a connection for up to 4 hours.
  - probe:https://hsync.tech 2026-11-19: the default hosted server answered HTTP 502 on 2026-11-19 | capture: sha256:a9964801ac61b043d66ebc8d739266348cf915b945faaff6d78ab49c1cdad1e9 | quote: "status": 502
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/monteslu/hsync
