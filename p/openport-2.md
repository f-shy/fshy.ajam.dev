# openport.pw

> openport.pw | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openport-2/ | JSON https://fshy.ajam.dev/api/v1/entity/openport-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## openport.pw

- `egress/openport-pw` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category tunnel (hosted, single operator)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:54.999Z (live) | stale on 2026-12-20
- url https://openport.pw/
- free tier: openport is 100% free with no paywalls or ads; one permanent port, TCP and UDP simultaneously, zero signup, and no published limit of any kind | unit: none | metered on: unstated | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: anonymous | detail: no signup is required
- interface: cli
- limits:
  - per-ip-shaping (binding): unverified: no numeric per-user egress rate or byte cap is published; the page describes only 'gigabit reverse tunneling' [1]
- interface detail: an openport client binds a public port to a local one
- tooling: not documented
- composes with: a free persistent port for a single TCP protocol; it composes with an origin and with nothing that needs a second port.
- reliability: a single-operator service on one donated host, which is the class that decays in months
- notes: Reverse port forwarding utility providing single-port allocations without published numeric transfer limits.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the donated host forwards the port and the bytes cross it
  - wg_path: inside-udp
  - ingress: tcp+udp
- evidence:
  - [1] 2026-10-22: a free persistent port with no signup, and no quota stated
  - [1] 2026-10-23: 'Both TCP and UDP are enabled by default', the persistent assigned port, and 'OpenPort is an independent project funded entirely through voluntary crypto donations ... We need ~$50/month'
  - [1] 2026-11-19: the vendor page states the service is free with gigabit reverse tunneling and publishes no numeric per-user egress cap | capture: sha256:48fe96e768277362db832051fbdffa6ead761662bbb3120e9eaafe006cf3a27d | quote: openport is 100% free with no paywalls or user data collection. our high-speed servers, dedicated ports, and gigabit reverse tunneling are supported by our infrastructure partners:
  - [1] 2026-11-19: the service is free with gigabit reverse tunneling and no published numeric egress cap | capture: sha256:48fe96e768277362db832051fbdffa6ead761662bbb3120e9eaafe006cf3a27d | quote: openport is 100% free with no paywalls or user data collection. our high-speed servers, dedicated ports, and gigabit reverse tunneling are supported by our infrastructure partners:
- sources:
  - [1] https://openport.pw/
