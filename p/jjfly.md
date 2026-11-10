# JJFLY

> jjfly.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jjfly/ | JSON https://fshy.ajam.dev/api/v1/entity/jjfly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JJFLY (拼好鸡)

- `compute/jjfly-nl-nat` | qualifies | evidence documented | binding volume-quota | category NAT VPS | tier 荷兰NAT (Netherlands NAT)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T02:17:25.934Z (live) | stale on 2026-12-03
- url https://idc.jjfly.cloud/cart
- price parsed USD 0.15/mo
- free tier: No free tier. 荷兰NAT is CNY 1.00 a month: 256 MB RAM, 1.5 GB disk, 10 IPv4 ports plus 1 dedicated IPv6, 500 Mbit unlimited traffic on fair use, Linux, in the Netherlands. The cart page prints 库存 (stock) 5 beside it. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: refunds rather than retention are documented: the vendor's pre-purchase note says products at CNY 5 and above support a 24-hour refund and others can 'self-refund' to account balance within 24 hours, and that if a product fails the remaining value is returned to balance. No deletion window for an unpaid service is stated | source: [2]
- egress: 500 Mbit, unlimited traffic on fair use ('500M不限流量(合理使用)'). The vendor states that if a server runs past its traffic allowance the term is extended to compensate rather than the box being cut off: '部分服务器流量有限，若流量超额，会补偿时长至流量恢复。' | metered: no | free allowance: unlimited, fair use | source: [3]
- identity: email | detail: The register page asks for an email address, a verification code sent to that email, a password and a password confirmation, plus a privacy checkbox. No card field, no phone field, no address field and no identity-document field is on it. The payment rails are not on any page read because the checkout sits behind the account.
- interface: ssh
- limits:
  - per-ip-shaping: 10 IPv4 ports on a shared address plus 1 dedicated IPv6 address with all ports [3]
  - volume-quota (binding): 256 MB RAM and 1.5 GB disk, the smallest shape among evaluated providers; LXC, so no custom kernel and no nested Docker. [3]
  - per-ip-shaping: outbound port 25 is blocked, and outbound 80/443 to China is blocked; on IPv4 only, with the vendor stating '以上仅屏蔽IPv4，IPv6目前无任何屏蔽' (the above blocks IPv4 only; IPv6 currently has no blocks) [2]
- binding note: 256 MB of RAM and 1.5 GB of disk bind long before the price or the traffic does; this is a single small service per box, not a host.
- interface detail: Root in an LXC container over SSH, reachable on one of the 10 assigned IPv4 ports or directly on the dedicated IPv6 address. OS images offered are Linux only: Debian 13 and Alpine 3.23 are the two named on the configuration page.
- tooling: any SSH client. The panel is a Chinese IDC billing system; no API is documented. The vendor states LXC containers may not themselves run Docker, because LXC and Docker are the same class of virtualization.
- composes with: USD 0.150 a month, the lowest price found among evaluated providers by a wide margin, for 256 MB and 1.5 GB with a dedicated IPv6 and 10 IPv4 ports; at this price it is a throwaway probe, a DNS resolver or a second tunnel endpoint, and the vendor itself calls the products 'toys'.
- reliability: The vendor publishes a status probe at status.jjfly.cloud and states in its own pre-purchase note that the products are cheap and positioned as toys ('定位为玩具属性'), that no China-mainland direct connectivity is guaranteed, and that data should be backed up. no reliability event observed.
- notes: The blocks are stated as IPv4-only, and the dedicated IPv6 address is described as carrying no blocks at all, which makes the IPv6 side strictly more capable than the IPv4 side here. The vendor publishes test addresses for both families, which is a useful first-party signal that the IPv6 is real rather than nominal. Not established: the payment rails (the checkout needs an account), the exact overage behaviour (the vendor says it compensates with time rather than cutting off), and whether the 10 ports are assigned or chosen. The storefront is at idc.jjfly.cloud, a different host from the jjfly.cloud marketing site.
- evidence note: the CNY 1.00 monthly price, the shape, the 10 ports plus dedicated IPv6, the stock count of 5 and the OS list are quoted from the vendor's own cart and product-configuration pages read. The registration fields are read from the vendor's own register page markup. The firewall rules and the fair-use compensation sentence are quoted from the vendor's own pre-purchase knowledge-base article.
- extras:
  - shape.ram_gib: 0.25
  - shape.disk_gib: 1.5
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 0.15
  - m24h_usd: 0.15
  - price_arithmetic: CNY 1.00 a month, billed monthly; 1.00 / 6.684864 = USD 0.1496, rounded to USD 0.150. Rate: 1 USD = CNY 6.684864 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000). A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same.
  - out_of_pocket_usd: 0.15
  - first_payment_usd: 0.15
  - renewal_usd: same CNY 1.00 a month; no promotional price and no end date printed
  - stock: in stock: the cart page prints '库存：5' (stock: 5) beside 荷兰NAT, read 2026-10-24
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 10 IPv4 ports on a shared address, plus a dedicated IPv6 address with all ports
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: one dedicated address, prefix not stated
  - signup_url: https://idc.jjfly.cloud/register
  - cart_url: https://idc.jjfly.cloud/cart?action=configureproduct&pid=6
  - ipv6_only: no
  - nat_config.ports_tcp: 10
  - nat_config.ssh_port_included: yes
  - nat_config.ports_assigned_or_chosen: not stated on any page read; the product page prints '10个IPv4端口+1个独立IPv6' and no mapping procedure. The dedicated IPv6 address is separate and unfiltered, so the port count is not the only route in.
  - payment_methods: not read: the checkout is behind the account
  - card_hold: not established; no hold is stated on any page read
  - checkout_fields: email, emailed verification code, password, password confirmation, privacy checkbox
  - udp: not stated for the NAT ports; the vendor's block list is protocol-specific on IPv4 (it blocks Shadowsocks/Vmess/Websocket/OpenVPN/Wireguard inbound from China IPs) and states IPv6 has no blocks at all
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = CNY 6.684864
- evidence:
  - [1] 2026-10-24: quoted cart listing: '库存：5 | 荷兰NAT | CNY 1.00 元 / 月' with the buy link 'https://idc.jjfly.cloud/cart?action=configureproduct&pid=6', in a list where 美国NAT is CNY 3.00 (stock 20), 美国②NAT CNY 2.00 (stock 4), 英国NAT CNY 4.00 (stock 8), 德国NAT CNY 2.00 (stock 20), 土耳其NAT CNY 3.50 (stock 13), 俄罗斯NAT CNY 2.00 (stock 7) and 巴西NAT CNY 5.00 (stock 7)
  - [3] 2026-10-24: quoted product configuration: '荷兰NAT | 测试IPv4：5.181.177.1；测试IPv6：2a12:bec4:1822:86::a | 内存 256MB | 硬盘 1.5GB | 公网访问 10个IPv4端口+1个独立IPv6 | 峰值带宽 500M不限流量(合理使用) | 操作系统 Linux | Debian13 Alpine3.23'
  - [4] 2026-10-24: the form's inputs, read from the markup: name='email' placeholder='请输入邮箱', name='code' placeholder='请输入验证码', name='password', name='checkPassword', plus a privacy checkbox - no card, address, phone or ID field
  - [2] 2026-10-24: quoted pre-purchase note: 'NAT服务器没有独立IP，仅有一个IP的部分端口使用权' and '4、屏蔽出站25端口' and '以上仅屏蔽IPv4，IPv6目前无任何屏蔽' and '因LXC和docker属于同一类型虚拟化，因此禁止LXC容器再安装docker使用' and '由于本站产品廉价，定位为玩具属性，无法并且不建议作为商用用途，请做好数据备份。'
  - [2] 2026-10-24: quoted refund and traffic terms: '部分服务器流量有限，若流量超额，会补偿时长至流量恢复。' and '本站产品仅5元及以上产品支持24小时内退款，其他可24小时内"自助退款"至余额'
  - [4] 2026-11-02: the register page's fields are an email address, an emailed code, a password and a confirmation | capture: sha256:f3bf752221aba608e3a3c8eaaf2f4c4f6e1c8b296c4f0fb872c1f31fcb9289ec | quote: 邮箱注册** 邮箱 请输入邮箱 发送验证码 获取验证码 密码 确认密码 注册 我已阅读并同意 服务条款 和 隐私政策
  - [4] 2026-11-02: registration asks for an email address and an emailed code, with no phone and no card field | capture: sha256:f3bf752221aba608e3a3c8eaaf2f4c4f6e1c8b296c4f0fb872c1f31fcb9289ec | quote: 邮箱注册** 邮箱 请输入邮箱 发送验证码 获取验证码 密码 确认密码 注册 我已阅读并同意 服务条款 和 隐私政策
- sources:
  - [1] https://idc.jjfly.cloud/cart
  - [2] https://idc.jjfly.cloud/knowledgebaseview?id=1
  - [3] https://idc.jjfly.cloud/cart?action=configureproduct&pid=6
  - [4] https://idc.jjfly.cloud/register
