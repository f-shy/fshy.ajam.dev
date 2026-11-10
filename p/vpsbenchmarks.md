# Alwyzon

> vpsbenchmarks.com | Compute; 8 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsbenchmarks/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsbenchmarks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Alwyzon

- `compute/alwyzon` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/alwyzon
- free tier: EUR 4.49/month for Virtual Server XS: 2 cores, 2 GB RAM, 40 GB storage, in Austria, with no bandwidth charge. Next rows: Virtual Server S at EUR 7.79 with 3 cores, 4 GB and 80 GB; Virtual Server L at EUR 23.49 with 6 cores, 16 GB and 240 GB; and the Performance G5 line from EUR 11.49 for 2 cores, 4 GB and 120 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no bandwidth charge, per the page. No allowance and no port speed are printed | metered: no | free allowance: no charge for bandwidth; no figure stated | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: The page states 'This provider does not charge for bandwidth', and no port speed or allowance is printed, so nothing in this record caps transfer.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: 2 cores and 2 GB for EUR 4.49 with uncapped transfer is a better machine per euro than Aruba's 1 GB at EUR 2.49 and a worse one than Dataforest's 10 TB at EUR 4.07, so the choice between them is Austria versus Germany and whether a stated 10 TB is worth more than an unstated 'no charge'
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks. The benchmark page records a trial on Virtual Server XS in March 2026 with a score of 51, which is the only performance evidence in this record. verification criteria: the vendor's own pricing page for the port speed and the traffic terms in writing.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 40
- evidence:
  - [1] 2026-10-22: plan row fields, transcribed and joined (unquoted values are not verbatim): [Virtual Server XS] 2 2.0GB 40GB 4.49 EUR / month; the networking line reads 'This provider does not charge for bandwidth.'
  - [1] 2026-10-22: further rows, transcribed and joined: [Virtual Server S] 3 4.0GB 80GB 7.79 EUR / month, [Virtual Server L] 6 16.0GB 240GB 23.49 EUR / month, [Virtual Server E4+] 2 4.0GB 120GB 11.49 EUR / month; 'It has data centers in: - Austria'
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/alwyzon

## Aruba Cloud

- `compute/aruba-cloud` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/aruba_cloud
- free tier: EUR 2.49/month for VPS O1I1 on the OpenStack Cloud VPS line: 1 core, 1 GB RAM, 20 GB NVMe on software-defined storage, hourly billing, unlimited traffic, 99.90% SLA. The instance type is described as 'AMD processors, SDS (Software-Defined Storage) NVMe and a 99.90% SLA. Window Server license is included.' The next rows step up cleanly: O1I2 at EUR 4.49 with 1 GB and 40 GB, O2A4 at EUR 6.29 with 2 and 4, O4A8 at EUR 11.79, O8A16 at EUR 19.89, O16A32 at EUR 38.90. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no bandwidth charge, per the page, and 'Unlimited traffic' on the virtual-data-center type. No port speed is printed | metered: no | free allowance: unlimited traffic; no figure stated | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: The page states 'This provider does not charge for bandwidth' and the virtual-data-center instance type is described as offering 'Unlimited traffic', so no byte allowance caps this plan. Nothing else on the row is a quota: the wall is the 1 GB of RAM and the 20 GB of disk.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: EUR 2.49 for 1 GB with unlimited traffic is the second-cheapest paid VPS row among evaluated providers after VirMach, and unlike that offer it is a current hourly-billed cloud product. 20 GB of disk is the limit, so it is a relay, a scheduler or a TLS terminator rather than a host that keeps what it fetches.
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks. The data-center list and the instance-type description disagree on country, and both are recorded rather than one being chosen. verification criteria: the vendor's VPS order page for the location list and the port speed.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: plan row fields, transcribed and joined (unquoted values are not verbatim): [VPS O1I1] 1 1.0GB 20GB 2.49 EUR / month; the networking line reads 'This provider does not charge for bandwidth.'
  - [1] 2026-10-22: instance type quoted: 'Built on top of OpenStack, those preconfigured servers offer AMD processors, SDS (Software-Defined Storage) NVMe and a 99.90% SLA. Window Server license is included.'; the Public Cloud type reads 'Latest generation hardware, data centers in Italy and guaranteed resources starting from EUR 9.49/month + VAT'
  - [1] 2026-10-22: the pages data-center list reads - Czech Republic - France - Germany, while the Public Cloud instance-type description says data centers in Italy'. Both are quoted because they disagree
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/aruba_cloud

## dataforest

- `compute/dataforest` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/dataforest_cloud
- free tier: EUR 4.07/month for Entry S in Frankfurt, Germany: 1 shared Intel Xeon Gold vCPU, 2 GB ECC RAM, 20 GB on Ceph with three-way replication, 10 TB of traffic included, 19% VAT included in the printed price. Next rows: Entry M at EUR 7.13 with 2 cores, 4 GB and 40 GB; Entry L at EUR 13.26 with 4 cores, 8 GB and 80 GB; Entry XL at EUR 21.09 with 8 cores, 16 GB and 160 GB. The Performance line is dedicated AMD EPYC 9575F with 20 TB included and starts at EUR 38.00 for 2 cores, 16 GB and 80 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 TB a month included on the Entry line and 20 TB on the Performance line, stated in the instance-type description. No overage price is printed | metered: yes | free allowance: 10 TB per month (Entry line); 20 TB per month (Performance line) | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 10 TB a month on the Entry line and 20 TB on the Performance line, stated on the page as '10 TB traffic included' and '20 TB traffic included'. That is the largest included allowance of any small VPS row among evaluated providers, and it is the constraint that would end a sustained crawl: 10 TB is about 333 GB a day. [1]
- limits note: 10 TB a month on the Entry line and 20 TB on the Performance line, stated on the page as '10 TB traffic included' and '20 TB traffic included'. That is the largest included allowance of any small VPS row among evaluated providers, and it is the constraint that would end a sustained crawl: 10 TB is about 333 GB a day.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: EUR 4.07 for 2 GB with 10 TB a month included is the best transfer-per-euro row among evaluated providers: the 500 GB to 1 TB daily transfer volume fits inside it with room, and the 20 GB disk forces the bytes out to storage rather than accumulating on the box, which is the shape earlier stated workload wants.
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks. json and compute/linceris. Prices are quoted with VAT included, as the page states, and no figure here has been adjusted. verification criteria: the vendor's own price list at cloud.dataforest.net, which the benchmark page links, for the overage rate past 10 TB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: instance type quoted: 'dataforest cloud Seeds Entry line: affordable cloud VPS for low CPU load. Shared Intel Xeon Gold vCPUs, ECC memory, 3-way replication via Ceph, 10 TB traffic included. Frankfurt, Germany. Prices on the site include 19% VAT.'
  - [1] 2026-10-22: plan rows, transcribed and joined (unquoted values are not verbatim): [Entry S] 1 2.0GB 20GB 4.07 EUR / month, [Entry M] 2 4.0GB 40GB 7.13 EUR / month, [Entry L] 4 8.0GB 80GB 13.26 EUR / month, [Entry XL] 8 16.0GB 160GB 21.09 EUR / month
  - [1] 2026-10-22: Performance line quoted: 'Dedicated AMD EPYC 9575F (Turin) vCPUs, ECC memory, 3-way replication via Ceph, 20 TB traffic included. Frankfurt, Germany', with [Performance S] 2 16.0GB 80GB 38.00 EUR / month
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/dataforest_cloud

## GPU Mart

- `compute/gpu-mart` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/gpu_mart
- free tier: USD 24.65/month for 'Express GPU VPS - 2GB': 1x NVIDIA GT730 with 2 GB of GPU memory, 8 CPU cores, 16 GB RAM, 120 GB disk, in the United States. Next rows on the same page: 'Lite Dedicated GPU Server - P600' at USD 55.00 with 4 cores, 16 GB and 1080 GB; 'Basic GPU VPS - RTX 5060' at USD 99.00 with 16 cores, 28 GB and 240 GB; 'Basic Dedicated GPU Server - T1000' at USD 119.00 with 8 cores, 64 GB and 1080 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read: the plan table carries a GPU, cores, RAM, storage and price only | metered: no | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: No transfer allowance and no port speed appear on the page read. The page's own note says it lists only plans the site has tested, and the vendor page it links is a pricing page that was not fetched, so no quota is asserted.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: USD 24.65 a month for a GT730 is not a training card: 2 GB of GPU memory holds a small inference graph or a desktop, and the row's 16 GB of system RAM and 120 GB of disk are the parts worth having. The RTX 5060 row at USD 99 with 28 GB of RAM is the first row on this page that could fine-tune anything
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks, which listed it among 76 provider slugs. The page warns its list is not exhaustive, so a cheaper GPU plan may exist that this record does not carry. verification criteria: https://www.gpu-mart.com/pricing, which the benchmark page links as the provider page for the instance type.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 16
  - facets.shape.disk_gib: 120
  - facets.shape.gpu_class: NVIDIA GT730
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: GPU plan row fields, transcribed and joined (unquoted values are not verbatim): [Express GPU VPS - 2GB] 1 x NVIDIA GT730, 2GB GPU RAM, 8, 16.0GB, 120GB, $24.65/month; the instance type is described as 'GPU Mart's GPU Hosting VPS provides high-performance virtual private servers equipped with dedicated NVIDIA GPUs like the RTX 4090 and 3090'
  - [1] 2026-10-22: the page states 'Only plans that have been tested by VPSBenchmarks or may be tested in the future are included' and lists further rows at $55.00, $99.00, $119.00, $129.35 and $149.00; It has data centers in: United States
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/gpu_mart

## Hivelocity

- `compute/hivelocity` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/hivelocity
- free tier: USD 10.00/month for PRO.SM.AMD: 2 shared CPU cores with guaranteed minimums, 4 GB RAM, 40 GB NVMe. Next rows: PRO.MD.AMD at USD 20.00 with 4 cores, 8 GB and 80 GB; PRO.LG.AMD at USD 39.00 with 8 cores, 16 GB and 160 GB; and the VDS line, which is dedicated-resource and starts at USD 21.00 for 2 cores, 4 GB and 80 GB. The page names 'United States' as the data-center country and reports three data centers. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read: the plan table carries cores, RAM, storage and price only, and no transfer allowance or port speed appears | metered: no | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits note: No transfer allowance and no port speed are printed on the page read, so nothing in this record caps bytes. The named constraints are elsewhere: hourly billing is marked missing ('Hourly Billing: No') and the block-storage price is USD 0.075 per GB per month, so disk beyond the 40 GB is the metered axis.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the features table states 'Admin REST API Yes URL: https://api-docs.hivelocity.net/' and 'SSH Keys Setup Yes'; the control panel is 'Custom'
- composes with: USD 10 for 2 cores and 4 GB with snapshots and a documented REST API is a reasonable control-plane machine, and the VDS line at USD 21 for dedicated cores is the one to price when a shared vCPU will not hold a latency budget. The GPU line is flagged as sold and unpriced, which makes this a lead for the GPU lane rather than a GPU finding
- reliability: no reliability event observed; the benchmark page reports an average provisioning time of 1607s from 13 samples, with a median of 210s and a maximum of 14400s.
- notes: Found on both serverhunter and vpsbenchmarks; the vpsbenchmarks page is documented because it carries the plan table. verification criteria: the vendor's pricing page with computeType=virtual-server, which the benchmark page links, for the transfer allowance that this record cannot state.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 40
- evidence:
  - [1] 2026-10-22: plan rows, transcribed and joined (unquoted values are not verbatim): [PRO.SM.AMD] 2 4.0GB 40GB $10.00 / month, [PRO.MD.AMD] 4 8.0GB 80GB $20.00 / month, [PRO.LG.AMD] 8 16.0GB 160GB $39.00 / month, [PRO.XL.AMD] 12 24.0GB 240GB $65.00 / month, [VDS.SM] 2 4.0GB 80GB $21.00 / month
  - [1] 2026-10-22: features table quoted: 'Hourly Billing No', 'DDOS Protection Yes', Admin REST API Yes URL: https://api-docs.hivelocity.net/, 'Backups Yes Hourly, daily, weekly and monthly snapshots', 'Total number of data centers 3'; block storage row reads 'Block $0.075'
  - [1] 2026-10-22: the extra-services table marks 'GPU instances' green, so the provider sells GPU time as a separate product line that this page does not price
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/hivelocity

## LayerStack

- `compute/layerstack` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/layerstack
- free tier: USD 28.06/month for R108 in Hong Kong, Singapore or Japan: 2 shared vCPUs, 4 GB RAM, 150 GB storage. The same price applies to the R108-HK and R108-TP variants; R208 is USD 53.80 with 4 cores, 12 GB and 250 GB. The page warns its plan list is not exhaustive, so this is the cheapest plan it has tested rather than the provider's floor. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: No transfer allowance and no port speed appear on the page read, so nothing here caps bytes. The plan list is explicitly partial, so even the price is a lower bound on what the provider sells.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: USD 28.06 for 4 GB and 150 GB in Hong Kong or Singapore is the cheapest Asian-presence row among evaluated providers, which matters for a crawler that needs a non-European source address. It is twice the price of Aruba for the same RAM, so the reason to take it is the location, not the machine.
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks. The benchmark page states twice that its list is not exhaustive, and R108 at USD 28.06 is unlikely to be a provider's entry plan, so the offer recorded here is explicitly the cheapest tested plan. verification criteria: https://www.layerstack.com/en/pricing, which the page links as the provider page for the instance type.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 150
- evidence:
  - [1] 2026-10-22: plan rows, transcribed and joined (unquoted values are not verbatim): [R108-HK] 2 4.0GB 150GB $28.06 / month, [R108] 2 4.0GB 150GB $28.06 / month, [R108-TP] 2 4.0GB 150GB $28.06 / month, [R208-HK] 4 12.0GB 250GB $53.80 / month
  - [1] 2026-10-22: 'It has data centers in: - Hong Kong - Japan - Singapore'; the instance type reads 'vCPUs are shared in all General Purpose plans'
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/layerstack

## Melbicom

- `compute/melbicom` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/melbicom
- free tier: EUR 3.90/month for VDS-1-SSD on the Cloud Servers line: 1 core, 2 GB RAM, 20 GB of local SSD NVMe, KVM. The benchmark page adds that the provider 'does not charge for bandwidth'. Next rows: VDS-2-SSD-TYO, then VDS-4-SSD and VDS-6-SSD, which are the plans the site has benchmarked. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'This provider does not charge for bandwidth' per the benchmark page. No allowance and no port speed are printed | metered: no | free allowance: no charge for bandwidth; no figure stated | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: The page states 'This provider does not charge for bandwidth' and prints no allowance and no port speed, so nothing in the record caps transfer. The wall is the 20 GB of disk and, for this provider, the hourly price.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: EUR 3.90 for 2 GB with no bandwidth charge is the cheapest uncapped-transfer small machine among evaluated providers, which is the shape a scraper with steady but modest throughput wants: the disk is the limit at 20 GB, so the bytes are collected and shipped rather than stored.
- reliability: no reliability event recorded
- notes: Found on both serverhunter (971-name index) and vpsbenchmarks (77-slug index); the vpsbenchmarks page is the one documented because it carries the plan price and the bandwidth statement. Location is not on the plan row: the benchmark page names it as EU-headquartered and its news item reports a Marseille PoP opened in September 2026, so no city is asserted here. verification criteria: the vendor's own VDS order page for the location list and the disk type.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: plan row fields, transcribed and joined (unquoted values are not verbatim): [VDS-1-SSD] 1 2.0GB 20GB 3.90 EUR / month; the pages networking line reads This provider does not charge for bandwidth.'
  - [1] 2026-10-22: the instance type is described as 'High-Performance KVM VPS with local SSD NVMe storage' and the page notes 'All VPS prices reported at VPSBenchmarks are for one month without any further commitment and before promotions unless noted otherwise'
  - [2] 2026-10-22: the vendor homepage returns 200 with the tagline 'IT-infrastructure for business' and no plan table; https://www.melbicom.net/vps/ returned a 404 body
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/melbicom
  - [2] https://www.melbicom.net/

## ServerCheap

- `compute/servercheap` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vpsbenchmarks.com/hosters/servercheap
- free tier: USD 3.00/month for NVMe-KVM-4GB-New: 2 cores, 4 GB RAM, 40 GB NVMe, KVM, instant provisioning, 7-day money-back guarantee and a 99.9% uptime SLA, in the United States. Next rows: the legacy SolusVM 1 line at USD 6.00 for 4 cores, 6 GB and 60 GB; USD 12.99 for 6 cores, 20 GB and 120 GB; USD 20.99 for 8 cores, 34 GB and 200 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: No transfer allowance and no port speed appear on the page read, so nothing here caps bytes.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the legacy line is described as SolusVM 1 with KVM
- composes with: USD 3.00 for 2 cores and 4 GB is the cheapest RAM-per-dollar row among documented hosts and roughly a fifth of Hivelocity's price for the same shape. The row is marked 'Off rankings', which means the provider exists at that price but the plan was not benchmarked, so the machine is priced and unmeasured
- reliability: no reliability event recorded
- notes: Found via vpsbenchmarks. The USD 3.00 row is flagged 'Off rankings' on the source page and is the only row in this record outside the benchmarked set. Unverified: a read of servercheap.com/vps/ for the transfer allowance and the location city.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 40
- evidence:
  - [1] 2026-10-22: plan row fields, transcribed and joined (unquoted values are not verbatim): [NVMe-KVM-4GB-New] (Off rankings) 2 4.0GB 40GB $3.00 / month; the instance type note reads 'ServerCheap offers a 7-day money back guarantee and 99.9% uptime SLA. These VMs are virtualized with KVM and are provisioned instantly after ordering in most circumstances.'
  - [1] 2026-10-22: legacy rows, transcribed and joined: [NVMe-KVM-6GB] 4 6.0GB 60GB $6.00 / month, [NVMe-KVM-20GB] 6 20.0GB 120GB $12.99 / month, [NVMe-KVM-34GB] 8 34.0GB 200GB $20.99 / month; 'It has data centers in: - United States'
- sources:
  - [1] https://www.vpsbenchmarks.com/hosters/servercheap
