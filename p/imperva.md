# Imperva DDoS Protection

> imperva.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imperva/ | JSON https://fshy.ajam.dev/api/v1/entity/imperva.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Imperva DDoS Protection

- `egress/imperva-ddos` | paid-only | evidence inferred | binding write-gated | category L4 anycast proxy (IP-level) | tier enterprise
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:23:43.555Z (live) | stale on 2026-12-26
- url https://www.imperva.com/products/ddos-protection/
- price unpublished (sales contract)
- free tier: No free tier is published; the page offers DDoS protection for individual IPs with no price. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No volume is published. The page states anycast routing and mitigation of layer 3/4 attacks including UDP floods, with no allowance, cap or rate.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: The page offers self-service onboarding for the platform; what an individual-IP account requires is unverified: not stated on the page. | country: None
- interface: unknown
- limits:
  - write-gated (binding): The page describes self-service onboarding through a portal for the Application Security platform; it publishes no price and no signup path for DDoS Protection for Individual IPs [1]
- binding note: No byte count is published, so no byte count can fail first. The sales contract is the gate at any volume, including 1 TiB/month.
- interface detail: not read; the marketing page documents no API for this product
- tooling: unknown: no client-side or API detail was read
- composes with: would take an origin IP directly, without a /24, if the individual-IP product works as its name suggests
- reliability: no reliability event recorded
- notes: The evidence supports 'protects an IP you point at Imperva', not 'forwards port X UDP to origin IP:port', and those are different products. No price, no trial, no self-serve path was found.
- evidence note: The page documents anycast L3/4 mitigation including UDP floods and 'DDoS Protection for Individual IPs', but it never says UDP is forwarded to an arbitrary origin port and port. Reading the individual-IP datasheet would raise this to documented.
- extras:
  - wg_path: inside-udp
  - wg_detail: protection for an individual IP is IP-level, so any UDP listener on that IP is carried; no tunnel or .conf is involved in the individual-IP shape.
  - ingress: tcp+udp
  - volume_stated: No volume is published. The page states anycast routing and mitigation of layer 3/4 attacks including UDP floods, with no allowance, cap or rate.
  - bytes_transit: yes
  - transit_note: traffic is diverted through Imperva's scrubbing network
- evidence:
  - [1] 2026-10-23: Imperva mitigates both Layer 3/4 (e.g., UDP floods, SYN floods, DNS amplification) and Layer 7 attacks. We also offer DDoS Protection for Individual IPs.
  - [1] 2026-10-23: Utilizing advanced Anycast routing and real-time capacity management, traffic is dynamically optimized across the most efficient paths
  - [1] 2026-11-25: the page claims self-service onboarding; the old 'no self-serve' wording is not on the page | capture: sha256:e12a30ca7c2bb6223037b77e7906bc8b57021cc18bbe15c8f6e75f424648b267 | quote: Imperva’s Application Security platform offers seamless self-onboarding and management, allowing users to easily configure and adjust DDoS protection settings through a self-service portal.
  - [1] 2026-11-25: self-service onboarding is stated; account requirements are not | capture: sha256:e12a30ca7c2bb6223037b77e7906bc8b57021cc18bbe15c8f6e75f424648b267 | quote: Imperva’s Application Security platform offers seamless self-onboarding and management, allowing users to easily configure and adjust DDoS protection settings through a self-service portal.
  - [1] 2026-11-25: the individual-IP product is named; the page gives no volume, rate or port detail | capture: sha256:e12a30ca7c2bb6223037b77e7906bc8b57021cc18bbe15c8f6e75f424648b267 | quote: We also offer DDoS Protection for Individual IPs.
- sources:
  - [1] https://www.imperva.com/products/ddos-protection/
