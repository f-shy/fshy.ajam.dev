# NetBird Reverse

> netbird.io | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netbird/ | JSON https://fshy.ajam.dev/api/v1/entity/netbird.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetBird

- `egress/netbird-free` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category mesh network
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://netbird.io/pricing
- free tier: 100 machines on the cloud plan | unit: users | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: direct WireGuard where possible; the cloud relay otherwise, at an unpublished rate | metered: no | source: [1]
- identity: email | detail: a NetBird account
- interface: cli
- limits:
  - per-ip-shaping (binding): no number: the cloud-hosted Reverse Proxy is 'shared, best-effort'; 'High-volume or sustained data transfers may be subject to bandwidth limits, rate limiting, and fair-use policies' [2]
- limits note: counts of things, not rates, so no vocabulary kind names them: 100 machines plus 10 per user
- binding note: No byte figure exists for the cloud Reverse Proxy, so 1 TiB/month is planned against a sentence rather than a number. The L4 mode accepts TCP and UDP, so the transport test passes, and the reverse proxy is free to use; what fails first is the unwritten fair-use clause, with self-hosting named by the vendor as the way the restrictions do not apply.
- interface detail: netbird up
- tooling: part of interface detail
- composes with: signalling with a relay fallback; self-hosting removes the machine cap and adds a server to run.
- reliability: The cloud Reverse Proxy is beta, is shared and best-effort, and carries a named but unnumbered bandwidth and rate-limit clause; L4 services support TCP and UDP, and HTTP services do not.
- notes: 2026-10-23: the cloud plan has a public ingress with UDP. NetBird Reverse Proxy offers L4 'TCP', 'UDP' and 'TLS' service modes, and a UDP service is 'a UDP relay with session tracking. The proxy accepts UDP packets on the service's listen port and forwards them to your backend. Sessions are reaped after an idle timeout'. Cloud domains are free and appear 'with a Free badge'. The meter is discretionary: 'NetBird's cloud-hosted Reverse Proxy is provided on a shared, best-effort basis. High-volume or sustained data transfers may be subject to bandwidth limits, rate limiting, and fair-use policies', and 'These restrictions do not apply if you self-host NetBird'. Whether the Free plan is entitled to the feature is not stated on either the pricing page or the docs page.
- extras:
  - stale_after_days: 180
  - bytes_transit: conditional
  - transit_note: peers negotiate a direct WireGuard path; the operator's relay carries bytes only when that fails, at an unpublished rate
- evidence:
  - [1] 2026-10-22: 100 machines on the free tier
  - [3] 2026-10-23: 'UDP | L4 | UDP relay with session tracking. The proxy accepts UDP packets on the service's listen port and forwards them to your backend.'
  - [2] 2026-10-23: 'Cloud-hosted usage limits: NetBird's cloud-hosted Reverse Proxy is provided on a shared, best-effort basis. High-volume or sustained data transfers may be subject to bandwidth limits, rate limiting, and fair-use policies'
- sources:
  - [1] https://netbird.io/pricing
  - [2] https://docs.netbird.io/manage/reverse-proxy/service-configuration
  - [3] https://docs.netbird.io/manage/reverse-proxy

## NetBird Reverse Proxy

- `egress/netbird-reverse-proxy` | qualifies-with-caveat | evidence unverified | binding none | category WireGuard overlay with public L4 proxy | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:52:57.444Z (live) | stale on 2026-11-19
- url https://docs.netbird.io/manage/reverse-proxy
- price EUR 0 on Free, subject to whether the feature is included
- free tier: NetBird Free is 0 EUR, 'up to 5 users', '100 machines'; the pricing page lists P2P connections, Networks, SSO, access controls, Private DNS, Network Routes and NetBird SSH, and does not list Reverse Proxy on any plan. | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: none published: the pricing page charges per active user and machine and states no byte allowance; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: 'No credit card is required.' A NetBird account, which on Free is up to 5 users, with social SSO available. | country: None
- interface: cli, rest
- limits:
  - volume-quota: none stated; billing is per active user and machine [1]
- limits note: On NetBird's shared cloud proxy clusters the proxy assigns the listen port of each TCP and UDP service automatically, so the user cannot choose it. The idle timeout after which a UDP session is reaped defaults to 30 seconds.
- binding note: No byte quota and no rate is published, so nothing in the vocabulary fails at 1 TiB/month. Whether the feature is available on the free plan at all is the open question, and that is a plan gate rather than a limit kind.
- interface detail: 'The netbird expose command lets peers expose local services to the public internet through the NetBird reverse proxy'
- tooling: netbird CLI or the dashboard; no WireGuard client needed
- composes with: turns a free VM running only the NetBird agent into a host with a public TCP or UDP port on a NetBird domain, which removes the need for a tunnel broker prefix
- reliability: UDP sessions are reaped after an idle timeout; ephemeral expose sessions die 90 seconds after the daemon stops renewing; Rosenpass is not supported with the reverse proxy.
- notes: This is the only free-plan path found where a WireGuard peer gets a public TCP and UDP listener with no card and no account review, provided the feature is not gated. L4 services listen on a port on the proxy cluster and several services can share a port; custom ports depend on a cluster flag. A self-hosted deployment needs Traefik. The alternative reading, that Reverse Proxy is paid, cannot be excluded from the pages read, which is why the rung is unverified rather than documented. L4 services carry no browser SSO, only IP and country restrictions. Re-read 2026-10-23: the docs open with 'Availability: Reverse Proxy is currently in beta', and netbird expose needs an account administrator to enable Peer Expose and name allowed peer groups.
- evidence note: The L4 TCP and UDP capability is documented in the vendor's docs. Whether the free plan includes Reverse Proxy is not: it is absent from every plan list on the pricing page. One sentence naming the plan that includes it would raise this to documented.
- extras:
  - wg_path: inside-udp
  - wg_detail: 'Incoming traffic to that domain is received at the NetBird proxy cluster, then forwarded through an encrypted NetBird tunnel to the target peer.' The diagram is labelled 'through WireGuard tunnel', so the WireGuard datagram rides NetBird's own transport rather than a .conf a user holds.
  - ingress: tcp+udp
  - volume_stated: none published: the pricing page charges per active user and machine and states no byte allowance
  - bytes_transit: yes
  - transit_note: NetBird's proxy cluster terminates the public side and forwards over its WireGuard mesh
- evidence:
  - [2] 2026-10-23: HTTP and L4 modes, the UDP relay with session tracking, the public domain with automatic TLS, and the WireGuard tunnel to the peer
  - [1] 2026-10-23: Free is 0 EUR with up to 5 users and 100 machines, and Reverse Proxy appears in no plan list
  - [3] 2026-10-23: 'This supports both HTTP and L4 (TCP, UDP, TLS) protocols' and the ephemeral session model
  - [2] 2026-11-03: the shared cloud proxy clusters allocate TCP and UDP ports automatically | capture: sha256:60515264ef102df9bd282b3e8592e8bba32fab41a08cf5bd142802fb707dce63 | quote: the proxy cluster automatically assigns an available port to TCP and UDP services. This is the case for NetBird's shared cloud proxy clusters
  - [1] 2026-11-03: the Free plan lists up to 5 users and 100 machines, and no plan list names Reverse Proxy | capture: sha256:e934e62f6183499bcce599a04db93c7c2c32f2a14c31cde99294bb392000cdb5 | quote: up to 5 users
  - [2] 2026-11-03: the UDP session idle timeout is configurable per service and defaults to 30 seconds | capture: sha256:60515264ef102df9bd282b3e8592e8bba32fab41a08cf5bd142802fb707dce63 | quote: how long a UDP session can be idle before the proxy reaps it. Specified as a duration string (e.g., `30s`, `2m`). Defaults to 30 seconds.
  - [2] 2026-11-03: the docs page updated 2026-11-03 states that Reverse Proxy is in beta and names no plan that includes it | capture: sha256:60515264ef102df9bd282b3e8592e8bba32fab41a08cf5bd142802fb707dce63 | quote: Availability: Reverse Proxy is currently in beta.
  - [3] 2026-11-03: one peer can hold at most 10 active ephemeral expose sessions | capture: sha256:8c24adb75fe24c8da8f120012e28619914287891859a0de4004a51c3cbdc8310 | quote: Each peer can have a maximum of 10 active expose sessions at the same time.
  - [1] 2026-11-04: the free plan is limited to 5 users | capture: sha256:e934e62f6183499bcce599a04db93c7c2c32f2a14c31cde99294bb392000cdb5 | quote: up to 5 users
- sources:
  - [1] https://netbird.io/pricing
  - [2] https://docs.netbird.io/manage/reverse-proxy
  - [3] https://docs.netbird.io/manage/reverse-proxy/expose-from-cli
