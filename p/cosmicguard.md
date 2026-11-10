# Cosmic Guard

> cosmicguard.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cosmicguard/ | JSON https://fshy.ajam.dev/api/v1/entity/cosmicguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cosmic Guard

- `egress/cosmic-guard` | trial-only | evidence documented | binding volume-quota | category game L4 reverse proxy (any UDP) | tier payg
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://cosmicguard.com/gaming/
- price USD 0.03 per average player per day, or USD 0.02 per GB transmit
- free tier: Start a free trial | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Unmetered volumetric traffic mitigation included with every plan; the gaming plan bills USD 0.03 per average player per day and the server plan USD 0.02 per GB of transmit bandwidth; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: card | detail: Signup at cosmicguard.com/signup; the free trial is the only zero-cost path and the paid plans are metered. The signup form was not opened. | country: None
- interface: rest
- limits:
  - volume-quota (binding): USD 0.02 per GB transmit on the server plan [3]
  - per-ip-shaping: gaming plan is billed per average player per day at USD 0.03 [3]
- binding note: At 1 TiB/month on the server plan the transmit meter is what runs: 1 TiB is 1099.5 GB, so about USD 22 per month at the published USD 0.02/GB, assuming transmit only. That figure is arithmetic on the vendor's rate, not a quote.
- interface detail: Signup portal at cosmicguard.com/signup; billing is pay-as-you-go.
- tooling: portal configuration, no agent
- composes with: Fronts a public origin with arbitrary UDP; would front a free VM's UDP port at roughly USD 22 per TiB of transmit.
- reliability: Mitigation is unmetered and flood traffic is not billed; the payable meter is players or transmit bytes.
- notes: DDoS mitigation and Layer 4 proxy network supporting TCP and UDP. Free trial provides temporary testing; sustained service requires a paid subscription.
- evidence note: The UDP claim, the per-player and per-GB rates and 'Start a free trial' are first-party. The trial's length and allowance are not published on the pages read.
- extras:
  - wg_path: inside-udp
  - wg_detail: The product scrubs any public UDP port, so a WireGuard listener would be reachable through it; there is no free tier to do it on.
  - ingress: tcp+udp
  - volume_stated: Unmetered volumetric traffic mitigation included with every plan; the gaming plan bills USD 0.03 per average player per day and the server plan USD 0.02 per GB of transmit bandwidth
  - bytes_transit: yes
  - transit_note: Cosmic Guard's six PoPs scrub and forward the traffic
- evidence:
  - [2] 2026-10-23: The service is described for Rust, FiveM, RedM, Minecraft (Java + Bedrock), Ark and 'any UDP game', including 'your own custom UDP daemon'
  - [3] 2026-10-23: Gaming plan USD 0.03 per average player per day with unmetered mitigation and TCP/UDP compatibility; server plan USD 0.02 per GB transmit bandwidth
  - [1] 2026-10-23: Six PoPs across NA and EU, sub-second mitigation, and the only zero-cost entry is 'Start a free trial'
- sources:
  - [1] https://cosmicguard.com/
  - [2] https://cosmicguard.com/gaming/
  - [3] https://cosmicguard.com/pricing/
