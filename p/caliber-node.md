# Caliber Node

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/caliber-node/ | JSON https://fshy.ajam.dev/api/v1/entity/caliber-node.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Caliber Node

- `compute/caliber-node` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://lowendtalk.com/discussion/221603/caliber-node-10-year-cloud-apps-dallas-nuremberg-singapore-new-bring-your-own-server
- free tier: USD 10/year for the Micro plan: 1 shared vCPU on an Intel Xeon Gold, 1 GB DDR4, 15 GB SSD, in Dallas, Nuremberg or Singapore, with a 250-app one-click catalogue, automatic HTTPS and custom domains, per-app CIDR allow-listing, one-click app updates, transactional email with SPF and DKIM, snapshots on a daily or weekly schedule, health-check monitoring with email alerts, and a container terminal, SFTP and app logs. The app count is limited only by the resources. A separate option puts the same panel on the customer's own server. This is app hosting and not a VPS: the thread says so directly. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated: no monthly transfer figure, no port speed and no overage term appear in the thread | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): no bandwidth figure appears anywhere in the thread, so the only numbered ceilings are the 1 GB of RAM, 15 GB of SSD and 1 shared vCPU that the plan caps. Nothing about traffic is established, and the field is named volume-quota only because the resource quota is the limit that exists; a reader should treat the transfer allowance as unverified rather than absent. [1]
- limits note: no bandwidth figure appears anywhere in the thread, so the only numbered ceilings are the 1 GB of RAM, 15 GB of SSD and 1 shared vCPU that the plan caps. Nothing about traffic is established, and the field is named volume-quota only because the resource quota is the limit that exists; a reader should treat the transfer allowance as unverified rather than absent.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a panel with a container terminal, SFTP, app logs, per-app CIDR firewall rules, scheduled snapshots and health-check alerts; no API or CLI is documented on the page read
- composes with: USD 10 a year is USD 0.83/month for 1 GB of RAM and 15 GB of disk on a container platform with automatic HTTPS, which is the cheapest way among evaluated providers to put a hosted application and its certificate online without administering a machine; the missing transfer figure is the whole risk, since an app that serves bytes could hit a cap nobody has published.
- reliability: no reliability event recorded
- notes: Recorded from the forum thread alone with no vendor page: the thread links no provider site, the offer index links only the thread, and evaluated providers does not guess a domain. That is why confidence is reported and the binding note says what is unverified. verification criteria: the vendor domain, the transfer allowance, and whether the Bring Your Own Server option is priced separately, since the thread describes it without a figure.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
- evidence:
  - [1] 2026-10-22: the offer thread, posted September 29, 2026, quoted from its table: 'Plan Micro', 'CPU 1 shared vCPU - Intel Xeon Gold', 'RAM 1 GB DDR4', 'Storage 15 GB SSD', 'App catalog 250+ one-click apps', 'App limit As many as your resources can handle', 'Location Dallas, USA - Nuremberg, Germany - Singapore'; body text: 'Managed Cloud Apps - $10/year'; 'Our managed hosting is an app hosting service, not a VPS'
  - [2] 2026-10-22: the thread carries no vendor URL in its body, and the only provider site reachable from the offer index entry is the LowEndTalk thread itself: did not establish a vendor domain for Caliber Node and did not guess one
- sources:
  - [1] https://lowendtalk.com/discussion/221603/caliber-node-10-year-cloud-apps-dallas-nuremberg-singapore-new-bring-your-own-server
  - [2] https://lowendtalk.com/
