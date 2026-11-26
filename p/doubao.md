# 豆包 AI云盘

> doubao.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doubao/ | JSON https://fshy.ajam.dev/api/v1/entity/doubao.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 豆包 AI云盘 (ByteDance Doubao drive)

- `netdisk-pan/doubao-drive` | fails-quota | evidence reported | binding retention-clamped | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T14:05:48.229Z (live) | stale on 2026-12-10
- url https://pan.doubao.com
- free tier: Advertised as unlimited at launch in 2025-05, then cut back: '后来被人发现不是无限，就改成5T还是限时'. A 5 TB grant that is time-limited, not permanent | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB per file in practice, per a forum report: '单文件限制实际是50G' | bytes: 50000000000 | source: [1]
- retention: The 5 TB is described as 限时, time-limited. No retention clock published | source: [1]
- egress: 我上传和下载差不多5G的文件都是不限制速度的 (about 5G file uploads and downloads were not speed-limited) | metered: no | source: [2]
- identity: country-phone | detail: a ByteDance account, which is phone-bound in practice | country: 86
- interface: rest
- limits:
  - per-object-cap: 50 GB per file in practice [1]
  - request-rate: bulk uploads trip risk control, capping single files at 100MB [3]
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
  - [2] 2026-11-19: the upload and download speed is reported as unthrottled and the upload limit was not stated | capture: sha256:681837ecb9d615523f2acd7f0bbd4e3a48723f3626b88818a1b3562f626c4989 | quote: 豆包的ai云盘，暂时还不知上传的限制是多少，我上传和下载差不多5G的文件都是不限制速度的
  - [3] 2026-11-19: the risk-control cap on single file size is 100MB after bulk uploads | capture: sha256:a599bf18fedab830b3f6628020623e755bfc4681cb7a6d8d79f67ca626424862 | quote: 如果用豆包云盘短时间内传输大量文件或超大文件，容易触发风控，导致单个文件大小限制为100M
  - [2] 2026-11-25: the poster reports no speed limit on uploads and downloads of about 5G files | capture: sha256:30614b9617f083cc3652aab0696d18d7af94a7946983be86f249c1c54832336c | quote: 豆包的ai云盘，暂时还不知上传的限制是多少，我上传和下载差不多5G的文件都是不限制速度的
  - [1] 2026-11-25: a forum report gives a 50G single-file limit in practice | capture: sha256:cda55bfa1d117bbe28d2d56142ff599b26649c74ee68e1ebc89f232d21f4c2d8 | quote: 之前说是无限，后来被人发现不是无限，就改成5T还是限时，随时可能再改，单文件限制实际是50G，云盘现在是非常好用，但是没见过分享链接，用户多了可能就会整改
- sources:
  - [1] https://linux.do/t/topic/1145191
  - [2] https://linux.do/t/topic/659711
  - [3] https://linux.do/t/topic/2482281

## 豆包云盘 Doubao Drive (ByteDance; storage provided by 北京飞书科技)

- `storage/doubao-drive` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T21:13:34.672Z (live) | stale on 2026-12-04
- url https://www.doubao.com
- free tier: The first-party terms state an unquantified free allowance for ordinary accounts (一定额度的免费云存储空间) and sell paid expansion plans; the exact quota is unverified on the first-party page. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
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
- notes: The stated allowance is deliberately unquantified: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'. Reported reality: legacy users 100 GB, new users 10 GB, API reports 5 TB but that is decorative. '注：抓包/facade/get_user_storage会显示5TB空间，但实测为上限为100G'. A 2026-06 protocol revision added paid expansion on top of the free allowance.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The stated allowance is deliberately unquantified: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'. Reported reality: legacy users 100 GB, new users 10 GB, API reports 5 TB but that is decorative — '注：抓包/facade/get_user_storage会显示5TB空间，但实测为上限为100G'. A 2026-06 protocol revision added paid expansion on top of the free allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '豆包通过云盘功能向普通账号提供一定额度的免费云存储空间'
  - [2] 2026-10-21: '豆包老用户给100g空间...抓包会显示5TB空间，但实测为上限为100G。新用户给10g空间。上传限制300MB'
  - [3] 2026-10-21: '云盘容量上限已锁定为5TB' after '近乎无限容量'
  - [1] 2026-11-19: the first-party terms give ordinary accounts an unquantified free allowance and sell paid expansion | capture: sha256:42d943994972572163c618df1e5292022f61bfb47df41af959995e102e4dc1fe | quote: 豆包通过云盘功能向普通账号提供一定额度的免费云存储空间，如果你需要更多存储空间，可自行选择付费购买云存储空间扩容服务的不同方案
  - [1] 2026-11-19: the service is restricted to logged-in users | capture: sha256:42d943994972572163c618df1e5292022f61bfb47df41af959995e102e4dc1fe | quote: 1.3 根据网络实名制规定的要求，本服务仅限登录用户使用。
- sources:
  - [1] https://www.doubao.com/legal/ai_space
  - [2] https://forum.naixi.net/thread-9862-1-1.html
  - [3] https://www.youleyou.com/wenzhang/3109022.html
