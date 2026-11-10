# 豆包 AI云盘

> doubao.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doubao/ | JSON https://fshy.ajam.dev/api/v1/entity/doubao.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 豆包 AI云盘 (ByteDance Doubao drive)

- `netdisk-pan/doubao-drive` | fails-quota | evidence reported | binding retention-clamped | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pan.doubao.com
- free tier: Advertised as unlimited at launch in 2025-05, then cut back: '后来被人发现不是无限，就改成5T还是限时'. A 5 TB grant that is time-limited, not permanent | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB per file in practice, per a forum report: '单文件限制实际是50G' | bytes: 50000000000 | source: [1]
- retention: The 5 TB is described as 限时, time-limited. No retention clock published | source: [1]
- egress: Fast and unmetered in practice: '我上传和下载差不多5G的文件都是不限制速度的', with a later test agreeing. No published egress term | metered: no | source: [2]
- identity: country-phone | detail: a ByteDance account, which is phone-bound in practice | country: 86
- interface: rest
- limits:
  - per-object-cap: 50 GB per file in practice [1]
  - request-rate: bulk uploads trip risk control, reportedly clearing after 7 to 14 days of light use [3]
- binding note: A 5 TB grant described as time-limited is a quota the provider can shorten, so what binds is the retention clamp: the capacity is real and the clock on it is unpublished. The 50 GB per-file ceiling is the second constraint.
- tooling: no official API. The OpenList/AList 豆包 driver mounts it, and Cloudflare Tunnel plus WebDAV recipes exist
- composes with: 5 TB per account if the grant holds, with no documented way to stack, and the capacity has changed at least twice, so it is not bankable. No share links at all means there is no CDN front and therefore no serving path
- reliability: ByteDance will keep tightening it: '先免费积累用户量，后面也会限速，要会员收费的'. Data vanishing is unlikely and quota repricing is likely. No share links means no way to serve from it
- notes: Notable as a large ByteDance-provided quota whose terms shifted rapidly: offered as unlimited at launch, reduced to 5 TB with time-limited duration within months, and lacking public share links. The absence of public link generation prevents integration with fronting CDNs.
- extras:
  - access_mode: registration-gated
  - launched: 2025-05
  - share_links: no
  - quota_trajectory: unlimited at launch, then 5 TB time-limited
  - per_file_cap_bytes_derived: 50000000000
  - slug_note: See the history entry for the other nine placeholder slugs and why they were not used verbatim
  - reserved_slug: ai
- evidence:
  - [1] 2026-10-21: '百度发现是无限量的，后来被人发现不是无限，就改成5T还是限时，单文件限制实际是50G，没见过分享链接'
  - [2] 2026-10-21: '豆包的ai云盘，我上传和下载差不多5G的文件都是不限制速度的'
  - [3] 2026-10-21: '豆包云盘上传下载都很快，就是可能我一次传太多被风控了，剩下几本漫画传不上去'
- sources:
  - [1] https://linux.do/t/topic/1145191
  - [2] https://linux.do/t/topic/659711
  - [3] https://linux.do/t/topic/2482281

## 豆包云盘 Doubao Drive (ByteDance; storage provided by 北京飞书科技)

- `storage/doubao-drive` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.doubao.com
- free tier: The stated allowance is deliberately unquantified: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'. Reported reality: legacy users 100 GB, new users 10 GB, API reports 5 TB but that is decorative. '注：抓包/facade/get_user_storage会显示5TB空间，但实测为上限为100G'. A 2026-06 protocol revision added paid expansion on top of the free allowance. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: '上传限制300MB | bytes: 300000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not applicable at these sizes; downloads are CDN-served with no published meter. | metered: no
- identity: country-phone | detail: country-phone (ByteDance/抖音 account)
- interface: rest, webdav-proxy
- limits:
  - per-object-cap (binding): per-object-cap: '上传限制300MB [1]
- limits note: quota: 100 GB for legacy accounts, 10 GB new. per-object-cap: '上传限制300MB，但是去除一个get参数' can be raised. The 5 TB API value does not correspond to usable capacity.
- interface detail: rest
- tooling: OpenList driver `doubao` (cookie auth, download_api select get_file_url/get_download_info, 2 r/s client-side rate limit). Reverse-engineered and explicitly unmaintained ('本接口是基于历史产物的逆向接口').
- composes with: ByteDance account per phone number, 10–100 GB each. The 5 TB figure in the API is exactly the 'unlimited that isn't' trap from §3.
- reliability: Quota direction is downward (AI-space free tier was cut to 5 TB then to 100 GB); the interface is unofficial and the 'unlimited' banner has already been retired.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The stated allowance is deliberately unquantified: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'. Reported reality: legacy users 100 GB, new users 10 GB, API reports 5 TB but that is decorative — '注：抓包/facade/get_user_storage会显示5TB空间，但实测为上限为100G'. A 2026-06 protocol revision added paid expansion on top of the free allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'
  - [2] 2026-10-21: '豆包老用户给100g空间...抓包会显示5TB空间，但实测为上限为100G。新用户给10g空间。上传限制300MB'
  - [3] 2026-10-21: '云盘容量上限已锁定为5TB' after '近乎无限容量'
- sources:
  - [1] https://www.doubao.com/legal/ai_space
  - [2] https://forum.naixi.net/thread-9862-1-1.html
  - [3] https://www.youleyou.com/wenzhang/3109022.html
