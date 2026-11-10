# Quark Cloud

> quark.cn | Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quark/ | JSON https://fshy.ajam.dev/api/v1/entity/quark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quark Cloud Drive (夸克网盘)

- `netdisk-pan/quark-cloud-drive` | fails-egress | evidence reported | binding per-ip-shaping | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pan.quark.cn
- free tier: 10 GB free; VIP 3 TB and SVIP 6 TB. A new account that saves one shared file gets 1 TB: '新用户保存一次别人分享的文件，可获取1TB的空间容量' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published for the free tier. Downloads above 50 MB need a desktop-client user agent and a cookie, else the API answers 23018 download file size limit | source: [2]
- retention: Accounts frozen after 12 months without a login, with the storage reclaimed if not unfrozen within a month: '超过1年未登录 … 回收存储容量 … 文件丢失、数据清空' | days: 365 | source: [3]
- egress: No per-GB fee, but the free tier is shaped to 2 to 4 MB/s against about 50 MB/s on SVIP, and a third-party fetch service measured a free account at about 60 KB/s. Downloads above 50 MB need a client user agent and a cookie | metered: yes | source: [4]
- identity: country-phone | detail: mainland +86 only, and SVIP payment needs a Chinese identity document | country: 86
- interface: rest
- limits:
  - per-ip-shaping (binding): 2 to 4 MB/s on the free tier [4]
  - retention-clamped: 12 months without a login freezes the account and reclaims the capacity [3]
  - write-gated: share downloads above 50 MB need a desktop-client user agent and a cookie [2]
- binding note: 10 GB free, and 2 to 4 MB/s is 170 to 340 GB a day at best, so the quota and the shaping both fail. The shaping is the one that would still bind on a paid tier, and the identity gate sits in front of both.
- tooling: no official open API. The reverse-engineered web API at drive-pc.quark.cn is what the OpenList quark driver uses; the netdisk-fast-download qk parser states that a logged-in cookie is mandatory; the OpenList docs warn quick-transfer now needs a local agent because of the speed limit
- composes with: Base free storage is 10 GB per mobile-verified account. Promotional 1 TB allocations granted upon saving shared files expire after promotional periods rather than providing permanent capacity.
- reliability: The anonymous path gets metadata and not bytes: a share token and a full file listing with fid and share_fid_token come back with no cookie at all, and the download call is 404 on all four documented hosts. Download tickets are IP-bound, so a link minted on one host dies when replayed from another, which is why every public Quark parser rots within weeks
- notes: Quark has largely replaced Baidu Pan as the default share host on Chinese forums, which is why it is recorded in full. The finding that matters for a bridge builder is that the anonymous token lists a whole share and cannot move a byte, and that download tickets are IP-bound so a harvested cookie does not survive a replay.
- extras:
  - access_mode: registration-gated
  - anonymous_read: metadata yes, bytes no
  - freeze_after_days: 365
  - aliases: Quark Cloud Drive / 夸克网盘
  - ip_bound_download_tickets: yes
- evidence:
  - [1] 2026-10-21: 'SVIP用户6TB空间，VIP用户3TB空间，普通用户初始容量10GB空间'
  - [3] 2026-10-21: '超过1年未登录 … 回收存储容量 … 文件丢失、数据清空'
  - probe:POST https://pan.quark.cn/1/clouddrive/share/sharepage/token 2026-10-21: 200, 756 B, data.stoken returned with a share title and no cookie
  - probe:GET https://pan.quark.cn/1/clouddrive/share/sharepage/detail 2026-10-21: 200, 3,016 B, list[0] with a file name, size 31614114, fid and share_fid_token, no cookie
  - probe:POST https://pan.quark.cn/1/clouddrive/share/sharepage/download 2026-10-21: 404 on pan.quark.cn, drive-pc.quark.cn, drive-h.quark.cn and drive.quark.cn, all four
  - probe:GET https://drive-pc.quark.cn/1/clouddrive/config?pr=ucpro&fr=pc 2026-10-21: 401 with {"code":31001,"message":"require login [guest]"}
  - [2] 2026-10-21: '分享通道绕过 无效, PC API 上 share/sharepage/download 等均 404'; downloads above 50 MB need a client UA and a cookie
- sources:
  - [1] https://www.quark.cn/articles/003.html
  - [2] https://github.com/woshihoujinxin/quarkpan-skill
  - [3] https://terms.alicdn.com/legal-agreement/terms/b_end_product_protocol/20230516173016165/20230516173016165.html
  - [4] https://kuake.ijinshan.com/membership/index.html

## Quark TV and UC TV (夸克网盘 TV版, UC网盘 TV版)

- `netdisk-pan/quark-tv-uc-tv` | fails-quota | evidence reported | binding write-gated | category TV-edition OAuth client for a Chinese pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:20:53.785Z (inherited) | stale on 2026-11-19
- url https://pan.quark.cn/
- free tier: Quark free 300 GB plus one-off 1 TB gift campaigns; two documented campaigns give 2 TB total. UC's free base is 10 GB | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published for the TV client | source: [1]
- retention: The gift campaigns are one-off per account and campaign-gated. No retention clock on stored files | source: [2]
- egress: Quark free is shaped to about 1.7 MB/s and about 5 MB/s at peak for 88VIP. The TV client streams in original quality without downloading, which is why the community uses it | metered: yes | source: [1]
- identity: any-phone | detail: a Quark or UC account, which is phone-bound in practice; the TV client's own login path exists but does not remove the account requirement
- interface: rest
- limits:
  - write-gated (binding): the TV client is read-only by design: the driver sets NoUpload and NoOverwriteUpload [3]
  - per-ip-shaping: free egress shaped to about 1.7 MB/s [1]
- binding note: 300 GB free, and the TV client cannot write at all, so the direction that fails is the write side: it is a download-and-stream path with no upload, which makes it a serving helper and not a store.
- tooling: a reverse-engineered TV OAuth client, fully documented in source: the OpenList quark_uc_tv driver hard-codes api https://open-api-drive.quark.cn for Quark and https://open-api-drive.uc.cn for UC, with a public client id, a TV sign key, an app version and a channel. WebDAV comes out once mounted
- composes with: The TV OAuth reads an account through a clean API with no client, so it is a serving and STRM path and not a write path. Paired with a writable pan it covers both directions, which is why the community keeps it alive
- reliability: The TV client's client id and sign key are public constants that Alibaba rotates, and when they rotate every mount breaks until the driver is re-patched. The free-tier space campaigns are monthly and quantity-capped, so they are a lottery and not a capacity plan
- notes: The canonical inverse of the public-instance problem. There an instance advertises a write it refuses; here a client is documented as read-only by design. Both are cases where the API's write surface must be read from the driver's own flags and not from the marketing page.
- extras:
  - access_mode: registration-gated
  - read_only: yes
  - driver: OpenList quark_uc_tv
  - aliases: Quark TV / UC TV (夸克网盘 TV版, UC网盘 TV版)
- evidence:
  - [3] 2026-10-21: two drivers, QuarkTV and UCTV, both API endpoints, the client id, signKey, app version, channel, and NoUpload: true with NoOverwriteUpload: true
  - probe:GET https://open-api-drive.quark.cn/1/clouddrive/config?pr=ucpro&fr=pc 2026-10-21: HTTP 400, 65 B, {"status":-1,"errno":10001,"error_info":"_timestamp格式错误"}, so the endpoint is live and wants a signed timestamp
  - probe:GET https://drive-pc.quark.cn/1/clouddrive/member?pr=ucpro&fr=pc 2026-10-21: HTTP 401, 117 B, {"status":401,"code":31001,"message":"require login [guest]"}
  - [2] 2026-10-21: two campaigns of 1 TB each, so 2 TB permanent
  - [1] 2026-10-21: 夸克网盘, 300G free, shaped at 1.7M/s
  - [3] 2026-11-03: the driver config still sets NoUpload for the TV client | capture: sha256:1b53ae8374929577d825b743246187cfea6572ccf23c7b82ae0a3c1a171749fb | quote: NoUpload: true,
  - [3] 2026-11-03: the driver still hard-codes the Quark TV API endpoint | capture: sha256:1b53ae8374929577d825b743246187cfea6572ccf23c7b82ae0a3c1a171749fb | quote: api: "https://open-api-drive.quark.cn",
  - [3] 2026-11-03: the driver still hard-codes the UC TV API endpoint | capture: sha256:1b53ae8374929577d825b743246187cfea6572ccf23c7b82ae0a3c1a171749fb | quote: api: "https://open-api-drive.uc.cn",
  - [1] 2026-11-03: the table row still reads 300G free, no upload limit and a 1.7M/s download limit | capture: sha256:87cfd4212b0eaf2bb73b16353c13f114920639a0b2df7d9e3a6465f3bf0ce870 | quote: | 夸克网盘 | 300G | 无 | | 有 | 1.7M/s | 是 | 是 |
  - probe:GET https://open-api-drive.quark.cn/1/clouddrive/config?pr=ucpro&fr=pc 2026-11-03: the endpoint is live and answers a body of 65 bytes that wants a signed timestamp | capture: sha256:c0d00823aa7af0c4e39c2e2154fb0ffa6deb7e1de99b20e6355108433e695198 | quote: "error_info":"_timestamp格式错误"
  - probe:GET https://drive-pc.quark.cn/1/clouddrive/member?pr=ucpro&fr=pc 2026-11-03: the member endpoint answers 401 to an anonymous caller | capture: sha256:b99e6cd7295296e1ab591e98363decec77baa2636c251a2e114dbd47897bfd52 | quote: "message":"require login [guest]"
  - [4] 2026-11-03: the vendor page still offers a TV client download | capture: sha256:26325190f535f5a7af4a740f6a05059969c0d82777fbdda632628587fac11e2a | quote: 下载 TV 端
- sources:
  - [1] https://zh.wikipedia.org/zh-cn/中国大陆网盘列表
  - [2] https://www.rayks.com/article/ucwp1tbhd.html
  - [3] https://github.com/OpenListTeam/OpenList/blob/main/drivers/quark_uc_tv/meta.go
  - [4] https://pan.quark.cn/
