# CORESERVER V2

> coreserver.jp | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coreserver/ | JSON https://fshy.ajam.dev/api/v1/entity/coreserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CORESERVER V2

- `compute/coreserver-v2` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:24:41.665Z (live) | stale on 2026-12-05
- url https://www.coreserver.jp/price/
- free tier: CORE-X is JPY 830 a month on the monthly subscription, JPY 610 a month on a twelve-month term and JPY 430 on thirty-six months, and the vendor's feature table gives it a 6 GB memory allocation, a 300 percent CPU allocation, 500 GB of NVMe, unlimited transfer, unlimited MySQL databases, cron, and a cap of 200 processes and 30 concurrent web connections per account. CORE-Y is 9 GB and 600 percent for JPY 1,190 a month, CORE-Z 12 GB and 1,200 percent for JPY 2,990. The V2 plans carry a JPY 1,650 setup fee and a 30-day free start. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: time-boxed-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Monthly transfer is listed as unlimited as a guideline (転送量目安); above the prescribed transfer, under server-wide load, throughput is adjusted and best-effort | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - write-gated (binding): The vendor's load-limit page states that accounts carrying load other than web purposes, naming mining and computational processing, are restricted, and the 200-process and 30-connection caps bind before the 6 GB of memory does; the shape is a web host with a large memory allocation, not a virtual machine. [1]
- limits note: The vendor's load-limit page states that accounts carrying load other than web purposes, naming mining and computational processing, are restricted, and the 200-process and 30-connection caps bind before the 6 GB of memory does; the shape is a web host with a large memory allocation, not a virtual machine.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: For JPY 830 a month with no term, CORE-X offers more memory than any Japanese VPS below JPY 1,600 and a cron scheduler, which is a real shape for a nightly extraction job; it composes with a VPS only where the job is expressed as a web request, because no inbound port can be opened.
- reliability: no reliability event recorded
- notes: The shape is the interesting part of this record: 6 GB of memory for JPY 830 a month is a quarter of the price of a 4 GB VPS in Japan, and the reason is that it is a shared web host with a large allocation rather than a machine. The constraints are all published, which is unusual: process count, connection count, disk throughput, IOPS and a written restriction on compute workloads. The 30-day free start is stated on the vendor's front page.
- extras:
  - facets.class: shared-compute
  - facets.free_tier_kind: time-boxed-trial
  - facets.shape.ram_gib: 6
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the price table gives CORE-X at 830円 a month on subscription, 610円 on twelve months and 430円 on thirty-six, CORE-Y at 1,190円 and CORE-Z at 2,990円, with a 1,650円 setup fee on the V2 plans
  - [2] 2026-10-22: the feature table gives CORE-X 500 GB of disk, unlimited transfer, a 6 GB memory allocation and a 300 percent CPU allocation, CORE-Y 700 GB with 9 GB and 600 percent, and CORE-Z 1,000 GB with 12 GB and 1,200 percent, all with cron and unlimited databases
  - [3] 2026-10-22: the vendor's load-limit page gives CORE-X 200 MB/s disk, 2,048 IO operations a second, 30 concurrent web connections and 200 processes per account, rising to 800 processes on CORE-Z, and states that accounts putting load on the server for non-web purposes such as mining or computational processing will be restricted
  - [2] 2026-11-03: monthly transfer is listed as unlimited, as a guideline figure | capture: sha256:a98ff715129956d06be2eb5e85786be65859a0ab3c60c04222e94b44de7e1a52 | quote: | 転送量目安（月）※1 | 無制限 | 無制限 | 無制限 | 月間に使用可能な転送量の目安です。 |
  - [1] 2026-11-03: above the prescribed transfer the service is best-effort | capture: sha256:12c00f99cb9e2b88f0bbd9929af9991a270de37b09d74268d450c0b30db098f4 | quote: 規定転送量までは無制限で、それ以上はベストエフォートとなります。
- sources:
  - [1] https://www.coreserver.jp/price/
  - [2] https://www.coreserver.jp/function/
  - [3] https://help.coreserver.jp/faq/load-limit/
