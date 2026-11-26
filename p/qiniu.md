# Qiniu

> qiniu.com | Inference, Compute, Storage; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qiniu/ | JSON https://fshy.ajam.dev/api/v1/entity/qiniu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qiniu

- `inference/qiniu-ai` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://developer.qiniu.com/aitokenapi/13330/subscription-introduction?category=buying_guide
- free tier: No free tier is stated. Billing is quoted against a base unit price of CNY 0.004 per thousand tokens, with a price coefficient of 1.0 meaning parity with that base. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Qiniu Cloud account and an API key; the page names no free allowance
- interface: rest
- limits:
  - volume-quota (binding): per-thousand-token billing from CNY 0.004 at a 1.0 coefficient [1]
- endpoint: https://api.qnaigc.com/v1
- tooling: the vendor's OpenAI-compatible endpoint with a Qiniu key
- composes with: the per-token rate is the whole cost model, so there is no free allowance to bridge a workload
- reliability: a coefficient-based price means the effective rate depends on which model the request lands on
- evidence:
  - [1] 2026-11-18: pricing is stated as CNY 0.004 per thousand tokens at a 1.0 coefficient with no free allowance | capture: sha256:a4a00c725d6a43dd03a424e75ecc086238259f035566b68a1d5147398e2e0777 | quote: - 以 ¥0.004/千token 为基准单价，价格系数为 1.0 表示与基准持平。
- sources:
  - [1] https://developer.qiniu.com/aitokenapi/13330/subscription-introduction?category=buying_guide

## Qiniu Cloud AI

- `compute/qiniu-cloud-ai` | fails-identity | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card unknown, phone no, ID yes, institution no | verified 2026-11-25T15:03:45.875Z (live) | stale on 2026-12-26
- url https://developer.qiniu.com/las/13281/sandbox-overview
- free tier: | vCPU | ~~0.00003 元/核/秒~~ | 0.00002 元/核/秒 | 按实际分配的 vCPU 核数线性计费，范围 1 ~ 8 核 | | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
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
  - [1] 2026-11-25: the domestic vCPU rate is now 0.00002 CNY per core-second, linearly billed over 1 to 8 cores | capture: sha256:9b3a0d33c12b8b175adc4e68a88d07921697c7d39c75b567b5ae238dd58c82f4 | quote: | vCPU | ~~0.00003 元/核/秒~~ | 0.00002 元/核/秒 | 按实际分配的 vCPU 核数线性计费，范围 1 ~ 8 核 |
  - [1] 2026-11-25: the current domestic vCPU price row is unchanged in the capture | capture: sha256:9b3a0d33c12b8b175adc4e68a88d07921697c7d39c75b567b5ae238dd58c82f4 | quote: | vCPU | ~~0.00003 元/核/秒~~ | 0.00002 元/核/秒 | 按实际分配的 vCPU 核数线性计费，范围 1 ~ 8 核 |
- sources:
  - [1] https://developer.qiniu.com/las/13281/sandbox-overview
  - [2] https://developer.qiniu.com/af/12968/freequota
  - [3] https://developer-doc.qiniu.com/products/las/sandbox-overview/0-sandbox-quickstart
  - [4] https://developer.qiniu.com/las/13480/sandbox-api-sandboxes

## Qiniu LAS Sandbox

- `compute/qiniu-las-sandbox` | fails-identity | evidence documented | binding write-gated | category sandbox | tier Pay as you go
- needs card no, phone no, ID yes, institution no | verified 2026-11-24T10:11:15.004Z (live) | stale on 2026-12-25
- url https://developer-doc.qiniu.com/products/las/sandbox-overview
- free tier: CNY 0 free standing compute allowance is published: every sandbox instance gets 20 GiB of local storage free while it runs, and persistent storage has a free allowance of 10 GiB per account per month; compute is billed per second from 2026-11-19 at CNY 0.00002 per vCPU-second and CNY 0.00001 per GiB-second in the China (Yangzhou 1) region | unit: mixed | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The free allowance is a monthly persistent-storage volume plus local scratch space, not free sandbox runtime. The documentation for a different Qiniu AI inference product states a 24-hour verification-free trial period; that policy is not stated for the sandbox service and is not applied here.
- per-object cap: not applicable: the unit is a running sandbox, not a stored object; each instance receives 20 GiB of local storage free while it runs | source: [1]
- retention: the local filesystem is not kept after the sandbox terminates; persistent templates and snapshots survive while billed, and paused sandboxes are not documented here | source: [1] | note: unverified: no sandbox-specific retention period in days is published on the pages read
- egress: network traffic is not charged separately; the China (Yangzhou 1) region blocks outbound port 25 and inbound port 53 by default on full-stack servers | metered: no | source: [1]
- identity: national-id | detail: A Qiniu account and an API key from the developer console are required. Personal verification offers a QR-code face scan with personal identity information, a bank-card check with a face photo, or a bank transfer of CNY 0.01 to 0.99 to the applicant's card with the amount returned; enterprise verification needs a business licence. A distinct Qiniu AI inference product grants a 24-hour verification-free trial, but no equivalent sandbox trial is published: unverified for the sandbox service. | country: CN
- interface: rest, cli
- limits:
  - volume-quota: 10 GiB of persistent storage per account per month free; excess is CNY 0.000145 per GiB-hour in China (Yangzhou 1) and CNY 0.00019575 per GiB-hour in the US (Dallas 1), rounded up to an… [1]
  - per-object-cap: 1 to 8 vCPU per sandbox and 512 MiB to 8192 MiB of memory in multiples of 512 MiB; each instance gets 20 GiB of local storage free [1]
  - write-gated (binding): creating a sandbox needs a Qiniu account and an E2B_API_KEY; real-name verification requires a national ID by QR-code face scan, a bank-card check, or a small bank transfer [2]
- limits note: unverified: the numeric RPM and TPM caps for unverified accounts are not published on the AI inference product's verification page and are not stated for the sandbox service
- binding note: The real-name check is the first constraint on a new account: creating a sandbox needs an API key from a Qiniu account, and personal verification requires a national ID or bank credential, while the monthly persistent-storage allowance is a volume that has to be exceeded to bind.
- interface detail: The sandbox service is fully E2B API compatible: an E2B SDK drives it with E2B_API_KEY and E2B_API_URL set for the chosen region; qshell is the command-line tool for sandbox, template and key-injection management.
- endpoint: https://cn-yangzhou-1-sandbox.qiniuapi.com or https://us-south-1-sandbox.qiniuapi.com
- tooling: The hosted sandbox service is reached with the E2B SDK (npm @e2b/code-interpreter or pip e2b-code-interpreter), which the user installs, and with qshell for command-line management; the account's API key comes from the Qiniu developer console.
- composes with: An existing E2B client works by changing E2B_API_URL to a Qiniu regional endpoint, so agent code that already calls E2B can be pointed at the China or US region without a second SDK.
- reliability: Persistent storage keeps billing while a sandbox is not running; an account in arrears cannot create new sandboxes and running instances are released.
- notes: Hosted E2B-compatible sandboxes in China (Yangzhou 1) and US (Dallas 1). The China vCPU and memory prices were cut by about 33.3% on 2026-11-19 to CNY 0.00002 per core-second and CNY 0.00001 per GiB-second; the US rates are CNY 0.0000405 and CNY 0.00002025. The persistent-storage allowance is 10 GiB per account per month free and network traffic carries no separate charge. A national-ID or bank verification gate applies to a Qiniu account.
- evidence note: The per-second rates, the free persistent-storage allowance, the local storage, the network terms and the E2B-compatible endpoint come from the vendor's sandbox documentation pages read on 2026-11-24; the verification methods come from the vendor's account-finance documentation read the same day.
- evidence:
  - [1] 2026-11-24: sandbox compute is metered by the second and stops when the sandbox stops | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: 沙箱服务采用按量计费模式，精确到秒级计费。沙箱停止运行后即停止计费。
  - [1] 2026-11-24: China-region vCPU price fell to CNY 0.00002 per core-second and memory to CNY 0.00001 per GiB-second on 2026-11-19, with 1 to 8 vCPU billed linearly | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: vCPU | ~~0.00003 元/核/秒~~ | 0.00002 元/核/秒 | 按实际分配的 vCPU 核数线性计费，范围 1 ~ 8 核 |
  - [1] 2026-11-24: persistent storage has a free allowance of 10 GiB per account per month | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: 免费额度 | 每账户每月 10 GiB
  - [1] 2026-11-24: each sandbox gets 20 GiB of local storage free while it runs and the filesystem is gone when the instance terminates | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: 每个沙箱实例会自动分配 20 GiB 本地存储空间，作为该沙箱运行期间的本地文件系统使用，免费使用，无需额外付费。
  - [1] 2026-11-24: network traffic is not charged separately | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: 网络流量暂不单独计费。
  - [1] 2026-11-24: persistent storage bills even while the sandbox is stopped and arrears release running sandboxes | capture: sha256:3685c5631572af369f1ae181a1271426f684a7d5f2aee48c5a09f7aad8051c8a | quote: 账户欠费后将无法创建新的沙箱实例，运行中的沙箱将被释放
  - [2] 2026-11-24: personal verification accepts a QR-code face scan, a bank-card check or a small bank transfer | capture: sha256:a7d9c36c83c336f1ed70b5d78d5129e4c01fb3c9fff0803e2af16873a72529e5 | quote: 个人认证有三种认证方式：个人扫码认证；个人银行卡转账认证；个人银行卡认证
  - [3] 2026-11-24: a distinct Qiniu AI inference product grants new users a 24-hour verification-free trial, not stated for the sandbox service | capture: sha256:20f057c7f7098584bc9c1f15828f97ce59b1b3e5a2594a1f142acee6873155f9 | quote: 为了让您更好地体验我们的 AI 推理服务，我们为新注册用户提供 24 小时免认证体验期
- sources:
  - [1] https://developer-doc.qiniu.com/products/las/sandbox-overview
  - [2] https://developer.qiniu.com/af/4062/quick-start-personal-authentication
  - [3] https://developer.qiniu.com/aitokenapi/13255/verify-real-name

## qiniu cloud kodo (七牛云对象存储)

- `storage/qiniu-cloud-kodo` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:39.877Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the Kodo price page still shows 0.26 CNY per GB outbound transfer, so the egress rejection holds | capture: sha256:d6545f5fa2c7b56165e9d131573fefd29b5ed8df7309b5c0395450720ee49fb2 | quote: 外网流出流量0 - 100 TB0.26 元/GB
  - [1] 2026-11-19: the page states a free allowance but no per-object cap clause, so the stated-absent finding holds | capture: sha256:d6545f5fa2c7b56165e9d131573fefd29b5ed8df7309b5c0395450720ee49fb2 | quote: 标准存储每月免费空间标准存储每月免费 CDN 回源流量标准存储每月免费写请求 PUT/DELETE标准存储每月免费读请求 GET每月免费上传流量10GB10GB10万次100万次无上限
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
