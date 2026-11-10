# AGG Loop

> Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agg-loop/ | JSON https://fshy.ajam.dev/api/v1/entity/agg-loop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AGG Loop

- `egress/agg-loop` | fails-egress | evidence reported | binding none | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.producthunt.com/products/agg-loop
- price USD 0
- free tier: AGG Loop provides instant, highly secure localhost tunneling with zero config. 100% free forever with no bandwidth limits, fully backed by the Aeolink Group Inc. lab program. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No bandwidth throttles, no artificial session cuts, and no premium paywalls, per the launch text. No number is given.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: A CLI with zero config; no account, card or phone is mentioned in the launch text or the client repository. | country: None
- interface: cli
- limits:
  - volume-quota: no bandwidth limit claimed; no number published [1]
- binding note: If the no-limit claim held, nothing would bind on volume; the practical failure is protocol, since the edge is HTTP and WSS only.
- interface detail: A single terminal command, per the launch text; no syntax published.
- tooling: Native CLI from the Loop-Client repository.
- composes with: Nothing to chain while the product page is gone; if it returns, an HTTP-only edge.
- reliability: Product page missing within six months of launch; the funding is described as a corporate lab program, which is the kind of backing that ends without notice.
- notes: Free tier claims of unmetered bandwidth originate from a launch page that became unavailable six months after publication. Third-party documentation noted vendor terms specified free while launch announcements stated free forever. Published specifications remain unconfirmed without an active product page.
- evidence note: The vendor's own product page at agglabs.com/loop returns 404 and the site root served nothing, so only the launch post and third-party write-ups support the claim.
- extras:
  - wg_path: none
  - wg_detail: The client maps local services onto the AGG Labs edge using WebSocket Secure and native HTTP request processing, per the Loop-Client repository. No UDP listener is described.
  - ingress: http-only
  - volume_stated: No bandwidth throttles, no artificial session cuts, and no premium paywalls, per the launch text. No number is given.
  - bytes_transit: yes
  - transit_note: AGG Labs edge relays the traffic over WSS.
- evidence:
  - [1] 2026-04-19: Launch on 2026-04-19; 100% free forever, no bandwidth throttles, no session cuts, funded by Aeolink Group; product acquired from Deposure.
  - [2] 2026-10-23: 404: the product page could not be found, and the site suggests it may be part of a product that has not launched.
  - [3] 2026-10-23: Client maps local services to the AGG Labs edge over WebSocket Secure and native HTTP request processing.
- sources:
  - [1] https://www.producthunt.com/products/agg-loop
  - [2] https://agglabs.com/loop
  - [3] https://github.com/deposure-lab/Loop-Client
