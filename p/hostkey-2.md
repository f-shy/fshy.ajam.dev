# HOSTKEY

> hostkey.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostkey-2/ | JSON https://fshy.ajam.dev/api/v1/entity/hostkey-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HOSTKEY

- `egress/hostkey-vps` | paid-only | evidence documented | binding volume-quota | category origin VM (paid VPS) | tier VPS shared vCPU
- needs card no, phone yes, ID yes, institution no | verified 2026-11-03T07:36:43.376Z (live) | stale on 2026-12-04
- url https://hostkey.com/vps/
- price from about EUR 1.72 a month; EUR 2.46 excluding VAT for 3 TB on the 1 vCPU / 1 GB plan (third-party index) | parsed USD 1.93/mo
- free tier: no free plan: VPS hosting starts 'from about €1.72/month' for a shared-vCPU plan, with incoming traffic free | unit: TB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The 3 TB outgoing allowance is stated on the vendor's IPv6 VPS page for its listed plans and on a third-party price index for the 1 GB plan; the vendor's main VPS page says outgoing traffic depends on the selected plan.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: incoming traffic is free and outgoing traffic depends on the selected plan; the 1 vCPU / 1 GB plan (vm.pico) lists 3 TB a month on a 1 Gbps port; each VPS gets a dedicated IPv4 and IPv6 address; inbound UDP policy is not stated on the pages read | metered: yes | free allowance: 3 TB a month on the 1 vCPU / 1 GB plan (vendor IPv6 VPS page, 1 Gbit/s) | source: [1]
- identity: national-id | detail: KYC is mandatory for every client of hostkey.com: an identity document, a selfie, and a working email address and mobile phone number; new orders are blocked if it is not completed within 30 days of registration | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 3 TB a month outgoing on the 1 vCPU / 1 GB plan on a 1 Gbit/s port [2]
- limits note: The plan behind the 'from about €1.72/month' headline was not identified on the pages read, so its allowance is unverified.
- binding note: at 1 TiB a month the 3 TB outgoing allowance is not passed on the 1 GB plan; the ID document check on the account is what gates use
- interface detail: SSH to the VPS public address
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 1.72 to 2.46 a month origin with a dedicated IPv4 and IPv6 address; the ID document check on the account, not the price, is the cost
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read
- notes: This is the hostkey.com storefront in euros; the existing compute records for HOSTKEY read the Russian-language hostkey.ru storefront. The 1 vCPU / 1 GB plan price and its 3 TB allowance come from a third-party index and are reported; the vendor's IPv6 page lists the same 3 TB figure but says IPv6-only VPS servers are not yet available in the region shown.
- evidence note: the headline price, free incoming traffic, the addresses and the KYC rule are quoted from vendor pages read on 2026-11-03; the 3 TB figure is on the vendor's IPv6 VPS page, which also says IPv6 VPS servers 'will be available soon'; no VPS was ordered
- extras:
  - wg_path: native-conf
  - wg_detail: a full Linux guest with a dedicated IPv4 and IPv6 address; wg-quick binds UDP natively unless a firewall is added; inbound UDP was not probed
  - ingress: unverified: no inbound port policy is stated on the pages read
  - volume_stated: incoming traffic free; outgoing depends on the plan; 3 TB on the 1 vCPU / 1 GB plan
  - bytes_transit: yes
  - transit_note: bytes leave through the VPS's own public address on HOSTKEY's network
- evidence:
  - [1] 2026-11-03: the cheapest VPS is about EUR 1.72 a month with a shared vCPU | capture: sha256:df9d82feec8a5def98291d5f61d3cf50b8226f4ebe825742051558532e183bed | quote: HOSTKEY offers VPS hosting that starts from about €1.72/month for a plan with shared vCPU.
  - [1] 2026-11-03: incoming traffic is free and outgoing traffic is plan-dependent | capture: sha256:df9d82feec8a5def98291d5f61d3cf50b8226f4ebe825742051558532e183bed | quote: Incoming traffic is free, while outgoing traffic depends on your selected plan.
  - [1] 2026-11-03: each VPS gets a dedicated IPv4 and IPv6 address | capture: sha256:df9d82feec8a5def98291d5f61d3cf50b8226f4ebe825742051558532e183bed | quote: Each VPS receives dedicated IPv4 and IPv6 addresses for full network functionality.
  - [2] 2026-11-03: the IPv6 VPS plans list a 1 Gbit/s port and 3 TB of traffic | capture: sha256:17caf92b4a7e39c92ac75311a0056684a4d1984e9fdf4714090b8e7e9c40b487 | quote: Traffic Inc 1 Gbit/s, 3 TB
  - [2] 2026-11-03: the IPv6 VPS page says IPv6 VPS servers are not yet available in the region shown | capture: sha256:17caf92b4a7e39c92ac75311a0056684a4d1984e9fdf4714090b8e7e9c40b487 | quote: VPS servers with IPv6 will be available soon. Please check other regions in the meantime.
  - [3] 2026-11-03: a third-party index reports the 1 vCPU / 1 GB plan (vm.pico) at EUR 2.46 excluding VAT with 3 TB a month | capture: sha256:13ea56a0681b34beac0aac728af661e6ba34ff257b2b64d268364de0b8a4eef6 | quote: HOSTKEY lists this plan at 2.46 EUR excluding VAT.
  - [4] 2026-11-03: KYC verification is mandatory for every client | capture: sha256:ee616a2d8d5a7369e395c9132f1e3147eabcb87009c66e478311fad5b368417a | quote: Completing the procedure is mandatory for all our clients.
  - [4] 2026-11-03: the first KYC stage is an identity document, followed by a selfie | capture: sha256:ee616a2d8d5a7369e395c9132f1e3147eabcb87009c66e478311fad5b368417a | quote: 1. Identity document - an identity document
  - [4] 2026-11-03: a working email address and mobile phone number are asked for | capture: sha256:ee616a2d8d5a7369e395c9132f1e3147eabcb87009c66e478311fad5b368417a | quote: Information must be up-to-date and accurate; please provide a working email address and mobile phone number.
- sources:
  - [1] https://hostkey.com/vps/
  - [2] https://hostkey.com/vps/ipv6/
  - [3] https://serverworth.com/plans/hostkey/vm.pico/
  - [4] https://hostkey.com/documentation/account/kyc_aml/
