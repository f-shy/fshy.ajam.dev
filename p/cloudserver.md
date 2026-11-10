# CloudServer

> cloudserver.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudserver/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudServer

- `egress/cloudserver-linux-kvm-1gb` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS: KVM VPS with a metered monthly allowance and a 1 Gbps port | tier 1GB
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:55:17.627Z (live) | stale on 2026-12-05
- url https://www.cloudserver.net/linux-vps/
- free tier: No free tier. The 1GB Linux KVM plan is $4.00/mo: 1GB RAM, 1 vCPU, 25GB SSD RAID-10, 1Gbps, 5TB, 1 IPv4. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 5TB of monthly bandwidth on a 1Gbps port; the overage action and the byte tolerance are not published on the pages read. | metered: yes | free allowance: 5 TB per month | source: [1]
- identity: card | detail: The terms have the customer allow a charge to a credit card or bank account before activation; an account is made when the first order is placed.
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB monthly bandwidth; overage action not published [1]
- binding note: 5 TB is the only countable figure and is above 1 TiB a month; its overage action is not published.
- interface detail: Root Linux KVM VPS.
- tooling: Any SSH client.
- composes with: A 5 TB, 1Gbps KVM box on one IPv4; port and protocol restrictions are not published on the pages read.
- reliability: The terms say service charges keep accruing on a suspended account.
- notes: The vendor lists a monthly price; the serverdeals annual LEB plan was not found on its pages.
- evidence note: Plan table, terms and account page read on 2026-11-04. The serverdeals listing LEB-1GB (USD 10.00 a year, 1000 GB) was not found on the vendor pages read.
- extras:
  - term: monthly
  - virtualization: KVM
- evidence:
  - [1] 2026-11-04: the 1GB plan lists 5TB of bandwidth, a 1Gbps port and USD 4.00 a month | capture: sha256:6701f15d05a43f83acfd976661ec418491bab01a37bd6ea852bb231661a46bf4 | quote: 1GB 1GB RAM 1 x vCPU 25GB SSD RAID-10 1Gbps 5TB 1 IPv4 $4.00/mo
  - [1] 2026-11-04: Linux KVM packages include a 1Gbps port and monthly bandwidth | capture: sha256:6701f15d05a43f83acfd976661ec418491bab01a37bd6ea852bb231661a46bf4 | quote: Linux KVM packages include SSD RAID-10 storage, 1Gbps port speed, monthly bandwidth, and one IPv4 address.
  - [2] 2026-11-04: activation involves a charge to a credit card or bank account | capture: sha256:28fdbed6bc9d0066d80870123815594f2a9b3a8e731b8e99806d8ead4d9fe38e | quote: 1.5.1 Prior to activation of your user account and at any applicable time thereafter you agree to allow CloudServer to charge your provided credit card or bank account.
  - [3] 2026-11-04: an account is created by placing an order | capture: sha256:f9edde3010dac476c103388daf275484d52c12ff441e86a457d508b3318eeb05 | quote: To create an account, please [place an order with us](https://cloudserver.net/billing/cart.php)
  - [4] 2026-11-04: serverdeals lists a CloudServer LEB-1GB at USD 10.00 a year with 1000 GB, a listing not found on the vendor pages read | quote: ###### LEB-1GB
- sources:
  - [1] https://www.cloudserver.net/linux-vps/
  - [2] https://www.cloudserver.net/tos/
  - [3] https://cloudserver.net/billing/register.php
  - [4] https://serverdeals.cc/
