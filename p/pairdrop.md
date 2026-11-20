# pairdrop

> pairdrop.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pairdrop/ | JSON https://fshy.ajam.dev/api/v1/entity/pairdrop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pairdrop

- `storage/pairdrop` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.423Z (live) | stale on 2026-12-04
- url https://pairdrop.net/
- free tier: none reachable: WebRTC device-to-device only; the server is a signalling relay and only carries bytes as a TURN fallback. There is no object store, therefore no quota to multiply. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: anonymous
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: WebRTC device-to-device only; the server is a signalling relay and only carries bytes as a TURN fallback. There is no object store, therefore no quota to multiply.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: WebRTC device-to-device only; the server is a signalling relay and only carries bytes as a TURN fallback. There is no object store, therefore no quota to multiply.
  - [2] 2026-11-19: the first-party project states no signup is required | capture: sha256:b9a307403a303dcf93d9ec87126cc9927c3f220765c87add18179f5e15c47997 | quote: PairDrop: Transfer Files Cross-Platform. No Setup, No Signup.
  - [3] 2026-11-19: WebRTC device-to-device transfer; the signalling server carries no stored object data | capture: sha256:10e181d7e83edf0e8d8653293a4af51e3d1e401a897088ae86f5427139e29f79 | quote: It uses a WebRTC peer-to-peer connection. WebRTC needs a signaling server that is only used to establish a connection. The server is not involved in the file transfer.
- sources:
  - [1] https://pairdrop.net/
  - [2] https://github.com/schlagmichdoch/PairDrop
  - [3] https://github.com/schlagmichdoch/pairdrop/blob/master/docs/faq.md
