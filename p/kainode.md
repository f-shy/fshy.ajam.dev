# Kainode

> kainode.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kainode/ | JSON https://fshy.ajam.dev/api/v1/entity/kainode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kainode

- `egress/kainode-vps-pro` | paid-only | evidence reported | binding volume-quota | category vps (hosted, Singapore, KVM, 100 Mbps port, single IPv4) | tier VPS Pro
- identity a placeholder: card and phone unknown | verified 2026-11-04T12:11:58.416Z (live) | stale on 2026-11-19
- url https://kainode.com/
- price USD 7.49 per month with 1 TB bandwidth included (vendor page price, renews at USD 7.49 a month); the vendor page shows no coupon price | parsed USD 7.49/TB-mo
- free tier: No free tier. VPS Pro is USD 4.89 a month after a 30 percent recurring coupon: 2 vCPU, 4 GB RAM, 60 GB SSD, 1 TB transfer a month, a 100 Mbps port and one IPv4, in Singapore. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1 TB a month transfer on VPS Pro with a 100 Mbps port. The post and the terms state no overage price and no post-allowance throttle: not published in the pages read; the terms say only that bandwidth and resource limits apply. | metered: yes | free allowance: 1 TB a month | source: [1]
- identity: card | detail: The offer post states cards are accepted through Stripe. Whether another method or any phone or ID check applies is behind the checkout and was not read: unverified: behind a sign-up.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB a month transfer on VPS Pro; overage rule not published [1]
  - per-ip-shaping: 100Mbps Port [1]
- binding note: The 1 TB monthly transfer allowance is the stated volume limit; no overage rule is published.
- interface detail: Full root on KVM per the offer post; the control panel was not read.
- tooling: ssh; the guest runs what its kernel supports.
- composes with: One IPv4 and a 100 Mbps port; no IPv6 is listed in the offer table and no NAT is stated. Outbound port 25 is blocked by default.
- reliability: The VPS service policy reserves limiting, suspension or termination of a service whose activity falls outside the approved usage standards; the vendor plan table loaded empty in a plain read.
- notes: Singapore KVM VPS with a 100 Mbps port. Larger plans raise the transfer allowance to 8 TB at USD 26.24 a month.
- evidence note: Price, transfer and port come from a third-party offer post dated 2026-09-03; the vendor VPS page returned an empty plan table. Port 25 and the bandwidth line are vendor terms lines.
- extras:
  - nat: none stated; one IPv4 is listed
  - ipv6: not listed in the offer table
  - inbound: not stated
  - udp: not stated
- evidence:
  - [1] 2026-11-04: VPS Pro is USD 4.89 a month after coupon with 1 TB transfer, 100 Mbps and one IPv4 | capture: sha256:5c2fecd8a0f3d1caf5035e6223b7780d2b62863a6f2b4a92b4cc44349fcb4e8f | quote: 2 vCPU4GB RAM60GB SSD Storage1TB Transfer100Mbps Bandwidth1× IPv4KVM VirtualizationCoupon: SGLEB30$4.89/month (after coupon)
  - [1] 2026-11-04: the 30 percent coupon discount recurs | capture: sha256:5c2fecd8a0f3d1caf5035e6223b7780d2b62863a6f2b4a92b4cc44349fcb4e8f | quote: Particularly since these offers include a recurring 30% recurring discount for our readers!
  - [1] 2026-11-04: payment is by card through Stripe | capture: sha256:5c2fecd8a0f3d1caf5035e6223b7780d2b62863a6f2b4a92b4cc44349fcb4e8f | quote: They accept credit and debit cards through Stripe.
  - [1] 2026-11-04: the Singapore plans carry a 100 Mbps port | capture: sha256:5c2fecd8a0f3d1caf5035e6223b7780d2b62863a6f2b4a92b4cc44349fcb4e8f | quote: 100Mbps Port
  - [2] 2026-11-04: outbound port 25 is blocked on VPS plans | capture: sha256:152b556bd82640f48df45a9577c380fddf0da7d3723c3eb5e1af1ccb9365dc35 | quote: SMTP Port 25 remains blocked by default on all VPS services and is not available for VPS plans.
  - [2] 2026-11-04: the terms say bandwidth and resource limits apply, without a number | capture: sha256:152b556bd82640f48df45a9577c380fddf0da7d3723c3eb5e1af1ccb9365dc35 | quote: Bandwidth and resource limits apply.
  - [3] 2026-11-04: the vendor page lists VPS Pro at USD 7.49 a month, with 1 TB bandwidth in its plan row | capture: sha256:715febe6effc8530b77d40fea984dc55851d8255aba2fda05d0fbc9452637650 | quote: $7.49 / Monthly
- sources:
  - [1] https://lowendbox.com/blog/cheap-vps-in-singapore-30-off-with-this-sweet-kainode-discount-code/
  - [2] https://kainode.com/terms
  - [3] https://kainode.com/
