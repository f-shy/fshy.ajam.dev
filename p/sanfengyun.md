# Sanfengyun

> sanfengyun.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sanfengyun/ | JSON https://fshy.ajam.dev/api/v1/entity/sanfengyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sanfengyun

- `compute/sanfengyun` | fails-identity | evidence documented | binding none | category cloud VM
- needs card no, phone yes, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.sanfengyun.com/freeServer/
- free tier: A free cloud server at 1 core, 1 GiB RAM, 5 Mbps bandwidth and a 10 GiB data disk, on BGP multi-line with an independent IP address, plus a free 免备案 (no ICP filing) service for domains pointed at it. The vendor states it has run the free product for eighteen years. Activation requires a mobile-number account and 实名认证 (real-name verification) that costs CNY 0.3. The first activation is 24 hours only. A renewal is earned by posting on a recommended site and submitting a screenshot for review, and each approved extension adds 5 days. A server that expires and is re-opened costs CNY 2. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: two network models: traffic-added, where the package traffic is issued per period and the port is throttled after exhaustion, and unlimited-traffic, where a lower fixed bandwidth is priced directly | metered: yes | source: [2]
- identity: national-id | detail: A mobile-number account plus real-name certification: the vendor page states '通过手机注册账号' (register an account by mobile phone) and '实名认证，实名认证需要花费0.3元钱' (real-name certification costs CNY 0.3), quoted in evidence row 1. The kind is national-id because the gate that fails is the real-name check, not the email. | country: CN
- interface: unknown
- limits note: no binding constraint identified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: no open question recorded The provider name was recorded only in Chinese and the promoter's ASCII fold emptied it; the ASCII transliteration is used here and the original is in the free-tier sentence.
- evidence:
  - [1] 2026-10-22: '云服务器的配置为1H-1G-5M'; '通过手机注册账号'; '实名认证，实名认证需要花费0.3元钱'; '默认开通1天，快到期，必须发帖延期审核，审核通过后可以继续使用5天'; '如果过期后，需要继续开通，需要收取2元开通费用'
  - [1] 2026-10-22: '完全免费只是第一天，续期需要延期发帖劳动成果换取，重开需要费用2元'
  - [3] 2026-10-22: initial activation is 24 hours of use, a free extension can be requested after 6 hours, and '每次免费延期将可以免费延长一定的时间，通过免费延期您可以永久免费使用'
  - [4] 2026-10-22: '每个用户免费开通1次，超过次数再次开通将收取一定的手续费'
  - [5] 2026-10-22: free product line also includes a 1 GiB web space with 5 GB monthly traffic, a 50 MB MySQL database, and a shared IP, with the free cloud server on BGP multi-line and an independent IP
  - [6] 2026-10-22: a community project exists solely to record and remind renewals for this free server because '免费产品到期后会自动删除', with 5 days added per approved extension post
  - [7] 2026-10-22: '一元试用' (a CNY 1 trial), a 7-day no-reason refund, and the site description '云服务器 2核2G 低至 19元/月' with Hong Kong, Japan, Korea and US no-filing nodes
  - [2] 2026-10-22: KVM instances billed monthly or annually in advance, on a CPU, memory and disk basis plus a separate charge for the independent IP; SSD or NVMe 30 GB default at CNY 0.4 per GB per month; the system disk backup at CNY 0.1 per GB per month '不可关闭' (cannot be switched off)
  - [2] 2026-10-22: two network models: traffic-added, where the package traffic is issued per period and the port is throttled after exhaustion, and unlimited-traffic, where a lower fixed bandwidth is priced directly
  - [8] 2026-10-22: no plan price table is published in the documentation; the purchase guide covers regions, CPU families and disk tiers only
  - [9] 2026-10-22: '免费云服务器配置 CPU 1核 内存 1G 带宽 5M 数据盘 10G', BGP multi-line with an independent IP and a free 免备案 service, '十年来我们从未间断，只为实现永久免费的承诺'
  - [9] 2026-10-22: the free virtual host is 1 GiB of web space, 5 GB of monthly traffic, a 50 MB MySQL database, a shared IP, and ASP or PHP
- sources:
  - [1] https://www.sanfengyun.com/freeServer/
  - [2] https://www.rainyun.com/docs/products/rcs/buy/billing
  - [3] https://www.sanfengyun.com/help/content_1058.html
  - [4] https://www.sanfengyun.com/help/content_1161.html
  - [5] https://www.sanfengyun.com/free/
  - [6] https://github.com/longzheng268/sanfengyun-keeper
  - [7] https://www.rainyun.com/
  - [8] https://www.rainyun.com/docs/products/rcs/buy/rcs
  - [9] https://www.abeiyun.com/free/
