# Tunnelite

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-cristipufu/ | JSON https://fshy.ajam.dev/api/v1/entity/github-cristipufu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnelite

- `egress/tunnelite` | fails-egress | evidence documented | binding none | category tunnel software with a managed http tier | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/cristipufu/tunnelite
- price USD 0
- free tier: The managed version of Tunnelite supports HTTP(S), WebSocket (WS/WSS) and Server-Sent Events tunneling. If you need TCP tunneling, you'll have to host the server yourself. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published for the managed tier.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account on the managed service; self-hosting needs no account. | country: None
- interface: cli
- binding note: Managed tier supports HTTP and WebSocket only; TCP port forwarding requires self-hosted deployments.
- interface detail: CLI client.
- tooling: .NET client plus self-hosted SignalR server.
- composes with: Needs a VM for anything beyond HTTP.
- reliability: Self-hosted deployment depends on host infrastructure availability.
- notes: Recorded to separate the managed product from the self-hostable server, since the aggregator lists it as TCP/HTTP/WS.
- evidence note: A UDP listener in the managed service would change the verdict; none is described.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published for the managed tier.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: managed tier is HTTP(S), WS/WSS and SSE; 'If you need TCP tunneling, you'll have to host the server yourself.'
- sources:
  - [1] https://github.com/cristipufu/tunnelite
