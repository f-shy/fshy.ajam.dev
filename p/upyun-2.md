# UPYUN 又拍云 USS

> upyun.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upyun-2/ | JSON https://fshy.ajam.dev/api/v1/entity/upyun-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UPYUN 又拍云 USS (Storage Service)

- `storage/upyun-uss` | fails-egress | evidence reported | binding none | category iaas
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.upyun.com
- free tier: No standing free tier. Free capacity comes from (a) a 7-day trial with no storage/traffic cap, (b) 61 CNY voucher on real-name signup (1 month), (c) the 又拍云联盟 programme: a one-off 12-month resource grant worth 67 CNY. Described as '一年内每月可免费使用 10GB 存储空间及 15GB 的 CDN 流量'. Billing model is unusual: '按照日 CDN 流量 1:1 免费日存储容量，仅收取对应差值存储容量费用'. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered. CDN traffic at ¥0.29/GB. The 1:1 storage-for-traffic credit is the only offset and it only covers storage, never egress. | metered: yes
- identity: national-id | detail: national-id (实名认证 required for the 61 CNY voucher).
- interface: s3, rest, rclone, webdav-proxy
- limits note: quota: 10 GB under the alliance grant. egress: ¥0.29/GB, the binding cost. real-name required for vouchers.
- interface detail: s3
- tooling: OpenList driver `uss` (bucket + endpoint + operator name/password + anti-leech token, sign_url_expire). Proves the UPYUN REST/S3-ish API is mountable; also a first-class rclone-adjacent target via S3 compatibility.
- composes with: 10 GB/month per alliance account is a rounding error. The multiplier that would matter: the 1:1 traffic-to-storage credit means a high-traffic public bucket is storage-free. But the egress is what you pay for, so it inverts into a loss.
- reliability: Mature CDN vendor; nothing unstable. The problem is purely economic.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: No standing free tier. Free capacity comes from (a) a 7-day trial with no storage/traffic cap, (b) 61 CNY voucher on real-name signup (1 month), (c) the 又拍云联盟 programme: a one-off 12-month resource grant worth 67 CNY — described as '一年内每月可免费使用 10GB 存储空间及 15GB 的 CDN 流量'. Billing model is unusual: '按照日 CDN 流量 1:1 免费日存储容量，仅收取对应差值存储容量费用'.
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '新账号注册，提交实名认证会赠送 61 元 1 个月有效期的代金券'; '联盟活动...合计 67'
  - [2] 2026-10-21: '一年内每月可免费使用 10GB 存储空间及 15GB 的 CDN 流量'
  - [3] 2026-10-21: '按照日 CDN 流量 1:1 免费日存储容量...（日存储量 - 日流量）× 存储容量单价'
  - [4] 2026-10-21: working driver
- sources:
  - [1] https://help.upyun.com/knowledge-base/账号及费用类/
  - [2] https://www.yigujin.cn/blog/p1440.html
  - [3] https://www.upyun.com/price_instruction
  - [4] https://github.com/OpenListTeam/OpenList/tree/main/drivers/uss
