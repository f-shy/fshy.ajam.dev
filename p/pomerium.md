# Pomerium

> pomerium.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pomerium/ | JSON https://fshy.ajam.dev/api/v1/entity/pomerium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pomerium

- `egress/pomerium-zero` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category identity-aware access proxy with SSH reverse tunnel (user-run data plane, managed control plane) | tier Zero Personal
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:39.627Z (live) | stale on 2026-12-04
- url https://www.pomerium.com/pricing
- free tier: Zero Personal: 'Free'; managed control plane, one Core cluster run by the user, 10 routes, 1 cluster, 1 administrator, 1 custom domain. No byte, bandwidth or traffic allowance is published. | unit: mixed | metered on: none | read on: 2026-11-03 | source: [1] | note: The plan is denominated in routes (10), clusters (1) and administrators (1); the vocabulary has no routes unit, so mixed is the nearest term.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte cap, bandwidth cap or traffic meter is published on the pricing page, the reverse-tunneling page or the native SSH page. Traffic does not pass through the vendor: the data plane runs on a host the user supplies, and the vendor states 'there are no ingress or egress costs'. The only published tolerance is the 30 s default upstream route timeout for HTTP routes. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a Pomerium Zero account is required ('Create a (free) Pomerium Zero account'), and the account is associated with an email address; the sign-up form fields are not in the captured page, so whether it asks for more than an email is unverified: behind a sign-up. The open-source Core needs no account.
- interface: ssh, cli
- limits note: Zero Personal caps routes at 10, clusters at 1, administrators at 1, service accounts at 2 and custom domains at 1; none is a byte meter and none fits the six kinds. Reverse tunnels carry HTTP (443) and SSH (22) routes only; UDP is not supported.
- binding note: no byte, request or bandwidth cap is published, because the data plane runs on the user's own host; the route-count caps are not a volume meter
- interface detail: an OpenSSH client run as `ssh -R 0 HOST` registers as the upstream of an HTTP or SSH route (runtime flag `ssh_upstream_tunnel`); `pomerium-cli` carries TCP routes
- tooling: the user installs and runs the Pomerium Core data plane on a rented or free machine with a public address; the hosted Zero Console configures it; clients use a stock OpenSSH client
- composes with: The hosted Zero control plane and starter domain come first; the byte-carrying data plane is software the user installs and runs on a rented or free machine, so a public reader reaches the tunnel only through a host the user supplies, last in any chain.
- reliability: the reverse-tunneling mode is opt-in behind the `ssh_upstream_tunnel` runtime flag, and an HTTP route times out an upstream request after 30 s by default
- notes: Fails as a public ingress because no hosted relay exists: every plan runs the data plane on the user's host, and Zero Personal manages only the control plane (configuration, policies, starter domain, certificates). The first paid plan is Zero Business at $9 per user per month billed monthly or $7 billed annually (100 routes, 5 clusters, 20 administrators). The reverse tunnel carries HTTP and SSH routes, not UDP. Pomerium Enterprise has a self-hosted control plane at a custom price.
- evidence note: first-party pricing, reverse-tunneling and native SSH pages were captured and quoted; no tunnel was run, and the account sign-up form was not seen, so the identity detail is partly unverified
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No byte allowance is published.
  - bytes_transit: self-hosted
  - transit_note: the user's own data plane carries the bytes; the vendor's Zero control plane does not
- evidence:
  - [1] 2026-11-03: every plan, Zero Personal included, carries application traffic through a data plane that the user runs, so no hosted relay carries bytes | capture: sha256:9ec58c9bebb1f4bb5796c4350c851887f07bc6ec03a9af51d3444cb797fecd58 | quote: Every plan uses a self-hosted data plane to handle application traffic in your environment.
  - [1] 2026-11-03: the Zero Personal plan is a managed control plane with one user-run Core cluster | capture: sha256:9ec58c9bebb1f4bb5796c4350c851887f07bc6ec03a9af51d3444cb797fecd58 | quote: Managed control plane. Run one Core cluster in your environment.
  - [1] 2026-11-03: Zero Personal is free; the first paid plan, Zero Business, is $9 per user per month billed monthly or $7 billed annually | capture: sha256:9ec58c9bebb1f4bb5796c4350c851887f07bc6ec03a9af51d3444cb797fecd58 | quote: | Price Business billing is based on monthly active users. | Free | $7 annual or $9 monthly per user | Custom |
  - [1] 2026-11-03: Zero Personal allows 10 routes and Zero Business 100; the plan table lists no byte, bandwidth or traffic meter | capture: sha256:9ec58c9bebb1f4bb5796c4350c851887f07bc6ec03a9af51d3444cb797fecd58 | quote: | [Routes](https://www.pomerium.com/docs/reference/routes) Connections to protected applications and services, each with its own access policy. | 10 | 100 | Custom |
  - [2] 2026-11-03: the reverse tunnel is an OpenSSH reverse port-forward that carries HTTP and SSH routes | capture: sha256:f17abe90d07ac2e4ae477aeb480ce085893b880a5401446abbb7a3e0f48cc549 | quote: Any HTTP or SSH route can be configured to route upstream traffic through authenticated SSH clients using reverse port-forwarding.
  - [2] 2026-11-03: the reverse tunnel carries TCP-based HTTP and SSH routes only, with no UDP | capture: sha256:f17abe90d07ac2e4ae477aeb480ce085893b880a5401446abbb7a3e0f48cc549 | quote: UDP is not supported.
  - [2] 2026-11-03: the only two route protocols a reverse tunnel matches are HTTP (443) and SSH (22) | capture: sha256:f17abe90d07ac2e4ae477aeb480ce085893b880a5401446abbb7a3e0f48cc549 | quote: The `port` functions as a protocol selector. If the port is `443`, it will match HTTP routes. If the port is `22`, it will match SSH routes.
  - [3] 2026-11-03: SSH routes ride the user-run data plane on a configurable port next to the HTTP port | capture: sha256:44b888565ce292b5ee6c6ddf0f36408bce59a644a56c1fc2e5e0d40b03753872 | quote: SSH traffic flows through the Pomerium data plane alongside HTTP traffic, using a separate port (configurable).
  - [4] 2026-11-03: an HTTP route times out an upstream request after 30 seconds by default; this is the only published time tolerance and no byte cap is published | capture: sha256:375cf34bc044ddd73fb908d2f6142041ad393c8d6ed051e383f03c7b1bee483b | quote: If unset, the route inherits the global [`default_upstream_timeout`](https://www.pomerium.com/docs/reference/global-timeouts) (default `30s`).
  - [5] 2026-11-03: the free plan needs a Pomerium Zero account | capture: sha256:9ebecd4709a9d0f973321c38c2e969498a2e0b739a780b43fa1ca1b175e39b06 | quote: Create a (free) [Pomerium Zero account](https://console.pomerium.app/create-account)
  - [5] 2026-11-03: the Zero account is associated with an email address | capture: sha256:9ebecd4709a9d0f973321c38c2e969498a2e0b739a780b43fa1ca1b175e39b06 | quote: a default policy that only grants access if the user's email matches the one associated with your Pomerium Zero account
  - [6] 2026-11-03: the vendor does not carry the application traffic: the user hosts the proxy | capture: sha256:c2c3e0ec9e691cd42436deb705529d8089ae0114641e311cf9be7e1dfbbb297e | quote: You host the proxy, so we can't see anything you don't want us to.
  - [6] 2026-11-03: the vendor states there are no ingress or egress costs because traffic does not pass through its hosts | capture: sha256:c2c3e0ec9e691cd42436deb705529d8089ae0114641e311cf9be7e1dfbbb297e | quote: No extra hops means every user's request is faster and also cheaper because there are no ingress or egress costs
  - [7] 2026-11-03: the Core data plane source is open and the user installs and runs it | capture: sha256:6fef8ffbea20ccf34468e2a62d6f7e0f3f85d1d4e4d9a8482a201518061673a8 | quote: This repository's source code is available under the [Apache License 2.0](https://github.com/pomerium/pomerium/blob/main/LICENSE).
  - [8] 2026-11-03: the list names Pomerium in its overlay section with a managed control plane | capture: sha256:6397389f25e1417987795f9c2fd203ce677e801e565d43a4bccc2d85d05a2e8a | quote: Open-core; a managed control plane (Pomerium Zero) is available.
- sources:
  - [1] https://www.pomerium.com/pricing
  - [2] https://www.pomerium.com/docs/capabilities/reverse-tunneling
  - [3] https://www.pomerium.com/docs/capabilities/native-ssh-access
  - [4] https://www.pomerium.com/docs/reference/routes/timeouts
  - [5] https://www.pomerium.com/docs/get-started/quickstart
  - [6] https://console.pomerium.app/create-account
  - [7] https://github.com/pomerium/pomerium
  - [8] https://github.com/anderspitman/awesome-tunneling
