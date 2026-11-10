# Apoxy

> apoxy.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apoxy/ | JSON https://fshy.ajam.dev/api/v1/entity/apoxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apoxy

- `compute/apoxy` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:41.664Z (live) | stale on 2026-12-05
- url https://apoxy.dev
- free tier: a free plan during an invite-only beta, requested rather than signed up for; endpoints dial out to edge relays so there are no inbound ports | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Free plan: 100 GB of bandwidth included, no overage on Free; bandwidth is client-ingress and client-egress totalled separately and the larger billed; traffic between the proxies and the origin is free | metered: yes | free allowance: 100 GB of bandwidth on the Free plan | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the free plan is invite-only: access is requested, not signed up for [1]
  - per-ip-shaping: endpoints dial out to edge relays, so no inbound port is opened and outbound is the only direction [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states that the free plan sits behind an invite-only beta. The product joins networks rather than renting machines, and the no-inbound-port design is the network answer
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a tunnel rather than a machine; there is no session to reap
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: no
  - net.ports: outbound only: endpoints dial out to edge relays
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Invite-only beta · Free plan · Request access' and 'Endpoints dial out to edge relays, so no inbound ports', quoted
  - [2] 2026-11-03: the Free plan includes 100 GB of bandwidth | capture: sha256:068cc6edb19b3c428f7288d0fb39ecd9b506fcd0c0272182cf5d23d0a1397e8b | quote: - 100 GB of bandwidth, included
  - [2] 2026-11-03: the egress meter bills the larger of ingress and egress | capture: sha256:068cc6edb19b3c428f7288d0fb39ecd9b506fcd0c0272182cf5d23d0a1397e8b | quote: Each billing period we total client-ingress and client-egress separately and bill whichever is larger; we never add the two together.
- sources:
  - [1] https://apoxy.dev
  - [2] https://apoxy.dev/pricing
