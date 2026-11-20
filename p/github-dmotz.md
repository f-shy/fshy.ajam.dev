# Trystero

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-dmotz/ | JSON https://fshy.ajam.dev/api/v1/entity/github-dmotz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trystero (WebRTC signalling over BitTorrent / Nostr / MQTT / IPFS / Supabase / Firebase)

- `storage/trystero` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category relay/P2P — pure SIGNALLING, zero relayed bytes
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:34.759Z (live) | stale on 2026-11-25
- url https://github.com/dmotz/trystero
- free tier: Trystero makes browsers discover each other and communicate directly. No accounts. No deploying infrastructure. Just import and connect. | unit: mixed | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: Each room defaults to a 256 MiB receive budget. | bytes: 268435456 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Data flows peer-to-peer via WebRTC; the signalling network never sees the payload. The operator's cost is SDP messages only. | metered: no
- identity: anonymous | detail: Trystero makes browsers discover each other and communicate directly. No accounts. No deploying infrastructure. Just import and connect.
- interface: unknown
- limits note: Signalling only. Browser WebRTC connection-count limits force a room/namespace design.
- interface detail: JavaScript library, `joinRoom` API
- tooling: npm @trystero-p2p/*
- composes with: The cleanest signalling example: because only SDP crosses the third party, there is no bandwidth quota to hit and no operator who could impose one. Note the caveat that WebRTC needs a TURN relay when both peers are behind symmetric NAT. That is where real relaying cost reappears, and Trystero does not supply it.
- reliability: No TURN service included; symmetric-NAT pairs will fail to connect rather than fall back.
- notes: No storage and no relayed bandwidth: Trystero borrows an existing decentralised network purely to exchange WebRTC SDP offers.
- evidence note: the github.com/dmotz/trystero README states browsers discover each other and communicate directly with no accounts and no infrastructure to deploy
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'To establish a direct peer-to-peer connection with WebRTC, a signalling channel is needed to exchange peer information (SDP). Typically this involves running your own matchmaking server but Trystero abstracts this away'; strategies listed: BitTorrent, Nostr, MQTT, Supabase, Firebase, IPFS, self-hosted WebSocket relay
  - [2] 2026-10-21: 'Use our free cloud server or host your own PeerServer' (free signalling broker; relayed data still needs a TURN server)
  - [1] 2026-11-09: the README states Trystero needs no accounts and no infrastructure | capture: sha256:64ab416b4354d96a0442e1388c670823691bf1f7ba6aefa61246f173346393e6 | quote: Trystero makes browsers discover each other and communicate directly. No accounts. No deploying infrastructure. Just import and connect.
  - [1] 2026-11-09: the README states a default 256 MiB receive budget per room | capture: sha256:64ab416b4354d96a0442e1388c670823691bf1f7ba6aefa61246f173346393e6 | quote: Each room defaults to a 256 MiB receive budget. Set maxReceiveBytes in the room config to allow larger files or reduce memory use.
- sources:
  - [1] https://github.com/dmotz/trystero
  - [2] https://peerjs.com/
