# Whplus

> whplus.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/whplus/ | JSON https://fshy.ajam.dev/api/v1/entity/whplus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Whplus (my.whplus.com)

- `compute/whplus-iix-nat-512mb` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS | tier IIX NAT VPS 512MB
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://my.whplus.com/cart.php?gid=20&language=indonesia
- price parsed USD 0.69/mo
- free tier: No free tier. IIX NAT VPS 512MB is IDR 12,500 a month, printed 'Rp12,500' with 'Per Bulan'. The page showed '3' in stock for this tier and 22 for the 1 GB tier. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: monthly billing; no deletion interval after expiry was published on the pages read | source: [1]
- egress: 500 GB a month on the 512 MB tier, printed '500GB Bandwidth' | metered: yes | free allowance: 500 GB a month | source: [1]
- identity: email | detail: there is no standalone registration form: the register page states 'Untuk membuat akun baru, mohon Order Layanan Baru Dengan Kami' (to create a new account, order a new service), so the account is created at checkout and its fields could not be read. Payment is by Indonesian bank transfer to a BCA or Mandiri account, or by PayPal, per the vendor's own payment page. No card hold is stated. No national ID requirement is published anywhere read.
- interface: ssh
- limits:
  - volume-quota: 500 GB a month on this tier [1]
  - per-ip-shaping (binding): 20 tcp/udp ports plus 1 redirect SSH port on the shared IPv4, with domain forwarding allowed only to ports 80 and 443 [1]
- binding note: the 20 ports are the whole inbound budget, and domain forwarding is restricted to 80 and 443, so anything else has to be reached by explicit port number.
- interface detail: Virtuozzo OpenVZ 7 container with a shared IPv4, 20 tcp/udp ports plus one redirected SSH port
- tooling: any SSH client; a WHMCS client area
- composes with: a 512 MB Indonesian container at USD 0.69 a month whose 20 forwarded ports are stated to carry both TCP and UDP, which is the single field almost every other row among documented hosts leaves blank
- reliability: every plan states 'No Technical Support'; no uptime figure or SLA published; no reliability event observed
- notes: The one row among documented hosts that answers the UDP question in words for the forwarded ports: '20 tcp/udp port + 1 redirect SSH port'. That matters because a NAT box with 20 TCP-only ports cannot host a WireGuard listener, and every other seller read either says nothing or says 'TCP' alone. The 1 GB tier at IDR 20,000 = USD 1.1045 a month is the better buy and shows 22 in stock, which is the largest stock count documented; the 512 MB tier at IDR 12,500 = USD 0.6903 shows 3. Two caveats. The 256 MB tier at IDR 7,500 reads no stock span on the listing, which is the stock-control-off state, and its cart answers 'Stok Tidak Tersedia', so the cheapest tier is not buyable and the price ladder starts at the 512 MB. And the cart route could not be made to price any NAT product: cart.php with pids 112, 113 and 158 all returned the cPanel hosting group, and with an invalid pid it returned a different group again, so the redirect is a property of the route rather than evidence about the product. The purchase path that does exist is the vendor's own payment page, which names bank transfer to BCA or Mandiri or PayPal, so a foreign buyer without an Indonesian bank account would need the PayPal route. What is not established: the checkout fields, whether the 1 GB tier's cart actually prices, and whether the ports are symmetric. The 1 GB tier is the row worth re-testing.
- evidence note: price, shape, bandwidth, the port count and the explicit tcp/udp wording, the stock counts and the 'No Technical Support' line are quoted from the vendor's own store page read; the payment rails are quoted from the vendor's own payment page read. Not documented: the checkout fields, because Whplus creates the account at checkout and the cart route would not price a NAT product; and the legal entity, which is not named anywhere read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 10
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 0.69
  - m24h_usd: 0.69
  - price_arithmetic: IDR 12,500 a month / 18,108 IDR per USD = USD 0.6903 a month, from the ECB reference rate read 2026-10-24 with rate date 2026-10-23. The 1 GB tier is IDR 20,000 = USD 1.1045. VPS billing: the machine bills whether it runs or not, so the 10 h/day and 24/7 figures are identical.
  - out_of_pocket_usd: 0.69
  - renewal_usd: IDR 12,500 a month; no separate renewal price published
  - fx: IDR 18,108 per USD, api.frankfurter.app/latest read 2026-10-24, rate date 2026-10-23
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 20 tcp/udp ports plus 1 redirect SSH port on the shared IPv4
  - network_out.static_ip: no
  - network_out.ipv6: no
  - udp: stated: '20 tcp/udp port + 1 redirect SSH port' - the ports carry both protocols, quoted from the vendor's own plan description
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: Indonesian bank transfer to a BCA or Mandiri account, or PayPal, per the vendor's payment page
  - card_hold: not stated on any page read
  - checkout_fields: not established: Whplus creates the account at checkout and the cart route would not price a NAT product
  - stock: 512 MB tier shows 3 and the 1 GB tier shows 22 on 2026-10-24; the 256 MB tier shows no stock span and its cart answers 'Stok Tidak Tersedia'
  - cart_works: unknown
  - product_url: https://my.whplus.com/cart.php?gid=20&language=indonesia
  - signup_url_note: there is no standalone registration page: /register.php redirects the buyer to the cart with 'Untuk membuat akun baru, mohon Order Layanan Baru Dengan Kami'.
  - cart_url_note: the order buttons target cart.php?a=add&pid=<id>, but pids 112, 113 and 158 all resolved to the cPanel hosting group and an invalid pid resolved elsewhere, so the cart was never seen to price a NAT product.
  - other_plans: IIX NAT VPS 1GB IDR 20,000 = USD 1.1045 with 22 in stock and 750 GB; 2GB IDR 30,000 with 17; 3GB IDR 40,000 with 10; 4GB IDR 50,000 with 10. The 256 MB tier at IDR 7,500 shows no stock span and its cart refuses.
- evidence:
  - [1] 2026-10-24: quoted plan: 'IIX NAT VPS 512MB Single Core, 512MB RAM, 10GB Storage, 500GB Bandwidth, 1 shared IPv4 , 20 tcp/udp port + 1 redirect SSH port, Domain Forwarding only to port 80/443, No outgoing SMTP traffic, Virtuozzo OpenVZ7 virtualization, No Technical Support, Indonesia Datacenter'
  - [1] 2026-10-24: quoted prices and stock from the page markup: 'IIX NAT VPS 256MB ... Rp7,500' with no stock span, 'IIX NAT VPS 512MB ... Rp12,500' with '3', 'IIX NAT VPS 1GB ... Rp20,000' with '22', 'IIX NAT VPS 2GB ... Rp30,000' with '17', and 'Per Bulan' as the cycle
  - [1] 2026-10-24: the order button for the 256 MB tier targets cart.php?a=add&pid=112, and the tiers carry product ids 112, 113, 158, 165, 166 and 167
  - [2] 2026-10-24: the cart refused the 256 MB tier: 'Stok Tidak Tersedia Mohon maaf saat ini stok tidak tersedia, silakan kembali lagi di lain waktu.' (stock unavailable), even though the listing shows no stock span for that tier
  - [3] 2026-10-24: quoted payment rails: 'Anda dapat melakukan pembayaran melalui transfer bank ke rekening BCA atau Mandiri kami.' and 'Anda bisa juga melakukan pembayaran secara online melalui Paypal.'
  - [4] 2026-10-24: quoted: 'Untuk membuat akun baru, mohon Order Layanan Baru Dengan Kami' - there is no standalone registration form, so the account is created during an order
- sources:
  - [1] https://my.whplus.com/cart.php?gid=20&language=indonesia
  - [2] https://my.whplus.com/cart.php?a=add&pid=112
  - [3] https://whplus.com/cara-pembayaran
  - [4] https://my.whplus.com/register.php
