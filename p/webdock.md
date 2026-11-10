# Webdock

> webdock.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webdock/ | JSON https://fshy.ajam.dev/api/v1/entity/webdock.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webdock

- `egress/webdock-vps-essential` | paid-only | evidence documented | binding volume-quota | category origin VM (paid VPS) | tier VPS Essential
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T05:55:18.737Z (live) | stale on 2026-12-05
- url https://webdock.io/en/pricing
- price EUR 2.15 a month with 1 TB outgoing; EUR 2.50 per TB overage | parsed USD 2.42/TB-mo
- free tier: no free plan: VPS Essential is '€2.15/mo' with a '1 TB Outgoing Transfer Limit /mo' | unit: TB | metered on: downloaded-bytes | read on: 2026-11-04 | source: [1] | note: No public trial; a 14-day sandbox of 1-2 instances is offered to VPN providers through the sales route.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB of outgoing transfer a month on a 1 Gbit/s port (up to 5 Gbit/s); incoming traffic is always free; overage is EUR 2.50 per TB in 100 GB increments; inbound UDP policy is not stated on the pages read | metered: yes | free allowance: 1 TB of outgoing transfer a month on the EUR 2.15 plan | source: [1]
- identity: card | detail: the sign-up form asks for a name, an e-mail address, a password and a country, with Google and GitHub sign-in as alternatives; the payment step accepts Visa, Mastercard, American Express, Discover and PayPal; no ID document or phone number is asked on the pages read | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB outgoing transfer a month on VPS Essential and VPS Advanced, 7 TB on VPS Pro; overage EUR 2.50 per TB [1]
- binding note: at 1 TiB a month the 1 TB allowance is passed first, and the overage is EUR 2.50 per TB in 100 GB increments
- interface detail: SSH to the VPS public IPv4 address
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 2.15 a month origin in Denmark with 1 TB outgoing and free incoming; the allowance is billed past the limit, so it is a price and not a wall
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read
- notes: The vendor runs a page for VPN providers and states typical sustained throughput of 70-120 Mbit/s for VPN stacks; the 14-day sandbox is a sales route and not self-service. VPS Advanced is EUR 4.30 a month with the same 1 TB and VPS Pro is EUR 19.6 a month with 7 TB.
- evidence note: price, outgoing allowance, overage, port and payment methods are quoted from the vendor's pricing page and sign-up form read on 2026-11-04; no server was ordered and no port was probed
- extras:
  - wg_path: native-conf
  - wg_detail: a KVM guest with root and a dedicated public IPv4 plus IPv6; wg-quick binds UDP natively unless a firewall is added; inbound UDP was not probed
  - ingress: unverified: no inbound UDP port policy is stated on the pages read
  - volume_stated: 1 TB outgoing transfer a month; incoming free
  - bytes_transit: yes
  - transit_note: bytes leave through the VPS's own public address on Webdock's network
- evidence:
  - [1] 2026-11-04: VPS Essential is EUR 2.15 a month | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: €2.15/mo
  - [1] 2026-11-04: VPS Essential includes 1 TB of outgoing transfer a month | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: 1 TB Outgoing Transfer Limit /mo
  - [1] 2026-11-04: the port is 1 Gbit/s, up to 5 Gbit/s | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: 1 Gbit/s port (up to 5 Gbit/s)
  - [1] 2026-11-04: incoming traffic is always free | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: Every plan includes a generous outgoing transfer allowance, and incoming traffic is always free.
  - [1] 2026-11-04: overage past the allowance is EUR 2.50 per TB in 100 GB increments | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: If you go over your allowance we bill a transparent overage of €2.50 per TB, in 100GB increments
  - [1] 2026-11-04: the accepted payment instruments are four card brands and PayPal | capture: sha256:aa41c0b87dc16c0c0c0796032f0cc64edda9989e0fa0d9244d8d0ecbed86f34c | quote: We accept major credit and debit cards, Visa, Mastercard, American Express, and Discover, as well as PayPal.
  - [2] 2026-11-04: the sign-up form asks for an e-mail address | capture: sha256:a9e7b5cc9055ee45c7999519fa0820855e95ad59242097e8a57cf1045db84986 | quote: Your E-mail \*
  - [2] 2026-11-04: the sign-up form offers GitHub and Google sign-in | capture: sha256:a9e7b5cc9055ee45c7999519fa0820855e95ad59242097e8a57cf1045db84986 | quote: Sign Up with GitHub
  - [3] 2026-11-04: the vendor quotes 70-120 Mbit/s sustained for VPN stacks on this hardware | capture: sha256:c7d277a73b485734a60953fae07b72ace7b14bf111cb983e3c350d28a2ee9355 | quote: CPU-intensive VPN stacks run stably on Xeon Gold cores, with typical 70-120 Mbit/s sustained depending on encryption model and destination mix.
  - [3] 2026-11-04: a 14-day sandbox is offered to VPN providers through sales | capture: sha256:c7d277a73b485734a60953fae07b72ace7b14bf111cb983e3c350d28a2ee9355 | quote: Evaluate Webdock with a 14-day sandbox (1-2 instances) using standard IP space.
- sources:
  - [1] https://webdock.io/en/pricing
  - [2] https://webdock.io/en/signup
  - [3] https://webdock.io/vpn-providers
