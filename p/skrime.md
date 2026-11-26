# SKRIME

> skrime.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/skrime/ | JSON https://fshy.ajam.dev/api/v1/entity/skrime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SKRIME

- `compute/skrime-epyc-1g-ipv6` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier EPYC 1G, Only IPv6
- needs card no, phone no, ID no, institution no | verified 2026-11-02T02:17:27.463Z (live) | stale on 2026-12-03
- url https://skrime.eu/server/order
- price parsed USD 1.11/mo
- free tier: No free tier. EPYC 1G is EUR 0.99 a month configured as IPv6-only, or EUR 1.49 with IPv4: 1 core, 1 GB RAM, 10 GB storage, 10 Gbit/s shared, unlimited traffic, DDoS protection included. The page prints the two network options side by side: 'Only IPv6 0.99EUR per month' and 'IPv4 + IPv6 1.49EUR per month'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: not stated on any page read; the order and terms pages are behind a Cloudflare challenge, so the deletion window is unverified | source: [1]
- egress: unlimited traffic on a 10 Gbit/s shared uplink, stated on the plan card; no fair-use figure and no overage price is published on the page read | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: no card and no phone number: the register page asks for a Username, an Email Address, a Password, a Repeat Password, a Captcha Code and a terms checkbox, and for no other field. The accepted payment methods are unverified: the payment-methods page did not answer. No country limit is stated: the register page asks only for those fields, and no address or country field is on it.
- interface: ssh
- limits:
  - per-ip-shaping (binding): IPv6-only at the EUR 0.99 rung: one /64 IPv6 subnet and no IPv4 address. IPv4 costs EUR 0.50 a month more at the same shape. [1]
  - volume-quota: none stated: 'Unlimited Traffic' on the plan card [1]
  - pull-count: the EUR 0.99 figure is a monthly rate on a configurator; the term length and any minimum contract were not read because the order page is challenge-walled [1]
- binding note: no IPv4 at this rung, so without IPv6 the EUR 1.49 dual-stack price applies; nothing else on the offer is close to binding.
- interface detail: KVM guest with root over SSH on the IPv6 address. The vendor is a German host running its own LIR services and API; the order page is a configurator that builds a server from a link.
- tooling: any SSH client; the vendor publishes an API documentation page; no panel is named on the plan card.
- composes with: USD 1.109 a month for 1 GB and 10 GB on a 10 Gbit/s shared port with unlimited traffic, in the same price band as the ST-Hosting row but on KVM rather than LXC and with a bigger uplink; the IPv4 version is EUR 0.50 more if a client needs it.
- reliability: no reliability event observed. The vendor states in-house inline DDoS protection on the plan card and operates a public status page.
- notes: The extracted-text route returned HTTP 403 with a 1462-word body that looked like the page, while the raw fetch of the same URL returned the real 192 KB document with the price table. The 403 body was a provider's stored snapshot with '00.00EUR per month' in the price slot - a placeholder that would have been recorded as a free server if it had been trusted. That is the HTTP-200 trap in its exact form, and the raw bytes settled it. The EUR 0.99 is a monthly rate on a configurator; the minimum contract length, the deletion window and the payment rails were not read because the order and payment pages sit behind Cloudflare. Not established: whether the price is incl. or excl. VAT (the German pages usually print both and this one prints one figure), the minimum term, and the payment methods. Unverified: an interactive session through the challenge.
- evidence note: the EUR 0.99 IPv6-only and EUR 1.49 dual-stack prices, the shape and the 10 Gbit/s uplink are quoted from the vendor's own order page, fetched as raw bytes because the extracted-text route returned a 403 on the same URL. The registration fields are read from the vendor's own register page markup. Payment methods are unverified because that page is challenge-walled.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 10
  - billing_model: monthly
  - term: monthly; minimum contract not read
  - m10h_usd: 1.109
  - m24h_usd: 1.109
  - price_arithmetic: EUR 0.99 a month, billed monthly; 0.99 / 0.892784 = USD 1.1089, rounded to USD 1.109. Rate: 1 USD = EUR 0.892784 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000). A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same.
  - out_of_pocket_usd: 1.109
  - first_payment_usd: 1.109
  - renewal_usd: not published; the page gives one monthly figure and no first-term discount is marked
  - stock: no sold-out marker on the EPYC 1G card; the configurator offers the IPv6-only variant as an orderable link. The vendor publishes no explicit stock counter on this page, so this is 'no out-of-stock signal' rather than a confirmed count
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all, on the server's own IPv6 address
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - signup_url: https://skrime.eu/register
  - cart_url: https://skrime.eu/order/server/eyJjIjoyLCJtIjoxLCJkIjoxMCwiNCI6MSwiNiI6MSwiY29uIjoxMH0=
  - ipv6_only: yes
  - payment_methods: not read: the payment-methods page is behind a Cloudflare challenge
  - card_hold: not established; no hold is stated on any page read
  - checkout_fields: username, email, password, repeat password, captcha, terms checkbox
  - udp: not separately stated; the server holds its own /64 with all ports, so no forwarding table gates UDP
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = EUR 0.892784
- evidence:
  - [1] 2026-10-24: quoted plan card: 'EPYC 1G / from 0.99EUR per month / 1 Core / 1GB RAM / 10GB Storage / 10 Gbit/s (shared) / Unlimited Traffic / incl. DDoS Protection' followed by 'Only IPv6 0.99EUR per month' and 'IPv4 + IPv6 1.49EUR per month'
  - [1] 2026-10-24: quoted host and network detail: 'AMD EPYC 7543 @ 3.7GHz / AMD EPYC 7763 @ 3.5GHz / AMD EPYC 7713 @ 3.6GHz / ECC DDR4 RAM / Datacenter NVMe SSD in RAID 1 / 2x 10 Gbit/s LACP' and 'SkyLink, Eygelshoven'
  - [2] 2026-10-24: the form's labelled fields and input ids, read from the markup: 'Username' (registerUsername), 'Email Address' (registerEmail), 'Password' (registerPassword), 'Repeat Password' (registerPasswordRepeat), 'Captcha Code' (registerCaptcha), and the terms checkbox (registerTos) - no card, address, phone or ID field
  - [1] 2026-10-24: the IPv6-only configuration is a separate product link on the page, read from the markup: 'https://skrime.eu/order/server/eyJjIjoyLCJtIjoxLCJkIjoxMCwiNCI6MSwiNiI6MSwiY29uIjoxMH0='. Decoded it is {"c":2,"m":1,"d":10,"4":1,"6":1,"con":10}, which does NOT match the 1-Core plan card (it carries c=2), so the payload is recorded as the link's shape and not as a specification of the EUR 0.99 offer.
  - [3] 2026-10-24: the page returns Cloudflare's 'Just a moment...' interstitial (title 'Just a moment...', body 'enable javascript and cookies to continue') - recorded as a failed read, not as a finding about the vendor
  - [2] 2026-11-02: the rendered register form has four fields and a captcha, and no card, phone, address or country field | capture: sha256:4902c62fa32462ad7a8684b5dd7bda75e7bfe6f4542dcf0915f4c531a9deb2b9 | quote: Username Email Address Password Repeat Password
  - [2] 2026-11-02: the register page is served normally and its fields are the four named ones plus a captcha | capture: sha256:de16b724b30977d9c647cf67dc466ecbbacb81d516af6fb21141ddebc947ed4a | quote: Register • SKRIME
  - [2] 2026-11-02: the register form's only fields are a username, an email address and two password fields | capture: sha256:4902c62fa32462ad7a8684b5dd7bda75e7bfe6f4542dcf0915f4c531a9deb2b9 | quote: Username Email Address Password Repeat Password
- sources:
  - [1] https://skrime.eu/server/order
  - [2] https://skrime.eu/register
  - [3] https://skrime.eu/payment-methods
