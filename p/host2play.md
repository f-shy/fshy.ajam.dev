# host2play

> host2play.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/host2play/ | JSON https://fshy.ajam.dev/api/v1/entity/host2play.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## host2play

- `compute/host2play-lxc-lite` | qualifies | evidence documented | binding per-ip-shaping | category NAT VPS | tier LXC Lite
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:04:00.000Z (live) | stale on 2026-11-24
- url https://host2play.pl/shop/vps-lxc
- price parsed USD 0.741/mo
- free tier: No free tier. LXC Lite is PLN 34.90 a year, listed under the heading 'Najtaniej' (cheapest) on the vendor's LXC shop page: 1 vCPU, 768 MB RAM, 10 GB SSD, 'Wspoldzielone (10 portow) + IPv6 (100Mbps)', located in Sweden at Bahnhof Pionen. Billing periods offered at checkout are 7 days, 1 month, 3 months (-5%), 6 months (-10%) and 12 months (-15%). | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: prepaid service, not a subscription: the checkout page states 'To nie jest subskrypcja, to usluga przedplacona. Nigdy nie obciazymy Cie po zakonczeniu okresu rozliczeniowego.' No deletion window for an unpaid service is published on the pages read. | source: [2]
- egress: unlimited, stated by the vendor's own LowEndSpirit offer post as '100Mbps Network (Unlimited Traffic)'; the shop page states the port as 'IPv6 (100Mbps)'. No cap and no overage price is published. | metered: no | free allowance: unlimited | source: [3]
- identity: email | detail: no card at registration. The registration page at host2play.pl/management/register renders a single input, 'Email Address', plus a CSRF token and a 'Next' button, and the login page has Email, Password and an optional 2FA code field. No card, address, phone or ID field appears on either page. Payment is chosen at checkout and the option list reads 'BLIK, Credit Card, Klarna, GPay, Apple Pay, Przelewy24, Swish', 'PaySafeCard', 'PayPal' and 'host2play Wallet'. No card hold or authorisation amount is stated on any page read.
- interface: ssh, cli
- limits:
  - per-ip-shaping (binding): shared IPv4 with 10 forwarded ports; the IPv6 address is separate and unfiltered [1]
  - volume-quota: none: unlimited traffic on a 100 Mbit port [3]
  - pull-count: annual prepay is the cheapest term at PLN 34.90; shorter terms exist (7 days up to 12 months) at a higher monthly rate [2]
- binding note: 10 shared ports is the only number here that can run out; traffic is unlimited, RAM is 768 MB and the price is the lowest in evaluated offerings.
- interface detail: Root in an LXC container over SSH, with the vendor's own control panel for install, reinstall and upgrade, stated to complete in 60 seconds. 10 shared IPv4 ports plus a routed IPv6 address.
- tooling: any SSH client; the vendor's panel; no API documented.
- composes with: USD 0.741 a month at annual prepay for 768 MB and 10 GB with unlimited traffic on a 100 Mbit port, the cheapest per-gigabyte offer found among evaluated providers, and the only one that gives both a NAT IPv4 with 10 ports and a routed IPv6 on the same box.
- reliability: no reliability event observed. The vendor advertises DDoS monitoring and no SLA is published.
- notes: The checkout page's price field is rendered by JavaScript - the HTML carries an empty <span id="price"> with a spinner - so the PLN 34.90 figure is taken from the server-rendered shop page, which prints it as static text under the heading 'Najtaniej'. The two agree in substance: PLN 34.90 converts to EUR 7.94 at today's cross rate, and the vendor's own 2024 offer post prices the same plan at EUR 7.90 a year. The stray '3.34PLN' string on the checkout page is the pre-render placeholder and is not used. The shop page renders no sold-out or unavailable marker on any of the six rungs. Not established: whether UDP is forwarded on any of the 10 ports, the exact overage behaviour at 100 Mbit sustained, and the deletion window for an unpaid service. The vendor also runs the same catalogue at host2play.se and host2play.com, with the Swedish site printing 91.90kr/yr for LXC Lite; the Polish storefront was used because it printed a PLN price on a server-rendered page.
- evidence note: the PLN 34.90 annual price, the shape, the 10-port NAT and the IPv6 address are quoted from the vendor's own shop page read, which is server-rendered. The registration fields are read from the vendor's own registration page markup. The unlimited-traffic sentence is from the vendor's own LowEndSpirit offer post, not from the shop page, and is marked as such. UDP on the forwarded ports is not stated anywhere read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.75
  - shape.disk_gib: 10
  - billing_model: annual prepay
  - term: 12 months at the price recorded; 7 days to 12 months available
  - m10h_usd: 0.741
  - m24h_usd: 0.741
  - price_arithmetic: PLN 34.90 a year / 12 = PLN 2.9083 a month, paid in one go; 2.9083 / 3.926013 = USD 0.7408, rounded to USD 0.741. Rate: 1 USD = PLN 3.926013 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000). A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same. Out of pocket for the first year: 34.90 / 3.926013 = USD 8.89.
  - out_of_pocket_usd: 8.89
  - first_payment_usd: 8.89
  - renewal_usd: same PLN 34.90 a year; the term discounts (-5% at 3 months, -10% at 6, -15% at 12) are term pricing, not a first-term promo, and no end date is printed
  - stock: no sold-out marker on any of the six LXC rungs on the vendor's shop page; the order page for LXC Lite loads its checkout form rather than refusing, which is the available signal - the vendor publishes no explicit stock flag
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 10 ports on a shared IPv4, plus a routed IPv6 address with all ports
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: one address, prefix length not stated
  - signup_url: https://host2play.pl/management/register
  - cart_url: https://host2play.pl/product/159?c=yearly
  - ipv6_only: no
  - nat_config.ports_tcp: 10
  - nat_config.ssh_port_included: yes
  - nat_config.ports_assigned_or_chosen: not stated on any page read; the vendor publishes the count (10) and no mapping procedure. The LowEndSpirit post describes them as 'forwarded' and the shop page as 'Wspoldzielone (10 portow)'.
  - payment_methods: BLIK, Credit Card, Klarna, GPay, Apple Pay, Przelewy24, Swish, PaySafeCard, PayPal, host2play Wallet
  - card_hold: none stated; prepaid, and the checkout page says 'Nigdy nie obciazymy Cie po zakonczeniu okresu rozliczeniowego'
  - checkout_fields: email only at registration, then password; 2FA optional at login
  - udp: not stated on any page read
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = PLN 3.926013, 1 USD = EUR 0.892784
- evidence:
  - [1] 2026-10-24: quoted: 'Najtaniej | LXC Lite | 34.90zl /Rok | CPU 1 vCPU | RAM 768MB | DYSK 10GB SSD | ADRESACJA Wspoldzielone (10 portow) + IPv6 (100Mbps) | LOKALIZACJA Szwecja Bahnhof Pionen'
  - [1] 2026-10-24: the same 10-port line on every rung of the range: LXC Essential 48.90zl/Rok 1GB/15GB, LXC Pro 94.90zl/Rok 2GB/30GB, LXC Power 109.90zl/Rok 3GB/35GB, LXC Ultimate 149.90zl/Rok 4GB/45GB, LXC Mega 199.90zl/Rok 6GB/70GB - all 'Wspoldzielone (10 portow) + IPv6'
  - [2] 2026-10-24: quoted checkout page: 'Waznosc uslugi | Wybierz waznosc uslugi 7 Dni 1 Miesiac 3 Miesiace (-5%) 6 Miesiecy (-10%) 12 Miesiecy (-15%)' and 'Metoda platnosci | BLIK, Credit Card, Klarna, GPay, Apple Pay, Przelewy24, Swish | host2play Wallet | PaySafeCard | PayPal' and 'To nie jest subskrypcja, to usluga przedplacona.'
  - [4] 2026-10-24: the registration form's only input, read from the markup: '<input ... id="email" name="email" ... placeholder="Email Address">' plus a hidden _csrf token and a 'Next' button - no card, address, phone or ID field
  - [5] 2026-10-24: the login form's inputs: name='loginEmail' placeholder='Email', name='loginPassword' placeholder='Password', name='2facode' placeholder='2FA Code' - a password login, unlike providers that now demand an SSH key…
  - [3] 2026-10-24: quoted vendor post: 'NAT IPv4 - 10 ports forwarded / 1x IPv6 / Free Reverse Proxy for hosting websites + Free Subdomain + Free SSL / Intel(R) Xeon(R) CPU E5-2630 v2 Processor / 100Mbps Network (Unlimited Traffic)' and 'LXC Lite - 1vCPU - 768MB RAM - 10GB SSD SATA - 7.90EUR/yr (6m,3m,1m,7d billing available)'
  - [6] 2026-10-24: quoted, showing the NAT line is a separate product family: 'VPS NAT Serwery VPS NAT posiadaja wspoldzielone IP, a do Twojej dyspozycji otrzymujesz az 100 portow!' with VPS NAT Mini at '24.90zl /miesiac' - the 100-port NAT range is a different, dearer product and is not the offer recorded here
- sources:
  - [1] https://host2play.pl/shop/vps-lxc
  - [2] https://host2play.pl/product/159
  - [3] https://lowendspirit.com/discussion/8493/cheap-lxc-servers-host2play
  - [4] https://host2play.pl/management/register
  - [5] https://host2play.pl/management/login
  - [6] https://host2play.pl/shop/vps-nat
