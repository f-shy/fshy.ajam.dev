# Trystero

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-dmotz/ | JSON https://fshy.ajam.dev/api/v1/entity/github-dmotz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trystero (WebRTC signalling over BitTorrent / Nostr / MQTT / IPFS / Supabase / Firebase)

- `storage/trystero` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category relay/P2P — pure SIGNALLING, zero relayed bytes
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/dmotz/trystero
- free tier: No storage and no relayed bandwidth: Trystero borrows an existing decentralised network purely to exchange WebRTC SDP offers. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Data flows peer-to-peer via WebRTC; the signalling network never sees the payload. The operator's cost is SDP messages only. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits note: Signalling only. Browser WebRTC connection-count limits force a room/namespace design.
- interface detail: JavaScript library, `joinRoom` API
- tooling: npm @trystero-p2p/*
- composes with: The cleanest signalling example: because only SDP crosses the third party, there is no bandwidth quota to hit and no operator who could impose one. Note the caveat that WebRTC needs a TURN relay when both peers are behind symmetric NAT. That is where real relaying cost reappears, and Trystero does not supply it.
- reliability: No TURN service included; symmetric-NAT pairs will fail to connect rather than fall back.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'To establish a direct peer-to-peer connection with WebRTC, a signalling channel is needed to exchange peer information (SDP). Typically this involves running your own matchmaking server but Trystero abstracts this away'; strategies listed: BitTorrent, Nostr, MQTT, Supabase, Firebase, IPFS, self-hosted WebSocket relay
  - [2] 2026-10-21: 'Use our free cloud server or host your own PeerServer' (free signalling broker; relayed data still needs a TURN server)
- sources:
  - [1] https://github.com/dmotz/trystero
  - [2] https://peerjs.com/
