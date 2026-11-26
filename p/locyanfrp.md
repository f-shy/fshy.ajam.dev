# LoCyanFrp

> locyanfrp.cn | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/locyanfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/locyanfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LoCyanFrp

- `egress/locyanfrp` | dead | evidence unverified | binding volume-quota | category udp port forward | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-25T09:55:01.929Z (live) | stale on 2026-12-10
- url https://www.locyanfrp.cn/
- price USD 0
- free tier: Free users: unlimited tunnels, speed limit varies by tunnel, traffic claimable by daily check-in, Docker supported. [translated from a forum roundup] | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: unverified: published terms state no explicit byte allowance. Traffic is allocated via check-in.; ingress: udp | metered: no | free allowance: none published | source: [2]
- identity: national-id | detail: Two-level real-name verification is reported; the document or provider used is not stated in the sources read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): daily check-in grant of 1000~4000 GB, per a third-party post [3]
- binding note: The only metering described is a daily check-in grant of unknown size, so the quota is what would fail first.
- interface detail: frpc plus a web panel, per the roundup.
- tooling: frpc, Docker
- composes with: None until the origin answers.
- reliability: The name www.locyanfrp.cn had no DNS answer on 2026-11-25.
- notes: HTTP 530 is Cloudflare reporting an origin DNS or connection failure, which usually means the backend is down rather than the page being blocked. Do not treat this as settled death without a second look.
- evidence note: Provider endpoint returned HTTP 530 on 2026-10-23, indicating origin connectivity failures.
- extras:
  - wg_path: unknown
  - wg_detail: Nothing could be read from the origin; the roundup does not say whether UDP tunnels are offered.
  - ingress: udp
  - volume_stated: Check-in traffic.
  - bytes_transit: yes
  - transit_note: Unverified.
- evidence:
  - [2] 2026-10-23: nothing established about the page
  - [1] 2026-10-23: roundup lists unlimited tunnels and check-in traffic
  - probe:https://8.8.8.8/resolve?name=www.locyanfrp.cn&type=A 2026-11-03: a public DNS-over-HTTPS resolver answered the name www.locyanfrp.cn with a CNAME to www.locyanfrp.cn.a1.inithh.com and DNS status 3 (NXDOMAIN), so the site name resolves to no address | capture: sha256:087ed4d1a5b3cd9c7ca5d5d7305624cdb7f7674c8944e72522ad524c4cd5ec4d | quote: "Status":3,"TC":false,"RD":true,"RA":true,"AD":false,"CD":false,"Question":[{"name":"www.locyanfrp.cn.","type":1}],"Answer":[{"name":"www.locyanfrp.cn.","type":5,"TTL":300,"data":"www.locyanfrp.cn.a1.inithh.com."}]
  - probe:https://1.1.1.1/dns-query?name=www.locyanfrp.cn&type=A 2026-11-03: a second public DNS-over-HTTPS resolver also answered DNS status 3 (NXDOMAIN) for www.locyanfrp.cn, which is a CNAME to www.locyanfrp.cn.a1.inithh.com | capture: sha256:f09940447ddf393c2dafe7ebb7b2d2f4c172576e1bfe552fac21aeecdace73f9 | quote: "Status":3
  - probe:locyanfrp.cn:443 2026-11-03: a TCP connect to the apex locyanfrp.cn on port 443 timed out on 2026-11-03, so the HTTPS port of the apex did not accept a connection | capture: sha256:90014ef9d71cebcfc870f324041eb35b8c97cbd12e4ac8ec442fce2d54f77f72 | quote: TimeoutError('timed out')
  - probe:https://locyanfrp.cn/ 2026-11-03: an HTTPS GET of the apex locyanfrp.cn timed out on 2026-11-03 with no status | capture: sha256:7fdf12c219ca17236d4c5157dbf024e4cea989a20da5b5da1decd4c1205de23e | quote: "error": "timeout"
  - [4] 2026-11-03: the Wayback Machine copy of the apex dated 2026-05-15 is a CDN not-found page, so the domain was not bound to a site on that date | capture: sha256:58dbf2699dcb0d0d2732b5f7b54e443ee2ffcbf9ddde9cc08ba160540d52b441 | quote: Sorry, Please confirm that this domain name has been bound to your website.
  - probe:https://www.locyanfrp.cn/ 2026-11-25: the first-party name still had no DNS answer on 2026-11-25 | capture: sha256:6676f5134fdd5aebe858d397106f63ea64fea4b85796e0d6e6c379ee46ecf364 | quote: "error": "dns"
  - [3] 2026-11-25: a third-party user report states the size of the daily check-in grant | capture: sha256:1512c279be394ddfad9fff4dc1a9b7b9a435a8b832448bfe6ce4110b7c5279d8 | quote: 每天签到 1000~4000GB 流量
  - [3] 2026-11-25: the post that states the check-in amount is the source named by the updated limit | capture: sha256:1512c279be394ddfad9fff4dc1a9b7b9a435a8b832448bfe6ce4110b7c5279d8 | quote: 每天签到 1000~4000GB 流量
  - [3] 2026-11-25: a third-party user report says two levels of real-name verification are needed | capture: sha256:1512c279be394ddfad9fff4dc1a9b7b9a435a8b832448bfe6ce4110b7c5279d8 | quote: 通过两级实名认证就能用了（实测我只通过二级认证会无法使用）
  - [3] 2026-11-25: a third-party user report describes the verification gate | capture: sha256:1512c279be394ddfad9fff4dc1a9b7b9a435a8b832448bfe6ce4110b7c5279d8 | quote: 通过两级实名认证就能用了（实测我只通过二级认证会无法使用）
  - [3] 2026-11-25: a third-party user report states the check-in grant and the real-name gate | capture: sha256:1512c279be394ddfad9fff4dc1a9b7b9a435a8b832448bfe6ce4110b7c5279d8 | quote: 每天签到 1000~4000GB 流量 ... 通过两级实名认证就能用了（实测我只通过二级认证会无法使用）
  - [5] 2026-11-25: the team site describes a free V3 service and a migration address | capture: sha256:ea17b87d21fa56ea450301c94b284d09426a87f0ed3bd22607c12825e97b7ed3 | quote: V3 迁移网址：https://migrate.locyanfrp.cn ... 以上功能都由我们这一款完全公益免费的内网穿透提供
- sources:
  - [1] https://www.nodeseek.com/post-570663-1
  - [2] https://www.locyanfrp.cn/
  - [3] https://blog.rimrose.work/posts/locyanfrp/locyanfrp/
  - [4] https://web.archive.org/web/20260515130252/http://locyanfrp.cn/
  - [5] https://www.locyan.cn/archives/le-qing-ying-she-locyanfrp-v3-geng-xin-ji-hua
