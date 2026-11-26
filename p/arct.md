# Arct Cloud

> arct.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arct/ | JSON https://fshy.ajam.dev/api/v1/entity/arct.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arct Cloud

- `compute/arct-cloud` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-12-08
- url https://www.arct.cloud/
- price parsed USD 3.89/mo
- free tier: USD 3.89 per month for cvm.pico in the Cost Optimized series: 1 vCPU, 1 GB RAM, 15 GB NVMe, 1 TB of outbound transfer a month, as the pricing page's table prints. The page prints monthly terms only; no annual or quarterly price appears on any page read. The terms state card plans renew automatically at the end of each billing period for a new period of the same length at the renewal price shown at checkout, and crypto or account-credit plans renew by invoice instead. The order flow is the console at console.arct.cloud behind a sign-up gate (e-mail address and password, or Google, Discord or GitHub sign-in), so the cart's own term prices are unverified: behind a sign-up. No sold-out marker on the pricing page. Overage beyond the allowance is USD 0.01 per GB, USD 0.02 per GB in Tokyo. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Outbound transfer is counted per plan: 1 TB a month on cvm.pico up to 6 TB a month on cvm.xlarge in the Cost Optimized series, 5 to 10 TB in the General Purpose and High Performance series; inbound is free and not counted. Overage above the allowance costs USD 0.01 per GB, or USD 0.02 per GB in Tokyo. Backups and snapshots are billed separately. | metered: yes | free allowance: 1 TB per month outbound | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 TB a month of outbound transfer on the entry plan is the wall, and the 25 Gbps network capacity behind it is unreachable at that allowance: 1 TB a month averages about 3 Mbit/s. The thread says '1 TB outbound transfer per month' specifically, so inbound is not counted. No overage price and no post-allowance throttle are stated. [1]
- limits note: 1 TB a month of outbound transfer on the entry plan is the wall, and the 25 Gbps network capacity behind it is unreachable at that allowance: 1 TB a month averages about 3 Mbit/s. The thread says '1 TB outbound transfer per month' specifically, so inbound is not counted. No overage price and no post-allowance throttle are stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a custom customer console at console.arct.cloud with VNC console, snapshots, resize, reinstall and daily backups; no API or CLI is documented on the pages read
- composes with: USD 3.89 is the lowest monthly rate for a 1 GB machine among evaluated providers and the quarterly term brings it to USD 3.50 a month; 1 TB of outbound caps it at a control node or an API front end, and the separate snapshot charge at USD 0.04 per GB per month is the line to watch on a 15 GB disk.
- reliability: no reliability event observed: the thread is a first post from a company registered in Wyoming, with no operating history read.
- notes: The vendor page prices one plan and the thread prices the same one, and they agree. verification criteria: the General Purpose and High Performance series, which the thread names but does not price, and whether the 25 Gbps network capacity is per-server or per-site, since the thread calls it 'network capacity' and not a port.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - price_on_page: USD 3.89/month for cvm.pico
  - renewal_usd: not published: the terms renew card plans at the checkout price and the checkout is behind a sign-up, so no public page prints a renewal figure
- evidence:
  - [1] 2026-10-22: vendor page quoted: 'cvm.pico 1 vCPU - 1 GB RAM - 15 GB NVMe $3.89/mo'; 'Daily backups add 20% to the server's monthly price. Snapshots cost $0.04 per GB per month'; page description: 'Cloud servers from $3.89/mo with NVMe storage and DDoS protection'
  - [2] 2026-10-22: the offer thread states: 'cvm.pico - 1 vCPU / 1 GB RAM / 15 GB NVMe / 1 TB outbound transfer per month', 'Monthly: $3.89', 'Quarterly: $10.50 total every 3 months'; 'Our footprint includes London, Frankfurt, Amsterdam, Salt Lake City, and Tokyo'; the operator is 'Arct Technology LLC, a Wyoming-registered company'
  - [3] 2026-11-07: the pricing table prices cvm.pico at USD 3.89 per month with 1 TB of outbound transfer | capture: sha256:11a3a9a9a923de94ac7f4e6c561290bd0af2f05f4d3a2449fb6dd4d10d880450 | quote: | cvm.pico | 1 | 1 GB | 15 GB | 1 TB/mo | $3.89 |
  - [3] 2026-11-07: the overage price is published on the pricing page | capture: sha256:11a3a9a9a923de94ac7f4e6c561290bd0af2f05f4d3a2449fb6dd4d10d880450 | quote: Outbound transfer above your plan's monthly allowance costs $0.01 per GB, or $0.02 per GB in Tokyo.
  - [3] 2026-11-07: the pricing table re-states the entry plan's price and 1 TB outbound allowance | capture: sha256:11a3a9a9a923de94ac7f4e6c561290bd0af2f05f4d3a2449fb6dd4d10d880450 | quote: | cvm.pico | 1 | 1 GB | 15 GB | 1 TB/mo | $3.89 |
  - [4] 2026-11-07: the console sign-up gate asks an e-mail address and password and offers Google, Discord and GitHub sign-in | capture: sha256:d0a07ab40b4d889feeae4f93af33afb2f2fb19ffc959b38c9bdf2ef2ccd7ffe7 | quote: Continue with Google
  - [5] 2026-11-07: the renewal rule is printed in the terms: automatic renewal at the checkout price, changed only under section 3.7 | capture: sha256:bc465bd759c5d5749288eaec3f15ff97939d7cd2413fef1f78bb8ce16ef402ac | quote: If you pay by card, each Server's plan renews automatically at the end of each billing period for a new period of the same length. We charge your saved card the renewal price until you cancel.
  - [3] 2026-11-07: the vendor's pricing table prices cvm.pico at USD 3.89 a month | capture: sha256:11a3a9a9a923de94ac7f4e6c561290bd0af2f05f4d3a2449fb6dd4d10d880450 | quote: | cvm.pico | 1 | 1 GB | 15 GB | 1 TB/mo | $3.89 |
  - [5] 2026-11-07: the terms print the renewal rule and point to the checkout price, which only an account sees | capture: sha256:bc465bd759c5d5749288eaec3f15ff97939d7cd2413fef1f78bb8ce16ef402ac | quote: If you pay by card, each Server's plan renews automatically at the end of each billing period for a new period of the same length. We charge your saved card the renewal price until you cancel.
- sources:
  - [1] https://www.arct.cloud/
  - [2] https://lowendtalk.com/discussion/221949/meet-arct-cloud-amd-epyc-kvm-vps-from-3-89-mo-nvme-ipv4-custom-control-panel
  - [3] https://www.arct.cloud/pricing
  - [4] https://console.arct.cloud/auth/login?screen_hint=signup&returnTo=/servers/new
  - [5] https://www.arct.cloud/legal/terms
