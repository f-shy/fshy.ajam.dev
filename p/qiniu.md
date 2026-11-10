# qiniu

> qiniu.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qiniu/ | JSON https://fshy.ajam.dev/api/v1/entity/qiniu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qiniu Cloud AI

- `compute/qiniu-cloud-ai` | fails-identity | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card unknown, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://developer.qiniu.com/las/13281/sandbox-overview
- free tier: Per-second billing with no free compute allowance: CNY 0.00003 per vCPU per second, which the page restates as CNY 0.108 per vCPU per hour, range 1 to 8 cores; CNY 0.000015 per GiB per second, or CNY 0.054 per GiB per hour, 512 MiB to 8192 MiB in 512 MiB steps. Each sandbox gets 20 GiB of local disk free of charge. Persistent storage carries 10 GiB per account per month free, then CNY 0.000145 per GiB per hour. Network traffic is not billed separately today. A 2 vCPU / 2 GiB sandbox is CNY 2.61 for an 8-hour day by the page's own worked example. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: A sandbox has a 5 minute default lifetime and a 15 second default exec timeout, both extendable through the API; the account itself needs real-name verification ( ) before any free allowance is granted. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: real-name verification of the account before any free allowance is granted: the free-quota page states the allowance is automatic once the service is activated and real-name verification completed. The record's notes add that topping up needs a Chinese payment method. Which document the real-name check accepts, whether a card is required for the free allowance itself, and any authorisation amount are not stated
- interface: rest
- limits:
  - retention-clamped (binding): A sandbox has a 5 minute default lifetime and a 15 second default exec timeout, both extendable through the API; the account itself needs real-name verification ( ) before any free allowance is granted. [1]
- limits note: A sandbox has a 5 minute default lifetime and a 15 second default exec timeout, both extendable through the API; the account itself needs real-name verification ( ) before any free allowance is granted.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Because it speaks the E2B protocol, the same client code that runs on E2B points at us-south-1 by changing E2B_API_URL, which makes this a drop-in cheaper backend for a Chinese or US-east workload rather than a rewrite.
- reliability: no reliability event recorded
- notes: This is the cheapest per-vCPU sandbox rate documented, at CNY 0.108 per vCPU-hour, and it is the only provider here that publishes a US region alongside a mainland one. It is recorded as fails-identity because the free allowance is gated on real-name verification and topping up needs a Chinese payment method; the sandbox compute itself has no free allowance at all, so even a verified account starts at CNY 0.432 per hour for 2 vCPU and 4 GiB. No USD figure is computed because no exchange rate was read verification. Isolation is described as system-level per-instance virtualization; the page does not name the technology. Qiniu also sells (LAS) as an ordinary VPS from CNY 14.2 per month domestic and offers a 2-core / 2 GB instance at CNY 66 per year for new customers in Singapore, Tokyo, Hong Kong and Changshan.
- extras:
  - facets.class: non-english-sandbox
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: CNY 0.00003 per vCPU per second (CNY 0.108 per vCPU-hour) and CNY 0.000015 per GiB per second (CNY 0.054 per GiB-hour), 1 to 8 cores, 512 MiB to 8192 MiB; 20 GiB local disk free per sandbox; persistent storage 10 GiB per account per month free then CNY 0.000145 per GiB-hour; network traffic not billed separately
  - [2] 2026-10-22: '开通对应服务并完成实名认证即可自动享受免费额度': the free allowance requires real-name verification, and the allowance table lists storage, CDN, multimedia and a 750-hour container allowance but no sandbox compute allowance
  - [3] 2026-10-22: the sandbox is fully compatible with the E2B API and SDK, with regions cn-yangzhou-1 and us-south-1, and states a 5 minute default sandbox lifetime
  - [4] 2026-10-22: the create call takes a timeout in seconds defaulting to 15, and a timeout endpoint extends a live sandbox
  - [1] 2026-10-22: 
- sources:
  - [1] https://developer.qiniu.com/las/13281/sandbox-overview
  - [2] https://developer.qiniu.com/af/12968/freequota
  - [3] https://developer-doc.qiniu.com/products/las/sandbox-overview/0-sandbox-quickstart
  - [4] https://developer.qiniu.com/las/13480/sandbox-api-sandboxes

## qiniu cloud kodo (七牛云对象存储)

- `storage/qiniu-cloud-kodo` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.qiniu.com/prices/kodo
- free tier: None reachable: Structurally identical trap to Tencent and marginally cheaper on storage. Standard ¥0.115/GB/mo ($17.60/TB/mo), archive ¥0.031, deep archive ¥0.012. But egress ¥0.26/GB = $39.79/TB per read. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Structurally identical trap to Tencent and marginally cheaper on storage. Standard ¥0.115/GB/mo ($17.60/TB/mo), archive ¥0.031, deep archive ¥0.012 — but egress ¥0.26/GB = $39.79/TB per…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Structurally identical trap to Tencent and marginally cheaper on storage. Standard ¥0.115/GB/mo ($17.60/TB/mo), archive ¥0.031, deep archive ¥0.012 — but egress ¥0.26/GB = $39.79/TB per…
  - [2] 2026-10-21: cited as the basis of the rejection: Structurally identical trap to Tencent and marginally cheaper on storage. Standard ¥0.115/GB/mo ($17.60/TB/mo), archive ¥0.031, deep archive ¥0.012 — but egress ¥0.26/GB = $39.79/TB per read
- sources:
  - [1] https://www.qiniu.com/prices/kodo
  - [2] https://www-static.qbox.me/products/kodo

## qiniu kodo free quota

- `storage/qiniu-kodo-free-quota` | fails-egress | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:35:01.219Z (live) | stale on 2026-12-04
- url https://developer.qiniu.com/af/12968/freequota
- free tier: none reachable: Free tier provides 10 GB per month standard storage, 10 GB per month CDN origin traffic, and 1M GET operations. Limited to China mainland CDN egress. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Free allowance 10 GB per month of CDN origin (回源) traffic; beyond it CDN origin traffic is metered at 0.15 yuan/GB. Internet outbound traffic is a separate meter with no free allowance, priced 0.26 yuan/GB for 0 to 100 TB in the first region tab and 0.29 yuan/GB in the other mainland region tabs. | metered: yes
- identity: email | detail: the free quota is granted once the service is opened and real-name verification (实名认证) is completed; the documents accepted are not stated on the page
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: vendor pages captured 2026-11-03: https://developer.qiniu.com/af/12968/freequota, https://www.qiniu.com/prices/kodo; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 10 GB/month standard storage + 10 GB/month CDN origin traffic + 1M GETs.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 10 GB/month standard storage + 10 GB/month CDN origin traffic + 1M GETs.
  - [1] 2026-11-03: the free quota carries 10 GB per month of CDN origin outbound traffic | capture: sha256:b21484bd7451e2890f9f237d641af349fe048f7160b7b1cf67c3a4705493bfca | quote: | 存储 | - 标准存储空间：10GB/月 - CDN回源流出流量：10GB/月 - PUT/DELETE 请求：10万次/月 - GET 请求：100万次/月 |
  - [1] 2026-11-03: the free quota requires real-name verification | capture: sha256:b21484bd7451e2890f9f237d641af349fe048f7160b7b1cf67c3a4705493bfca | quote: 开通对应服务并完成实名认证即可自动享受免费额度。
  - [2] 2026-11-03: the mainland pay-as-you-go price list puts outbound traffic at 0.26 yuan per GB for the first 100 TB | capture: sha256:bb3a0bfa54114fbca543266abaf2bd0a51446e57013e0d321202dd094f1add77 | quote: 外网流出流量0 - 100 TB0.26 元/GB
  - [2] 2026-11-03: CDN origin traffic is billed at 0.15 yuan/GB past the free allowance | capture: sha256:bb3a0bfa54114fbca543266abaf2bd0a51446e57013e0d321202dd094f1add77 | quote: CDN 回源流量0.15 元/GB0.15 元/GB0.15 元/GB0.15 元/GB0.15 元/GB0.15 元/GB
  - [2] 2026-11-03: internet outbound traffic for 0 to 100 TB is 0.29 yuan/GB in the other mainland region tabs | capture: sha256:bb3a0bfa54114fbca543266abaf2bd0a51446e57013e0d321202dd094f1add77 | quote: 外网流出流量0 - 100 TB0.29 元/GB0.29 元/GB
  - [2] 2026-11-03: the monthly free allowance lists storage, CDN origin traffic, write and read requests and upload traffic, and no internet outbound traffic | capture: sha256:bb3a0bfa54114fbca543266abaf2bd0a51446e57013e0d321202dd094f1add77 | quote: 标准存储每月免费空间标准存储每月免费 CDN 回源流量标准存储每月免费写请求 PUT/DELETE标准存储每月免费读请求 GET每月免费上传流量10GB10GB10万次100万次无上限
- sources:
  - [1] https://developer.qiniu.com/af/12968/freequota
  - [2] https://www.qiniu.com/prices/kodo
