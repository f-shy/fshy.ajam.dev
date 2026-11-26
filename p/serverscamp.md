# ServersCamp

> serverscamp.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serverscamp/ | JSON https://fshy.ajam.dev/api/v1/entity/serverscamp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ServersCamp

- `compute/serverscamp` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-25T05:18:25.129Z (live) | stale on 2026-12-10
- url https://serverscamp.com/
- free tier: Simple VPS from EUR 1.00/month in Bucharest, Romania: VPS 0.75 gives 0.5 vCore, 768MB RAM, 10GB storage and 500GB bandwidth. VPS 1 is EUR 1.50 for 1 vCore, 1GB RAM, 20GB storage and 1TB bandwidth; VPS 2 is EUR 3.00 for 2 vCores, 2GB RAM, 40GB storage and 2TB bandwidth; VPS 4 is EUR 6.00 for 2 vCores, 4GB RAM, 80GB storage and 3TB bandwidth. Every server gets a 1 Gbit/s port, 1x IPv4 plus IPv6 /56, daily backups (+20% of the plan price, last 5 kept), VNC and serial console, and reverse DNS; the CPU depends on the node: Intel Xeon Gold 6154, Xeon Gold 6132, Xeon Silver 4116 or AMD EPYC 7543. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: outbound only, throttled to 100 Mbit/s after the monthly quota with no overage charge | metered: yes | free allowance: 3 TB per month on VPS 4; 500 GB on the EUR 1.00 plan | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): each plan carries a monthly allowance and then drops to 100 Mbit/s until the next month, with no overage charge: 500 GB on VPS 0.75, 1 TB on VPS 1, 2 TB on VPS 2 and 3 TB on VPS 4. That is the unusual case where the post-quota behaviour is stated, and it is a throttle rather than a stop, so the counter binds and then the port does. [2]
- limits note: each plan carries a monthly allowance and then drops to 100 Mbit/s until the next month, with no overage charge: 500 GB on VPS 0.75, 1 TB on VPS 1, 2 TB on VPS 2 and 3 TB on VPS 4. That is the unusual case where the post-quota behaviour is stated, and it is a throttle rather than a stop, so the counter binds and then the port does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a control panel with VNC, serial console and reverse DNS is named, plus a documented cloud API on the separate cloud product; no CLI is mentioned for Simple VPS
- composes with: EUR 6.00 for 4 GB and 80 GB with 3 TB of outbound and a stated throttle instead of a surprise invoice is the most predictable bandwidth row among documented hosts, and the EUR 1.00 plan is the cheapest machine here of any size; the Romanian location is the only site, so latency to Western Europe is the trade
- reliability: no reliability event recorded
- notes: The vendor page states hourly billing on the cloud line while the thread prices Simple VPS monthly, which are two products and not a disagreement. Unverified: whether the Simple VPS plans are orderable without the cloud account, and whether the 100 Mbit/s post-quota throttle also applies to inbound, which the thread does not say. The thread states prices in EUR and no USD conversion was performed here.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 80
- evidence:
  - [1] 2026-10-22: the offer thread, posted October 22, 2026, quoted: 'VPS 4 - EUR 6.00/mo ... 2 vCores / 4GB RAM / 80GB Storage / 3TB Bandwidth'; 'VPS 0.75 - EUR 1.00/mo ... 0.5 vCore / 768MB RAM / 10GB Storage / 500GB Bandwidth'; 'Location: Bucharest, Romania'; 'Network: 1 Gbit/s port, 1x IPv4 + IPv6 /56'; 'Traffic: only outbound counts, 100 Mbit/s after the quota until next month, no overage charges'
  - [2] 2026-10-22: the vendor page answered 200 and describes the platform ('Cloud servers, managed databases and storage in Europe, billed by the hour in EUR', replicated software-defined storage, 200k IOPS per disk) but renders no Simple VPS plan table or price, so the figures rest on the forum post
  - [1] 2026-11-25: the vendor announcement states the EUR 1.00 entry plan, the VPS 1, VPS 2 and VPS 4 rows, the Bucharest location, the included network, panel and backup terms, and the CPU options | capture: sha256:b6daf367c69d5753cd24af771aa8acc75a3b6fb7929011692994f694a91d202d | quote: VPS 0.75 · €1.00/mo ... 0.5 vCore / 768MB RAM / 10GB Storage / 500GB Bandwidth ... VPS 1 · €1.50/mo ... 1 vCore / 1GB RAM / 20GB Storage / 1TB Bandwidth ... VPS 2 · €3.00/mo ... 2 vCores / 2GB RAM / 40GB Storage / 2TB Bandwidth ... VPS 4 · €6.00/mo ... 2 vCores / 4GB RAM / 80GB Storage / 3TB Bandwidth ... Location: Bucharest, Romania ... CPU: depends on the node, Intel Xeon Gold 6154, Xeon Gold 6132, Xeon Silver 4116 or AMD EPYC 7543 ... Network: 1 Gbit/s port, 1x IPv4 + IPv6 /56 ... Backups: daily, +20% of the plan price, last 5 kept ... Panel: VNC and serial console, reverse DNS
  - [1] 2026-11-25: the vendor's offer still states the entry price, the four plan rows and the included network and backup terms | capture: sha256:b6daf367c69d5753cd24af771aa8acc75a3b6fb7929011692994f694a91d202d | quote: VPS 0.75 · €1.00/mo ... 0.5 vCore / 768MB RAM / 10GB Storage / 500GB Bandwidth ... VPS 1 · €1.50/mo ... 1 vCore / 1GB RAM / 20GB Storage / 1TB Bandwidth ... VPS 2 · €3.00/mo ... 2 vCores / 2GB RAM / 40GB Storage / 2TB Bandwidth ... VPS 4 · €6.00/mo ... 2 vCores / 4GB RAM / 80GB Storage / 3TB Bandwidth ... Location: Bucharest, Romania ... CPU: depends on the node, Intel Xeon Gold 6154, Xeon Gold 6132, Xeon Silver 4116 or AMD EPYC 7543 ... Network: 1 Gbit/s port, 1x IPv4 + IPv6 /56 ... Backups: daily, +20% of the plan price, last 5 kept ... Panel: VNC and serial console, reverse DNS
  - [1] 2026-11-25: the vendor announcement, not the vendor cloud page, states the Simple VPS entry plan and price | capture: sha256:b6daf367c69d5753cd24af771aa8acc75a3b6fb7929011692994f694a91d202d | quote: VPS 0.75 · €1.00/mo ... 0.5 vCore / 768MB RAM / 10GB Storage / 500GB Bandwidth
- sources:
  - [1] https://lowendtalk.com/discussion/222400/serverscamp-new-simple-vps-starting-1-month
  - [2] https://serverscamp.com/
