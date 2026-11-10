# Firezone

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-firezone/ | JSON https://fshy.ajam.dev/api/v1/entity/github-firezone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Firezone

- `egress/firezone` | fails-egress | evidence documented | binding none | category zero trust access built on WireGuard (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/firezone/firezone
- price USD 0
- free tier: 'Firezone is a secure remote access platform built on WireGuard. Connect users to private applications, databases, servers, and subnets with granular policies'. 'Sign up free' is offered with no number on the page read. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unverified: the pricing page renders client-side and its extracted text carries no plan numbers; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: app.firezone.dev sign-up | country: None
- interface: cli
- binding note: No published byte meter and no public listener. The design is the constraint: a Gateway 'in the network containing your Resources' answers authenticated Clients, not the internet.
- interface detail: Gateway deployment plus per-platform clients
- tooling: Firezone Gateway, the Firezone client (Apple, Android, Rust GUI), Docker
- composes with: a private access layer over a VPS; it publishes nothing, so it needs an ingress in front
- reliability: self-hosted production deployment is 'not officially supported'; published clients are only guaranteed against the managed service
- notes: The strongest WireGuard name that is still not an ingress: it is the same shape as Tailscale's private tailnet, not Funnel. Production self-hosting is explicitly unsupported, which matters if the plan was to run it on a free VPS.
- evidence note: A rendered read of the pricing page would fill the missing numbers; it would not change the ingress verdict.
- extras:
  - wg_path: none
  - wg_detail: WireGuard is the data plane but a user is the vendor's: 'WireGuard tunnels encrypt traffic between Clients and Gateways or between devices in a Device Pool'. No .conf export is documented.
  - ingress: none
  - volume_stated: unverified: the pricing page renders client-side and its extracted text carries no plan numbers
  - bytes_transit: yes
  - transit_note: Client to Gateway over WireGuard, with Relays when a direct path fails
- evidence:
  - [1] 2026-10-23: 'a secure remote access platform built on WireGuard. Connect users to private applications, databases, servers, and subnets'; 'Gateways run in your infrastructure'
  - [2] 2026-10-23: the page returned 200 with an extraction that yields plan names only ('Starter: Free tier for small teams'), no numbers
- sources:
  - [1] https://github.com/firezone/firezone
  - [2] https://www.firezone.dev/pricing
