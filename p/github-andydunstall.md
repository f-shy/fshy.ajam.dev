# piko

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-andydunstall/ | JSON https://fshy.ajam.dev/api/v1/entity/github-andydunstall.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## piko

- `egress/piko` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.144Z (live) | stale on 2026-12-20
- url https://github.com/andydunstall/piko
- price USD 0
- free tier: Piko is an open-source alternative to Ngrok, designed to serve production traffic and be simple to host (particularly on Kubernetes). MIT License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. HTTP and TCP in a self-hosted server.
- interface detail: not established
- tooling: The user installs and runs the Piko server and agent on a host the user supplies, such as a Kubernetes cluster.
- reliability: the same as interface detail
- notes: HTTP and TCP in a self-hosted server. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes an open-source reverse proxy the user hosts on their own cluster, with no hosted endpoint or byte allowance. The first-party source supersedes the aggregator list sentence.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Piko is an open-source alternative to Ngrok, designed to serve production traffic and be simple to host (particularly on Kubernetes). MIT License. Written in Go
  - [2] 2026-11-19: the first-party README describes a self-hosted reverse proxy with no hosted endpoint or published byte allowance | capture: sha256:89c1cdd78d843e723b9f3db2cb5d1d9d4f610ea5b39a168536e62b81df290af1 | quote: Piko is a reverse proxy that provides a secure way to connect to services that aren’t publicly routable, known as tunneling.
  - [2] 2026-11-19: the first-party README describes hosting the server on infrastructure the user supplies | capture: sha256:89c1cdd78d843e723b9f3db2cb5d1d9d4f610ea5b39a168536e62b81df290af1 | quote: Piko is built to be simple to host on Kubernetes.
  - [2] 2026-11-19: the first-party README is the basis for the egress finding | capture: sha256:89c1cdd78d843e723b9f3db2cb5d1d9d4f610ea5b39a168536e62b81df290af1 | quote: Piko is a reverse proxy that provides a secure way to connect to services that aren’t publicly routable, known as tunneling.
  - [2] 2026-11-19: the first-party README describes self-hosted software with no hosted endpoint | capture: sha256:89c1cdd78d843e723b9f3db2cb5d1d9d4f610ea5b39a168536e62b81df290af1 | quote: Piko is a reverse proxy that provides a secure way to connect to services that aren’t publicly routable, known as tunneling.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/andydunstall/piko
