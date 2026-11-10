# OuiHeberg

> ouiheberg.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ouiheberg/ | JSON https://fshy.ajam.dev/api/v1/entity/ouiheberg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OuiHeberg

- `egress/ouiheberg-linux-vps-01g` | paid-only | evidence documented | binding volume-quota | category IPv6-only VPS | tier Linux VPS 01G
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.032Z (live) | stale on 2026-12-05
- url https://www.ouiheberg.com/en/linux-vps
- free tier: No free tier. Linux VPS 01G is USD 2.09 a month: 1 GB RAM, 1 Xeon Platinum vCore, 10 GB NVMe, 500 GB of traffic a month, native IPv6 and no IPv4 address. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The aggregator lists a 'LET-MR-2' plan at EUR 18 a year with 20 TB; no such plan is on the vendor's public pages read, and the aggregator's order link did not answer a text read, so that plan and its 20 TB are not confirmed.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB of traffic per month on a 1 Gbps port (homepage card '1 Gbps / 500 GB'); no overage price or post-cap throttle is stated on the pages read. | metered: yes | free allowance: 500 GB a month | source: [1]
- identity: email | detail: unverified: behind a sign-up. The terms say the customer 'undertakes to prove their identity and exact contact details by providing supporting documents' and that the vendor may verify this at any time; the sign-up fields are not shown to a text read. Payment is by card, PayPal or crypto.
- interface: ssh
- limits:
  - volume-quota (binding): 500 GB of traffic per month [1]
  - per-ip-shaping: no IPv4 address on this plan: IPv6 only [1]
- binding note: 500 GB a month is the first number to fail; the missing IPv4 address restricts reachability but does not fail on a schedule.
- interface detail: KVM Linux VPS with root access over IPv6 only; the page names no port or protocol filter.
- tooling: Any SSH client over IPv6.
- composes with: An IPv6-only box: outbound IPv4 destinations are reachable only through a translator or proxy that the user supplies, and inbound reaches the VPS only over IPv6.
- reliability: The terms allow the vendor to suspend the service for false or inaccurate identity details.
- notes: The cheapest public tier is IPv6-only; the vendor's IPv4 plans start higher (Linux VPS 04G is USD 8.11 a month).
- evidence note: Price, allowance and IPv6-only network are quoted from the vendor's plan page. Sign-up fields are not shown to a text read.
- extras:
  - ipv4: none on this plan
  - ipv6: native
  - locations: Marseille, Frankfurt, Amsterdam and New York
- evidence:
  - [1] 2026-11-04: Linux VPS 01G has 1 GB RAM, 1 vCore, 10 GB NVMe, 500 GB of traffic and no IPv4 address | capture: sha256:b374a7ce9e9caeaf4bfae21a8a90c49fecbc38de75a5d373ce1cf92321a1c7e5 | quote: 1 GB of RAM, 1 Xeon Platinum vCore, 10 GB NVMe and 500 GB of traffic. For your bots, scripts and development environments. Native IPv6 connectivity, no IPv4 address.
  - [1] 2026-11-04: the plan is USD 2.09 a month | capture: sha256:b374a7ce9e9caeaf4bfae21a8a90c49fecbc38de75a5d373ce1cf92321a1c7e5 | quote: $2.09/monthOrder →
  - [1] 2026-11-04: the plan is IPv6-only and the 500 GB is per month | capture: sha256:b374a7ce9e9caeaf4bfae21a8a90c49fecbc38de75a5d373ce1cf92321a1c7e5 | quote: It has no IPv4 address and suits bots, scripts and test environments reachable over IPv6.
  - [2] 2026-11-04: the entry Linux VPS card shows a 1 Gbps port with 500 GB | capture: sha256:8b4577b5adc49fb3e814bedae1557246bc0a0302c02203fd888a65308a85636d | quote: - 1 Gbps / 500 GB
  - [2] 2026-11-04: payment is by card, PayPal or crypto, with no commitment | capture: sha256:8b4577b5adc49fb3e814bedae1557246bc0a0302c02203fd888a65308a85636d | quote: Monthly, cancel anytime. Pay by card, PayPal or crypto.
  - [3] 2026-11-04: the terms require the customer to prove identity with documents on request; the sign-up fields are not shown | capture: sha256:e6720f6f8c6650a8329cc95c9ab0482ccc0160f104455c54d7a199775de39165 | quote: The client undertakes to prove their identity and exact contact details by providing supporting documents.
  - [4] 2026-11-04: the aggregator lists a LET-MR-2 plan at EUR 18 a year with 20 TB, which is not on the vendor's public pages read | quote: ###### LET-MR-2
- sources:
  - [1] https://www.ouiheberg.com/en/linux-vps
  - [2] https://ouiheberg.com/
  - [3] https://ouiheberg.com/en/terms
  - [4] https://serverdeals.cc/
