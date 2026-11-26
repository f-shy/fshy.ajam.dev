# jprq

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-azimjohn/ | JSON https://fshy.ajam.dev/api/v1/entity/github-azimjohn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## jprq

- `egress/jprq` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.939Z (live) | stale on 2026-12-20
- url https://github.com/azimjohn/jprq
- price USD 0
- free tier: Proxies over WebSockets. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: A hosted relay exists but offers only a 1-week trial then paid plans, so no free hosted allowance reaches the volume bar. The user installs the software and can run a self-hosted edge.
- interface detail: not established
- tooling: The user installs and runs the jprq software and authenticates with a token from the service; the hosted relay offers a 1-week trial then paid plans, and the software can be pointed at a self-hosted edge.
- reliability: the same as interface detail
- notes: WebSocket proxy. The first-party site and README were read on 2026-11-19: the hosted relay is a 1-week free trial then paid plans, the README notes members-only hosted use and a free self-host option.
- evidence note: First-party site and README read on 2026-11-19; the hosted relay offers a 1-week free trial then paid plans and the README notes members-only hosted use with a free self-host option. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Proxies over WebSockets. Written in Go.
  - [3] 2026-11-19: the first-party site offers only a 1-week trial then a paid plan, with no free hosted byte allowance | capture: sha256:ac097e55d29db6d70271d555456ae0bf8e0529ff441d314a829a5fb8c3a07790 | quote: Yes. JPRQ starts with a 1-week free trial. After that, the self-serve plan is $5 monthly or $42 yearly.
  - [2] 2026-11-19: the first-party README states a user is user-installed and offers a self-host option alongside the hosted relay | capture: sha256:0a4d5213bc202d60ebbf806e7bb63060de98b1ebe390ecbf24b7b84f1714a470 | quote: it still stays open and free to self-host
  - [3] 2026-11-19: the hosted relay has no free tier beyond a 1-week trial | capture: sha256:ac097e55d29db6d70271d555456ae0bf8e0529ff441d314a829a5fb8c3a07790 | quote: Yes. JPRQ starts with a 1-week free trial. After that, the self-serve plan is $5 monthly or $42 yearly.
  - [2] 2026-11-19: the first-party README establishes the hosted relay is members-only | capture: sha256:0a4d5213bc202d60ebbf806e7bb63060de98b1ebe390ecbf24b7b84f1714a470 | quote: jprq is now members-only service
  - [3] 2026-11-19: the first-party site replaces the list sentence as the basis | capture: sha256:ac097e55d29db6d70271d555456ae0bf8e0529ff441d314a829a5fb8c3a07790 | quote: Yes. JPRQ starts with a 1-week free trial. After that, the self-serve plan is $5 monthly or $42 yearly.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/azimjohn/jprq
  - [3] https://jprq.io/
