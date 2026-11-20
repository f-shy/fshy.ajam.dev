# CloudPub

> cloudpub.ru | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudpub/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudpub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudPub

- `egress/cloudpub` | fails-quota | evidence documented | binding volume-quota | category udp port forward (hosted, RU) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://cloudpub.ru/plans
- price USD 0
- free tier: 250 GB of traffic per month on the free plan, with HTTP and HTTPS publishing and Minecraft servers on the standard core | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 250 GB of traffic per month on the free plan; PRO is stated as unlimited at 399 RUB per month; ingress: tcp | metered: yes | free allowance: 250 GB of traffic per month on the free plan; PRO is stated as unlimited at 399 RUB per month | source: [1]
- identity: email | detail: an account at cloudpub.ru/auth/sign-up | country: None
- interface: cli
- limits:
  - volume-quota (binding): 250 GB traffic per month [1]
  - write-gated: TCP, UDP and SSH publishing is a PRO feature [1]
- binding note: 250 GB is 0.227 TiB, and UDP is behind the paid plan as well.
- interface detail: clo publish http 3000 and a web dashboard
- tooling: clo CLI, desktop app, Docker, Rust and Python SDKs
- composes with: the Minecraft path is a TCP game tunnel; nothing here reaches a WireGuard peer
- reliability: Client software is distributed as a signed binary from cloudpub.ru. Free-tier traffic is metered.
- notes: Russian tunneling provider supporting TCP, HTTP and UDP forwarding. Free plan provides 250 GB of transfer and excludes UDP.
- evidence note: The plan table is a Russian-language page; the free column lists HTTP/HTTPS, subdomains, certificates, support, Minecraft and 250 GB, and the PRO column adds TCP/UDP/SSH. That reading is the one the layout supports.
- extras:
  - wg_path: none
  - wg_detail: TCP, UDP and SSH publishing is listed in the PRO-only group of the plan table, not the free group, so the free plan has no UDP port
  - ingress: tcp
  - volume_tib_month: 0.227374
  - volume_stated: 250 GB of traffic per month on the free plan; PRO is stated as unlimited at 399 RUB per month
  - bytes_transit: yes
  - transit_note: CloudPub relays the published traffic
- evidence:
  - [1] 2026-10-23: free plan: 250 GB traffic per month, HTTP/HTTPS publishing; PRO adds 'Publishing TCP, UDP and SSH services' and unlimited traffic
  - [2] 2026-10-23: 'Eleven protocols out of the box' including TCP and UDP, and 'free tier forever'
- sources:
  - [1] https://cloudpub.ru/plans
  - [2] https://cloudpub.ru/
