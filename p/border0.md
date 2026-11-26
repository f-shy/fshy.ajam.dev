# Border0

> border0.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/border0/ | JSON https://fshy.ajam.dev/api/v1/entity/border0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Border0

- `egress/border0` | fails-egress | evidence documented | binding none | category privileged access management (acquired by Tailscale) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.border0.com/
- price unverified
- free tier: No allowance could be read: https://www.border0.com/pricing returns a 404 body. The home page offers 'Start for free today' with no number and no plan table. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unverified: no plan or allowance page could be read; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a portal account at portal.border0.com/register; the company is now part of Tailscale | country: None
- interface: cli
- binding note: No meter is published to bind. The deciding fact is elsewhere: the socket families carry no UDP and the generic TCP socket is explicitly 'with authentication', so a public unauthenticated reader is not the shape of the product.
- interface detail: connector deployed in the private network, clients authenticate through the portal
- tooling: Border0 connector and client, portal dashboard
- composes with: Private access layer using authenticated sockets; does not provide public arbitrary ingress.
- reliability: an acquired product with 'no short-term migrations planned' is a moving target; expect the control plane to fold into Tailscale
- notes: The 404 and the Tailscale sales link have three possible causes: the provider is dead, the pricing path moved, or the reader rewrote the link. The blog post and a law-firm deal note show the provider is dead only in part - the company was acquired on 2026-03-17 - but its docs still serve and the product still runs, so the record is fails-egress rather than dead. The reader did not rewrite the link: the origin returned a real 404 body with upstream_status 404.
- evidence note: The socket list and the acquisition are first-party and dated today. The free allowance is unverified because the pricing page is gone.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard and no .conf. A socket is a platform-managed service: 'HTTP(s), SSH, Database: MySQL, Postgres, TLS (Generic TCP ports with authentication)'.
  - ingress: tcp
  - volume_stated: unverified: no plan or allowance page could be read
  - bytes_transit: yes
  - transit_note: the connector carries the session to Border0's platform, which terminates it for an authenticated user
- evidence:
  - [2] 2026-10-23: 'The platform currently support various service types: HTTP(s) SSH Database: MySQL, Postgres TLS (Generic TCP ports with authentication)'
  - [3] 2026-10-23: 'Today I'm excited to share that Border0 has been acquired by Tailscale', dated March 17, 2026, with 'no short-term migrations planned'
  - [4] 2026-10-23: the sales path now says 'talk to us about Tailscale PAM', which is where Border0's commercial page leads
- sources:
  - [1] https://www.border0.com/
  - [2] https://docs.border0.com/docs/sockets
  - [3] https://www.border0.com/blogs/border0-is-joining-tailscale
  - [4] https://tailscale.com/contact/sales-border0
