# fastTURN

> fastturn.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastturn/ | JSON https://fshy.ajam.dev/api/v1/entity/fastturn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## fastTURN

- `egress/fastturn-net` | paid-only | evidence documented | binding volume-quota | category relay (metered, WebRTC) | tier Pro Membership
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T00:21:58.037Z (live) | stale on 2026-12-04
- url https://fastturn.net/
- free tier: none: the home page lists only a Monthly plan at $9 and a Yearly plan at $99, and no free plan | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: the absence of a free plan is read from the plan list of the home page; the pages read name no trial
- per-object cap: not applicable: a TURN relay carries streams, not objects | source: [1]
- retention: not applicable: a relay stores no bytes | source: [1] | note: both plans list No logging
- egress: 25 GB of TURN traffic per month on both paid plans and unlimited STUN; the price of traffic above 25 GB: unverified: no overage price on any page read | metered: yes | free allowance: none: the 25 GB per month belongs to the paid plans | source: [1]
- identity: card | detail: a purchase is required for any TURN access: Buy Now buttons lead to a checkout paid through payment gateways such as PayPal or Stripe, and an account registration may ask for name, company name, address, email address and telephone number. The checkout and registration fields as shown to a buyer: unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): 25 GB of TURN traffic per month on both plans; STUN unlimited [1]
- limits note: the allowance is a byte volume per month, which volume-quota names
- binding note: the 25 GB per month of TURN traffic is the quantity that runs out, and no free plan exists to try it
- interface detail: STUN and TURN over UDP and TCP with SSL encryption (TURNS); the yearly plan lists long-term credentials; credential issuance and the ICE server hostnames are shown after purchase: unverified: behind a sign-up
- tooling: any WebRTC, SIP or ICE client's STUN and TURN settings; the home page says the service integrates through generic ICE settings
- composes with: a paid NAT-traversal relay for a WebRTC-shaped workload: 25 GB per month of relayed traffic does not compound, so it is a fallback path and not a transfer path.
- reliability: the plan page states 99.99% uptime and a 24-location server list; no measurement was taken of either; a status page lists live latency values per location
- notes: successor of freeturn.net, which redirected to this site with HTTP 301 on 2024-12-31. Prices: the home page lists $9 and $99, the product pages list 9,00 EUR and 99,00 EUR, and the shop page for a US visitor lists $11.00 and $111.00; the cause of the difference is unverified. Prices exclude VAT.
- extras:
  - stale_after_days: 90
  - bytes_transit: yes
  - transit_note: TURN relays media or data when a direct path fails, which is what its 25 GB per month counts
- evidence:
  - [1] 2026-11-03: both plans carry unlimited STUN and 25 GB of TURN traffic per month | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Our plans include unlimited STUN connections and 25 GB of TURN traffic per month.
  - [1] 2026-11-03: the TURN allowance is 25 GB per month | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: TURNS: 25 GB / Month.
  - [1] 2026-11-03: the monthly plan is listed at USD 9 | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Monthly $9
  - [1] 2026-11-03: the yearly plan is listed at USD 99 | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: $99
  - [1] 2026-11-03: listed prices exclude VAT | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Prices plus VAT.
  - [1] 2026-11-03: both plans serve UDP and TCP | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: UDP & TCP
  - [1] 2026-11-03: the yearly plan lists long-term credentials | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Long Term Credentials
  - [1] 2026-11-03: server bandwidth is stated as location dependent, 1-20 GBit/s | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Fiber optic connections width location dependent bandwidth (1-20 GBit/s).
  - [2] 2026-11-03: the monthly product page lists 9,00 EUR | capture: sha256:0893a4bbad778310d33e01e89d414c93ab7268ad3054a0d66157fd5734cf1a65 | quote: 9,00 €
  - [3] 2026-11-03: the yearly product page lists 99,00 EUR | capture: sha256:3afc4317302c92d62552fe7af3a9f4d18ea2f741bc6638dbdfe41943448b6f9d | quote: 99,00 €
  - [4] 2026-11-03: purchases are paid through PayPal or Stripe gateways | capture: sha256:3ed3e9b37e2ed78c697bf308851bdf0e04173aa64b34540881eab77df3e3ee6c | quote: All transactions for purchase of intangible products are made through payment gateways such as PayPal or Stripe that use SSL encryption.
  - [5] 2026-11-03: an account registration may ask for contact details, the exact fields are not stated | capture: sha256:768abc8a62f479f31b8cefda5a99d0badd8330b2b16499d9ab06fb55a544dff5 | quote: When you register for an Account, we may ask for your contact information, including items such as name, company name, address, email address, and telephone number.
- sources:
  - [1] https://fastturn.net/
  - [2] https://fastturn.net/product/pro-membership-monthly/
  - [3] https://fastturn.net/product/pro-membership-yearly/
  - [4] https://fastturn.net/refund-policy/
  - [5] https://fastturn.net/privacy-policy/
