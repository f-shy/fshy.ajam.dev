# 萌盘 PAN.MOE

> pan.moe | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pan/ | JSON https://fshy.ajam.dev/api/v1/entity/pan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 萌盘 PAN.MOE (Moe Drive)

- `netdisk-pan/pan-moe` | qualifies | evidence documented | binding write-gated | category community cloud drive on Cloudreve, non-profit
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:06:37.166Z (live) | stale on 2026-11-13
- url https://pan.moe/
- free tier: 1 TB free for every registrant and described as permanent, 2 to 5 TB for community members by application, and above 5 TB a cold-storage plan. Terms section 3.1 confirms '1TB（或更高）空间' | unit: TiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: Not published | source: [1] | note: per-object cap unknown and not published anywhere in the terms or on the landing page
- retention: No durability guarantee at all: terms section 2.1 states '不对用户的数据进行任何形式的长期或永久性保证' | source: [1]
- egress: No published egress cap for the free tier; bandwidth is policed only by a fair-use clause allowing throttling for '占用过多带宽'. Both domestic and overseas storage nodes are offered with cross-region transfer | metered: no | source: [1]
- identity: email | detail: the signup form at pan.moe/signup asks for email, password, a repeat and a human-verification step, with no phone field
- interface: webdav
- limits:
  - write-gated (binding):  [1]
  - per-object-cap: not published [1]
- binding note: Offers 1 TB of free storage with class 2 WebDAV endpoint access without phone verification. the provider explicitly prohibits maintaining multiple accounts, enforcing a strict 1 TB account limit.
- tooling: a Cloudreve front end with a live WebDAV endpoint at https://pan.moe/dav answering as DAV class 2 with PUT in Allow, plus the standard Nextcloud-family clients. No S3 layer is exposed
- composes with: Terms section 3.1 explicitly routes anyone needing more than 5 TB to a bespoke cold-storage plan, so it is a 1 TB building block and not a pool. Its value is the WebDAV endpoint, which mounts into TrueNAS Cloud Sync, rclone, Duplicati and restic without a wrapper
- reliability: Zero durability commitment in the terms plus an explicit rule against the several-accounts pattern that would make it useful at 20 TB. The domestic storage node carries a compliance clause, so the overseas node is the only one that fits
- notes: The service provides no formal uptime or data durability SLA.
- evidence note: The 1 TB offer was re-read live on the landing page; `documented` and not `measured` because the DAV endpoint refused without a credential, which is the expected answer and not a measurement of the read path.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - webdav_class: 2
  - webdav_put_enabled: yes
  - bans_multi_account_expansion: yes
  - durability_commitment: none, disclaimed in terms 2.1
  - aliases: 萌盘 PAN.MOE (Moe Drive); pan.moe / 萌盘 (Moe Drive); Moe Drive; 萌社区网盘
  - alias_note: this record is the single home for both deferred spellings: '萌盘 PAN.MOE (Moe Drive)' and the audit's 'pan.moe / 萌盘 (Moe Drive)'
  - launched: 2025-02-01
- evidence:
  - [2] 2026-10-22: the served page reads '萌社区网盘（萌盘）是一款面向广大用户的免费云存储服务，注册即享1TB永久免费空间，萌社区成员可享最大5TB容量。支持境内外多节点高速存储、WebDav挂载'
  - [1] 2026-10-21: section 3.1 gives 1 TB free, 2 to 5 TB for members and a cold-storage plan above 5 TB; section 2.1 disclaims any permanence guarantee
  - [3] 2026-10-21: the launch announcement on 2025-02-01 offering 免费 1TB / 5TB, WebDAV support, 4,681 views
  - [4] 2026-10-21: the form is email, password, repeat and a human-verification step only, with no phone field
  - probe:https://pan.moe/dav 2026-10-21: OPTIONS returned HTTP 401 with www-authenticate Basic realm="cloudreve" and Allow: OPTIONS, LOCK, PUT, MKCOL, and dav: 1, 2, so WebDAV class 2 with PUT enabled behind Cloudflare
  - probe:https://pan.moe/dav 2026-10-21: PROPFIND returned 401 with 0 bytes, so the endpoint is auth-gated and not a 200 carrying an error body
- sources:
  - [1] https://pan.moe.one/terms/
  - [2] https://pan.moe/
  - [3] https://moe.one/thread-924.htm
  - [4] https://pan.moe/signup
