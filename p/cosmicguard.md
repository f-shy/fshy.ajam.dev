# Cosmic Guard

> cosmicguard.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cosmicguard/ | JSON https://fshy.ajam.dev/api/v1/entity/cosmicguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cosmic Guard

- `egress/cosmic-guard` | trial-only | evidence documented | binding volume-quota | category game L4 reverse proxy (any UDP) | tier payg
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:10:53.038Z (live) | stale on 2026-12-20
- url https://cosmicguard.com/gaming/
- price USD 0.03 per average player per day, or USD 0.02 per GB transmit
- free tier: Start a free trial | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Unmetered volumetric traffic mitigation included with every plan; the gaming plan bills USD 0.03 per average player per day and the server plan USD 0.02 per GB of transmit bandwidth; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: card | detail: Signup at cosmicguard.com/signup; the free trial is the only zero-cost path and the paid plans are metered. The signup form was not opened. | country: None
- interface: rest
- limits:
  - volume-quota (binding): $0.02/ GB TX bandwidth on the server plan [3]
  - per-ip-shaping: $0.03/ avg player / day on the gaming plan [3]
- binding note: The vendor's pricing page states Unmetered DDoS mitigation on every plan and a $0.02/ GB TX bandwidth charge on the server plan. The transmit-byte meter is the first numeric constraint that runs; mitigation bandwidth itself is unmetered.
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
  - [3] 2026-11-19: the vendor pricing page states the server plan's transmit rate with a number and unit | capture: sha256:026127834e70a1b0d4cf90f696ec4d341b07f718cc0a6c2436769f9ac7fff5d4 | quote: $0.02/ GB TX bandwidth
  - [3] 2026-11-19: the vendor pricing page states the gaming plan's per-player-per-day rate | capture: sha256:026127834e70a1b0d4cf90f696ec4d341b07f718cc0a6c2436769f9ac7fff5d4 | quote: $0.03/ avg player / day
  - [3] 2026-11-19: mitigation is unmetered, so the first numeric binding constraint is the per-GB transmit charge | capture: sha256:026127834e70a1b0d4cf90f696ec4d341b07f718cc0a6c2436769f9ac7fff5d4 | quote: Unmetered DDoS mitigation
  - [3] 2026-11-19: the binding is the vendor's $0.02 per GB transmit charge | capture: sha256:026127834e70a1b0d4cf90f696ec4d341b07f718cc0a6c2436769f9ac7fff5d4 | quote: $0.02/ GB TX bandwidth
  - [3] 2026-11-19: the vendor states mitigation bandwidth is unmetered on every plan | capture: sha256:026127834e70a1b0d4cf90f696ec4d341b07f718cc0a6c2436769f9ac7fff5d4 | quote: Unmetered DDoS mitigation included with every plan
- sources:
  - [1] https://cosmicguard.com/
  - [2] https://cosmicguard.com/gaming/
  - [3] https://cosmicguard.com/pricing/
