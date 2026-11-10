# 坚果云 Nutstore

> jianguoyun.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jianguoyun/ | JSON https://fshy.ajam.dev/api/v1/entity/jianguoyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 坚果云 Nutstore (jianguoyun.com)

- `storage/nutstore` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.jianguoyun.com
- free tier: Traffic-based, not capacity-based: '每位免费用户每月最多可上传1GB的文件，可下载3GB的文件'. Space grows with what you upload and is bounded by the traffic allowance, so effective free storage ≈ 1 GB/month of net new data. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap number read | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered in the same currency: 3 GB/month of downloads for free users. No per-GB pricing on the free tier. It just stops syncing. | metered: yes | free allowance: 3 GB per month
- identity: email | detail: email
- interface: webdav, rclone
- limits:
  - per-object-cap (binding): No per-file cap number read [1]
- limits note: request-rate (monthly byte-rate): 1 GB up / 3 GB down per month, hard stop when exhausted ('当流量耗尽后将无法继续同步'). No per-file cap number read.
- interface detail: webdav
- tooling: Official WebDAV. '国内少数官方支持 WebDAV 的同步盘', app-password generation documented at help.jianguoyun.com/?p=2803. Works with rclone's `webdav` backend directly, no reverse engineering.
- composes with: 1 GB/month upload per account is not a capacity play at all. Its value is the only approved WebDAV endpoint in the Chinese consumer market. Useful as a control plane, not as bytes.
- reliability: Very stable, ten-year-old service; the constraint is deliberate and enforced.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Traffic-based, not capacity-based: '每位免费用户每月最多可上传1GB的文件，可下载3GB的文件'. Space grows with what you upload and is bounded by the traffic allowance, so effective free storage ≈ 1 GB/month of net new data.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '每位免费用户每月最多可上传1GB的文件，可下载3GB的文件'
  - [2] 2026-10-21: '免费版用户每月上传流量1GB、下载流量3GB'
  - [3] 2026-10-21: '免费 流量制...WebDAV 支持'
- sources:
  - [1] https://help.jianguoyun.com/?p=3766
  - [2] https://help.jianguoyun.com/?p=2803
  - [3] https://panhunt.com/pan-platforms/nutstore
