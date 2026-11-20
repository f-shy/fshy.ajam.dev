# UC Drive

> uc.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uc/ | JSON https://fshy.ajam.dev/api/v1/entity/uc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UC Drive (UC网盘)

- `netdisk-pan/uc-drive` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:21:07.067Z (inherited) | stale on 2026-11-19
- url https://drive.uc.cn
- free tier: 1 TB permanent handed out as claimable promo codes that are repeatable and stackable: '加上之前的活动，有 2t 了' and '都是永久'. A separate 1 TB plus 10 GB baseline per a 2026 comparison post | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB per file on a free account: 'UC网盘2t,但单文件就1G，相当难用' | bytes: 1000000000 | source: [2]
- retention: Promo capacity is permanent once claimed. No retention clock on stored files is published | source: [1]
- egress: Free downloads are throttled hard, with reports of 300 to 400 KB/s for video: 'UC网盘之前宣称不限速，现在下载视频三四百k'. The paid tier advertises 上传下载不限速 as an SVIP benefit | metered: yes | source: [3]
- identity: country-phone | detail: an Alibaba account, which is +86-bound in practice, and the SVIP tier needs a Chinese identity document | country: 86
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per file on a free account [2]
  - per-ip-shaping: free downloads reported at 300 to 400 KB/s [3]
  - write-gated: the OpenList driver is cookie-based, and the netdisk-fast-download auth table requires a logged-in cookie for UC [4]
- binding note: The per-file cap is what closes it, not the quota or the identity.
- tooling: No public API. A reverse-engineered client mounts it: the OpenList UC driver takes a pasted browser cookie, root folder id 0. A separate UC TV driver pairs by QR code from the mobile app and supports list and download only. Same backend family as Quark. No official S3 or WebDAV
- composes with: Codes are batch-minted, a hundred a month per one poster, and shared in threads, so one account can stack several to 2 TB. Each account is a +86 identity, and the 1 GB per-file ceiling makes the capacity useless as a dataset store
- reliability: Promo capacity is permanent once claimed, but the 1 GB per-file ceiling makes it a media-hoarding pan and not a dataset store. Download tickets are IP-bound on the shared Quark backend, so a harvested cookie dies on the first replay
- notes: Covers both SVIP paid tiers and promo-code allocations. While nominal storage capacity reaches 2 TB permanently, individual file uploads are constrained by a strict 1 GB ceiling.
- extras:
  - access_mode: registration-gated
  - aliases: UC Drive / UC网盘; UC网盘 (UC Browser drive, Alibaba); UC Browser drive
  - per_file_cap_bytes_derived: 1000000000
  - shared_backend_with_quark: yes
- evidence:
  - [1] 2026-10-21: 'UC网盘1TB永久容量领取...公益~还剩20个', and a reply '加上之前的活动，有 2t 了...都是永久'
  - [2] 2026-10-21: 'UC网盘2t,但单文件就1G，相当难用'
  - [3] 2026-10-21: 'uc网盘之前宣称不限速，现在下载视频三四百k'
  - [5] 2026-10-21: '开通UC网盘SVIP畅享6TB存储空间', '上传下载不限速...开通UC网盘SVIP畅享专属极速通道'
  - [4] 2026-10-21: the auth table states 'UC网盘(UC) 必须', meaning a cookie is mandatory
  - [6] 2026-11-03: the OpenList UC driver takes a browser cookie | capture: sha256:90b3a655e5b4e2eb98615afca63dda79d94f886a53fd3456a5979aebd43211bb | quote: Press F12 to open "Debug", select "Network", select any request on the left, and find the one with the `Cookie` parameter.
  - [6] 2026-11-03: the UC TV driver is list and download only | capture: sha256:90b3a655e5b4e2eb98615afca63dda79d94f886a53fd3456a5979aebd43211bb | quote: The TV version supports `302`, but only `List` and `Download` operations are supported.
  - [5] 2026-11-03: the vendor page advertises 6 TB under the SVIP tier | capture: sha256:622c94b57c266dd2e22a3d49c272358f1804ea158fd3d87a7e12dcc81c40f822 | quote: 开通UC网盘SVIP畅享6TB存储空间
- sources:
  - [1] https://linux.do/t/topic/269012
  - [2] https://linux.do/t/topic/1426604
  - [3] https://linux.do/t/topic/623279
  - [4] https://github.com/qaiu/netdisk-fast-download
  - [5] https://drive.uc.cn/
  - [6] https://openlistteam.github.io/docs/guide/drivers/uc.html
