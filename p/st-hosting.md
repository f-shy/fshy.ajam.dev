# ST-Hosting

> st-hosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/st-hosting/ | JSON https://fshy.ajam.dev/api/v1/entity/st-hosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ST-Hosting

- `compute/st-hosting-ipv6-lxc-type9` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier IPv6 LXC "Type 9"
- needs card no, phone no, ID no, institution no | verified 2026-10-24T05:58:00.000Z (live) | stale on 2026-11-24
- url https://st-hosting.com/en/server?standort=nuernberg&technik=lxc&kategorie=lxc&ipv4=0
- price parsed USD 1.11/mo
- free tier: No free tier. The smallest IPv6-only LXC plan is EUR 0.99 a month billed monthly: 1 vCore, 512 MB RAM, 20 GB SSD, no IPv4 address, one IPv6 address, fair-use traffic. The page states 'No dedicated IPv4 address. Your server is reachable via IPv6 only.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Prepaid credit model with no minimum contract term. The payment page states: 'If your service is not extended after the paid term, we will automatically block it. You will then have 7-14 days* to renew most products before they are completely deleted.' | days: 14 | source: [2]
- egress: Fair use, with the vendor's own wiki putting the working figure at 25 TB a month: 'only a few of our customers require more than 25 TB of traffic per month when operating a server'. Connection is 1 Gbit/s. No hard cap is published and no overage price is published. | metered: no | free allowance: fair use, 25 TB a month stated as the typical ceiling | source: [3]
- identity: email | detail: no card at registration. The signup form at cp.st-hosting.com/en/signup carries E-mail address, Password, Repeat password, Country, Language and a captcha, and no card, address or phone field. Payment is a separate prepaid top-up after the account exists, and the payment page lists Bank transfer, PayPal, BitPay, Crypto, paysafecard and Credit card with the line 'you can top up your credit at any time without fees'. No card hold or authorisation amount is stated on any page read.
- interface: ssh
- limits:
  - per-ip-shaping (binding): no IPv4 address at all on this product line; the vendor states 'Keep in mind, thats not possible to add a IPv4 Address on those servers.' [4]
  - volume-quota: fair-use traffic, with 25 TB a month named as the level above which the vendor starts measuring [3]
  - pull-count: prepaid credit: the account is topped up and drawn down, so a purchase needs a funded balance rather than a recurring charge [2]
- binding note: The product has no IPv4 at all and the vendor states an IPv4 address cannot be added to this line, so any client without IPv6 reachability cannot use it; traffic is generous and the price is not a constraint.
- interface detail: Root shell in an unprivileged LXC container, reached over the IPv6 address. A web control panel at cp.st-hosting.com handles reinstall, rDNS and credit top-up. Delivery is stated at 60 seconds.
- tooling: any SSH client; the vendor's own panel for reinstall and rDNS. No API is documented.
- composes with: The cheapest IPv6-only root shell documented at USD 1.109 a month with a full 20 GB of disk, which makes it the natural WireGuard endpoint or health-monitor box where IPv6 is already in place at the edge. The EUR 1.29 / USD 1.445 rung doubles RAM to 1 GB and disk to 30 GB for 0.336 USD more.
- reliability: no reliability event observed. The vendor runs its own status page at status.cyberse.de, linked from the 404 page, and no SLA is offered.
- notes: The order link on the product card is an addToCart POST target; fetched as a GET it returns the vendor's empty cart page rather than an error, so the cart URL is recorded but the cart contents could not be read without adding an item, which this category does not do. The Monthly/Annually toggle exists and the annual rate was not captured; only the monthly figure is claimed. Whether the container can be reached over IPv4 through some proxy was not established - the vendor says no, and the LowEndTalk post repeats that an IPv4 address cannot be added to these plans. The IPv6 address count is one per server, with more on request, which is enough for a tunnel endpoint but not for a routed prefix. Unverified: fetching the same URL with the annual toggle's query parameter, which was not identified in the markup.
- evidence note: the EUR 0.99 monthly price, the shape and the IPv6-only statement are quoted from the vendor's own server-selection page read, which is the page the vendor's own product link redirects to; the signup fields are read from the signup page's form markup; the payment list is quoted from the vendor's payment page. The annual rate was not read: the page has a Monthly/Annually toggle and only the Monthly state was captured.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 20
  - billing_model: monthly
  - term: monthly, no minimum contract term
  - m10h_usd: 1.109
  - m24h_usd: 1.109
  - price_arithmetic: EUR 0.99 a month, billed monthly. Converted at 1 USD = EUR 0.892784 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000): 0.99 / 0.892784 = USD 1.1089, rounded to USD 1.109. A VPS bills whether it runs or not, so the 24/7 and 10 h/day figures are identical.
  - out_of_pocket_usd: 1.109
  - first_payment_usd: 1.109
  - renewal_usd: same EUR 0.99 monthly; no promotional price and no end date printed
  - stock: no out-of-stock badge on the Type 9 card on the vendor's own selection page; the page lists 8 plans in the IPv6-only LXC line and none carried a sold-out marker
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all, on the server's own IPv6 address
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /128 (one address; more on request)
  - signup_url: https://cp.st-hosting.com/en/signup
  - cart_url: https://cp.st-hosting.com/en/cart/addToCart/772
  - ipv6_only: yes
  - payment_methods: Bank transfer, PayPal, BitPay, Crypto, paysafecard, Credit card - all as prepaid credit top-up, 'at any time without fees'
  - card_hold: none stated; the account is prepaid, so a card is only touched when the buyer chooses to top up with one
  - checkout_fields: email, password, country, language, captcha
  - udp: not separately stated; the server has its own routable IPv6 address with all ports, so UDP is not gated by a port-forwarding table
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = EUR 0.892784
- evidence:
  - [1] 2026-10-24: quoted product card: 'IPv6 LXC "Type 9" vCores 1 Memory 512 MB SSD 20 GB EUR 0.99 / month billed monthly' with the order link 'https://cp.st-hosting.com/en/cart/addToCart/772'
  - [1] 2026-10-24: quoted: 'No dedicated IPv4 address. Your server is reachable via IPv6 only.' and 'Add an IPv4 address' shown as a separate control, and 'LXC VPS 2/5 SSD - IPv6 only from EUR 0.99 / mo.'
  - [5] 2026-10-24: the form's labelled fields, read from the page markup: 'E-mail address', 'Password', 'Repeat password', 'Country', 'Sprache/Language', plus a captcha - no card, address or phone field
  - [2] 2026-10-24: quoted: 'Bank transfer / PayPal / BitPay / Crypto / paysafecard / Credit card' and 'With all available payment methods, you can top up your credit at any time without fees.' and 'If your service is not extended after the paid term, we will automatically block it. You will then have 7-14 days* to renew most products before they are completely deleted.'
  - [3] 2026-10-24: quoted: 'only a few of our customers require more than 25 TB of traffic per month when operating a server, for instance for private purposes or projects'
  - [4] 2026-10-24: quoted vendor post: 'Please keep in mind, thats not possible to add a IPv4 Address on those servers.' and the plan list 'IPv6 LXC X-Small with 1 vCore 512 MB RAM 20 GB SSD Storage 0,99 EUR per month'
  - [6] 2026-10-24: quoted comparison table: 'Traffic | Fair Use Limit', 'Connection | 1 GBit/s', 'Virtualization | LXC', 'Delivery | 60 seconds*'
- sources:
  - [1] https://st-hosting.com/en/server?standort=nuernberg&technik=lxc&kategorie=lxc&ipv4=0
  - [2] https://st-hosting.com/en/abrechnung
  - [3] https://st-hosting.com/wiki?entryId=38
  - [4] https://lowendtalk.com/discussion/175817/st-hosting-ipv6-only-lxc-servers-and-server-management-offers-stating-at-0-99
  - [5] https://cp.st-hosting.com/en/signup
  - [6] https://st-hosting.com/en/vserver
