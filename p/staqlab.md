# StaqLab Tunnel

> staqlab.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/staqlab/ | JSON https://fshy.ajam.dev/api/v1/entity/staqlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StaqLab Tunnel

- `egress/staqlab-tunnel` | fails-egress | evidence reported | binding none | category ssh tunnel (http and tcp) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-20T04:02:26.823Z (live) | stale on 2026-12-05
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
- reliability: unverified: the host did not resolve in a probe on 2026-11-19; the landing page was last captured in an archive on 2026-08-12 and published no byte allowance
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
  - probe:staqlab-tunnel 2026-11-19: the live host returned no HTTP status in a probe on 2026-11-19, so the live page could not be re-read | capture: sha256:2046899a6244399240f3b23de59470ac1239c666b260fa4297f3b7e519683036 | quote: "status": null
  - [1] 2026-11-20: a live 2026-11-20 probe of https://tunnel.staqlab.com/ failed at the transport layer and read no HTTP status | capture: sha256:28a6232b83f0d7c360796add96307d7b907a69d3588461b431a60c8fd912d390 | quote: "error": "transport"
- sources:
  - [1] https://tunnel.staqlab.com/
  - [2] https://github.com/anderspitman/awesome-tunneling
