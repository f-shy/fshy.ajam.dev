# Kemnir

> kemnir.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kemnir/ | JSON https://fshy.ajam.dev/api/v1/entity/kemnir.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kemnir

- `egress/kemnir` | fails-egress | evidence unverified | binding write-gated | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:52:58.389Z (live) | stale on 2026-11-19
- url https://kemnir.com/
- price USD 0
- free tier: A free plan is named (portless Minecraft Java hostnames 'on every plan including free'); generic access is planned 'on a paid plan, deliberately'. No price, byte allowance or plan table is published, and the beta is waitlist-only. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Nothing is published. The site is a pre-launch waitlist page.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Joining the waitlist requires an email address; the page promises no spam. | country: None
- interface: unknown
- limits:
  - write-gated (binding): beta waitlist; no account can be created yet [1]
- binding note: There is no product to measure: the gate is the closed beta, and no quota can fail before it opens. The page states generic access is for a paid plan and the free plan is game-hostname oriented, so a free general-purpose tunnel is not planned; no UDP path is named.
- interface detail: One small agent dials out; the page names no CLI, API or configuration format.
- tooling: A Windows app and a single binary are promised; neither is downloadable from the page read.
- composes with: Would sit between a home service and friends' clients; with no launched product it composes with nothing yet.
- reliability: Not operating; nothing can be said about reliability.
- notes: Private relay software providing internal network connectivity without exposing public inbound internet ports.
- evidence note: The waitlist page names no price, allowance or retention window ('The retention window gets published before launch'); the numbers await a launch and a pricing page.
- extras:
  - wg_path: none
  - wg_detail: The product page offers generic TCP behind a private relay and names no UDP forwarding and no WireGuard configuration.
  - ingress: tcp
  - volume_stated: Nothing is published. The site is a pre-launch waitlist page.
  - bytes_transit: yes
  - transit_note: A Kemnir edge relay would carry the bytes.
- evidence:
  - [1] 2026-10-23: Pre-beta waitlist page: private relay for services at home, one outbound agent, generic TCP, no ports; no price, no plan, no allowance.
  - [1] 2026-11-03: generic (non-game) access is planned for a paid plan, not the free one | capture: sha256:9c6c80d6297cde95f6ec65fcbb7a6ac8a232b885100638711515357ae4f8529f | quote: Generic access follows once that's running under real load — on a paid plan, deliberately, so it doesn't become free infrastructure for whoever wants to abuse it.
  - [1] 2026-11-03: the waitlist takes an email address and nothing can be tried before the beta opens | capture: sha256:9c6c80d6297cde95f6ec65fcbb7a6ac8a232b885100638711515357ae4f8529f | quote: The beta opens to the waitlist first. Leave an email and you'll hear from us when there's something real to try — not before.
  - [1] 2026-11-03: a free plan is named, and its use named on the page is Minecraft Java hostnames | capture: sha256:9c6c80d6297cde95f6ec65fcbb7a6ac8a232b885100638711515357ae4f8529f | quote: Minecraft Java players type it with no port number at all, on every plan including free.
  - [1] 2026-11-04: the beta is waitlist-only and takes an email address | capture: sha256:9c6c80d6297cde95f6ec65fcbb7a6ac8a232b885100638711515357ae4f8529f | quote: The beta opens to the waitlist first. Leave an email and you'll hear from us when there's something real to try — not before.
- sources:
  - [1] https://kemnir.com/
