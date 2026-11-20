# BILI NAT

> bili.ren | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bili/ | JSON https://fshy.ajam.dev/api/v1/entity/bili.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BILI NAT

- `egress/bili-nat` | paid-only | evidence documented | binding none | category tcp+udp port forward | tier personal
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://nat.bili.ren/
- price CNY 8.88 one-time
- free tier: Personal edition, CNY 8.88 one-time: 2 tunnels, free traffic from a daily check-in that does not reset, supports TCP/UDP/HTTP/HTTPS tunnels; this edition is available on registration. [translated] | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No monthly byte figure is published for the personal edition; traffic comes from a daily check-in that the vendor says does not reset at month end. The advanced edition states 500 GB of permanent traffic as a one-off.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Registration asks for an account name, an email address, an emailed verification code, an invite code and a password. The invite code link points to a storefront at afdian.com, so the account cannot be created without buying one; the entry price on the price table is CNY 8.88 one-time. | country: None
- interface: cli
- limits:
  - volume-quota: daily check-in traffic, not reset at month end; amount not published [1]
  - request-rate: 2 tunnels on the personal edition [1]
- binding note: The entry price is CNY 8.88 rather than zero, and the traffic figure is not published, so no constraint can be named from the page read.
- interface detail: A web console for tunnel creation and a frp-based client.
- tooling: frp-based client plus wg-quick on the local box
- composes with: One-off CNY 8.88 payment provides low-cost UDP ingress; requires non-zero payment.
- reliability: None established; the vendor advertises nodes from various upstream providers rather than owning them.
- notes: Community NAT FRP provider. Account creation costs a one-time fee of CNY 8.88, with bandwidth allocations earned through daily check-in. Optional one-off payment of CNY 199 provides 500 GB of transfer.
- evidence note: The price table is on the vendor page read. What would raise the rung is the check-in amount and whether a free account exists at all, which needs a console login.
- extras:
  - wg_path: inside-udp
  - wg_detail: TCP/UDP/HTTP/HTTPS tunnels are sold on every tier, so a WG datagram can ride a UDP tunnel. No WG config is issued.
  - ingress: udp
  - volume_stated: No monthly byte figure is published for the personal edition; traffic comes from a daily check-in that the vendor says does not reset at month end. The advanced edition states 500 GB of permanent traffic as a one-off.
  - bytes_transit: yes
  - transit_note: Community-donated relays carry the tunnel.
- evidence:
  - [1] 2026-10-23: personal edition CNY 8.88 one-time with 2 tunnels and check-in traffic; advanced edition CNY 199 with 500 GB; enterprise CNY 499/year with 1 TB monthly
  - [2] 2026-10-23: registration fields are account, email, emailed code, invite code obtained from afdian.com, password
- sources:
  - [1] https://nat.bili.ren/
  - [2] https://nat.bili.ren/?page=register
