# photon

> photonengine.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/photonengine/ | JSON https://fshy.ajam.dev/api/v1/entity/photonengine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## photon (realtime / pun / fusion / chat)

- `storage/photon` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.980Z (live) | stale on 2026-12-04
- url https://www.photonengine.com/realtime/pricing
- free tier: none reachable: No storage product at all. The free tier is 100 CCU for Fusion/Quantum and traffic allowances measured in GB of message relay; there is no bucket, file API or persistence surface to write… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage product at all. The free tier is 100 CCU for Fusion/Quantum and traffic allowances measured in GB of message relay; there is no bucket, file API or persistence surface to write…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No storage product at all. The free tier is 100 CCU for Fusion/Quantum and traffic allowances measured in GB of message relay; there is no bucket, file API or persistence surface to write…
  - [2] 2026-10-21: cited as the basis of the rejection: No storage product at all. The free tier is 100 CCU for Fusion/Quantum and traffic allowances measured in GB of message relay; there is no bucket, file API or persistence surface to write by
  - [2] 2026-11-19: the free allowance is 100 concurrent users for Fusion and Quantum, a game relay quota | capture: sha256:6048c85893f9555a372d5f0422d82b81c77ce1ca1fc6f27a702d053b3e6904de | quote: Photon Engine proudly introduces a substantial upgrade to our service offerings: the launch of a FREE 100 Concurrent Users (CCU) tier
  - [1] 2026-11-19: the metered dimension is message relay traffic, not file or bucket storage | capture: sha256:b597dac1b3f9a5430368b28f082b63b656f03c31ba17ad485505548e91f7f9c3 | quote: The included traffic depends on your subscription plan. All incoming and outgoing messages to the Photon Cloud servers count towards the traffic limit.
- sources:
  - [1] https://www.photonengine.com/realtime/pricing
  - [2] https://blog.photonengine.com/new-free-100-ccu-for-photon-fusion-and-quantum-games/
