# Bacloud

> bacloud.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/bacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bacloud

- `egress/bacloud-openvz-vps` | paid-only | evidence reported | binding per-ip-shaping | category origin VM (paid VPS) | tier Linux OpenVZ 1
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:43.376Z (live) | stale on 2026-11-18
- url https://www.bacloud.com/en/linux-vps-hosting
- price EUR 3.38 a month; transfer allowance not published on the vendor page | parsed USD 3.79/mo
- free tier: no free plan: Linux OpenVZ 1 is '3.38€/Mo.' with a 3-month minimum order and a 500 Mbps port; no transfer allowance is printed on the vendor page read | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: A third-party price index lists the plan's transfer as unmetered, limited by port speed and fair use; the vendor page read does not state a transfer figure.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: transfer allowance not published on the vendor page read; a third-party index reports unmetered, limited by port speed and fair use; port speed 500 Mbps; dedicated IPv4 and IPv6; TUN/TAP is supported for VPN use | metered: no | free allowance: not published on the vendor page read | source: [1]
- identity: email | detail: unverified: the sign-up and order pages were not read; the vendor states that cryptocurrencies are accepted at checkout | country: None
- interface: ssh
- limits:
  - per-ip-shaping (binding): 500 Mbps port speed on Linux OpenVZ 1; a 3-month minimum order [1]
- limits note: The transfer allowance and the fair-use threshold are not stated on the vendor page read.
- binding note: the only limit the vendor page states is the 500 Mbps port speed; the transfer quota behind the fair use wording is unverified, so what fails first at 1 TiB a month cannot be named
- interface detail: SSH root management and a serial console
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 3.38 a month origin in four locations (Lithuania, the USA, the Netherlands, the UK) that pays in cryptocurrency; the missing transfer figure is the unknown
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read
- notes: The plan is OpenVZ 7 container virtualization with TUN/TAP stated by the vendor. The vendor page read lists no transfer figure, and the index value is third-party.
- evidence note: the price, port speed, minimum order, IPv6 and TUN/TAP lines are vendor text read on 2026-11-03; the transfer figure is third-party only; no server was ordered, so inbound UDP was not…
- extras:
  - wg_path: native-conf
  - wg_detail: OpenVZ 7 container with TUN/TAP stated by the vendor; inbound UDP was not probed
  - ingress: unverified: no inbound port policy is stated on the pages read
  - volume_stated: not published on the vendor page read; unmetered per a third-party index
  - bytes_transit: yes
  - transit_note: bytes leave through the container's own public address on Bacloud's network
- evidence:
  - [1] 2026-11-03: Linux OpenVZ 1 is EUR 3.38 a month | capture: sha256:9dc58934517e732d1febb1995948666253d8a99f1a6ad137e4fe4a9568bc8364 | quote: 3.38€/Mo.
  - [1] 2026-11-03: the plan's port speed is 500 Mbps | capture: sha256:9dc58934517e732d1febb1995948666253d8a99f1a6ad137e4fe4a9568bc8364 | quote: Speed 500 Mbps\*
  - [1] 2026-11-03: the OpenVZ line lists a dedicated IPv4 and IPv6 address | capture: sha256:9dc58934517e732d1febb1995948666253d8a99f1a6ad137e4fe4a9568bc8364 | quote: - Dedicated IPv4 / IPv6
  - [1] 2026-11-03: the plan has a 3-month minimum order | capture: sha256:9dc58934517e732d1febb1995948666253d8a99f1a6ad137e4fe4a9568bc8364 | quote: Minimum order 3 months
  - [2] 2026-11-03: the vendor states TUN/TAP support for VPN use | capture: sha256:a587a724f04d031766d8c40e5e7925c9e80dcf4ee780f3a96ed92d6ffd33d71f | quote: With support for TUN/TAP, the essential feature needed for VPN functionality, users can configure a secure and private connection.
  - [3] 2026-11-03: the vendor accepts Bitcoin, Ethereum, Litecoin and USDC for a Linux VPS | capture: sha256:7aecb6f761f2285de7f596f9f6a91be36ed3308b5e6b21683116394023b00791 | quote: It supports multiple cryptocurrencies such as Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), and now USDC, providing a flexible and secure payment option.
  - [4] 2026-11-03: a third-party index lists the plan's transfer as unmetered, limited by port speed and fair use | capture: sha256:74bc0c9f4a39840d49c51bd05031d6549233c8f27b14de0ded1301a1bb3b9287 | quote: Unmetered (limited by port speed and fair use)
- sources:
  - [1] https://www.bacloud.com/en/linux-vps-hosting
  - [2] https://www.bacloud.com/en/knowledgebase/275/vps-for-vpn-secure-and-private-internet-access.html
  - [3] https://www.bacloud.com/en/knowledgebase/272/buy-linux-vps-with-usdc.html
  - [4] https://serverworth.com/plans/bacloud/openvz-15/
