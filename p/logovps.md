# VmShell Hong Kong CMI port forward

> logovps.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/logovps/ | JSON https://fshy.ajam.dev/api/v1/entity/logovps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VmShell Hong Kong CMI port forward

- `egress/vmshell-hk-port-forward` | dead | evidence reported | binding retention-clamped | category tcp port forward (hosted, Hong Kong) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:51:45.685Z (live) | stale on 2026-11-14
- url https://www.logovps.com/1180.html
- price USD 0 for one month
- free tier: unit: hours | metered on: wall-clock | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] 'Free for one month', with no traffic allowance, rate or session length stated. The notice describes it as a test product with no technical support.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: [translated] 'Limit: one product per ID', ordered through a vmshell.com cart link. The notice does not state what registration requires. | country: None
- interface: unknown
- limits:
  - retention-clamped (binding): [translated] 'free for one month' [1]
- binding note: The month ends before 1 TiB/month can be reached, and the notice publishes no byte allowance to fail first.
- interface detail: [translated] The notice gives a vmshell.com cart link and a Telegram support group; no client or API is described.
- tooling: panel-configured port forward; no client documented in the notice
- composes with: A Hong Kong forward on a high port would front a service that speaks on 13800-59999, for one month.
- reliability: Described by the vendor as a test product with no technical support; the blocked port list removes 22, 80, 443 and 3306.
- notes: A free Hong Kong CMI three-network direct port forward. It is a one-month free test product announced in January 2023 with no technical support. Country: Hong Kong. The notice does not say whether UDP is forwarded in the allowed port range.
- evidence note: The offer facts come from a third-party blog post dated 2023-01-23 that reproduces the vendor's Telegram notice, so the record's rung is reported. On 2026-10-30 the notice's order link https://vmshell.com/cart.php?a=add&pid=76, followed through the site's validator redirect, ended at the store page https://vmshell.com/index.php?rp=/store/cmin2hk, which lists four VPS plans in a Hong Kong data center and no port-forward product.
- extras:
  - wg_path: unknown
  - wg_detail: [translated] The notice names a port range (13800-59999) and no protocol. A TCP-only forward could not carry a WireGuard datagram; whether UDP is forwarded in that range is not stated by the notice.
  - ingress: tcp
  - volume_stated: [translated] 'Free for one month', with no traffic allowance, rate or session length stated. The notice describes it as a test product with no technical support.
  - bytes_transit: yes
  - transit_note: VmShell's Hong Kong CMI address forwards to the local machine.
  - death.on: 2026-10-30
  - death.cause: free-tier-removed
- evidence:
  - [1] 2026-10-23: 
  - [1] 2026-10-30: [translated] the post dated 2023-01-23 reproduces a VmShell notice: Hong Kong CMI port-forwarding test, free for 1 month | capture: sha256:4a6ac694ddd49e5e6b977a41daf960b329814f1df38d688505fa65dbb04a4256 | quote: CMI-端口转发测试通知（获取建议） 免费1个月
  - [1] 2026-10-30: [translated] the notice blocks ports 22, 443, 80 and 3306 and allows ports 13800-59999 | capture: sha256:4a6ac694ddd49e5e6b977a41daf960b329814f1df38d688505fa65dbb04a4256 | quote: 禁止端口号 22,443,80,3306 允许的端口号 13800-59999
  - [1] 2026-10-30: [translated] the notice limits each ID to one product | capture: sha256:4a6ac694ddd49e5e6b977a41daf960b329814f1df38d688505fa65dbb04a4256 | quote: 限额：每个ID一个产品
  - [1] 2026-10-30: [translated] the notice describes the offer as free for a limited time with no technical support | capture: sha256:4a6ac694ddd49e5e6b977a41daf960b329814f1df38d688505fa65dbb04a4256 | quote: 限时免费,无技术支持
  - probe:https://vmshell.com/cart.php?a=add&pid=76 2026-10-30: a GET of the order link https://vmshell.com/cart.php?a=add&pid=76 answered HTTP 403 with 0 bytes on 2026-10-30 | capture: sha256:0278b7203838553aa9054a05e303479693b850ec1662b7a1675347a6733706bd | quote: "status": 403
  - [2] 2026-10-30: on 2026-10-30 the store page the order link lands on lists two categories, CMIN2.HK and USA-VPS, and four VPS plans in a Hong Kong data center priced from USD 7.00 to USD 23.00 a month; no port-forward product is listed | capture: sha256:29a18000f7440f9fb14f49460d515b022e57ab58d4ed5bb9137b70df5804109c | quote: Annual Pay For Cheap From $7.00 /mo
  - [2] 2026-10-30: on 2026-10-30 the order link https://vmshell.com/cart.php?a=add&pid=76, followed through the site's validator redirect, ended at https://vmshell.com/index.php?rp=/store/cmin2hk, a store page and not an order form | capture: sha256:29a18000f7440f9fb14f49460d515b022e57ab58d4ed5bb9137b70df5804109c | quote: x-web-final-url: https://vmshell.com/index.php?rp=/store/cmin2hk
  - [1] 2026-10-30: it names no carrier and no protocol | capture: sha256:4a6ac694ddd49e5e6b977a41daf960b329814f1df38d688505fa65dbb04a4256 | quote: 免费香港CMI三网直连端口转发： CMI-端口转发测试通知（获取建议） 免费1个月 因为测试产品 建议电报我们 TeleGram 群组建议： https://t.me/vmshellhk 禁止端口号 22,443,80,3306 允许的端口号 13800-59999 欢迎联系我们 因为测试产品 希望大家给出建议 祝大家大展宏兔 我们晚点提供大陆中转服务 限时免费,无技术支持
- sources:
  - [1] https://www.logovps.com/1180.html
  - [2] https://vmshell.com/cart.php?a=add&pid=76
