# netmask

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-josephdove/ | JSON https://fshy.ajam.dev/api/v1/entity/github-josephdove.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## netmask

- `egress/netmask` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.740Z (live) | stale on 2026-12-20
- url https://github.com/josephdove/netmask
- price USD 0
- free tier: A TCP/UDP self-hostable network tunneling solution that supports IPv4 and IPv6. Client has a GUI. MIT License. Written in Python. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. A TCP/UDP self-hostable network tunnel.
- interface detail: not established
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: A TCP/UDP self-hostable network tunnel. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes a self-hostable TCP/UDP tunnel with a server the user runs and no hosted endpoint or byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: A TCP/UDP self-hostable network tunneling solution that supports IPv4 and IPv6. Client has a GUI. MIT License. Written in Python.
  - [2] 2026-11-19: the first-party README presents the tool as self-hostable software with no hosted endpoint | capture: sha256:36b06b770560aff48b745acce4cdb18124cfb71d59f1ec02d666f27c18179592 | quote: Netmask is a robust tool designed to facilitate secure and seamless network tunneling, similar to Ngrok, but with the added advantage of supporting TCP/UDP protocols and being entirely self-hostable.
  - [2] 2026-11-19: the first-party README describes a server the user runs, so the software is installed and run by the user | capture: sha256:36b06b770560aff48b745acce4cdb18124cfb71d59f1ec02d666f27c18179592 | quote: Netmask Server (netmasks): The server component, netmasks, is responsible for listening to incoming connections from clients and managing the tunnels.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:36b06b770560aff48b745acce4cdb18124cfb71d59f1ec02d666f27c18179592 | quote: Netmask is a robust tool designed to facilitate secure and seamless network tunneling, similar to Ngrok, but with the added advantage of supporting TCP/UDP protocols and being entirely self-hostable.
  - [2] 2026-11-19: the first-party README describes a server the user runs, so the software is installed and run by the user | capture: sha256:36b06b770560aff48b745acce4cdb18124cfb71d59f1ec02d666f27c18179592 | quote: Netmask is a robust tool designed to facilitate secure and seamless network tunneling, similar to Ngrok, but with the added advantage of supporting TCP/UDP protocols and being entirely self-hostable.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/josephdove/netmask
