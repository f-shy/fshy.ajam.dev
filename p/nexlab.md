# wsssh

> nexlab.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nexlab/ | JSON https://fshy.ajam.dev/api/v1/entity/nexlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wsssh

- `egress/wsssh` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.707Z (live) | stale on 2026-12-20
- url https://git.nexlab.net/nexlab/wsssh
- price USD 0
- free tier: Websocket jump host based SSH/SCP tunnelling with self hosted server. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Websocket jump host for SSH/SCP.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: the same as interface detail
- notes: Websocket jump host for SSH/SCP. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party README gives a command to start a self-hosted wssshd daemon; no hosted egress allowance is published.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Websocket jump host based SSH/SCP tunnelling with self hosted server.
  - [3] 2026-11-19: the daemon is started by the user; no hosted egress allowance is published | capture: sha256:04e69d0efbfe7b67964674dcff323f09ba672217c47e358ca2dd42d6100ce590 | quote: ./wssshd --host 0.0.0.0 --port 9898 --domain example.com --password mysecret
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://git.nexlab.net/nexlab/wsssh
  - [3] https://git.nexlab.net/nexlab/wsssh/-/raw/master/README.md
