# Hosting Int

> hosting.international | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosting/ | JSON https://fshy.ajam.dev/api/v1/entity/hosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosting Int

- `compute/hosting-int` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.037Z (live) | stale on 2026-12-08
- url https://hosting.international/
- price parsed USD 6.65/mo
- free tier: Linux VPS at EUR 5.90/month: 1 vCPU Xeon Gold up to 3.9 GHz, 1 GB ECC RAM, 10 GB SSD, "100 Mb/s unlimited bandwidth", private firewall rules, KVM based and fully configurable, in EU, UA and Singapore. The tracker puts the same EUR 5.90 floor in two locations, Singapore with 10 GB SSD and Ukraine with 10 GB HDD, both at 31,641 GB/month on a 0.1 Gbps port, and prices a 20 GB SSD Singapore variant at EUR 6.80. A dedicated server line starts at EUR 49.00/month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited bytes at a stated 100 Mb/s port, with no monthly allowance and no overage price; the tracker's 31,641 GB/month is what that port carries at saturation for a month, not a quota | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): the vendor sells "100 Mb/s unlimited bandwidth", which is a port rate and not a byte allowance, so the wall is throughput: at 100 Mb/s flat a month carries about 32 TB, which is why the tracker's 31,641 GB/month is the saturation of the port rather than a quota the vendor imposes. [1]
- limits note: the vendor sells "100 Mb/s unlimited bandwidth", which is a port rate and not a byte allowance, so the wall is throughput: at 100 Mb/s flat a month carries about 32 TB, which is why the tracker's 31,641 GB/month is the saturation of the port rather than a quota the vendor imposes.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, private firewall rules and a configurable build, sold through a WHMCS site; the company is registered as International Hosting Solutions LLP . No API documented on the page read.
- composes with: A Ukrainian or Singapore address at EUR 5.90 with unlimited bytes at 100 Mb/s is the cheapest sustained egress among evaluated providers, and 100 Mb/s sustains about 1 TB a day, which is the order of the daily transfer volume on one port; 1 GB of RAM and 10 GB of disk mean the bytes have to be streamed from somewhere else rather than stored here.
- reliability: no reliability event recorded
- notes: The tracker and the vendor agree on the price and on the port, and they disagree on what the bandwidth is: the vendor says unlimited at 100 Mb/s, the tracker publishes 31,641 GB/month. The two are consistent if the tracker's figure is the port's monthly saturation, which it is to within 3 percent, so the record is bound by shaping and not by a quota. verification criteria: whether the 100 Mb/s is guaranteed or burstable, and whether the Ukrainian location has the same terms as the Singapore one.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - term: monthly
  - price_on_page: EUR 5.90/mo
  - out_of_pocket_usd: 6.59
  - renewal_usd: not published: the cart prints no renewal price
  - cart_url: https://hosting.international/cart.php?gid=1
- evidence:
  - [1] 2026-10-22: the plan quoted from the homepage: "Linux or Windows VPS" / "Starting From" / "EUR 5.90" / "Per month for:" / "1vCPU Xeon Gold up to 3.9 Ghz" / "1 Gb RAM ECC" / "10 Gb SSD Cloud Storage" / "100 Mb/s unlimited bandwidth" / "with private firewall rules" / "KVM based 100% configurable" / "Multiple locations EU, UA, Singapore"
  - [1] 2026-10-22: "Dedicated server" / "Starting From" / "EUR 49.00" / "Per month for:" with "IPMI access", "KVM-over-IP by request" and the same "100 Mb/s unlimited bandwidth"
  - [2] 2026-10-22: the tracker rows quoted: "Hosting Int. - EUR 5.90 / month" with "disk 10 GB SSD" / "bandwidth 31,641 GB/month bandwidth" / "rj45 0.1 Gbps port speed" / "city Singapore", a second EUR 5.90 row with "10 GB HDD" and "city Ukraine", and a EUR 6.80 row with "20 GB SSD" in Singapore, under "starting at EUR 5.90 per month"
  - [3] 2026-11-07: the cart lists Linux VPS EU from EUR 5.90 monthly | capture: sha256:299b17e8cccd480513dea6e9964daf7bbac191b746b26800316e1442090254fb | quote: Starting from €5.90EUR Monthly
- sources:
  - [1] https://hosting.international/
  - [2] https://vpspricetracker.com/provider/Hosting_Int/vps
  - [3] https://hosting.international/cart.php?gid=1
