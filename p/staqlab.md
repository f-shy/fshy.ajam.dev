# StaqLab Tunnel

> staqlab.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/staqlab/ | JSON https://fshy.ajam.dev/api/v1/entity/staqlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StaqLab Tunnel

- `egress/staqlab-tunnel` | fails-egress | evidence reported | binding none | category ssh tunnel (http and tcp) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://tunnel.staqlab.com/
- price USD 0
- free tier: Yes, it supports custom domain for free. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published on the page read.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account on the SSH service; the page does not describe signup terms. | country: None
- interface: ssh
- binding note: No quota is published and the transport is SSH-forwarded TCP, so the byte wall is unknown and UDP is absent.
- interface detail: ssh
- tooling: open-source client.
- composes with: TCP ingress only.
- reliability: Small operator, no status page found.
- notes: Thin page; recorded with the rung it earns rather than guessed.
- evidence note: The extraction was thin.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No byte allowance is published on the page read.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: SSH-based tunnel service; 'Yes, it supports custom domain for free.'
  - [2] 2026-10-23: 'SSH-based. A user is open source. The server doesn't appear to be.' (third party)
- sources:
  - [1] https://tunnel.staqlab.com/
  - [2] https://github.com/anderspitman/awesome-tunneling
