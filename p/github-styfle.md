# vgrok

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-styfle/ | JSON https://fshy.ajam.dev/api/v1/entity/github-styfle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vgrok

- `egress/vgrok` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.706Z (live) | stale on 2026-12-20
- url https://github.com/styfle/vgrok
- price USD 0
- free tier: ] - CLI to get a secure public URL for your local web server. Built with Vercel Sandbox and written in JavaScript. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Public URL for a local web server.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Public URL for a local web server. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party README instructs the user to install the Vercel CLI, log in and link a project, so the tunnel runs on the user's own Vercel account with no hosted egress allowance.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: ] - CLI to get a secure public URL for your local web server. Built with Vercel Sandbox and written in JavaScript.
  - [2] 2026-11-19: the tunnel runs on the user's own Vercel account after CLI login; no hosted egress allowance is published | capture: sha256:0d5cd9916033de8429ed0c5936d1994320992630dfb5e6bba3f13a55d02145a0 | quote: Next, install vercel cli from npm and login and link to a project:
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/styfle/vgrok
