# UpCloud

> upcloud.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/upcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UpCloud (Compute)

- `compute/upcloud` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:16.227Z (live) | stale on 2026-11-22
- url https://upcloud.com/pricing/
- price parsed USD 14/mo
- free tier: no free tier: servers from EUR 3 a month or by the hour, with data transfer included and 250 Mbit/s of bandwidth at the entry size | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): billed by the hour; the entry plan is EUR 3 a month for 1 GB, 1 core and 10 GB of storage [1]
  - per-ip-shaping: data transfer carries zero cost and bandwidth is fixed per plan, from 250 Mbit/s to 500 Mbit/s in the shown rows [1]
  - retention-clamped: pricing changes take effect on 2026-11-16 for Cloud Server plans, standard and archive block storage, and Windows licences [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the ladder, the bandwidth per size and the zero-cost transfer position. There is no free tier, so the verdict moves to paid-only, and the 2026-11-16 price change is recorded
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 10
  - shape.note: the entry plan; the ladder runs to 16 GB and 4 cores
  - session_cap.restart_required: no
  - session_cap.note: hourly billing on a server that runs until stopped; the page states no reap
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 6.25
  - m24h_usd: 14.0
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - granularity.min_billed_s: 3600
  - burst_x: 2.0249
  - burst_bill: min 1 h
  - ps.gib: 10
  - ps.price: included in the plan; block storage priced separately
  - ps.durability: standard block storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.ipv6: yes
  - net.allowance: zero-cost data transfer
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'All services are billed by the hour' with 'zero-cost data transfer fees' and the ladder '1 GB 1 core 250 Mbit/s 10 GB EUR 3/mo' through '16 GB 4 core 500 Mbit/s 50 GB EUR 28/mo', plus a notice that pricing changes on 2026-11-16, quoted
- sources:
  - [1] https://upcloud.com/pricing/

## UpCloud (Starter 1 vCPU / 1 GB)

- `egress/upcloud-starter-vps` | paid-only | evidence documented | binding volume-quota | category origin VM (paid VPS) | tier Starter 1 vCPU / 1 GB
- needs card yes, phone yes, ID no, institution no | verified 2026-11-03T07:36:43.376Z (live) | stale on 2026-12-04
- url https://upcloud.com/pricing/
- price EUR 3 a month with 0.5 TB of egress included | parsed USD 6.72/TB-mo
- free tier: no free plan: the Starter 1 GB plan is EUR 3 a month and includes 0.5 TB of public egress under a fair transfer limit | unit: TB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: A third-party price index lists the same plan as unmetered; the vendor's network-transfer page gives 0.5 TB.
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: STARTER-1xCPU-1GB includes 0.5 TB of public egress, Fair Transfer Policy applies; public ingress is included with no stated cap; bandwidth is 250 Mbit/s at this size; inbound UDP policy is not stated on the pages read | metered: yes | free allowance: 0.5 TB a month of public egress on the EUR 3 plan | source: [1]
- identity: card | detail: registration asks for name, email address and phone number, and a credit card with a billing address is required to activate the free trial; whether a paid order without the trial needs the same was not read | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 0.5 TB of public egress included on STARTER-1xCPU-1GB, Fair Transfer Policy applies [1]
  - per-ip-shaping: 250 Mbit/s bandwidth on the 1 GB and 1 vCPU size [2]
- limits note: The overage rate beyond the fair transfer limit was not read: the page says transfer 'exceeding the fair amount is no longer automatically charged'.
- binding note: at 1 TiB a month the 0.5 TB included egress runs out first on this size; larger Starter sizes include 1 TB or more
- interface detail: SSH to the server's public IPv4 or IPv6 address; up to five public IPv4 and five public IPv6 addresses can be attached to one server
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 3 a month origin in London or elsewhere with a public IPv4 and a public IPv6 address; the 0.5 TB included egress, not the price, is the limit
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read
- notes: The trial with EUR 10 of credit is a trial of this product, not a free plan. The price index serverworth.com lists this plan as unmetered; the vendor's own table gives 0.5 TB, which is the figure used here.
- evidence note: price, bandwidth and the 0.5 TB allowance are quoted from the vendor's pricing and network-transfer pages read on 2026-11-03; no server was ordered, so inbound UDP was not probed
- extras:
  - wg_path: native-conf
  - wg_detail: a full Linux guest with a public IPv4 and IPv6; wg-quick binds UDP natively unless a firewall is added; inbound UDP was not probed
  - ingress: unverified: no inbound port policy is stated on the pages read
  - volume_stated: 0.5 TB of public egress included on STARTER-1xCPU-1GB
  - bytes_transit: yes
  - transit_note: bytes leave through the server's own public address on UpCloud's network
- evidence:
  - [2] 2026-11-03: the entry Starter plan is 1 GB, 1 core, 250 Mbit/s and 10 GB at EUR 3 a month | capture: sha256:fcfbc0b293caaea9d2ef21ca4f9ea5a7c77626bcbad147091e2d1e4219d068e9 | quote: | 1 GB | 1 | 250 Mbit/s | 10 GB | **€3/mo *** |
  - [1] 2026-11-03: STARTER-1xCPU-1GB includes 0.5 TB of public egress | capture: sha256:9d77b362c772662671039574dbb0db5280a08edcf9fd5a3888b37ceb319faa33 | quote: | STARTER-1xCPU-1GB | 0.5 TB |
  - [1] 2026-11-03: public ingress carries no transfer charge or stated cap | capture: sha256:9d77b362c772662671039574dbb0db5280a08edcf9fd5a3888b37ceb319faa33 | quote: Public ingress transfer and private network transfer in both the Utility network and SDN Private Networks are included in all Cloud Servers.
  - [3] 2026-11-03: a server can hold public IPv4 and IPv6 addresses, up to five of each | capture: sha256:25a433135ea105b6e24cb367e1b4354cea223f71af734ca5b87a6e6f31b2cacc | quote: You can have up to five public IPv4 and five public IPv6 addresses on your server.
  - [4] 2026-11-03: registration asks for name, email address and phone number | capture: sha256:bb808a8eef1ab00e633057cbdbb1706f3ab9b17ecea7b3c0f4f2e4337a19db08 | quote: UpCloud users are required to enter certain personal details when registering an account including name, email address and phone number.
  - [5] 2026-11-03: the free trial is gated by a credit card and billing information | capture: sha256:047567873584fdbea333f6733ea1c5971e440073f30bd36dc9c50e92e2f9b104 | quote: Just verify your identity with a credit card and billing information to enter the free trial.
  - [5] 2026-11-03: the 7-day trial carries EUR 10 of credit | capture: sha256:047567873584fdbea333f6733ea1c5971e440073f30bd36dc9c50e92e2f9b104 | quote: You also get €10 of free credit, which pays for the resources you use during the trial.
- sources:
  - [1] https://upcloud.com/docs/products/networking/network-transfer/
  - [2] https://upcloud.com/pricing/
  - [3] https://upcloud.com/docs/guides/attaching-new-ip-addresses/
  - [4] https://upcloud.com/docs/getting-started/accounts/account-requirements/
  - [5] https://upcloud.com/docs/getting-started/free-trial/
