# sshuttle

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-sshuttle/ | JSON https://fshy.ajam.dev/api/v1/entity/github-sshuttle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sshuttle

- `egress/sshuttle` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.296Z (live) | stale on 2026-12-20
- url https://github.com/sshuttle/sshuttle
- price USD 0
- free tier: Open source project originally from one of the founders of Tailscale. Server doesn't require root; client does. Explicitly designed to avoid TCP-over-TCP issues. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. VPN over SSH; explicitly avoids TCP-over-TCP, no UDP listener.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: VPN over SSH; explicitly avoids TCP-over-TCP, no UDP listener. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README confirms a self-hosted program that needs remote network access via ssh; no hosted endpoint is offered.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Open source project originally from one of the founders of Tailscale. Server doesn't require root; client does. Explicitly designed to avoid TCP-over-TCP issues
  - [2] 2026-11-19: the first-party project README describes a program the user runs against a remote network the user already has ssh access to, with no hosted endpoint offered | capture: sha256:10d73699365a44f6fdc88ce9ad0a77564b50ddab65bf76a3b7aa1636d9655fa1 | quote: You don't necessarily have admin access on the remote network.
  - [2] 2026-11-19: the first-party README requires the user to have ssh access to a remote network, so egress begins with a host the user supplies | capture: sha256:10d73699365a44f6fdc88ce9ad0a77564b50ddab65bf76a3b7aa1636d9655fa1 | quote: You have access to a remote network via ssh.
  - [2] 2026-11-19: the first-party README confirms a self-hosted program that needs a remote network the user reaches via ssh | capture: sha256:10d73699365a44f6fdc88ce9ad0a77564b50ddab65bf76a3b7aa1636d9655fa1 | quote: You have access to a remote network via ssh.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/sshuttle/sshuttle
