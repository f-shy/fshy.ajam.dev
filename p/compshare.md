# Compshare

> compshare.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/compshare/ | JSON https://fshy.ajam.dev/api/v1/entity/compshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Compshare

- `compute/compshare` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID yes, institution no | verified 2026-11-06T18:41:34.656Z (live) | stale on 2026-12-07
- url https://www.compshare.cn/price-list
- free tier: RTX4090 24G with 14 vCPU and 32G RAM at CNY 1.92 per hour on demand, CNY 42.33 per day, CNY 1154.64 per month, or CNY 1.31 per hour preemptible, quoted from the price list. The same price list gives the A100 80G (1 GPU, 16 vCPU, 64 GiB RAM) at CNY 10.75 per hour on demand, CNY 236.58 per day, CNY 6452.40 per month or CNY 7.52 per hour preemptible; it has no H100, L40S or L4 table. The same provider sells a no-GPU mode at CNY 0.15 per hour for development on a retained instance, and individual real-name certification pays a one-off CNY 5 credit. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: is required and pays CNY 5 on success; is a separate institutional route that adds a 5 percent discount. The documentation read does not state whether a non-Chinese passport passes individual certification, so the reachability of this gate for an international registrant is unverified.
- interface: unknown
- limits note: Billing is per second and shutdown stops the meter, so nothing throttles a running job. The first thing that fails is the cheap lane: the CNY 1.31 preemptible rate is reclaimable, and the CNY 1154.64 monthly rate beats on-demand only above about 601 hours a month.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The CNY 0.15/hour no-GPU mode turns this into a cheap always-on 14 vCPU / 32 GiB box attached to a dataset, which composes with a GPU step rented for minutes; the pair is a full training loop for under USD 30 a month.
- reliability: no reliability event recorded
- notes: Per-card rates on the price list read on 2026-11-06: RTX4090 24G CNY 1.92 per hour on demand (1 GPU, 14C 32G), A100 80G CNY 10.75 per hour on demand (1 GPU, 16C 64G); H100, L40S and L4 are not listed. The page's card sections are RTX4090, RTX4090 48G, RTX5090, RTX3080Ti, RTX3090, RTX2080, RTX2080Ti, A800, H20, P40, V100S and A100, and the CNY 0.42 per hour 8C 40G row sits in the RTX2080 8G section. No free GPU hours are stated; individual real-name certification pays a one-off CNY 5 credit.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: one-time-credit
  - facets.shape.vcpu: 14
  - facets.shape.ram_gib: 32
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: price table row for RTX4090 24G, 1 GPU, 14C 32G: 按量计费 1.92, 包日 42.33, 包月 1154.64, 抢占式 1.31, quoted from the table
  - [1] 2026-10-22: page description names the GPU set RTX4090, RTX5090, A800, H20 and A100 and the billing modes 按量, 包日, 包月 and 抢占式
  - [2] 2026-10-22: front page states 无卡模式（0.15元/小时）and 关机不收费（保留数据）, quoted
  - [3] 2026-10-22: 个人认证 pays CNY 5 on success; 高校认证 adds a 5 percent discount, quoted
  - [1] 2026-11-03: the last table of the price list, headed A100 80G, has one row: 1 GPU, 16C 64G, 10.75 on demand, 236.58 per day, 6452.40 per month, 7.52 preemptible (CNY); the card headings on the page run RTX4090, RTX4090 48G, RTX5090, RTX3080Ti, RTX3090, RTX2080, RTX2080Ti, A800, H20, P40, V100S, A100, with no H100, L40S or L4 | capture: sha256:a448f54d962328fae7e592c2b905a936edca4639b37af6cda4c8031418fb9f15 | quote: | 1*GPU | 16C 64G | 10.75 | 236.58 | 6452.40 | 7.52 |
  - [4] 2026-11-03: on-demand (按量) billing is per second, invoiced at the hour mark; stopping an instance stops the GPU, CPU and memory charge while disk and image storage keep billing; daily and monthly plans are prepaid | capture: sha256:586d1c0bb40d3d58320de91ae9d2e05db9eda593a58d373de0de7a6bb1e70dfe | quote: 按照小时计费的后付费模式，秒级计费。
  - [1] 2026-11-03: the RTX4090 24G 1 GPU 14C 32G row is unchanged: 1.92 on demand, 42.33 per day, 1154.64 per month, 1.31 preemptible (CNY) | capture: sha256:a448f54d962328fae7e592c2b905a936edca4639b37af6cda4c8031418fb9f15 | quote: | 1*GPU | 14C 32G | 1.92 | 42.33 | 1154.64 | 1.31 |
  - [1] 2026-11-06: the RTX4090 24G section prices one GPU with 14C 32G at CNY 1.92 per hour on demand | capture: sha256:8d4ce04cea3648650f3a83bff17d28b4b28d0f842c3ec81bd38ac6cefb3cb6ef | quote: <td>1*GPU</td><td>14C 32G</td><td class="pl-price">1.92</td>
  - [1] 2026-11-06: the last card section is headed A100 80G | capture: sha256:8d4ce04cea3648650f3a83bff17d28b4b28d0f842c3ec81bd38ac6cefb3cb6ef | quote: <span class="pl-table-name">A100</span><span class="pl-table-spec">80G</span>
  - [1] 2026-11-06: the A100 80G section prices one GPU with 16C 64G at CNY 10.75 per hour on demand | capture: sha256:8d4ce04cea3648650f3a83bff17d28b4b28d0f842c3ec81bd38ac6cefb3cb6ef | quote: <td>1*GPU</td><td>16C 64G</td><td class="pl-price">10.75</td>
  - [1] 2026-11-06: the page's card list runs RTX4090, RTX4090 48G, RTX5090, RTX3080Ti, RTX3090, RTX2080, RTX2080Ti, A800, H20, P40, V100S and A100, with no H100, L40S or L4 | capture: sha256:8d4ce04cea3648650f3a83bff17d28b4b28d0f842c3ec81bd38ac6cefb3cb6ef | quote: class="pl-anchor-item">A800</button></li><li><button type="button" class="pl-anchor-item">H20</button></li><li><button type="button" class="pl-anchor-item">P40</button></li><li><button type="button" class="pl-anchor-item">V100S</button></li><li><button type="button" class="pl-anchor-item">A100</button></li>
  - [3] 2026-11-06: individual real-name certification pays a one-off CNY 5 credit, which is account credit and not GPU hours | capture: sha256:906592932b389b0eb3fc4116a9bdc9bc91be0874fc93d103201e1eadd1ac66cf | quote: 实名成功后系统自动发放5元赠金
  - [1] 2026-11-06: the first card section is headed RTX4090 24G | capture: sha256:8d4ce04cea3648650f3a83bff17d28b4b28d0f842c3ec81bd38ac6cefb3cb6ef | quote: <span class="pl-table-name">RTX4090</span><span class="pl-table-spec">24G</span>
- sources:
  - [1] https://www.compshare.cn/price-list
  - [2] https://compshare.cn/
  - [3] https://www.compshare.cn/docs/uaccount/identity/authentication
  - [4] https://www.compshare.cn/docs/operation/charge/billdescribe
