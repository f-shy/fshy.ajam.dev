# 超星云盘 Chaoxing Cloud

> chaoxing.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chaoxing/ | JSON https://fshy.ajam.dev/api/v1/entity/chaoxing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 超星云盘 Chaoxing Cloud (pan-yz.chaoxing.com) + 超星小组盘

- `storage/chaoxing-cloud` | fails-quota | evidence reported | binding per-object-cap | category academic
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url http://pan-yz.chaoxing.com
- free tier: 100 GB free per account (was 150 GB before a reduction; one vendor page still advertises '为每个用户提供150G的初始容量空间'). Per-file: 1 GB on web, up to 15 GB via the desktop client ('客户端上传单文件上限15G'). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file: 1 GB | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Upload/download not speed-limited ('上传下载不限速'). Downloads of shared files require login. A read-gate on the sharing path, not the byte path. | metered: no
- identity: national-id | detail: national-id (超星学习通 account, effectively student/real-name bound).
- interface: rest, webdav-proxy
- limits:
  - per-object-cap (binding): Per-file: 1 GB [1]
- limits note: per-object-cap: 1 GB (web) / 15 GB (client). pull-count / write-gate: sharing requires the recipient to log in. No published API rate limit; parsers require a Referer header and CHAOXING marks the group drive as proxy-only.
- interface detail: rest
- tooling: OpenList driver `chaoxing` (超星小组盘. Group drive variant, explicitly '需要代理才能使用') and qaiu/netdisk-fast-download `pcx` with a mandatory `Referer: https://pan-yz.chaoxing.com`. Both are reverse-engineered.
- composes with: Accounts provide 100 GB each, tied to institutional student identifiers (学号), with group drives (小组盘) adding shared pools per course.
- reliability: Quota was cut 150 GB → 100 GB, i.e. it moves downward. Interfaces are reverse-engineered and break when the university portal changes.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 GB free per account (was 150 GB before a reduction; one vendor page still advertises '为每个用户提供150G的初始容量空间'). Per-file: 1 GB on web, up to 15 GB via the desktop client ('客户端上传单文件上限15G').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '「超星云盘」目前免费提供 100G 的容量空间，之前的用户是 150G'; '网页版上传单个文件最大为1GB，客户端不限制'
  - [2] 2026-10-21: '不限速，免费空间100G，客户端上传单文件上限15G'
  - [3] 2026-10-21: vendor's own app listing: '为每个用户提供150G的初始容量空间'
- sources:
  - [1] https://xiaoyi.vc/chaoxing.html
  - [2] https://dh.fwfly.com/post/62.html
  - [3] https://z.chaoxing.com/application/center/getAppDetail?appId=32
