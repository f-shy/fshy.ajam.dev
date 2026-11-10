# iWebFusion

> iwebfusion.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iwebfusion/ | JSON https://fshy.ajam.dev/api/v1/entity/iwebfusion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iWebFusion

- `compute/iwebfusion` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:07.274Z (live) | stale on 2026-12-08
- url https://iwebfusion.net/vps
- price parsed USD 9.38/mo
- free tier: Tiny at $9.38 per month: 1 CPU core, 4 GB RAM, 30 GB SSD, 2 TB bandwidth, 1 IPv4, KVM with SSH access and a SolusVM panel. The vendor's own plan table lists, down the Tiny column, 'Pure SSD' 30 GB, 'Bandwidth' 2TB, 'RAM' 4GB, 'CPU Cores' 1, 'IP addresses' 1, and a price row of '$9.38 Per Month'. The cart (2026-11-07) offers 1, 3, 6 and 12-month terms priced $9.38, $28.14, $56.28 and $112.56 - exactly 1, 3, 6 and 12 times the monthly rate, so every term prices at the monthly rate with no prepay discount, the 12-month term totals $112.56, and the cart accepted the plan add with no stock warning. No renewal price is published. Starter is $18.99 per month with 50 GB, 2.5 TB, 8 GB RAM and 2 cores; Pro is $34.99 with 100 GB, 5 TB, 16 GB and 2 cores. The page prints a bare dollar sign and declares no currency anywhere in it, so the figure is recorded as $ and not as USD. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month included on the Tiny plan as the vendor's table states; the vendor publishes no overage rate on the plan page | metered: yes | free allowance: 2 TB a month | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): 2 TB a month on a 1 Gbps port, with 30 GB of SSD. The disk is the tighter of the two for an indexing role: the monthly transfer is about 68 times the disk's own size. [1]
- limits note: 2 TB a month on a 1 Gbps port, with 30 GB of SSD. The disk is the tighter of the two for an indexing role: the monthly transfer is about 68 times the disk's own size.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: SolusVM and SSH access are named on the plan page; no API or object-storage interface was read.
- composes with: Four gigabytes of RAM and 2 TB of transfer for $9.38 is the best RAM-per-dollar ratio among evaluated providers after mivoCloud, and it is the only one of the seven listing a US west-coast location at the same price as its east-coast one; the 30 GB disk keeps it a front end or a control node, never a store.
- reliability: no reliability event recorded
- notes: Two disagreements between the tracker and the vendor, both recorded rather than resolved in the tracker's favour: the tracker labels the disk 'HDD' while the vendor's table says 'Pure SSD Space', and the tracker states a 1 Gbps port that the plan table does not state (the tracker's own headline figure for this provider is 1 Gbps on every row). Location is tracker-only: the vendor's VPS page names no city, so Bend, Oregon is reported, not documented. verification criteria: the order form, for whether the 1 core is a fair-share vCPU and what the overage rate is above 2 TB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 30
  - price_on_page: $9.38/month for Tiny
- evidence:
  - [1] 2026-10-22: the Tiny column of a table whose rows are features and whose columns are plans, read down that column: disk 'Pure SSD' '30 GB', 'Bandwidth' '2TB', 'RAM' '4GB', 'CPU Cores' '1', 'IP addresses' '1', price '$9.38' 'Per Month'; the page heading reads 'KVM VPS Hosting' and the feature list under the table names 'SSH access', 'SolusVM access', 'Weekly Backups'
  - [1] 2026-10-22: the same table across five plans: 30/50/100/150/300 GB, 2/2.5/5/8/15 TB, 4/8/16/16/24 GB RAM, 1/2/2/4/6 cores at $9.38, $18.99, $34.99, $44.99, $64.99 per month
  - [2] 2026-10-22: tracker row, whose cells the page prints one per line, read in page order: '1 Intel Cores (shared)', '4,096 MB RAM', '30 GB HDD', '2,048 GB/month bandwidth', '1 Gbps port speed', 'IPv4', 'Bend Oregon U.S.A.', with the price cell '$9.38 / month'; the identical row repeats at the same price for Los Angeles, California and Charlotte, North Carolina
  - [3] 2026-11-07: the WHMCS cart resolved the Tiny plan add (final URL cart.php?a=confproduct&i=0) and its price list leads with $9.38, the plan's monthly price; the cart accepted the add, so the plan is in stock | capture: sha256:96bf4a78d68d4f50d88601ca7f50dc305166f4e0d6eb6bfe95b5c229b552b066 | quote: Shopping Cart - iWebFusion ... $9.38
  - [3] 2026-11-07: the cart resolved the Tiny plan and its price list carries $9.38, $28.14, $56.28 and $112.56 | capture: sha256:96bf4a78d68d4f50d88601ca7f50dc305166f4e0d6eb6bfe95b5c229b552b066 | quote: Shopping Cart - iWebFusion ... $9.38
  - probe:https://my.iwebfusion.net/cart.php?a=add&pid=450706 2026-11-07: the cart resolved the Tiny add (final URL cart.php?a=confproduct&i=0) and its price list carries $9.38, $28.14, $56.28 and $112.56 with no stock warning | capture: sha256:89013e76b865a9554270e5888e04971bd28fc32e79ea616285e0625f3951aaa6 | quote: "prices": [ "$9.38", "$28.14", "$56.28", "$112.56",
  - [1] 2026-11-07: the vendor's plan table still prices Tiny at $9.38 Per Month | capture: sha256:23da3895760bee5fba69dee6b0469fd1b3f4f59b10675585dd3d1b414675abea | quote: $9.38 Per Month
  - probe:https://my.iwebfusion.net/cart.php?a=add&pid=450706 2026-11-07: the cart prices Tiny $9.38/$28.14/$56.28/$112.56 across the 1/3/6/12-month terms, unchanged | capture: sha256:89013e76b865a9554270e5888e04971bd28fc32e79ea616285e0625f3951aaa6 | quote: "prices": [ "$9.38", "$28.14", "$56.28", "$112.56",
- sources:
  - [1] https://iwebfusion.net/vps
  - [2] https://vpspricetracker.com/provider/iWebFusion/vps
  - [3] https://my.iwebfusion.net/cart.php?a=add&pid=450706
