# Feige

> fgnwct.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fgnwct/ | JSON https://fshy.ajam.dev/api/v1/entity/fgnwct.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Feige (fgnwct)

- `egress/feige-fgnwct` | fails-quota | evidence documented | binding per-ip-shaping | category tcp+udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.fgnwct.com/price.html
- price USD 0
- free tier: Free: 0 yuan, speed 0.5 Mbps, 20 concurrent connections, free domain, custom domain allowed, 2 TCP/UDP port numbers, unlimited traffic, daily check-in stacks duration. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Traffic is stated as unlimited on the free plan, with no byte counter named anywhere. The binding number is the speed: 0.5 Mbps sustained for 30 days is about 162 GB, so the plan cannot reach 1 TiB/month even at line rate.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The registration form asks for username, email, emailed verification code and password. No mobile number field and no real-name step appear on it. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): 0.5 Mbps on the free plan [1]
  - request-rate: 20 concurrent connections on the free plan [1]
- binding note: 0.5 Mbps is 5.27 GB/day at line rate, about 162 GB over 30 days, against the 3.24 Mbps that 1 TiB/month needs. Unlimited traffic is true and useless at this speed.
- interface detail: Windows, Linux, macOS and Android clients; http(s) domain proxying plus TCP and UDP port forwarding.
- tooling: vendor client (3.5 MB, unpack and run) plus wg-quick on the local box
- composes with: Two fixed UDP ports at 0.5 Mbps is enough for a WG control channel and a trickle, not for bulk transfer; pair it with a metered free VM for the volume.
- reliability: Daily check-in adds time to the free mapping rather than traffic, so a free tunnel can expire; the vendor states it is a small operation with no guaranteed support.
- notes: Chinese FRP provider offering UDP ingress with email registration. Provides two mapped ports per tunnel under value-added telecom licensing.
- evidence note: Plan table and registration form both read first-party. What would raise the rung is a probe measuring whether the 0.5 Mbps is per tunnel or per account, and whether the two assigned ports survive a reconnect.
- extras:
  - wg_path: inside-udp
  - wg_detail: The site describes a UDP proxy mode for reaching internal machines over UDP, and the free plan includes two TCP/UDP port numbers, so a WG datagram addressed to one of those public UDP ports reaches the local listener. No WG config is issued.
  - ingress: udp
  - volume_stated: Traffic is stated as unlimited on the free plan, with no byte counter named anywhere. The binding number is the speed: 0.5 Mbps sustained for 30 days is about 162 GB, so the plan cannot reach 1 TiB/month even at line rate.
  - bytes_transit: yes
  - transit_note: Vendor relays on Alibaba Cloud, Tencent Cloud and older domestic datacentres.
- evidence:
  - [1] 2026-10-23: free plan is 0 yuan, 0.5 Mbps, 20 concurrent, 2 TCP/UDP ports, unlimited traffic
  - [2] 2026-10-23: the service carries http(s) domain proxying plus TCP and UDP port forwarding
  - [3] 2026-10-23: registration is username, email, emailed code, password
- sources:
  - [1] https://www.fgnwct.com/price.html
  - [2] https://www.fgnwct.com/
  - [3] https://www.fgnwct.com/register.html
