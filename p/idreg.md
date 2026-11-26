# IDreg Net

> idreg.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/idreg/ | JSON https://fshy.ajam.dev/api/v1/entity/idreg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IDreg Net

- `compute/idreg-nat-1` | qualifies | evidence documented | binding per-ip-shaping | category NAT VPS | tier NAT-1
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:17:00.000Z (live) | stale on 2026-11-24
- url https://ca.idreg.net/store/vps-nat?language=english
- price parsed USD 0.47/mo
- free tier: No free tier. NAT-1 is Rp 8,500.00 a month: 128 MB RAM, 2 GB disk, 125 GB bandwidth, 1 shared NAT IPv4, 19 range ports plus 1 SSH port, a /80 IPv6 block, OpenVZ, multi-location. The store page marks it '10 Available'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the payment page states the vendor waits 2 days for payment: 'Kami menunggu pembayaran dari anda selama 2 (DUA) Hari.' No deletion window after that is stated on the pages read | days: 2 | source: [2]
- egress: 125 GB of bandwidth a month on NAT-1; no overage price and no shaping rule is published on the page read | metered: yes | free allowance: 125 GB | source: [1]
- identity: email | detail: no card at registration, and no separate registration form: the vendor's register.php states 'To create an account, please place an order with us', so the account is created at checkout. Payment is by bank transfer or PayPal - the payment page says 'Pembayaran dapat di lakukan melalui Bank dan Rekening Paypal di bawah ini' and the account details are shown only after login, at ca.idreg.net/rekening.php, which states 'Anda harus login untuk mengakses halaman ini'. No card hold or authorisation amount is stated anywhere read, and no card is needed because neither rail is a card rail.
- interface: ssh
- limits:
  - per-ip-shaping (binding): 1 shared NAT IPv4 with '19 range Port + 1 SSH Port'; the ports are a range, not individually chosen [1]
  - volume-quota: 125 GB of bandwidth a month [1]
  - volume-quota: 2 GB of disk, the smallest disk among evaluated providers; OpenVZ rather than KVM, so no custom kernel. [1]
- binding note: 128 MB of RAM and 2 GB of disk bind before the traffic does: the box will run a resolver or a tunnel but not a package manager's worth of updates on top of a web stack.
- interface detail: Root on an OpenVZ container over SSH, reached through the shared IPv4 on one of the assigned ports or directly over the /80 IPv6 block. 'Multi Location' is printed but the locations are not enumerated on the store page.
- tooling: any SSH client. The panel is WHMCS; no API documented and no VPS control panel is named on the store page.
- composes with: USD 0.470 a month, the cheapest monthly figure among evaluated providers and cheaper than any annual prepay found, for 128 MB and 2 GB with a /80 IPv6 block and 19 NAT ports; the shape is small enough that it is a DNS resolver, a monitoring probe or a tunnel endpoint rather than a general host.
- reliability: no reliability event observed. No SLA and no status page were found on the pages read.
- notes: This is the cheapest monthly figure found among evaluated providers at USD 0.470, and unlike most of the others it needs no annual prepay. The stock counter is explicit and per-plan, which is the strongest stock signal in evaluated offerings. Two things were not established. First, the locations: 'Multi Location' is printed but no list of countries appears on the store page, so a buyer cannot tell which country the box lands in before ordering. Second, whether the 19 ports are assigned or chosen - the page says 'range', which implies a contiguous assigned block, but no mapping procedure is documented. The vendor is Indonesian (idreg.net, prices in rupiah, Indonesian-language storefront with an English toggle). Payment being bank transfer and PayPal means the first payment may need manual confirmation rather than instant provisioning. The storefront's own 'Pesan Sekarang' link points at cart.php?a=add&pid=297, but that URL redirects to an unrelated cPanel hosting page ('Web Hosting Singapore', final_url /store/cpanel-host-sg) when fetched, so the working entry point recorded here is the product page /store/vps-nat/nat-1, which renders the NAT-1 card and its stock counter. The pid link may still work in a browser with a session; it does not work for a cold reader, which is what a human following this record would be.
- evidence note: the Rp 8,500 monthly price, the shape, the 19+1 port split, the /80 IPv6 block and the '10 Available' stock line are quoted from the vendor's own store page read. The registration-at-checkout behaviour and the payment rails are quoted from the vendor's own register.php and payment pages. UDP on the forwarded ports is not stated. The locations are not enumerated.
- extras:
  - shape.ram_gib: 0.125
  - shape.disk_gib: 2
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 0.47
  - m24h_usd: 0.47
  - price_arithmetic: Rp 8,500.00 a month, billed monthly; 8500 / 18089.973852 = USD 0.4699, rounded to USD 0.470. Rate: 1 USD = IDR 18089.973852 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000). A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same.
  - out_of_pocket_usd: 0.47
  - first_payment_usd: 0.47
  - renewal_usd: same Rp 8,500 a month; no promotional price and no end date printed
  - stock: in stock: the store page prints 'NAT-1 | 10 Available' beside the plan, read 2026-10-24
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 19 ports in a range on a shared IPv4, plus 1 SSH port, plus a /80 IPv6 block with all ports
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /80
  - signup_url: https://ca.idreg.net/store/vps-nat/nat-1
  - cart_url: https://ca.idreg.net/store/vps-nat/nat-1
  - ipv6_only: no
  - nat_config.ports_tcp: 19
  - nat_config.ssh_port_included: yes
  - nat_config.ports_assigned_or_chosen: the page says '19 range Port + 1 SSH Port', which reads as a contiguous assigned range plus a dedicated SSH port; no page describes the buyer choosing a mapping, and no panel is named
  - payment_methods: bank transfer and PayPal, per the vendor's payment page; the bank details are shown only after login
  - card_hold: none; neither rail is a card rail, and no hold is stated
  - checkout_fields: not read: the account is created during checkout and the order form's field list was not captured before the store page redirected
  - udp: not stated on any page read
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = IDR 18089.973852
- evidence:
  - [1] 2026-10-24: quoted product block: 'Starting from Rp 8.500,00 Monthly | 128 MB RAM | 2 GB Disk Space | 125 GB Bandwidth | 1 NAT IPv4 (Shared) | 19 range Port + 1 SSH Port | /80 Block IPv6 | Multi Location | OpenVZ' with order link '/cart.php?a=add&pid=297'
  - [1] 2026-10-24: the stock counters, read from the page markup: 'NAT-1 | 10 Available', 'NAT-2 | 10 Available', 'NAT-3 | 3 Available', 'NAT-4 | 5 Available'; the same page also lists NAT-2 at Rp 14.000,00 for 256 MB / 4 GB / 250 GB and NAT-3 at Rp 20.000,00 for 512 MB / 8 GB / 500 GB
  - [3] 2026-10-24: quoted: 'To create an account, please place an order with us' - there is no standalone registration form; the page carries only a login form
  - [2] 2026-10-24: quoted: 'Pembayaran dapat di lakukan melalui Bank dan Rekening Paypal di bawah ini' and 'Kami menunggu pembayaran dari anda selama 2 (DUA) Hari.'
  - [4] 2026-10-24: quoted: 'Anda harus login untuk mengakses halaman ini. Rincian ini berbeda dengan login username dan password control panel website anda.' - the bank details are behind the account
- sources:
  - [1] https://ca.idreg.net/store/vps-nat?language=english
  - [2] https://www.idreg.net/metode-pembayaran/
  - [3] https://ca.idreg.net/register.php?language=english
  - [4] https://ca.idreg.net/rekening.php
