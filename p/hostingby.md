# Hosting by Design

> hostingby.design | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostingby/ | JSON https://fshy.ajam.dev/api/v1/entity/hostingby.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosting by Design — App hosting 24 TB (owners of seedbox.io)

- `storage/hosting-by-design-app-hosting-24-tb` | qualifies | evidence reported | binding none | category seedbox / app hosting
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:15:44.284Z (live) | stale on 2026-12-10
- url https://hostingby.design/app-hosting/
- price 24TB: €49.95 -> €2.08/TB/mo (~$2.39). 28TB: €59.95 -> €2.14/TB. 18TB: €39.95 -> €2.22/TB. 4TB: €10.95 -> €2.74/TB. 1TB: €6.59 -> €6.59/TB | parsed USD 2.34/TB-mo
- free tier: 24TB HDD (Dedicated Disk) Unlimited 10Gbit+ €49.95 | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The app-hosting table lists storage, outgoing data, uplink port and price per tier; it states no per-object cap.
- retention: source: [1] | note: not stated
- egress: Outgoing data by tier: 1 TB plan 3 TB, 2 TB plan 6 TB, 4 TB plan 10 TB, 8 TB plan 25 TB; the 18 TB, 24 TB and 28 TB dedicated-disk tiers list Unlimited. Uplink port is 10Gbit+ on every tier except the 28 TB tier, which lists 50Gbit. | metered: yes
- identity: email | detail: email
- interface: ssh
- limits note: Metered egress below 18 TB; ~$2.42/TB only achievable at the 24 TB dedicated tier
- interface detail: SSH access to the slot
- tooling: the same as interface detail
- composes with: The dedicated-disk tiers list Unlimited outgoing data; the fair-use policy states no strict limit on data traffic.
- reliability: Seedbox.io now 301-redirects to hostingby.design. Same operator (HNielsen Technologies ApS, DK). Brand consolidation means the old seedbox.io plans/prices are no longer separately purchasable.
- notes: 1 / 2 / 4 / 8 TB shared; 18 / 24 / 28 TB dedicated disk
- evidence note: the app-hosting page states the 24TB dedicated-disk plan with unlimited outgoing data, a 10Gbit+ uplink and a €49.95 price
- extras:
  - price_verbatim: 24TB: €49.95 -> €2.08/TB/mo (~$2.39). 28TB: €59.95 -> €2.14/TB. 18TB: €39.95 -> €2.22/TB. 4TB: €10.95 -> €2.74/TB. 1TB: €6.59 -> €6.59/TB
- evidence:
  - [1] 2026-10-21: full table: 1TB/3TB/€6.59, 2TB/6TB/€8.25, 4TB/10TB/€10.95, 8TB/25TB/€19.95, 18TB/Unlimited/€39.95, 24TB/Unlimited/€49.95, 28TB/Unlimited/€59.95
  - [2] 2026-10-21: 
  - [1] 2026-11-09: the 24 TB dedicated-disk plan costs €49.95 with unlimited outgoing data and a 10Gbit+ uplink | capture: sha256:3578acd77cd806538f8a75e098c259fc4b493f6bf1f1c84e1f4d8a4c43d58533 | quote: 24TB HDD (Dedicated Disk) Unlimited 10Gbit+ €49.95
  - [1] 2026-11-09: the 1 TB shared plan lists 3 TB outgoing data, a 10Gbit+ uplink and a €6.59 price | capture: sha256:3578acd77cd806538f8a75e098c259fc4b493f6bf1f1c84e1f4d8a4c43d58533 | quote: 1TB HDD Storage 3TB 10Gbit+ €6.59
  - [1] 2026-11-25: the 24 TB dedicated-disk plan lists unlimited outgoing data, a 10Gbit+ uplink and €49.95 | capture: sha256:6de913005fe756cf6396f161ca507017be0bab873f826f147515ceee72504ca8 | quote: 24TB HDD (Dedicated Disk) Unlimited 10Gbit+ €49.95
  - [1] 2026-11-25: the table row carries no per-object cap | capture: sha256:6de913005fe756cf6396f161ca507017be0bab873f826f147515ceee72504ca8 | quote: 24TB HDD (Dedicated Disk) Unlimited 10Gbit+ €49.95
  - [1] 2026-11-25: the 28 TB tier lists Unlimited outgoing data and a 50Gbit uplink | capture: sha256:6de913005fe756cf6396f161ca507017be0bab873f826f147515ceee72504ca8 | quote: 28TB HDD (Dedicated disk) Unlimited 50Gbit €59.95
  - [3] 2026-11-25: the fair-use policy sets no strict traffic limit | capture: sha256:47598c54507ce8d553de444f93957796b3f8da774cc81cd9edfbb1f0f00f6a6e | quote: While there is no strict limit on data traffic, users are encouraged to operate within reasonable usage patterns.
  - [4] 2026-11-25: the slot is accessed over SSH | capture: sha256:46ce0c0ccebc9c9aa5f631d538bc56f034fbce971d095f78e55712fe142bf82f | quote: In order to connect to your slot at HostingByDesign, you'll need to access your slot via SSH.
- sources:
  - [1] https://hostingby.design/app-hosting/
  - [2] https://seedbox.io/
  - [3] https://docs.hostingby.design/vps-hosting/fair-use-policy
  - [4] https://docs.hostingby.design/application-hosting/getting-started/how-do-i-connect
