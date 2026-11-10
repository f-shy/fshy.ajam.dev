# AutoDL

> autodl.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/autodl/ | JSON https://fshy.ajam.dev/api/v1/entity/autodl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AutoDL

- `compute/autodl` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone unknown, ID yes, institution no | verified 2026-11-06T18:39:12.191Z (live) | stale on 2026-12-07
- url https://www.autodl.com/
- free tier: Retail per-hour GPU rental with no minimum term, from the front-page price table: RTX 4090 24GB CNY 1.88 per hour, RTX 3090 CNY 1.32, RTX 5090 CNY 2.78, A800-80GB CNY 5.59, PRO 6000 96GB CNY 6.98, H800-80GB CNY 9.98, H20 96GB CNY 9.98, V100 CNY 1.88, RTX 2080Ti CNY 0.88, RTX A4000 CNY 0.92, RTX 3080Ti CNY 0.98 and MTT S4000 48GB CNY 1.86; every row is marked 会员95折, a 5 percent member rate. H100, L40S and L4: not listed. A100 SXM4 80 GB and L40 48 GB are named in the card ranking with no rate. No free hour and no credit are stated on the page. A banner announces a change to part of the GPU price list on 12 November. | unit: hours | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: The passport route is the one a non-Chinese person can produce. The registration form itself was not read, so the phone requirement is unstated.
- interface: unknown
- limits note: Nothing throttles: billing is per second from container start to container stop with a CNY 0.01 minimum, so the constraint is money. A 24 GB RTX 4090 at CNY 1.88 an hour exhausts a CNY 100 deposit in about 53 hours, and the account stops when the balance reaches zero.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The per-second meter composes with object storage for checkpoints: rent a 4090 for the training step, stop it, and keep the dataset on the 20 GiB free netdisk, so idle time costs nothing between runs.
- reliability: no reliability event recorded
- notes: Per-card hourly rates on the front-page table, CNY per hour before the 5 percent member rate: RTX 4090 24GB CNY 1.88, RTX 3090 CNY 1.32, RTX 5090 32GB CNY 2.78, A800-80GB CNY 5.59, PRO 6000 96GB CNY 6.98, H800-80GB CNY 9.98, H20 96GB CNY 9.98, V100 32GB CNY 1.88, RTX 2080Ti CNY 0.88, RTX A4000 CNY 0.92, RTX 3080Ti CNY 0.98 and MTT S4000 48GB CNY 1.86. H100, L40S and L4: not listed. A100 SXM4 80GB and L40 48GB are named in the GPU算力排名 ranking with no rate, so no A100 80 GB price is published. The undiscounted figure is the one kept because the member price is not published per card. Billing is per second with a CNY 0.01 minimum, and a banner announces a change to part of the GPU price list on 12 November.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: front-page price table lists RTX 3090 at CNY 1.32/hour, RTX 4090 at CNY 1.88/hour, A800-80GB at CNY 5.59/hour and H800-80GB at CNY 9.98/hour, each marked 会员95折, quoted
  - [1] 2026-10-22: banner states 学生认证即刻升级炼丹会员 (student verification upgrades to the member tier) and 注册立送30天会员 (30 days of membership on registration), quoted
  - [2] 2026-10-22: real-name accepts 身份证 plus 人脸视频, or 其他个人证件 named as 海外护照, 港澳居民来往内地通行证 or a non-China driver licence, quoted
  - [3] 2026-10-22: student certification runs one year per cycle and is performed by educational email, quoted: 通过教育邮件进行认证
  - [4] 2026-10-22: billing rules: per-second metering with a CNY 0.01 floor, 20 GiB of free netdisk, 30 GiB of free image storage, data deletion reserved after 3 months without a login or CNY 50 of arrears
  - [5] 2026-10-22: quoted per-hour CNY rates for 12 accelerator classes from RTX 2080Ti at CNY 0.88 to H800 80GB at CNY 9.98; translated from the Chinese page: the signup banner offers 30 days of membership as a registration gift, and the footer states 20000 or more cards online
  - [6] 2026-10-22: the registration form is a phone number plus an SMS code, and the country selector renders four codes: +86 China, +852 China Hong Kong, +853 China Macao and +886 China Taiwan
  - [5] 2026-10-22: translated from the Chinese page: a free membership upgrade channel is offered to students, which is a discount rather than compute
  - [7] 2026-10-22: USD 1 = CNY 6.6743 on 2026-10-22, used for every conversion above
  - [1] 2026-11-06: the RTX 4090 24GB row is CNY 1.88 an hour with the 95 percent member rate marked on it | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA RTX 4090 / 24GB单精 82.58 TFLOPS / 半精 165.2 Tensor TFLOPS￥1.88 /时 会员95折
  - [1] 2026-11-06: the price is quoted per hour of a card, not per byte | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA RTX 4090 / 24GB单精 82.58 TFLOPS / 半精 165.2 Tensor TFLOPS￥1.88 /时 会员95折
  - [1] 2026-11-06: the RTX 4090 24GB row is unchanged at CNY 1.88 an hour | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA RTX 4090 / 24GB单精 82.58 TFLOPS / 半精 165.2 Tensor TFLOPS￥1.88 /时 会员95折
  - [1] 2026-11-06: the platform announces a change to part of the GPU price list on 12 November | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: 因供应侧成本剧烈波动，平台将于11月12日调整部分GPU价格。
  - [1] 2026-11-06: the front-page rate table is unchanged | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA RTX 4090 / 24GB单精 82.58 TFLOPS / 半精 165.2 Tensor TFLOPS￥1.88 /时 会员95折
  - [1] 2026-11-06: the A100 SXM4 80GB appears in the ranking with no rate | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA A100 SXM4 / 80GB
  - [1] 2026-11-06: the L40 48GB appears in the ranking with no rate, and no L40S is listed | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA L40 / 48GB
  - [1] 2026-11-06: the RTX 4090 24GB is CNY 1.88 an hour before the member rate | capture: sha256:9777623abcfd3b44ff5751d03d56464fa85b78e3a6e69eb13eacdd9f8e328f8a | quote: NVIDIA RTX 4090 / 24GB单精 82.58 TFLOPS / 半精 165.2 Tensor TFLOPS￥1.88 /时 会员95折
- sources:
  - [1] https://www.autodl.com/
  - [2] https://www.autodl.com/docs/real_name_cert/
  - [3] https://www.autodl.com/docs/student/
  - [4] https://www.autodl.com/docs/price/
  - [5] https://www.autodl.com/home
  - [6] https://www.autodl.com/register
  - [7] https://api.frankfurter.app/latest?from=USD&to=CNY
