# hide.me

> hide.me | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hide/ | JSON https://fshy.ajam.dev/api/v1/entity/hide.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hide.me

- `egress/hide-me` | paid-only | evidence documented | binding write-gated | category vpn port forward | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://hide.me/en/help/how-do-i-activate-dynamic-port-forwarding/
- price USD 11.99 per month; USD 2.50 per month on 28 months (69.99); USD 3.93 per month on 14 months (54.99) | parsed USD 2.5/mo
- free tier: Dynamic Port Forwarding, an exclusive feature for Premium members. The free tier carries 10 GB per month: For our Free users, you can use one device and 10 GB per month. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: With the hide.me VPN Premium plan you can use unlimited data traffic and up to 10 devices simultaneously.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Premium purchase with card, PayPal, Google Pay, Apple Pay, SEPA, SOFORT, bank transfer or crypto; the free tier needs no payment. | country: None
- interface: cli
- limits:
  - write-gated (binding): static port forwarding is refused outright: hide.me views static port forwarding as a potential security concern. Due to this, we refrain from permitting static port forwarding across our VPN server network. Instead, we introduce Dynamic Port Forwarding. [1]
  - retention-clamped: the mapping is UPnP-negotiated by the application rather than reserved by the account, so it is not addressable across a reconnect: Once the application maps a port, it can be contacted from the public Internet as though it is running on the router [2]
- binding note: There is no byte quota on Premium, so volume does not bind. The refusal of static forwarding does: the vendor will not give a port that persists, which removes the stable public address the ingress test asks for.
- interface detail: In-app activation, or the @pf suffix on the username for manual clients.
- tooling: Official app with the port-forwarding menu, or any client with the @pf username suffix.
- composes with: Works as a throwaway endpoint for a test on a free VM; a DNS record pointing at it will rot.
- reliability: UPnP negotiation is per session; if the UPnP request is not repeated the mapping disappears with no server-side notice.
- notes: The forum thread that surfaced first told users to buy a static IP, which supports the third reading, and the help page's own wording supports the second. Both can hold at once, and neither yields a free stable port.
- evidence note: Measured would need a Premium account and a UPnP negotiation observed. Prices were taken from the vendor page as indexed rather than rendered, because the page body served was FAQ text only; the forwarding sentences were read directly.
- extras:
  - wg_path: native-conf
  - wg_detail: Manual connections are supported with a username suffix rather than an app: make sure you add the @pf suffix to your username if you intend to use the port forwarding feature. A user still configures the tunnel itself, which is what a WireGuard config does.
  - ingress: tcp+udp
  - volume_stated: With the hide.me VPN Premium plan you can use unlimited data traffic and up to 10 devices simultaneously.
  - bytes_transit: yes
  - transit_note: Traffic crosses hide.me servers on the selected location.
- evidence:
  - [1] 2026-10-23: Dynamic port forwarding only, Premium only, no static forwarding on the network, and the @pf username suffix for manual connections.
  - [2] 2026-10-23: The forwarding is UPnP, in-house server implementation, Premium only, and the mapping is requested by the application rather than reserved by the account; the failure case is described as No incoming TCP connections will get established, nor will UDP responses be sent in the proper manner, which is why ingress is recorded as tcp+udp.
  - [3] 2026-10-23: Free users get one device and 10 GB per month; Premium gets unlimited data traffic and up to 10 devices.
  - [4] 2026-10-23: Indexed price rows: 1 month $11.99, 24 months plus 4 extra at $2.50 per month billed $69.99 every 28 months, 12 months plus 2 extra at $3.93 per month billed $54.99. The rendered page served FAQ text only.
- sources:
  - [1] https://hide.me/en/help/how-do-i-activate-dynamic-port-forwarding/
  - [2] https://hide.me/en/help/what-is-upnp-port-forwarding-and-how-can-i-enable-it/
  - [3] https://hide.me/en/vpn-deals-discounts
  - [4] https://hide.me/en/pricing
