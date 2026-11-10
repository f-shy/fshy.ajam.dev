# Oeck

> oeck.com | Egress and tunnels, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oeck/ | JSON https://fshy.ajam.dev/api/v1/entity/oeck.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Oeck (Egress and tunnels)

- `egress/oeck-vpn` | paid-only | evidence documented | binding request-rate | category vpn tunnel (hosted subscription) | tier 12 Months, $83.58 per 12 months ($6.97 per month)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:11:45.779Z (live) | stale on 2026-12-05
- url https://www.oeck.com/pricing/
- price USD 6.97 per month on the 12 Months plan (USD 83.58 per 12 months); a subscription price, not a per-TB price | parsed USD 6.97/mo
- free tier: No free tier read. The live pricing page lists '7 Days Charged at $3.94 USD for 7 day block', '1 Month Charged at $9.95 USD per month' and '12 Months Charged at $83.58 USD per 12 months', each with a '30-Day Money-Back Guarantee'. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The cheapest yearly price is $83.58 for 12 months ($6.97 per month, 'Save 59%'). The 7-day block is the cheapest entry price. No trial page was read.
- per-object cap: not applicable: an exit address, not an object | source: [2] | note: No object is stored; the constraint is the 6-device cap in limits.
- retention: not applicable: a live tunnel and a rented exit address, not stored bytes | source: [3] | note: The vendor says its VPN servers have no hard drives and that it keeps no user logs; no byte retention applies.
- egress: The pricing page states a price per term and no byte allowance, cap or per-GB price; the FAQ has a question 'Does Oeck ever limit customer usage?' whose answer was not on the pages read. metered is false on the absence of any stated byte figure, and no byte was counted through a tunnel. | metered: no | free allowance: none published: the pages price a term, not a volume | source: [1]
- identity: email | detail: An email address is required to create an account ('we need to be able to get in touch with you'). Payments run through Stripe, Coinbase and 2Checkout, so a card or cryptocurrency is how the plan is paid; the sign-up form itself was not read, so the exact field list is unverified: behind a sign-up.
- interface: unknown
- limits:
  - request-rate (binding): 6 devices at once: 'You may have up to 6 devices logged in to our network concurrently' [4]
  - per-ip-shaping: an OpenVPN client gets a random server in the chosen region, the apps get the server the network picks by load [5]
- limits note: Three facts no limit kind names. (1) The first-party pages read name no protocol list other than OpenVPN config files; WireGuard, UDP, a SOCKS5 endpoint and an obfuscation mode are unverified: not stated on any first-party page read. (2) Registration: whether sign-up is open today is unverified: the register page was not read; the pricing page carries Buy buttons. (3) Residential claim: the vendor's home page says a 'residential IP smartRouting' is built into the network, while its FAQ says the streaming exits are on a proxy network of colocated, dedicated and virtual private servers; it is a vendor claim that no page lets anyone check.
- binding note: No byte quota is stated, so the first stated limit is the 6-concurrent-device cap; the torrent-region rule decides where BitTorrent may run. No rate was measured.
- interface detail: Vendor apps (Android, iOS, macOS, Windows, Linux) and OpenVPN configuration files that list every server, per the FAQ. No SOCKS5 endpoint, API or WireGuard configuration is named on the first-party pages read. No interface term names a VPN tunnel.
- tooling: The vendor's apps or any OpenVPN client with the vendor's .ovpn files; port forwarding is configured on a device profile in the account area.
- composes with: A compute node runs an OpenVPN client with a vendor .ovpn file, so its traffic leaves at the region's exit address (a random server in the region for OpenVPN); a Worker cannot dial the tunnel directly and no proxy endpoint is documented.
- reliability: unverified: whether the service itself is up, since only marketing and FAQ pages were read and no tunnel was brought up. Per the FAQ the company is incorporated in Hong Kong with a planned move to Singapore.
- notes: Port forwarding: Yes: 'Advanced Port Forwarding', ports issued by the vendor and enabled per device profile, with a custom domain name per port that works from any region.
- evidence note: Documented from the vendor's pricing, features and FAQ pages. Registration status and the protocol list are unverified. Measured would need an account, a tunnel per protocol and the register and downloads pages.
- evidence:
  - [1] 2026-11-04: The 12 Months plan is charged $83.58 USD per 12 months. | capture: sha256:ff95eb0df609e75221a179b2defd1ebc9fb0809eaf93751e6d4f5ff99a4ece7e | quote: Charged at $83.58 USD per 12 months
  - [1] 2026-11-04: The 12 Months plan is shown as $6.97 per month, 'Save 59%'; the 1 Month plan is $9.95 per month and the 7 Days block $3.94. | capture: sha256:ff95eb0df609e75221a179b2defd1ebc9fb0809eaf93751e6d4f5ff99a4ece7e | quote: $ 6.97 / mo
  - [2] 2026-11-04: Advanced Port Forwarding: the vendor issues ports, the user enables them on a device profile and names the target port, and each port gets a custom domain name. | capture: sha256:a70eee3d43360e5e58da9b2bcd13a2fa0e52c364bc9f2dcb75fb9826fa049570 | quote: We issue you ports and you enable ports you select on your device profile(s).
  - [5] 2026-11-04:  | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: Yes.
  - [4] 2026-11-04: Up to 6 devices may be connected at once. | capture: sha256:d39c3cbc7ee08e273a85d208dab265a10a3cadfb7bab19745db602cb8b4727f5 | quote: You may have up to 6 devices logged in to our network concurrently
  - [3] 2026-11-04: An email address is required to create an account; the FAQ lists password resets, ticket replies and expiry notices as its purposes. | capture: sha256:11424b5937e5e79b0c0ec47ef11c763b8e6246b6f6545b86a460e389c54402eb | quote: In order to make the user experience the best we possibly can, we need to be able to get in touch with you.
  - [3] 2026-11-04: Payments are processed by Stripe, Coinbase and 2Checkout. | capture: sha256:11424b5937e5e79b0c0ec47ef11c763b8e6246b6f6545b86a460e389c54402eb | quote: Oeck uses Stripe, Coinbase and 2Checkout to process all of our payments.
  - [5] 2026-11-04: OpenVPN configuration files carry the full server list; a user can connect with an OpenVPN client instead of the apps. | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: If you want to see our full server list, it is available in the OpenVPN config files.
  - [2] 2026-11-04: The features page lists AES-256 encryption and a 4096-bit key exchange. | capture: sha256:a70eee3d43360e5e58da9b2bcd13a2fa0e52c364bc9f2dcb75fb9826fa049570 | quote: AES-256 Encryption
  - [5] 2026-11-04: Streaming exits are on a separate proxy network (opNetwork) of colocated, dedicated and virtual private servers, reached by a multi-hop from the VPN network. | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: The second is the Proxy Network (opNetwork).
  - [6] 2026-11-04: The vendor's home page says a residential IP smartRouting is built into the network: a vendor claim for streaming unblock, with no ASN or sample address published. | capture: sha256:ed151c1cb834bf9c6933949808b47ef9e9fb314358a9c3b97e4ab03cf479fa76 | quote: Our revolutionary residential IP smartRouting is built in to the OECK network.
- sources:
  - [1] https://www.oeck.com/pricing/
  - [2] https://www.oeck.com/features/
  - [3] https://www.oeck.com/faq/privacy_and_security/
  - [4] https://www.oeck.com/faq/account/
  - [5] https://www.oeck.com/faq/technical/
  - [6] https://www.oeck.com/

## Oeck (IP and proxies)

- `ip-proxy/oeck-vpn` | paid-only | evidence documented | binding request-rate | category VPN subscription (exit source) | tier 12 Months, $83.58 per 12 months ($6.97 per month)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:00:31.322Z (live) | stale on 2026-12-05
- url https://www.oeck.com/pricing/
- price USD 6.97 per month on the 12 Months plan (USD 83.58 per 12 months); a subscription price, not a per-TB price | parsed USD 6.97/mo
- duplicate of `egress/oeck-vpn`
- free tier: No free tier read. The live pricing page lists '7 Days Charged at $3.94 USD for 7 day block', '1 Month Charged at $9.95 USD per month' and '12 Months Charged at $83.58 USD per 12 months', each with a '30-Day Money-Back Guarantee'. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The cheapest yearly price is $83.58 for 12 months ($6.97 per month, 'Save 59%'). The 7-day block is the cheapest entry price. No trial page was readable.
- per-object cap: not applicable: an exit address, not an object | source: [2] | note: No object is stored; the constraint is the 6-device cap in limits.
- retention: not applicable: a live tunnel and a rented exit address, not stored bytes | source: [3] | note: The vendor says its VPN servers have no hard drives and that it keeps no user logs; no byte retention applies.
- egress: The pricing page states a price per term and no byte allowance, cap or per-GB price; the FAQ has a question 'Does Oeck ever limit customer usage?' whose answer was not on the pages read. metered is false on the absence of any stated byte figure, and no byte was counted through a tunnel. | metered: no | free allowance: none published: the pages price a term, not a volume | source: [1]
- identity: email | detail: An email address is required to create an account ('we need to be able to get in touch with you'). Payments run through Stripe, Coinbase and 2Checkout, so a card or cryptocurrency is how the plan is paid; the sign-up form itself was not readable (live register page HTTP 504; the archived copy is a closed-registration notice), so the exact field list is unverified: behind a sign-up.
- interface: unknown
- limits:
  - request-rate (binding): 6 devices at once: 'You may have up to 6 devices logged in to our network concurrently' [4]
  - per-ip-shaping: an OpenVPN client gets a random server in the chosen region, the apps get the server the network picks by load [5]
- limits note: Three facts no limit kind names. (1) The first-party pages read name no protocol list other than OpenVPN config files; WireGuard is reported by a third-party review only, and UDP, a SOCKS5 endpoint and an obfuscation mode are unverified: not stated on any page read (the live downloads, manual, terms and network-graph pages answered HTTP 504 on every attempt, and archived copies of the manual and downloads pages carry no protocol text). (2) Registration: an archived copy dated 2025-04-29 of the register page shows a notice 'Registrations are temporarily closed' that refers to a January 2022 re-opening date, and the live register page was unreadable (HTTP 504), so whether sign-up is open today is unverified; the live pricing page carries Buy buttons. (3) Residential claim: the vendor's home page says a 'residential IP smartRouting' is built into the network, while its FAQ says the streaming exits are on a proxy network of colocated, dedicated and virtual private servers; the class of the claim is a vendor claim that no page lets anyone check.
- binding note: No byte quota is stated, so the first stated limit is the 6-concurrent-device cap; the torrent-region rule decides where BitTorrent may run. No rate was measured.
- interface detail: Vendor apps (Android, iOS, macOS, Windows, Linux) and downloadable .ovpn configuration files per the archived downloads page, plus OpenVPN config files that list every server. No SOCKS5 endpoint, API or WireGuard configuration is named on the first-party pages read. No vocabulary term names a VPN tunnel.
- tooling: The vendor's apps or any OpenVPN client with the vendor's .ovpn files; port forwarding is configured on a device profile in the account area.
- composes with: A compute node runs an OpenVPN client with a vendor .ovpn file, so its traffic leaves at the region's exit address (a random server in the region for OpenVPN); a Worker cannot dial the tunnel directly and no proxy endpoint is documented.
- reliability: The host is intermittently unreachable: direct requests to oeck.com and www.oeck.com timed out on 2026-11-04 and a page reader answered HTTP 504 on many attempts, while some reads succeeded. unverified: whether the service itself is up, since only marketing pages were reachable and no tunnel was brought up. Per the FAQ the company is incorporated in Hong Kong with a planned move to Singapore.
- notes: Duplicate of egress/oeck-vpn, which holds the offer.
- evidence note: Documented from the vendor's live pricing, features and FAQ pages, read through a page reader. Registration status and the protocol list are unverified. Measured would need an account, a tunnel per protocol and the live register and downloads pages.
- evidence:
  - [1] 2026-11-03: The 12 Months plan is charged $83.58 USD per 12 months. | capture: sha256:ff95eb0df609e75221a179b2defd1ebc9fb0809eaf93751e6d4f5ff99a4ece7e | quote: Charged at $83.58 USD per 12 months
  - [1] 2026-11-03: The 12 Months plan is shown as $6.97 per month, 'Save 59%'; the 1 Month plan is $9.95 per month and the 7 Days block $3.94. | capture: sha256:ff95eb0df609e75221a179b2defd1ebc9fb0809eaf93751e6d4f5ff99a4ece7e | quote: $ 6.97 / mo
  - [6] 2026-11-03: An archived copy dated 2025-04-29 of the pricing page lists the same 1 Month price of $9.95 and carries no 12 Months card; the live page was read on 2026-11-04. | capture: sha256:bd2302ea388e101b663ef01513fbab2c4e0aaba9ba1b2fcbfe5e16e35b67e8f9 | quote: Charged at $9.95 USD per month
  - [2] 2026-11-03: Advanced Port Forwarding: the vendor issues ports, the user enables them on a device profile and names the target port, and each port gets a custom domain name. | capture: sha256:a70eee3d43360e5e58da9b2bcd13a2fa0e52c364bc9f2dcb75fb9826fa049570 | quote: We issue you ports and you enable ports you select on your device profile(s).
  - [5] 2026-11-03:  | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: Yes.
  - [4] 2026-11-03: Up to 6 devices may be connected at once. | capture: sha256:d39c3cbc7ee08e273a85d208dab265a10a3cadfb7bab19745db602cb8b4727f5 | quote: You may have up to 6 devices logged in to our network concurrently
  - [3] 2026-11-03: An email address is required to create an account; the FAQ lists password resets, ticket replies and expiry notices as its purposes. | capture: sha256:11424b5937e5e79b0c0ec47ef11c763b8e6246b6f6545b86a460e389c54402eb | quote: In order to make the user experience the best we possibly can, we need to be able to get in touch with you.
  - [3] 2026-11-03: Payments are processed by Stripe, Coinbase and 2Checkout. | capture: sha256:11424b5937e5e79b0c0ec47ef11c763b8e6246b6f6545b86a460e389c54402eb | quote: Oeck uses Stripe, Coinbase and 2Checkout to process all of our payments.
  - [5] 2026-11-03: OpenVPN configuration files carry the full server list; a user can connect with an OpenVPN client instead of the apps. | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: If you want to see our full server list, it is available in the OpenVPN config files.
  - [2] 2026-11-03: The features page lists AES-256 encryption and a 4096-bit key exchange. | capture: sha256:a70eee3d43360e5e58da9b2bcd13a2fa0e52c364bc9f2dcb75fb9826fa049570 | quote: AES-256 Encryption
  - [5] 2026-11-03: Streaming exits are on a separate proxy network (opNetwork) of colocated, dedicated and virtual private servers, reached by a multi-hop from the VPN network. | capture: sha256:78f150acae82fa3265eb51225f41fdf484272a89a5cf97474673c82da20e3046 | quote: The second is the Proxy Network (opNetwork).
  - [7] 2026-11-03: The vendor's home page says a residential IP smartRouting is built into the network: a vendor claim for streaming unblock, with no ASN or sample address published. | capture: sha256:ed151c1cb834bf9c6933949808b47ef9e9fb314358a9c3b97e4ab03cf479fa76 | quote: Our revolutionary residential IP smartRouting is built in to the OECK network.
  - [8] 2026-11-03: A third-party review lists OpenVPN and WireGuard as the protocols (reported rung; no first-party page read names WireGuard). | capture: sha256:fc693469a2bd1ebd32749ecefa103ca38d54ce5904ed48a186fd642616eb2ae5 | quote: ProtocolsOpenVPN, WireGuard
  - probe:www.oeck.com 2026-11-03: A direct read-only request to https://www.oeck.com/ timed out on 2026-11-04 (about 21 seconds, no HTTP status); the live pages above were read through a page reader that reached the host on some attempts and answered HTTP 504 on others. | capture: sha256:4a96f0c251d08623f8f7d5f5ee59d9ab491b52e04a95f6265d43e2d29f55e7a2 | quote: "error": "timeout"
  - probe:oeck.com 2026-11-03: The apex https://oeck.com/ also timed out on a direct request on 2026-11-04, so the 2026-10-31 non-resolution of the apex host is not repeated as a DNS failure: the host answers no direct connection from the probe's network, and a page reader reaches www.oeck.com intermittently. | capture: sha256:9095312c7bac12249001b0b99a4882071a0d98270d8a113d7b753d79f680300c | quote: "error": "timeout"
  - [1] 2026-11-04: The vendor pricing page lists the VPN plan that both records cite. | capture: sha256:ff95eb0df609e75221a179b2defd1ebc9fb0809eaf93751e6d4f5ff99a4ece7e | quote: Charged at $83.58 USD per 12 months
- sources:
  - [1] https://www.oeck.com/pricing/
  - [2] https://www.oeck.com/features/
  - [3] https://www.oeck.com/faq/privacy_and_security/
  - [4] https://www.oeck.com/faq/account/
  - [5] https://www.oeck.com/faq/technical/
  - [6] https://web.archive.org/web/20250429005015/https://www.oeck.com/pricing/?provider=wayback
  - [7] https://www.oeck.com/
  - [8] https://top10vpns.com/reviews/oeck-vpn
