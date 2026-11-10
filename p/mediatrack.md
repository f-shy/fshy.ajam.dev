# 分秒帧 MediaTrack

> mediatrack.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mediatrack/ | JSON https://fshy.ajam.dev/api/v1/entity/mediatrack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 分秒帧 MediaTrack (app.mediatrack.cn)

- `storage/mediatrack` | fails-quota | evidence reported | binding per-object-cap | category media
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mediatrack.cn
- free tier: Free personal plan: 10 GB storage, 5 members per project, 1 GB per single file (secondary source says 2 GB free). Paid: 100 GB / 300 GB / 1 TB / 2 TB / 3 TB / 5 TB+. Storage counts '归属于团队的项目、资源库中的文件及回收站内未永久删除的文件'. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB per single file | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered separately; the product is a review/approval tool, not a CDN. No public bandwidth line found. | metered: yes
- identity: any-phone | detail: any-phone (WeChat scan or phone login)
- interface: rest, webdav-proxy
- limits:
  - per-object-cap (binding): 1 GB per single file [1]
- limits note: per-object-cap: 1 GB. quota: 10 GB free. Commercial pivot in 2022 ('将于2022年7月25日起正式收费') means the free tier is a residual, not a strategy.
- interface detail: rest
- tooling: OpenList driver `mediatrack` (access_token + project_id, order_by/order_desc). A working mount over the video-collaboration API.
- composes with: 10 GB per account, team-based, so projects multiply but storage is billed per team. 1 GB/file.
- reliability: Paying product with a stable API; free tier is deliberately vestigial.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free personal plan: 10 GB storage, 5 members per project, 1 GB per single file (secondary source says 2 GB free). Paid: 100 GB / 300 GB / 1 TB / 2 TB / 3 TB / 5 TB+. Storage counts '归属于团队的项目、资源库中的文件及回收站内未永久删除的文件'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '存储空间 100GB / 300GB / 1TB / 2TB / 3TB / 5TB起' and '1GB / 单文件'
  - [2] 2026-10-21: '免费版 | 2GB 存储 + 3 人协作'
  - [3] 2026-10-21: '将于2022年7月25日起正式收费'
- sources:
  - [1] https://www.mediatrack.cn/pricing
  - [2] https://juejin.cn/post/7509659058342314018
  - [3] https://mediatrack.cn/news/qyxw/1540729039898017792
